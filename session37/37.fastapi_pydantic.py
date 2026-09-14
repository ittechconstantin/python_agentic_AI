# FastAPI + Pydantic  -  validarea datelor primite  (Bounty Board)
# =============================================================
# In s36, la  POST /task-uri, am primit datele ca parametri simpli (query):
# suma, limbaj, dificultate - orice text, orice numar, FARA nicio verificare.
# Puteai trimite  recompensa=-500  sau  limbaj="orice-imi-trece-prin-cap"
# si serverul le accepta fara sa clipeasca.
#
# Ideea principala, ca PROBLEMA -> SOLUTIE:
#   PROBLEMA: parametri simpli accepta ORICE. Nu stii daca recompensa e
#             pozitiva, daca limbajul e unul valid, daca titlul nu e gol.
#             Verificarile de mana sunt multe si usor de uitat.
#   SOLUTIA:  descrii datele cu o SCHEMA Pydantic (le stii de la sesiunile
#             34-35). FastAPI o valideaza SINGUR si, la date gresite,
#             intoarce automat  422  cu detalii clare.
#
# Ce trebuie sa stii deja (recap):
#   - FastAPI de baza (s36): app, @app.get/post, path/query param, HTTPException
#   - Pydantic (s34-35): BaseModel, Field, ValidationError
# =============================================================

from enum import Enum
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field, ValidationError

app = FastAPI(title="Bounty Board", version="0.2.0")

task_uri = [
    {"id": 1, "titlu": "Fix bug la login",     "limbaj": "Python",     "dificultate": "usor",  "recompensa": 50,  "rezolvat": False},
    {"id": 2, "titlu": "Adauga dark mode",      "limbaj": "JavaScript", "dificultate": "mediu", "recompensa": 150, "rezolvat": False},
    {"id": 3, "titlu": "Optimizeaza query SQL", "limbaj": "Python",     "dificultate": "greu",  "recompensa": 300, "rezolvat": True},
]


# #############################################################
# PARTEA 1 - UN MODEL PYDANTIC CA BODY (validare automata)
# #############################################################


# 1. PROBLEMA (s36) -> SOLUTIA: schema in loc de parametri simpli
# -------------------------------------------------------------
# Descriem forma unui task nou cu un model. Field(gt=0) = strict pozitiv;
# pentru limbaj si dificultate refolosim Enum, exact ca la sesiunea 34 -
# campul poate avea DOAR una din valorile din Enum, nimic altceva.


class Limbaj(str, Enum):
    PYTHON   = "Python"
    JAVASCRIPT = "JavaScript"
    GO = "Go"
    JAVA = "Java"

class Dificultate(str, Enum):
    USOR = "Usor"
    MEDIU = "Mediu"
    GREU = "Greu"


class TaskIn(BaseModel):
    titlu: str = Field(min_length=3)
    limbaj: Limbaj
    dificultate: Dificultate
    recompensa: float=Field(gt=0)



# 2. ENDPOINT cu model ca body  ->  FastAPI valideaza SINGUR
# -------------------------------------------------------------
# Cand un parametru al functiei e un model Pydantic (nu str/int/float
# simplu), FastAPI il citeste din BODY (JSON), nu din query - asta e
# diferenta fata de s36. Daca datele sunt gresite -> 422 AUTOMAT, nici nu
# mai ajungi in corpul functiei. status_code=201 = "am creat ceva".

@app.post("/task-uri")
def adauga_task(data: TaskIn):
    nou = {
        "id": len(task_uri) + 1,
        "titlu": data.titlu,
        "limbaj": data.limbaj,
        "dificultate": data.dificultate,
        "recompensa": data.recompensa,
        "rezolvat": False,
    }
    task_uri.append(nou)
    return nou


# CUM TESTEZI, pas cu pas (in /docs) - ACUM E DIFERIT fata de s36:
#   1. python 37.fastapi_pydantic.py   apoi   http://127.0.0.1:8000/docs
#   2. POST /task-uri -> "Try it out"
#   3. De data asta apare UN SINGUR camp mare, cu JSON gata schitat:
#        {"titlu": "string", "limbaj": "Python", "dificultate": "usor",
#         "recompensa": 0}
#      NU mai sunt 4 casute separate ca la s36 - pentru ca acum e BODY,
#      nu query. Editezi direct JSON-ul (ex: recompensa: 120) si Execute.
#   4. Incearca sa trimiti  "recompensa": -50  -> vezi 422, cu mesajul
#      exact care camp a picat si de ce (Field gt=0 -> "greater than 0").
#
# Din COD (cu requests) - acum chiar folosesti  json=, la fel ca la s32:
#   requests.post(url, json={"titlu": "...", "limbaj": "Python",
#                             "dificultate": "usor", "recompensa": 120})


# #############################################################
# PARTEA 2 - CITIRE + ERORI DETALIATE
# #############################################################


@app.get("/task-uri")
def lista_taskuri():
    return task_uri



# 3. .errors()  -  raport DETALIAT (util cand vrei sa-l arati clientului)
# -------------------------------------------------------------
# FastAPI iti da automat 422 pe date invalide. Dar poti oricand valida
# TU manual o schema (de ex. intr-un endpoint cu forma dinamica) si
# transforma erorile intr-un raspuns propriu - ai facut asta la s34-35.


@app.post("/valideaza-task")
def valideaza(payload: dict):
    try:
        TaskIn.model_validate(payload)
        return{'valid': True}
    except ValidationError as e:
        return {'valid': False, "erori": [eroare['msg']  for eroare in e.errors()]}




# #############################################################
# PARTEA 3 - CRUD COMPLET (PUT + DELETE) + CALCUL
# #############################################################


# 4. PUT  -  marchezi un task ca REZOLVAT
# -------------------------------------------------------------

@app.put("/task-uri/{task_id}/rezolva")
def rezolva_task(task_id:int):
    for t in task_uri:
        if t['id'] == task_id:
            t['rezolvat'] = True
            return t
    raise HTTPException(status_code=404, detail=f"Task-ul {task_id} nu exista.")

# 5. DELETE
# -------------------------------------------------------------




# =============================================================
# CUM RULEZI ACEST FISIER
# =============================================================
#       python 37.fastapi_pydantic.py
# apoi:  http://127.0.0.1:8000/docs
# =============================================================
import uvicorn
uvicorn.run(app, host="127.0.0.1", port=8003)


# =============================================================
# RECAP / IDEI CHEIE
# =============================================================
# - Un parametru de tip model Pydantic = BODY, validat AUTOMAT de FastAPI;
#   date gresite -> 422 automat, cu detalii, fara cod scris de tine.
# - Field(gt=0), Field(min_length=...), Enum (ca la sesiunea 34) - constrangeri.
# - response_model / status_code=201 - controlezi forma si codul raspunsului.
# - Diferenta fata de s36: parametri simpli (str/int/float) = query, chiar
#   si pe POST; un model Pydantic = body. /docs arata diferit: casute
#   separate (query) vs un singur camp JSON (body).
# - CRUD complet: GET (citire), POST (creare, body validat), PUT (update),
#   DELETE (stergere).
#
# In s38: task-urile le salvam in MySQL cu SQLAlchemy (nu se mai pierd).
# =============================================================