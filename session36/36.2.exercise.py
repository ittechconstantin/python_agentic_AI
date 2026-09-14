# EXERCITIUL 2  (FastAPI)  -  SCRIERE + CALCULE: OBIECTIVE
# =============================================================
#
# CE FACI IN ACEST EXERCITIU (pe scurt)
# --------------------------------------
# Continuarea exercitiului 1. Acolo doar CITEAI. Aici chiar MODIFICI datele
# (adaugi bani) SI calculezi rapoarte din ele (POST + 2x GET):
#   1. POST /obiective/{id}/contribuie?suma=..  -> "am pus 200 lei in
#      obiectivul asta" - ii CRESTE suma-actuala cu suma data.
#   2. GET /progres     -> "cat la suta am strans din FIECARE obiectiv?"
#                           (dict  {nume: procent})
#   3. GET /gata        -> "care obiective sunt COMPLET atinse?" (suma
#                           actuala a ajuns la suma tinta sau a trecut de ea)
#
# Diferenta esentiala fata de exercitiul 1: 1 = citire (GET, nu schimba
# nimic); 2 = scriere (POST, chiar schimba o valoare) + calcule pe urma.
#
#
# CONTEXT (caz real)
# ------------------
# Continui obiectivele de economisire din exercitiul 1: adaugi bani intr-un
# obiectiv (o "contributie") si scoti rapoarte: progresul fiecarui obiectiv
# si care sunt deja atinse.
#
# ATENTIE - diferit fata de lectie: la lectie POST-ul crea o resursa NOUA cu
# parametri simpli. Aici endpoint-ul de contributie combina DOUA lucruri
# invatate separat: un PATH param (care obiectiv) SI un QUERY param (cat
# adaugi) - pe ACELASI endpoint.
#
# `app` si lista `obiective` sunt deja date. Tu scrii ENDPOINT-urile.
#
#
# CE AI DE FACUT
# --------------
# 1. POST /obiective/{obiectiv_id}/contribuie   (query param  suma: float)
#       -> gaseste obiectivul cu id-ul dat, ADAUGA  suma  la  suma_actuala
#          lui, si intoarce obiectivul actualizat. 404 daca id-ul nu exista.
# 2. GET /progres
#       -> dict  {nume: procent}  pentru TOATE obiectivele (procentul =
#          suma_actuala / suma_tinta * 100, rotunjit la 1 zecimala).
# 3. GET /gata
#       -> lista obiectivelor unde  suma_actuala >= suma_tinta  (complet atinse).

# =============================================================

from fastapi import FastAPI, HTTPException

app = FastAPI(title="Buget - obiective (scriere)")

obiective = [
    {"id": 1, "nume": "Vacanta", "suma_tinta": 1000, "suma_actuala": 800},
    {"id": 2, "nume": "Laptop",  "suma_tinta": 2000, "suma_actuala": 1500},
]


# ---- ZONA TA DE LUCRU ---------------------------------------
# TODO: POST /obiective/{obiectiv_id}/contribuie  (path param + query param)
@app.post("/obiective/{obiectiv_id}/contribuie")
def contribuie(obiectiv_id,suma: float):
    for obiectiv in obiective:
        if obiectiv["id"] == obiectiv_id:
            obiectiv["suma_actuala"] += suma
        return obiectiv

    raise HTTPException(status_code=404, detail="Obiectivul nu exista")

# TODO: GET /progres
@app.get("/progres")
def progres():
    for obiectiv in obiective:
        procent = obiectiv["suma_actuala"] / obiectiv["suma_tinta"] * 100
        if obiectiv:
            return{obiectiv["nume"] : obiectiv.get(procent)}

# TODO: GET /gata
@app.get("/gata")
def gata():
    return [obiectiv for obiectiv in obiective if obiectiv["suma_actuala"] > obiectiv["suma_tinta"]]


# ---- COD DE TEST (nu trebuie sa-l modifici) -----------------
from fastapi.testclient import TestClient
c = TestClient(app)

r = c.post("/obiective/1/contribuie", params={"suma": 200})
print("POST .../contribuie?suma=200 -> suma_actuala:", r.json()["suma_actuala"])  # 1000
print("GET /progres ->", c.get("/progres").json())          # {'Vacanta': 100.0, 'Laptop': 75.0}
print("GET /gata ->", [o["nume"] for o in c.get("/gata").json()])  # ['Vacanta']

