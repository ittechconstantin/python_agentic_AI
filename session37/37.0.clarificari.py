# TREI LUCRURI CARE VA INCURCA  (si de ce va incurca)
# =============================================================
# Fisierul asta nu preda ceva nou. Ia trei intrebari care au aparut in
# sesiunile 36 si 37 si le lamureste pana la capat:
#
#   1. Type hints. Peste tot ai auzit ca sunt "doar o sugestie, Python
#      nu le verifica". Dar in FastAPI `task_id: int` chiar face ceva -
#      respinge "abc". Cine minte?
#
#   2. if __name__ == "__main__":  - il copiezi de la inceputul cursului
#      si merge. Dar ce e, de fapt, `__name__`?
#
#   3. params= sau json= ? Cand trimiti date catre un endpoint FastAPI,
#      de unde stii care din ele? Aici se incurca toata lumea, si nu
#      pentru ca ar fi greu - ci pentru ca regula NU e cea la care te
#      gandesti prima data.
#
# Fisierul chiar ruleaza:  python3 37.0.clarificari.py
# La final vezi demonstratiile, nu doar teoria.
# =============================================================


# #############################################################
# PARTEA 1 - TYPE HINTS: si sugestie, si obligatoriu
# #############################################################
#
# Intrebarea, pusa cinstit
# -------------------------
# Ti s-a spus ca type hints-urile sunt decorative. Ca Python nu le
# verifica. Ca poti scrie  def f(x: int)  si sa-i dai un string, si nu
# se intampla nimic.
#
# Apoi scrii in FastAPI:
#
#       @app.get("/task-uri/{task_id}")
#       def un_task(task_id: int):
#           ...
#
# ...si cand ceri /task-uri/abc primesti 422. Deci ceva le verifica.
#
# Raspunsul: ambele lucruri sunt adevarate, dar vorbesc despre doi
# actori diferiti. PYTHON nu verifica nimic. FASTAPI verifica tot.
#
#
# Ce face Python cu un type hint
# -------------------------------
# Nimic. Zero. Cand scrii:
#
#       def aduna(a: int, b: int) -> int:
#           return a + b
#
#       aduna("sal", "ut")     # merge, intoarce "salut"
#
# ...interpretorul nu se uita niciodata la acele `: int`. Le citeste la
# definirea functiei, le PUNE DEOPARTE si trece mai departe. Nu e o
# scapare, e prin design - Python a fost dintotdeauna un limbaj in care
# tipul conteaza la rulare, nu la scriere.
#
# Si aici e partea pe care o rateaza aproape toata lumea: "le pune
# deoparte" nu inseamna "le arunca". Le pune intr-un dictionar lipit de
# functie, care se numeste __annotations__:
#
#       aduna.__annotations__
#       -> {'a': <class 'int'>, 'b': <class 'int'>, 'return': <class 'int'>}
#
# Deci informatia exista, la rulare, si e citibila de oricine o vrea.
# Python nu o foloseste. Dar o LASA ACOLO.
#
#
# Ce face FastAPI cu acelasi type hint
# -------------------------------------
# Exact ce ai banuit deja: se uita in __annotations__.
#
# Cand scrii @app.get("/task-uri/{task_id}"), FastAPI iti inspecteaza
# functia inainte sa porneasca serverul. Vede ca are un parametru
# `task_id` si ca adnotarea lui e `int`. De acolo incolo stie trei
# lucruri pe care nu i le-ai spus explicit niciodata:
#
#   - de unde sa ia valoarea:  "task_id" apare intre acolade in cale,
#     deci o scoate din URL
#   - in ce sa o transforme:   din retea vine mereu TEXT; "3" trebuie
#     sa devina numarul 3, si o face automat
#   - ce sa faca daca nu poate: "abc" nu devine niciun int, deci
#     raspunde 422 si nici nu-ti mai cheama functia
#
# Al treilea punct e cel important. Cand primesti 422, codul tau NU a
# rulat. Nu ai apucat sa ajungi la `for t in task_uri`. Verificarea s-a
# intamplat inainte, la usa.
#
# Deci regula reala nu e "type hints-urile sunt optionale", ci:
#
#       Type hints-urile sunt optionale PENTRU PYTHON.
#       Pentru o biblioteca care alege sa le citeasca, sunt instructiuni.
#
# FastAPI e o astfel de biblioteca. Pydantic la fel - de asta
# `recompensa: float` intr-un BaseModel chiar respinge textul. Sunt
# printre putinele locuri din Python unde ce scrii dupa doua puncte
# schimba efectiv comportamentul programului.
#
# Practic: in FastAPI, adnotarile nu sunt documentatie. Sunt cod.
# Daca scoti `: int` din  def un_task(task_id: int)  nu ai "pierdut un
# comentariu" - ai schimbat endpointul, care acum primeste text brut si
# nu mai compara niciodata egal cu un id numeric.


# #############################################################
# PARTEA 2 - if __name__ == "__main__":
# #############################################################
#
# Il scrii de la inceputul cursului si functioneaza, deci nu l-ai pus
# la indoiala. Merita totusi doua minute, pentru ca in FastAPI incepe
# sa conteze cu adevarat.
#
#
# `__name__` e o variabila normala
# ---------------------------------
# Fiecare fisier .py, cand e incarcat, primeste automat de la Python o
# variabila numita `__name__`. Nu o declari tu, exista deja. Contine un
# string, si valoarea lui depinde de UN SINGUR lucru: cum a ajuns
# fisierul sa fie incarcat.
#
#   - L-ai pornit tu direct, cu  python3 fisier.py
#         -> __name__ este "__main__"
#
#   - L-a importat altcineva, cu  import fisier
#         -> __name__ este "fisier"  (numele modulului)
#
# Atat. Toata "magia" e o variabila cu doua valori posibile.
#
#
# La ce foloseste
# ----------------
# Cand importi un fisier, Python ii RULEAZA tot continutul, de sus in
# jos. Nu doar defintiile - tot. Asta surprinde pe multi.
#
# Imagineaza-te cu doua fisiere:
#
#       # calcule.py
#       def aduna(a, b):
#           return a + b
#
#       print("test:", aduna(2, 3))
#
#       # main.py
#       from calcule import aduna
#
# Rulezi main.py. Nu ai cerut nimanui sa printeze nimic. Si totusi apare
# "test: 5" pe ecran, pentru ca `import` a executat tot fisierul
# calcule.py ca sa ajunga la definitia lui `aduna`.
#
# `if __name__ == "__main__":` e gardul care rezolva asta. Pui inauntru
# ce vrei sa se intample DOAR cand fisierul e rulat direct:
#
#       def aduna(a, b):
#           return a + b
#
#       if __name__ == "__main__":
#           print("test:", aduna(2, 3))
#
# Acum fisierul are doua vieti. Rulat direct - isi face demonstratia.
# Importat - ofera doar functia, in tacere. Exact de asta il ai in
# exercitii: codul de test ruleaza cand deschizi tu fisierul, dar nu
# incurca pe nimeni daca cineva vrea doar sa imprumute o functie.
#
#
# De ce conteaza in FastAPI in mod special
# -----------------------------------------
# La finalul fisierelor de FastAPI ai:
#
#       if __name__ == "__main__":
#           import uvicorn
#           uvicorn.run(app, host="127.0.0.1", port=8000)
#
# Un server FastAPI se porneste in doua feluri, si asta e cheia:
#
#   (a)  python3 37.fastapi_pydantic.py
#        Rulezi TU fisierul direct. __name__ e "__main__", conditia e
#        adevarata, uvicorn.run porneste serverul. Asa lucrezi in curs.
#
#   (b)  uvicorn 37.fastapi_pydantic:app --reload
#        Aici pornesti uvicorn, iar el IMPORTA fisierul tau ca sa ia
#        obiectul `app`. Fiind import, __name__ e numele modulului, nu
#        "__main__" - deci blocul NU se executa. Si foarte bine:
#        uvicorn deja ruleaza, nu vrei sa porneasca un al doilea server
#        dinauntrul primului. Forma (b) e cea folosita in productie,
#        pentru ca asa merge --reload (restart automat la salvare).
#
# Cu alte cuvinte: acel `if` face ca acelasi fisier sa functioneze in
# ambele moduri, fara sa-l modifici. Scos, varianta (b) fie se blocheaza,
# fie porneste un server in server.
#
# Si o observatie mica, dar care lamureste multe: FastAPI si uvicorn nu
# au nevoie de blocul asta ca sa afle rutele. Rutele s-au inregistrat
# deja, mai sus in fisier, in momentul in care Python a executat fiecare
# @app.get(...). Cand uvicorn ajunge la `app`, totul e gata montat.
# Blocul de la final doar APASA butonul de pornire.


# #############################################################
# PARTEA 3 - params= sau json= ?  (query vs body)
# #############################################################
#
# Aici se incurca toata lumea, si merita spus de ce: pentru ca regula pe
# care o ghiceste toata lumea e gresita, dar suficient de aproape de
# adevar cat sa functioneze cateva zile si apoi sa te lase balta.
#
#
# Regula GRESITA pe care o deduci singur
# ---------------------------------------
#       "GET are date in URL, POST are date in body."
#
# Suna logic. E si aproape adevarat in majoritatea API-urilor din lume.
# In FastAPI nu e regula. Ai vazut-o cazand chiar in sesiunea 36, unde
# un POST primea datele prin URL:
#
#       @app.post("/task-uri")
#       def adauga_task(titlu: str, limbaj: str, recompensa: float):
#           ...
#
#       # se apeleaza asa, desi e POST:
#       requests.post(url, params={"titlu": "X", "recompensa": 100})
#
#
# Regula ADEVARATA
# -----------------
# In FastAPI, locul din care se citeste un parametru nu depinde de
# metoda HTTP. Depinde de TIPUL parametrului din semnatura functiei.
# (Da - tot type hints. Partea 1 se plateste aici.)
#
# Trei cazuri, si nu mai sunt altele:
#
#   1. Tip simplu (int, str, float, bool) SI numele apare intre acolade
#      in cale        ->  PATH param, se ia din adresa
#
#           @app.get("/task-uri/{task_id}")
#           def f(task_id: int)                 # /task-uri/3
#
#   2. Tip simplu, dar numele NU apare in cale
#                     ->  QUERY param, se ia de dupa ? din adresa
#
#           @app.get("/dupa-limbaj")
#           def f(limbaj: str | None = None)    # /dupa-limbaj?limbaj=Python
#
#      Asta ramane valabil si pe POST, si pe PUT. Metoda nu conteaza.
#
#   3. Model Pydantic (BaseModel)
#                     ->  BODY, se citeste JSON-ul trimis de client
#
#           @app.post("/task-uri")
#           def f(data: TaskIn)                 # datele vin in body
#
# Deci intrebarea corecta nu e "e GET sau POST?", ci:
#
#       "Parametrul e un tip simplu, sau e un model Pydantic?"
#
#
# Acum, cealalta jumatate: ce face requests
# ------------------------------------------
# De partea clientului, `params=` si `json=` sunt doua destinatii
# diferite din cererea HTTP, si niciuna nu "cauta" cealalta:
#
#       params={"limbaj": "Python"}
#           -> lipeste in URL:   http://.../dupa-limbaj?limbaj=Python
#           -> aterizeaza in QUERY
#
#       json={"titlu": "X", "recompensa": 100}
#           -> trimite in corpul cererii, ca text JSON, cu headerul
#              Content-Type: application/json
#           -> aterizeaza in BODY
#
# Si de aici tot tabelul de potriviri:
#
#   endpointul asteapta      clientul trimite     ce se intampla
#   -----------------------------------------------------------------
#   tip simplu (query)       params={...}         merge
#   tip simplu (query)       json={...}           422 - campuri lipsa
#   model Pydantic (body)    json={...}           merge
#   model Pydantic (body)    params={...}         422 - campuri lipsa
#
# Cele doua randuri cu 422 sunt aceeasi greseala, in oglinda. Si e o
# greseala care deruteaza pentru ca mesajul de eroare zice "field
# required" - suna ca si cum nu ai fi trimis datele. Le-ai trimis. Doar
# ca le-ai pus in sertarul in care serverul nu se uita.
#
#
# Cum verifici in 5 secunde, fara sa ghicesti
# --------------------------------------------
# Deschide /docs si apasa "Try it out" pe endpointul respectiv:
#
#   - vezi mai multe CASUTE separate, cate una per camp
#         -> sunt query params  -> in cod folosesti  params=
#
#   - vezi UN SINGUR camp mare, cu un JSON schitat inauntru
#         -> e body  -> in cod folosesti  json=
#
# Diferenta asta se vede clar daca pui alaturi 36.fastapi.py si
# 37.fastapi_pydantic.py: acelasi POST /task-uri, aceeasi idee, dar in
# s36 apar 4 casute, iar in s37 un singur camp JSON. Singurul lucru care
# s-a schimbat intre ele a fost tipul parametrului.
#
# Mai e un indiciu, dupa ce apesi Execute: /docs iti arata "Request URL".
# Daca parametrii apar acolo, lipiti dupa ?, au plecat ca query. Daca
# URL-ul e curat, datele au plecat in body.
#
#
# Doua capcane inrudite
# ----------------------
# `data=` NU e acelasi lucru cu `json=`. `data={"a": 1}` trimite tot in
# body, dar in format de formular web (a=1), nu JSON. FastAPI il citeste
# doar daca ai declarat explicit Form(...) in endpoint. Cu un model
# Pydantic obisnuit, iti va da tot 422. Daca vrei JSON, scrie json=.
#
# Si: poti combina linistit path + body pe acelasi endpoint. Nu e o
# exceptie, e regula de mai sus aplicata de doua ori - fiecare parametru
# e judecat separat, dupa tipul lui:
#
#       @app.put("/obiective/{obiectiv_id}/contribuie")
#       def contribuie(obiectiv_id: int, data: ContributieIn):
#           ...                    # ^ path (tip simplu, e in cale)
#                                  #                ^ body (model)
#
#       requests.put(".../obiective/1/contribuie", json={"suma": 200})
#
# Ai facut exact asta in 37.2.exercise.py.


# =============================================================
# DEMONSTRATII  (astea chiar ruleaza)
# =============================================================
# Tot ce e scris mai sus e verificabil. Mai jos sunt demonstratiile, iar
# faptul ca sunt puse sub  if __name__ == "__main__":  e in sine exemplul
# din Partea 2: daca cineva ar importa fisierul asta, nu s-ar afisa nimic.

if __name__ == "__main__":

    print("=" * 62)
    print("  PARTEA 1  -  type hints")
    print("=" * 62)

    def aduna(a: int, b: int) -> int:
        return a + b

    # Python nu verifica nimic: dam doua string-uri unei functii "de int"
    print("  aduna('sal', 'ut') =", aduna("sal", "ut"), " <- Python nu s-a plans")

    # ...dar adnotarile exista, la rulare, si oricine le poate citi:
    print("  aduna.__annotations__ =", aduna.__annotations__)
    print("  ^ exact de aici isi ia FastAPI informatia")
    print()

    print("=" * 62)
    print("  PARTEA 2  -  __name__")
    print("=" * 62)
    print(f"  __name__ este acum: {__name__!r}")
    print("  (ai pornit fisierul direct; daca l-ar importa cineva,")
    print("   ar fi numele modulului, iar blocul asta ar fi sarit)")
    print()

    print("=" * 62)
    print("  PARTEA 3  -  query vs body, pe un server adevarat")
    print("=" * 62)

    from fastapi import FastAPI
    from fastapi.testclient import TestClient
    from pydantic import BaseModel, Field

    app = FastAPI()

    # Endpoint A: parametri simpli -> FastAPI ii asteapta din QUERY
    @app.post("/query-style")
    def query_style(titlu: str, recompensa: float):
        return {"unde": "query", "titlu": titlu, "recompensa": recompensa}

    # Endpoint B: model Pydantic -> FastAPI il asteapta din BODY
    class TaskIn(BaseModel):
        titlu: str = Field(min_length=3)
        recompensa: float = Field(gt=0)

    @app.post("/body-style")
    def body_style(data: TaskIn):
        return {"unde": "body", "titlu": data.titlu, "recompensa": data.recompensa}

    c = TestClient(app)
    date = {"titlu": "Fix bug", "recompensa": 100}

    print()
    print("  ENDPOINT A  (parametri simpli = query)")
    r = c.post("/query-style", params=date)
    print(f"    params= -> {r.status_code}  {r.json() if r.status_code == 200 else 'esuat'}")
    r = c.post("/query-style", json=date)
    print(f"    json=   -> {r.status_code}  <- aceleasi date, sertarul gresit")

    print()
    print("  ENDPOINT B  (model Pydantic = body)")
    r = c.post("/body-style", json=date)
    print(f"    json=   -> {r.status_code}  {r.json() if r.status_code == 200 else 'esuat'}")
    r = c.post("/body-style", params=date)
    print(f"    params= -> {r.status_code}  <- exact aceeasi greseala, in oglinda")

    print()
    print("  Amandoua sunt POST. Amandoua primesc aceleasi date.")
    print("  Singura diferenta: tipul parametrului din semnatura functiei.")

    print()
    print("  Cum arata un 422 pe dinauntru:")
    r = c.post("/body-style", params=date)
    for eroare in r.json()["detail"]:
        print(f"    camp {eroare['loc']} -> {eroare['msg']}")
    print("    ('Field required', desi datele AU fost trimise - doar nu in body)")
    print()


# =============================================================
# PE SCURT, DACA RETII TREI RANDURI
# =============================================================
# - Type hints: Python le ignora, dar le pastreaza in __annotations__.
#   FastAPI le citeste de acolo si le trateaza ca instructiuni. In
#   FastAPI, adnotarea nu e comentariu, e cod.
#
# - if __name__ == "__main__":  ruleaza doar cand pornesti TU fisierul,
#   nu si cand il importa altcineva. In FastAPI, asta lasa acelasi
#   fisier sa mearga si cu  python3 fisier.py,  si cu  uvicorn fisier:app.
#
# - params= vs json=: nu se decide dupa GET/POST, ci dupa tipul
#   parametrului. Tip simplu -> query (params=). Model Pydantic -> body
#   (json=). Cand esti nesigur, deschide /docs: mai multe casute inseamna
#   query, un singur camp JSON inseamna body.
# =============================================================