# QUIZ INTERVIU  -  FastAPI & FastAPI + Pydantic
#                    (sesiunile 36 - FastAPI de baza, 37 - Pydantic + CRUD)
# =============================================================
# Pe baza a tot ce s-a predat in 36.fastapi.py si 37.fastapi_pydantic.py
# (tema: Bounty Board).
# Fiecare intrebare contine:
#   - o SECVENTA DE COD (de tip "ce afiseaza? / ce raspunde serverul?")
#   - 4 variante A/B/C/D
#   - EXPLICATIE obligatorie dupa raspuns (afisata si cand
#     raspunzi corect — la interviu conteaza sa stii DE CE)
#
# Gotcha-urile clasice din sesiunile 36 si 37:
#   FASTAPI DE BAZA (36):
#     - app = FastAPI() se face O SINGURA DATA; daca redefinesti `app`
#       mai tarziu, rutele vechi raman agatate de obiectul vechi, iar
#       uvicorn.run primeste obiectul NOU, care nu are nicio ruta
#     - fara uvicorn.run(app, ...) in "if __name__ == '__main__'",
#       fisierul ruleaza si se termina, dar niciun server nu porneste
#     - ce RETURNEAZA functia (dict/lista) devine JSON automat, fara
#       cod de conversie scris de tine
#   PATH & QUERY PARAMETERS (36):
#     - {ceva} in cale + type hint (ex: task_id: int) => FastAPI extrage
#       si CONVERTESTE singur din URL; daca nu poate converti (ex.
#       /task-uri/abc), raspunde cu 422, nu 404 — nici nu ajunge in
#       corpul functiei
#     - rutele se verifica in ORDINEA in care sunt DEFINITE; o ruta
#       dinamica (/task-uri/{id}) definita INAINTEA uneia statice cu
#       acelasi prefix (/task-uri/populare) o "fura" pe cea statica
#     - argument normal (nu intre acolade), cu valoare implicita =>
#       query param OPTIONAL; daca lipseste din URL, ramane pe default
#     - parametri simpli (str/int/float) pe POST, FARA model Pydantic,
#       sunt cititi din QUERY, nu din body — trimisi cu json= in loc
#       de params=, raman "invizibili" pentru FastAPI (422, lipsa)
#   PYDANTIC CA BODY (37):
#     - un parametru care e MODEL Pydantic (nu str/int/float simplu)
#       e citit din BODY (JSON), nu din query — asta schimba complet
#       cum arata /docs si cum trimiti cererea
#     - Field(gt=0), Enum etc. sunt verificate INAINTE sa ajunga in
#       corpul functiei; date invalide => 422 automat
#     - un parametru `payload: dict` (nu un model concret) NU e validat
#       automat de FastAPI — orice JSON trece; validarea manuala cu
#       Model.model_validate(payload) + try/except ValidationError e
#       cod scris de TINE, iar raspunsul ei normal (dict) vine cu
#       status 200, chiar daca datele erau invalide
#   CRUD COMPLET (37):
#     - status_code=201 din decorator se aplica DOAR raspunsului de
#       succes; la eroare de validare FastAPI raspunde tot cu 422
#     - modificarea unei liste (remove) IN TIMPUL iterarii peste ea e
#       riscanta — merge "din intamplare" doar daca faci return imediat
#       dupa, oprind bucla pe loc
#
# Cum se ruleaza:
#   python3 37.quiz.py
#
# Apasa Q oricand pentru iesire.
# =============================================================


# =============================================================
# BANCA DE INTREBARI
# =============================================================
# Fiecare intrebare e un DICT cu:
#   runda       (int)    1..4
#   categorie   (str)
#   puncte      (int)    1 / 2 / 3 — dificultate
#   cod         (str)    secventa de cod (triple-quoted)
#   intrebare   (str)    intrebarea propriu-zisa
#   optiuni     (dict)   {"A": ..., "B": ..., "C": ..., "D": ...}
#   corect      (str)    "A" / "B" / "C" / "D"
#   explicatie  (str)    DE CE — afisata mereu dupa raspuns

intrebari = [
    # ---------- RUNDA 1: FASTAPI DE BAZA — APP, DECORATOR, GET ----------
    {"runda": 1, "categorie": "app-redefinit", "puncte": 3,
     "cod": 'app = FastAPI(title="Bounty Board")\n\n@app.get("/")\ndef acasa():\n    return {"ok": True}\n\n# mai jos, din greseala, o a doua initializare:\napp = FastAPI(title="Alta aplicatie")\n\nif __name__ == "__main__":\n    uvicorn.run(app, host="127.0.0.1", port=8000)',
     "intrebare": "Ce raspunde serverul la GET / dupa ce porneste?",
     "optiuni": {"A": "{\"ok\": True}, ca de obicei", "B": "404 — ruta a fost inregistrata pe primul obiect app, dar uvicorn.run primeste al DOILEA obiect, gol",
                 "C": "eroare la pornirea serverului, app e redefinit de doua ori", "D": "FastAPI combina automat rutele din ambele obiecte app"},
     "corect": "B",
     "explicatie": "@app.get(\"/\") inregistreaza ruta pe obiectul `app` care exista in acel moment. Rescrierea `app = FastAPI(...)` mai jos creeaza un obiect COMPLET NOU, fara nicio ruta. uvicorn.run(app, ...) primeste acest al doilea obiect — cel cu ruta inregistrata a ramas 'orfan', nefolosit de nimeni."},

    {"runda": 1, "categorie": "return-devine-json-automat", "puncte": 1,
     "cod": '@app.get("/task-uri")\ndef lista_task_uri():\n    return task_uri   # o lista Python de dicturi',
     "intrebare": "Clientul face GET /task-uri. Ce primeste efectiv, pe retea?",
     "optiuni": {"A": "un string cu repr() al listei Python", "B": "un array JSON, generat automat de FastAPI din lista Python",
                 "C": "eroare, pentru ca nu ai facut json.dumps() manual", "D": "un fisier .py trimis ca atasament"},
     "corect": "B",
     "explicatie": "FastAPI transforma AUTOMAT ce returneaza functia (dict, lista de dicturi) in JSON, fara niciun cod de conversie scris de tine. Asta e diferenta fata de un script normal: aici valoarea de return devine raspunsul HTTP."},

    {"runda": 1, "categorie": "uvicorn-lipsa-din-main", "puncte": 2,
     "cod": 'app = FastAPI()\n\n@app.get("/")\ndef acasa():\n    return {"aplicatie": "Bounty Board"}\n\n# fisierul se termina aici, fara "if __name__ == \'__main__\': uvicorn.run(...)"',
     "intrebare": "Rulezi acest fisier cu `python 36.fastapi.py`. Ce se intampla?",
     "optiuni": {"A": "porneste un server pe portul implicit 8000, la fel ca oricand", "B": "scriptul ruleaza si se termina imediat, fara erori — dar niciun server nu porneste",
                 "C": "eroare, FastAPI cere obligatoriu blocul uvicorn.run", "D": "browserul deschide automat /docs"},
     "corect": "B",
     "explicatie": "FastAPI, de una singura, STIE ce sa raspunda la fiecare ruta, dar nu asculta nimic pe retea. Fara uvicorn.run(app, ...), care sa porneasca efectiv acel proces, scriptul doar defineste `app` si rutele lui, apoi ajunge la finalul fisierului si se inchide — nicio eroare, dar nici server."},

    {"runda": 1, "categorie": "query-param-fara-valoare-in-url", "puncte": 2,
     "cod": '@app.get("/dupa-limbaj")\ndef dupa_limbaj(limbaj: str | None = None):\n    if limbaj is None:\n        return task_uri\n    return [t for t in task_uri if t["limbaj"] == limbaj]',
     "intrebare": "Clientul cheama GET /dupa-limbaj, FARA sa puna nimic dupa semnul ?. Ce raspunde endpointul?",
     "optiuni": {"A": "eroare 422 — lipseste parametrul limbaj", "B": "lista goala []",
                 "C": "toata lista task_uri, nefiltrata", "D": "None"},
     "corect": "C",
     "explicatie": "`limbaj: str | None = None` are o valoare IMPLICITA, deci e query param OPTIONAL. Daca nu apare deloc in URL, functia primeste `limbaj=None`, intra pe ramura `if limbaj is None` si intoarce toata lista, nefiltrata."},


    # ---------- RUNDA 2: PATH & QUERY PARAMETERS + POST FARA VALIDARE (s36) ----------
    {"runda": 2, "categorie": "path-param-conversie-esuata", "puncte": 3,
     "cod": '@app.get("/task-uri/{task_id}")\ndef un_task(task_id: int):\n    for t in task_uri:\n        if t["id"] == task_id:\n            return t\n    raise HTTPException(status_code=404, detail="nu exista")',
     "intrebare": "Clientul cere GET /task-uri/abc (\"abc\", nu un numar). Ce raspunde FastAPI?",
     "optiuni": {"A": "404 Not Found, ca si cum id-ul nu ar exista", "B": "422 Unprocessable Entity — \"abc\" nu poate fi convertit la int, inainte sa ruleze functia",
                 "C": "TypeError, iar serverul cade", "D": "merge normal, task_id devine string-ul \"abc\""},
     "corect": "B",
     "explicatie": "`task_id: int` cere conversie la numar intreg INAINTE ca functia sa apuce sa ruleze. Cand conversia esueaza (\"abc\" nu e numar), FastAPI raspunde direct cu 422 — codul tau din `un_task`, inclusiv 404-ul manual, nici nu ajunge sa se execute."},

    {"runda": 2, "categorie": "ordinea-rutelor-conflict", "puncte": 3,
     "cod": '@app.get("/task-uri/{task_id}")\ndef un_task(task_id: int):\n    ...\n\n# definita DUPA ruta dinamica de mai sus:\n@app.get("/task-uri/populare")\ndef task_uri_populare():\n    return [t for t in task_uri if t["recompensa"] > 100]',
     "intrebare": "Clientul cere GET /task-uri/populare. /task-uri/{task_id} e definita PRIMA. Ce se intampla?",
     "optiuni": {"A": "raspunde task_uri_populare(), FastAPI stie sa deosebeasca text de numar", "B": "422 — /task-uri/{task_id} e verificata prima, \"populare\" nu e un int valid, iar task_uri_populare() nu se executa niciodata",
                 "C": "amandoua endpointurile ruleaza, iar raspunsurile se combina", "D": "404, pentru ca /task-uri/populare nu exista ca ruta separata"},
     "corect": "B",
     "explicatie": "FastAPI (prin Starlette) verifica rutele in ORDINEA in care au fost inregistrate. /task-uri/{task_id} fiind prima, \"populare\" ajunge sa fie interpretat ca valoare pentru task_id — iar cum e Mapped la int, conversia esueaza -> 422. Solutia clasica: rutele STATICE (/task-uri/populare) se declara INAINTEA celor dinamice cu acelasi prefix."},

    {"runda": 2, "categorie": "post-parametri-simpli-e-query-nu-body", "puncte": 3,
     "cod": '@app.post("/task-uri")\ndef adauga_task(titlu: str, limbaj: str, dificultate: str, recompensa: float):\n    ...\n\n# clientul trimite asa (gresit):\nrequests.post(url, json={"titlu": "X", "limbaj": "Python",\n                          "dificultate": "usor", "recompensa": 100})',
     "intrebare": "adauga_task are parametri simpli (str/float), FARA model Pydantic. Clientul trimite cu json=. Ce se intampla?",
     "optiuni": {"A": "merge normal, FastAPI citeste automat din body JSON", "B": "422 — parametrii simpli sunt cititi din QUERY, nu din body; json= ii lasa \"invizibili\", deci lipsesc",
                 "C": "201, dar cu toate campurile None", "D": "eroare de conexiune, requests refuza sa trimita json= pe POST"},
     "corect": "B",
     "explicatie": "Cand parametrii unei functii sunt tipuri simple (str, int, float) si NU un model Pydantic, FastAPI ii citeste automat din QUERY STRING, chiar si pe POST. Trimisi cu json=, ei ajung in body, unde FastAPI nu se uita dupa ei — sunt considerati lipsa, iar fiind fara valoare implicita, raspunsul e 422 (campuri obligatorii absente). Varianta corecta era params={...}."},

    {"runda": 2, "categorie": "http-exception-format-json", "puncte": 1,
     "cod": 'raise HTTPException(status_code=404, detail="task-ul 99 nu exista")',
     "intrebare": "Ce primeste clientul, ca raspuns HTTP, cand se ridica aceasta exceptie?",
     "optiuni": {"A": "status 404, body JSON: {\"detail\": \"task-ul 99 nu exista\"}", "B": "status 200, cu mesajul de eroare in text simplu",
                 "C": "serverul se opreste (crash)", "D": "status 500, Internal Server Error"},
     "corect": "A",
     "explicatie": "HTTPException e mecanismul standard FastAPI pentru raspunsuri de eroare: seteaza codul de status dat (404 aici) si intoarce automat un body JSON de forma {\"detail\": <mesajul tau>} — exact ca un raspuns normal, doar ca semnaleaza clientului ca ceva a esuat."},


    # ---------- RUNDA 3: PYDANTIC CA BODY — MODEL, ENUM, FIELD (s37) ----------
    {"runda": 3, "categorie": "model-pydantic-e-citit-din-body", "puncte": 2,
     "cod": 'class TaskIn(BaseModel):\n    titlu: str = Field(min_length=3)\n    limbaj: Limbaj\n    dificultate: Dificultate\n    recompensa: float = Field(gt=0)\n\n@app.post("/task-uri", status_code=201)\ndef adauga_task(data: TaskIn):\n    ...\n\n# clientul trimite (gresit, ca la s36):\nrequests.post(url, params={"titlu": "X", "recompensa": 100})',
     "intrebare": "data e acum un MODEL Pydantic, nu parametri simpli. Clientul trimite cu params= (query), nu json=. Ce se intampla?",
     "optiuni": {"A": "merge normal, FastAPI citeste din query ca la s36", "B": "422 — un parametru de tip model Pydantic e citit din BODY; datele trimise ca query raman invizibile pentru el",
                 "C": "201, cu valorile din query preluate automat", "D": "TypeError la pornirea serverului"},
     "corect": "B",
     "explicatie": "Diferenta esentiala fata de s36: cand parametrul e un MODEL Pydantic (nu str/int/float simplu), FastAPI stie sa il citeasca din BODY (JSON), nu din query. Trimise cu params=, datele ajung in query string, unde FastAPI nu se uita pentru acest parametru — campurile obligatorii ale TaskIn lipsesc -> 422."},

    {"runda": 3, "categorie": "field-gt-0-respinge-negativ", "puncte": 2,
     "cod": 'recompensa: float = Field(gt=0)\n\n# body trimis:\n{"titlu": "Bug fix", "limbaj": "Python", "dificultate": "usor", "recompensa": -50}',
     "intrebare": "Ce raspunde POST /task-uri la acest body, cu recompensa negativa?",
     "optiuni": {"A": "201, task-ul se creeaza cu recompensa -50", "B": "422 automat — Field(gt=0) respinge valoarea inainte sa ajunga in corpul functiei adauga_task",
                 "C": "201, dar recompensa e corectata automat la 0", "D": "500 Internal Server Error"},
     "corect": "B",
     "explicatie": "Field(gt=0) e o constrangere verificata de Pydantic/FastAPI in etapa de VALIDARE, inainte ca functia ta sa apuce sa ruleze macar o linie de cod. Orice valoare care nu trece constrangerea (recompensa <= 0) produce automat un raspuns 422, cu detaliul exact (\"greater than 0\")."},

    {"runda": 3, "categorie": "enum-valoare-in-afara-listei", "puncte": 2,
     "cod": 'class Limbaj(str, Enum):\n    PYTHON = "Python"\n    JAVASCRIPT = "JavaScript"\n    GO = "Go"\n    RUST = "Rust"\n\n# body trimis:\n{"titlu": "X", "limbaj": "Java", "dificultate": "usor", "recompensa": 50}',
     "intrebare": "Clientul trimite limbaj=\"Java\" (nu e in Enum-ul Limbaj: Python/JavaScript/Go/Rust). Ce se intampla?",
     "optiuni": {"A": "422 — \"Java\" nu e una din valorile permise de Enum-ul Limbaj", "B": "merge normal, orice text e acceptat ca limbaj",
                 "C": "FastAPI alege automat cea mai apropiata valoare din Enum (\"JavaScript\")", "D": "201, dar campul limbaj ramane None"},
     "corect": "A",
     "explicatie": "Un camp tipat cu un Enum accepta STRICT una din valorile declarate in acel Enum, nimic altceva. \"Java\" nu apare in lista (Python/JavaScript/Go/Rust), deci validarea esueaza -> 422, cu detaliul care arata exact valorile acceptate."},

    {"runda": 3, "categorie": "payload-dict-nu-se-valideaza-singur", "puncte": 3,
     "cod": '@app.post("/valideaza-task")\ndef valideaza(payload: dict):\n    try:\n        TaskIn.model_validate(payload)\n        return {"valid": True}\n    except ValidationError as e:\n        return {"valid": False, "erori": [er["msg"] for er in e.errors()]}',
     "intrebare": "payload e tipat `dict`, nu `TaskIn`. Clientul trimite {\"titlu\": \"X\"} (recompensa lipsa cu totul). Ce se intampla?",
     "optiuni": {"A": "422 automat, FastAPI valideaza singur orice camp lipsa", "B": "FastAPI accepta payload-ul (e doar un dict oarecare); abia TaskIn.model_validate(payload), scris de tine, prinde lipsa lui recompensa si intoarce {\"valid\": False, ...}",
                 "C": "eroare la pornirea serverului, dict nu e un tip valid de parametru", "D": "payload ramane None, indiferent ce trimite clientul"},
     "corect": "B",
     "explicatie": "FastAPI valideaza AUTOMAT doar parametrii tipati cu un model Pydantic concret. `dict` e un tip generic — orice JSON valid trece de FastAPI fara verificare. Validarea reala se intampla abia in cod, manual, cand chemi TaskIn.model_validate(payload) intr-un try/except — exact scopul acestui endpoint de \"preview\"."},


    # ---------- RUNDA 4: CRUD COMPLET + ERORI (s37: PUT, DELETE, status_code) ----------
    {"runda": 4, "categorie": "status-code-201-doar-la-succes", "puncte": 2,
     "cod": '@app.post("/task-uri", status_code=201)\ndef adauga_task(data: TaskIn):\n    ...\n\n# body invalid trimis: {"titlu": "X", "recompensa": -10, ...}',
     "intrebare": "status_code=201 e setat in decorator. Ce cod HTTP primeste clientul cand trimite date INVALIDE?",
     "optiuni": {"A": "201, pentru ca asa e configurat decoratorul, indiferent de date", "B": "422 — status_code=201 se aplica DOAR raspunsului de succes; validarea esuata intoarce automat 422, inainte sa conteze status_code-ul din decorator",
                 "C": "200, FastAPI ignora status_code=201 la erori", "D": "eroare de configurare, status_code si validarea intra in conflict"},
     "corect": "B",
     "explicatie": "status_code=201 spune doar \"daca functia ruleaza si returneaza ceva cu succes, raspunde cu 201 in loc de 200 implicit\". Validarea Pydantic se intampla INAINTE ca functia sa ruleze — daca esueaza, FastAPI raspunde direct cu 422, iar status_code-ul din decorator nici nu mai e luat in calcul."},

    {"runda": 4, "categorie": "put-apelat-de-doua-ori", "puncte": 2,
     "cod": '@app.put("/task-uri/{task_id}/rezolva")\ndef rezolva_task(task_id: int):\n    for t in task_uri:\n        if t["id"] == task_id:\n            t["rezolvat"] = True\n            return t\n    raise HTTPException(status_code=404, detail="nu exista")\n\n# clientul apeleaza PUT .../1/rezolva de DOUA ori la rand',
     "intrebare": "Al doilea apel PUT .../1/rezolva, pe un task deja rezolvat=True. Ce raspunde?",
     "optiuni": {"A": "404, pentru ca un task deja rezolvat 'nu mai exista' de rezolvat", "B": "200, cu acelasi task, rezolvat ramane True — apelul repetat nu strica nimic",
                 "C": "eroare, nu poti seta True peste True", "D": "500, conflict intern"},
     "corect": "B",
     "explicatie": "Endpointul doar SETEAZA rezolvat=True, indiferent de valoarea anterioara — nu verifica o stare 'deja facut'. Apelat de mai multe ori pe acelasi id, rezultatul final e identic (True), fara efecte secundare suplimentare: exact ce iti doresti de la un PUT de actualizare de stare."},

    {"runda": 4, "categorie": "remove-in-timpul-iterarii", "puncte": 3,
     "cod": '@app.delete("/task-uri/{task_id}")\ndef sterge_task(task_id: int):\n    for t in task_uri:\n        if t["id"] == task_id:\n            task_uri.remove(t)\n            return {"sters": task_id}\n    raise HTTPException(status_code=404, detail="nu exista")',
     "intrebare": "Modificarea listei (remove) IN INTERIORUL buclei for care o parcurge e riscanta in general. De ce merge corect AICI totusi?",
     "optiuni": {"A": "Python interzice modificarea listelor in bucle, deci codul ar da oricum eroare", "B": "return-ul de imediat dupa remove() opreste bucla pe loc — nu mai apuca sa continue iterarea peste lista modificata",
                 "C": "list.remove() creeaza automat o copie noua, sigura de iterat", "D": "FastAPI protejeaza automat listele partajate intre cereri"},
     "corect": "B",
     "explicatie": "Stergerea unui element din lista IN TIMP CE o parcurgi cu for poate sari peste elementul urmator (indicii se muta) — un bug clasic. Aici functioneaza pentru ca, imediat dupa remove(), urmeaza `return`: functia iese pe loc, bucla nu mai continua niciodata peste lista modificata. Fara acel return, comportamentul ar deveni imprevizibil."},

    {"runda": 4, "categorie": "validare-manuala-nu-produce-422", "puncte": 6,
     "cod": '@app.post("/valideaza-task")\ndef valideaza(payload: dict):\n    try:\n        TaskIn.model_validate(payload)\n        return {"valid": True}\n    except ValidationError as e:\n        return {"valid": False, "erori": [er["msg"] for er in e.errors()]}\n\n# clientul trimite un payload INVALID: {"titlu": "X"}  (fara limbaj, dificultate, recompensa)',
     "intrebare": "Payload-ul e invalid (ii lipsesc campuri obligatorii). Ce STATUS HTTP primeste clientul, per total?",
     "optiuni": {"A": "422, la fel ca la orice validare Pydantic esuata", "B": "200 — functia a rulat cu succes si a RETURNAT NORMAL un dict; \"valid\": False e doar o valoare in JSON, nu un semnal de eroare HTTP",
                 "C": "400 Bad Request", "D": "500, pentru ca exceptia ValidationError a fost ridicata"},
     "corect": "B",
     "explicatie": "422 automat apare DOAR cand FastAPI insusi valideaza un parametru tipat cu un model Pydantic si esueaza. Aici, payload e `dict` (netipizat pentru FastAPI), iar exceptia ValidationError e prinsa TU, manual, cu try/except — funcia se termina normal, cu un `return` obisnuit. Din perspectiva HTTP, cererea a reusit (200): mesajul de eroare traieste doar in continutul JSON (\"valid\": False), nu in codul de status. E un gotcha clasic: nu orice eroare din date inseamna automat status de eroare."},
]


# =============================================================
# CONFIGURARE INITIALA
# =============================================================
punctaj_maxim = 0
for q in intrebari:
    punctaj_maxim += q["puncte"]

scor                  = 0
intrebari_corecte     = 0
categorii_stapanite   = set()
intrebari_gresite     = []
runda_curenta         = 0


print("=" * 62)
print("===  QUIZ INTERVIU  -  FastAPI & FastAPI + Pydantic  ===")
print("=" * 62)
print()
print("Fiecare intrebare are o secventa de COD si o EXPLICATIE")
print("dupa raspuns. Citeste codul cu atentie inainte sa raspunzi.")
print()

nume = input("Numele jucatorului (Enter -> 'Candidat'): ").strip()
if nume == "":
    nume = "Candidat"
print(f"\nSucces, {nume}!  Q + Enter = iesire devreme.\n")


# =============================================================
# MOTORUL QUIZ-ULUI
# =============================================================

i = 0
abandonat = False

while i < len(intrebari) and not abandonat:
    q = intrebari[i]

    # Antet de runda
    if q["runda"] != runda_curenta:
        runda_curenta = q["runda"]
        titluri = {
            1: "FASTAPI DE BAZA — APP, DECORATOR, GET",
            2: "PATH & QUERY PARAMETERS + POST FARA VALIDARE (s36)",
            3: "PYDANTIC CA BODY — MODEL, ENUM, FIELD (s37)",
            4: "CRUD COMPLET + ERORI (s37: PUT, DELETE, status_code)",
        }
        print()
        print("=" * 62)
        print(f"  RUNDA {runda_curenta}:  {titluri[runda_curenta]}")
        print("=" * 62)
        print()

    # Afisam intrebarea cu codul
    print(f"Q{i + 1}  [{q['categorie']}, {q['puncte']}p]  -  {q['intrebare']}")
    print()
    print("    --- COD ---")
    for linie in q["cod"].split("\n"):
        print(f"    {linie}")
    print("    -----------")
    print()
    for litera in ("A", "B", "C", "D"):
        print(f"    {litera})  {q['optiuni'][litera]}")
    print()

    # Validare input
    raspuns = ""
    while True:
        raspuns = input("Raspunsul tau (A/B/C/D, Q=iesire): ").strip().upper()
        if raspuns in ("A", "B", "C", "D", "Q"):
            break
        print("  ! Alege A, B, C, D — sau Q ca sa iesi.")

    if raspuns == "Q":
        abandonat = True
        print("\n(ai iesit din quiz)\n")
        break

    # Verificare + AFISARE EXPLICATIE (mereu)
    corect = (raspuns == q["corect"])
    if corect:
        scor += q["puncte"]
        intrebari_corecte += 1
        categorii_stapanite.add(q["categorie"])
        print(f"  >>> CORECT! +{q['puncte']}p   (scor: {scor}/{punctaj_maxim})")
    else:
        intrebari_gresite.append({
            "nr": i + 1,
            "categorie": q["categorie"],
            "raspuns_dat": raspuns,
            "raspuns_corect": q["corect"],
        })
        print(f"  >>> Hmm, nu. Raspuns corect: {q['corect']}) {q['optiuni'][q['corect']]}")
        print(f"      (scor: {scor}/{punctaj_maxim})")

    # Explicatia se afiseaza MEREU (si la corect, si la gresit)
    print(f"  DE CE: {q['explicatie']}")
    print()
    i += 1


# =============================================================
# RAPORT FINAL
# =============================================================
print("=" * 62)
print(f"===          RAPORT INTERVIU  -  {nume}          ===")
print("=" * 62)

procent = (scor / punctaj_maxim * 100) if punctaj_maxim > 0 else 0
print(f"\n  scor:                {scor} / {punctaj_maxim} puncte  ({procent:.0f}%)")
print(f"  intrebari corecte:   {intrebari_corecte} / {i}")

# Evaluare in stil interviu
print()
if procent >= 85:
    print(f"  *** {nume}: profil JUNIOR SOLID — gata de proiecte reale cu API-uri.")
elif procent >= 65:
    print(f"  ** {nume}: profil JUNIOR DECENT — mai cizelam gotcha-urile query/body si validare.")
elif procent >= 45:
    print(f"  * {nume}: profil INCEPATOR — fundamentele sunt, ne trebuie practica.")
else:
    print(f"  {nume}: revizuiti materialul; aproape sigur reusiti la a doua iteratie.")

# Categorii stapanite
print()
print(f"  categorii stapanite ({len(categorii_stapanite)}):")
if categorii_stapanite:
    for cat in sorted(categorii_stapanite):
        print(f"    + {cat}")
else:
    print("    (inca niciuna)")

# Punctele slabe — categorii greșite
if intrebari_gresite:
    print()
    print(f"  zone slabe (de reluat inainte de interviu):")
    zone_slabe = set()
    for g in intrebari_gresite:
        zone_slabe.add(g["categorie"])
    for cat in sorted(zone_slabe):
        print(f"    - {cat}")

    print()
    print(f"  intrebari de revazut:")
    for g in intrebari_gresite:
        print(f"    Q{g['nr']}  [{g['categorie']}]  ai zis {g['raspuns_dat']}, corect {g['raspuns_corect']}")

print()
print("=" * 62)
print("Pregateste-te de interviu: relueaza intrebarile gresite,")
print("apoi reia quiz-ul. La interviu, EXPLICATIA conteaza la fel")
print("de mult cat raspunsul.")
print("=" * 62)