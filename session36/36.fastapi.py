# FastAPI  -  introducere de la ZERO  (tema: Bounty Board pentru cod)
# =============================================================
#
# CE AI FACUT PANA ACUM (recap, ca sa vezi ce se schimba)
# --------------------------------------------------------
# Toate programele tale de pana acum au fost SCRIPT-uri: le rulai
# (`python ceva.py`), faceau o treaba (citeau un CSV, calculau ceva,
# scriau in MySQL), AFISAU rezultatul in terminal si SE INCHIDEAU.
# Programul traieste cateva secunde, apoi moare.
#
#
# PROBLEMA pe care o rezolva un API
# ----------------------------------
# Vrei sa construiesti un BOUNTY BOARD pentru cod: o platforma unde
# programatorii POSTEAZA task-uri (bug-uri, functionalitati noi) cu o
# RECOMPENSA in bani, iar alti programatori le rezolva si iau banii -
# exact ca pe platforme reale (Gitcoin, IssueHunt). Dar:
#   - vrei ca ORICINE sa vada task-urile disponibile, de pe orice
#     dispozitiv (telefon, laptop, alt site) - nu doar tu, in terminal;
#   - cand cineva rezolva un task, vrei ca TOATA LUMEA sa vada imediat
#     ca s-a rezolvat (nu doar tu, care ai rulat scriptul);
#   - poate vrei mai tarziu o aplicatie mobila sau un site, peste
#     ACELASI cod Python care stie sa gestioneze task-urile si banii.
#
# Un script care ruleaza si se inchide NU poate face asta. Ai nevoie de
# un program care STA PORNIT PERMANENT si care ASCULTA: oricine (telefonul
# tau, un site, alt program) poate sa-i CEARA ceva, oricand, iar el
# raspunde. Acest program se numeste SERVER, iar felul in care ii vorbesti
# se numeste API (Application Programming Interface - "interfata prin
# care alte programe iti folosesc programul").
#
#
# SOLUTIA: FastAPI
# -----------------
# FastAPI e o BIBLIOTECA Python care te ajuta sa construiesti exact acest
# gen de server, numit API REST (o "aroma" foarte raspandita de API, care
# foloseste HTTP - acelasi protocol pe care il foloseste si browser-ul
# cand deschide un site).
#
# DE CE NU SCRII TU asta de la zero, in Python simplu?
# Tehnic, ai putea - Python are un modul `socket` care iti da acces direct
# la reteaua calculatorului. Dar atunci ai ramane tu cu toata partea
# "murdara": sa citesti textul brut care vine pe retea si sa-l descifrezi
# ca sa afli ce a cerut clientul, sa scoti singur bucata de adresa care
# te intereseaza (si sa ai grija ce se intampla daca nu e ce te astepti),
# sa transformi manual raspunsul tau intr-un text JSON corect, sa trimiti
# inapoi headerele potrivite, sa te descurci cand vin mai multi clienti
# deodata. Nimic din toate astea nu tine de ce vrei tu sa faci de fapt
# (calculezi recompense, gestionezi task-uri) - e doar "instalatia" pe
# care trebuie sa o pui o data, ca sa poti vorbi cu lumea de afara.
# FastAPI face exact instalatia asta pentru tine, ca sa ramai cu partea
# care chiar conteaza.
#
# ROLUL exact al lui FastAPI in bounty board-ul tau:
#   - tu scrii cod Python NORMAL (functii, liste, dicturi - ce stii deja)
#   - FastAPI "expune" acel cod pe INTERNET/RETEA: ii da o ADRESA
#     (ex: GET /task-uri) pe care o poate apela oricine
#   - cand cineva apeleaza acea adresa, FastAPI cheama functia ta Python,
#     ia ce returneaza si il trimite INAPOI ca JSON (text pe care orice
#     limbaj/aplicatie il intelege - il stii de la sesiunea 23)
#
# ANALOGIE: FastAPI e ca un RECEPTIONIST. Tu (codul Python) stii sa faci
# treaba (calculezi recompensa disponibila, adaugi un task nou).
# Receptionistul (FastAPI) sta la usa, primeste cereri de la vizitatori
# (programatori - telefon, site, alt program), te intreaba pe tine, si le
# da inapoi raspunsul intr-un format pe care il inteleg toti (JSON).
#
# FASTAPI + UVICORN  -  de ce instalezi doua biblioteci, nu una
# -----------------------------------------------------------------
# S-ar putea sa te intrebi de ce comanda de instalare are doua nume,
# `fastapi` si `uvicorn`, nu unul singur - nu e o scapare, fac lucruri
# diferite. FastAPI stie CE sa raspunda: la ce adrese ai endpoint-uri, ce
# functie se cheama pentru fiecare, cum arata raspunsul in JSON. Dar
# FastAPI, de unul singur, nu asculta nimic - nu deschide nicio conexiune
# de retea. De asta se ocupa Uvicorn: e programul care chiar sta pornit,
# asculta pe un port (la noi, 8000) si, de fiecare data cand vine o
# cerere, o preda mai departe catre FastAPI, ca sa afle ce sa raspunda.
# Le vezi lucrand impreuna la finalul fisierului, in linia
# `uvicorn.run(app, ...)` - `app` e chiar obiectul FastAPI, dat lui
# Uvicorn ca sa stie pe cine sa intrebe.
#
# CERINTE:  pip install fastapi uvicorn
# Ce trebuie sa stii deja: functii, dicturi, liste (orice sesiune anterioara).
# =============================================================

from fastapi import FastAPI, HTTPException


# #############################################################
# PARTEA 1 - PRIMUL SERVER, PAS CU PAS
# #############################################################


# 1. `app`  -  obiectul central al aplicatiei
# -------------------------------------------------------------
# FastAPI() creeaza "aplicatia" - un obiect in care inregistram toate
# adresele (numite ENDPOINT-uri) pe care le va oferi serverul nostru.
# O facem O SINGURA DATA, la inceputul fisierului.

app = FastAPI(title="Bounty Board", version="0.1.0")


# 2. Datele - deocamdata, in memorie (o lista Python obisnuita)
# -------------------------------------------------------------
# Inainte sa bagam baza de date (asta vine in sesiunea 38), tinem datele
# intr-o lista Python normala, exact ca in orice script de-al tau. Ideea de
# API e SEPARATA de unde stau datele - azi sunt in RAM, maine in MySQL,
# API-ul din exterior arata LA FEL.

task_uri = [
    {"id": 1, "titlu": "Fix bug la login",     "limbaj": "Python",     "dificultate": "usor",  "recompensa": 50,  "rezolvat": False},
    {"id": 2, "titlu": "Adauga dark mode",      "limbaj": "JavaScript", "dificultate": "mediu", "recompensa": 150, "rezolvat": False},
    {"id": 3, "titlu": "Optimizeaza query SQL", "limbaj": "Python",     "dificultate": "greu",  "recompensa": 300, "rezolvat": True},
    {"id": 4, "titlu": "Scrie teste unitare",   "limbaj": "Python",     "dificultate": "usor",  "recompensa": 80,  "rezolvat": False},
]


# 3. PRIMUL ENDPOINT:  @app.get("/")
# -------------------------------------------------------------
# Un ENDPOINT e o "adresa" a serverului + o functie Python care ruleaza
# cand cineva o cere. Il declari cu un DECORATOR (le stii de la sesiunea 14):
#
#     @app.get("<cale>")
#     def functia_mea():
#         return ceva
#
#   - @app.get(...)  spune: "cand vine o cerere GET pe calea asta, cheama
#     functia de dedesubt". GET = "vreau sa CITESC ceva" (ca la sesiunea 32).
#   - CE RETURNEAZA functia (aici un dict), FastAPI transforma AUTOMAT
#     in JSON si trimite inapoi clientului. Nu scrii tu cod de conversie.

@app.get("/")
def acasa():
    return {"aplicatie": "Bounty Board", "versiune": app.version}


# 4. AL DOILEA ENDPOINT: o lista intreaga
# -------------------------------------------------------------
# La fel de simplu: functia intoarce lista Python `task_uri`, iar FastAPI
# o transforma intr-un array JSON.

@app.get("/task-uri")
def lista_taskuri():
    return task_uri



# #############################################################
# PARTEA 2 - PARAMETRI: cum primesti informatie DE LA client
# #############################################################
# Pana acum toate endpoint-urile intorc mereu ACELASI lucru. Dar un client
# vrea sa ceara lucruri SPECIFICE: "da-mi task-ul cu id 3", "da-mi doar
# task-urile in Python". Pentru asta ai nevoie de PARAMETRI - doua feluri.


# 5. PATH PARAMETER  -  parte din adresa (calea) in sine
# -------------------------------------------------------------
# Cand pui  {ceva}  in cale, iar functia are un argument cu ACELASI nume,
# FastAPI ia bucata din URL si o baga in argument, CONVERTITA la tipul
# cerut de type hint. `task_id: int` inseamna: trebuie sa fie un numar -
# daca cineva cere /task-uri/abc, FastAPI refuza SINGUR, fara sa scrii tu
# vreo verificare.
#
# Daca nu gasim ce se cere, raspundem cu eroare 404 ("Not Found") folosind
# HTTPException - exact statusurile HTTP pe care le-ai vazut la sesiunea 32.

@app.get("/task-uri/{task_id}")
def un_task(task_id: int):
    for task in task_uri:
        if task['id'] == task_id:
            return task

    raise HTTPException(status_code=404, detail="Task-ul nu exista")


# 6. QUERY PARAMETER  -  ce vine dupa  ?  in URL
# -------------------------------------------------------------
# Un argument al functiei care NU apare intre acolade in cale devine
# automat parametru de QUERY (partea de dupa "?" din URL, ca la sesiunea 32
# cu `requests`). Daca ii dai o valoare implicita (`= None`), devine
# OPTIONAL - clientul poate sa nu il trimita deloc.
#
#   GET /dupa-limbaj                -> toate
#   GET /dupa-limbaj?limbaj=Python  -> doar task-urile in Python

@app.get("/dupa_limbaj")
def dupa_limbaj(limbaj: str | None = None):
    if limbaj is None:
        return task_uri
    return [task for task in task_uri if task['limbaj'].lower() == limbaj]


# #############################################################
# PARTEA 3 - SCRIEREA DATELOR + CALCULE + DOCUMENTATIE
# #############################################################


# 7. POST  -  clientul ne TRIMITE date, ca sa CREAM ceva
# -------------------------------------------------------------
# GET = citire; POST = creare (ai vazut maparea CRUD <-> HTTP la sesiunea 32).
# Deocamdata primim datele ca parametri simpli (query) - e ok pentru
# inceput, dar NU e "corect": nu avem nicio validare (poti trimite orice
# text ca limbaj, orice recompensa negativa). In sesiunea 37 le trimitem
# CORECT, in BODY, validate cu Pydantic.

@app.post("/task-uri")
def adauga_task(titlu:str, limbaj:str, dificultate:str, recompensa:int, rezolvat:bool):

    nou = {
        "id": len(task_uri) + 1,
        "titlu": titlu,
        "limbaj": limbaj,
        "dificultate": dificultate,
        "recompensa": recompensa,
        "rezolvat": rezolvat
    }
    task_uri.append(nou)

    return nou

# CUM TESTEZI CHIAR ACEST ENDPOINT, pas cu pas (in /docs):
#   1. Ruleaza fisierul:  python 36.fastapi.py
#   2. Deschide in browser:  http://127.0.0.1:8000/docs
#   3. Cauta randul albastru  POST /task-uri  si apasa pe el (se extinde).
#   4. Apasa butonul  "Try it out"  (dreapta-sus in sectiunea extinsa).
#   5. Acum apar 4 CASUTE SEPARATE de completat: titlu, limbaj, dificultate,
#      recompensa (NU un singur camp mare de JSON - pentru ca, dupa cum am
#      vazut mai sus, sunt query params, nu body).
#      Completezi de exemplu:
#        titlu=Adauga cache   limbaj=Python   dificultate=mediu   recompensa=120
#   6. Apasa butonul albastru  "Execute".
#   7. Mai jos apare "Server response": codul (200) si raspunsul JSON.
#      Uita-te si la "Request URL" afisat acolo - arata exact:
#        http://127.0.0.1:8000/task-uri?titlu=...&limbaj=Python&dificultate=mediu&recompensa=120
#      Vezi? toti parametrii sunt LIPITI DUPA "?" in adresa - dovada clara
#      ca au mers ca query params, nu ca JSON in body.
#
# ACELASI lucru, dar din COD (cu requests, ca la sesiunea 32) - ATENTIE,
# aici NU folosesti json=, ci params= (pentru ca endpoint-ul asteapta query):
#   import requests
#   r = requests.post(
#       "http://127.0.0.1:8000/task-uri",
#       params={"titlu": "Adauga cache", "limbaj": "Python",
#               "dificultate": "mediu", "recompensa": 120},
#   )
#   print(r.json())


# 8. UN ENDPOINT DE CALCUL  -  recompensa inca disponibila
# -------------------------------------------------------------
# Un endpoint nu trebuie sa intoarca direct date brute - poate calcula
# ceva folosind functii Python obisnuite (sum, list comprehension - de
# la sesiunile 7-10). Aici: cati bani mai sunt "pe masa", in task-urile
# NErezolvate inca.

@app.get("/recompensa-disponibila")
def recompensa_disponibila():
    total = sum([task['recompensa'] for task in task_uri if not task['rezolvat']])
    nr_taskuri = sum(1 for task in task_uri if not task['rezolvat'])
    return {'task-uri_nerezolvate': nr_taskuri, "total": total}


# 9. DOCUMENTATIA AUTOMATA  -  cel mai tare feature al FastAPI
# -------------------------------------------------------------
# Nu scrii NIMIC in plus. FastAPI citeste toate endpoint-urile tale si
# genereaza singur o pagina WEB interactiva:
#   http://127.0.0.1:8000/docs   -> Swagger UI: apesi "Try it out",
#                                    completezi campurile, apesi "Execute"
#                                    si vezi raspunsul, FARA sa scrii cod.
# E cel mai rapid mod sa "vezi" API-ul tau si sa il testezi manual.


# =============================================================
# CUM RULEZI ACEST FISIER
# =============================================================
# Exact ca orice aplicatie FastAPI reala:
#       python 36.fastapi.py
# apoi deschizi in browser:
#       http://127.0.0.1:8000/docs
# si testezi fiecare endpoint cu butonul "Try it out".
# Opresti serverul cu Ctrl+C in terminal (ramane pornit pana atunci -
# asta e ideea de "server", vezi Partea 1).
# =============================================================

import uvicorn
uvicorn.run(app, host="127.0.0.1", port="8000")

# =============================================================
# RECAP / IDEI CHEIE
# =============================================================
# - Un API = un program-SERVER care sta pornit si raspunde la cereri prin
#   retea (HTTP), spre deosebire de un script care ruleaza si se inchide.
# - FastAPI = biblioteca Python care "expune" codul tau ca API REST:
#   scrii functii Python normale, le pui adresa (endpoint) cu un decorator.
# - Uvicorn = programul care CHIAR asculta reteaua si tine serverul
#   pornit; fara el, FastAPI stie ce sa raspunda dar n-are cine sa-l
#   intrebe. Le folosesti impreuna (uvicorn.run(app, ...)), niciodata
#   pe una singura.
# - app = FastAPI()  -  o data, la inceput.
# - @app.get("/cale")  /  @app.post("/cale")  -  decorator = endpoint.
# - Ce intoarce functia (dict/lista) devine JSON automat.
# - PATH param:  /task-uri/{id}  + type hint  -> FastAPI extrage si
#   converteste singur, din URL.
# - QUERY param: argument normal, in afara caii; cu default -> optional.
# - HTTPException(status_code=404, detail=...)  -> raspuns de eroare curat.
# - /docs  -> pagina interactiva, generata automat, ca sa testezi vizual.
#
# ATENTIE (intentionat): POST-ul de mai sus NU valideaza nimic - poti
# trimite orice. Rezolvam asta in sesiunea 37 cu Pydantic.
# =============================================================