# EXERCITIUL 1  (FastAPI + Pydantic)  -  OBIECTIVE: CREARE VALIDATA
# =============================================================
#
# CE FACI IN ACEST EXERCITIU (pe scurt)
# --------------------------------------
# Continui obiectivele de economisire din sesiunea 36. Acolo nu aveai
# validare deloc. Aici definesti o SCHEMA Pydantic pentru un obiectiv nou
# si o folosesti ca BODY intr-un POST (validare automata).
#   1. POST /obiective  -> creezi un obiectiv nou (body validat)
#   2. GET /obiective   -> toate
#   3. GET /obiective/{id} -> unul (404)
#
#
# CONTEXT (caz real)
# ------------------
# Un obiectiv nou are nevoie de un NUME (macar 2 caractere) si o
# SUMA-TINTA (strict pozitiva). `suma_actuala` porneste mereu de la 0 -
# nu o primesti de la client, o setezi TU in cod.
#
# `app` si lista `obiective` sunt deja date. Tu scrii SCHEMA si ENDPOINT-urile.
#
#
# CE AI DE FACUT
# --------------
# 1. Modelul  ObiectivIn(BaseModel):
#       nume: str        cu  min_length=2
#       suma_tinta: float cu  gt=0
# 2. POST /obiective  (body: data: ObiectivIn) -> creeaza
#       {"id": urmatorul, "nume": data.nume, "suma_tinta": data.suma_tinta,
#        "suma_actuala": 0}, il adauga in lista si il intoarce.
# 3. GET /obiective -> toata lista.
# 4. GET /obiective/{obiectiv_id} -> unul; 404 daca nu exista.
#
#
# CERINTE
# -------
#   - model Pydantic ca parametru = body, validat AUTOMAT
#   - `suma_actuala` NU vine de la client - o pui TU, mereu 0 la creare
#
#
# OUTPUT ASTEPTAT (din codul de test de mai jos)
# ----------------------------------------------
#   POST valid -> status 201, {'id': 2, 'nume': 'Laptop', 'suma_tinta': 5000.0, 'suma_actuala': 0}
#   POST nume scurt -> status 422
#   POST suma_tinta <= 0 -> status 422
#   GET /obiective -> count: 2
#   GET /obiective/1 -> nume: Vacanta
#   GET /obiective/99 -> status: 404
#
#
# INDICII
# -------
#   - class ObiectivIn(BaseModel): nume: str = Field(min_length=2); ...
#   - @app.post("/obiective", status_code=201)  def f(data: ObiectivIn): ...
#   - id nou:  len(obiective) + 1
# =============================================================

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="Obiective - creare validata")

obiective = [
    {"id": 1, "nume": "Vacanta", "suma_tinta": 3000, "suma_actuala": 0},
]


# ---- ZONA TA DE LUCRU ---------------------------------------
# TODO: ObiectivIn(BaseModel)
class ObiectivIn(BaseModel):
    nume: str = Field(min_length=2)
    suma_tinta: float = Field(gt=0)

# TODO: POST /obiective
@app.post("/obiective", status_code=201)
def creeaza_obiective(data:ObiectivIn):
    nou = {
        "id": len(obiective) + 1,
        "nume": data.nume,
        "suma_tinta": data.suma_tinta,
        "suma_actuala": 0
    }
    obiective.append(nou)
    return nou

# TODO: GET /obiective
@app.get("/obiective")
def obiectivele():
    return obiective


# TODO: GET /obiective/{obiectiv_id}  (cu 404)
@app.get("/obiective/{obiectiv_id}")
def un_obiectiv(obiectiv_id:int):
    for obiectiv in obiective:
        if obiectiv["id"] == obiectiv_id:
            return obiectiv
    raise HTTPException(status_code=404, detail="Obiectivul nu exista")


# ---- COD DE TEST (nu trebuie sa-l modifici) -----------------
from fastapi.testclient import TestClient
c = TestClient(app)

r = c.post("/obiective", json={"nume": "Laptop", "suma_tinta": 5000})
print("POST valid ->", r.status_code, r.json())
print("POST nume scurt ->", c.post("/obiective", json={"nume": "L", "suma_tinta": 5000}).status_code)
print("POST suma_tinta<=0 ->", c.post("/obiective", json={"nume": "Laptop", "suma_tinta": 0}).status_code)
print("GET /obiective -> count:", len(c.get("/obiective").json()))
print("GET /obiective/1 -> nume:", c.get("/obiective/1").json()["nume"])
print("GET /obiective/99 -> status:", c.get("/obiective/99").status_code)