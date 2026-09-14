# EXERCITIUL 1  (FastAPI)  -  CITIRE: OBIECTIVE DE ECONOMISIRE
# =============================================================
#
# CE FACI IN ACEST EXERCITIU (pe scurt)
# --------------------------------------
# Acesta e un exercitiu DOAR DE CITIRE: NU modifici nimic, doar intrebi
# datele in 3 feluri diferite (toate 3 sunt GET):
#   1. GET /obiective              -> "da-mi TOATE obiectivele"
#   2. GET /obiective/{id}         -> "da-mi DOAR obiectivul cu id-ul asta"
#                                      (eroare 404 daca nu exista)
#   3. GET /aproape-gata           -> "da-mi doar obiectivele APROAPE gata"
#                                      (procent atins >= un prag)
#
# (In exercitiul 2 faci partea complementara: SCRIEREA + calcule derivate.)
#
#
# CONTEXT (caz real)
# ------------------
# Pe langa tranzactii, aplicatia de buget mai are o parte: OBIECTIVE de
# economisire (ex: "vreau 3000 lei pentru vacanta"). Fiecare obiectiv are o
# suma-tinta si o suma-actuala stransa pana acum.
#
# ATENTIE - diferit fata de lectie: la lectie ai filtrat dupa un camp care
# se POTRIVESTE EXACT (tip == "cheltuiala"). Aici, la punctul 3, filtrezi
# dupa o valoare CALCULATA (procentul atins) - nu exista un camp gata facut
# in date, trebuie sa il calculezi TU in interiorul filtrului.
#
# `app` si lista `obiective` sunt deja date. Tu scrii ENDPOINT-urile.
#
#
# CE AI DE FACUT
# --------------
# 1. GET /obiective                 -> intoarce toata lista  obiective.
# 2. GET /obiective/{obiectiv_id}   -> obiectivul cu  id == obiectiv_id
#                                      (path param).  daca nu exista ->
#                                      HTTPException 404.
# 3. GET /aproape-gata              -> query param  prag: float = 80;
#                                      intoarce doar obiectivele unde
#                                      PROCENTUL atins ( suma_actuala /
#                                      suma_tinta * 100 ) este  >= prag.
#
#
# CERINTE
# -------
#   - path param cu type hint:  def f(obiectiv_id: int)
#   - query param cu default:   def f(prag: float = 80)
#   - 404:  raise HTTPException(status_code=404, detail=...)
#   - la punctul 3 CALCULEZI procentul, nu il citesti dintr-un camp
#
#
# OUTPUT ASTEPTAT (din codul de test de mai jos)
# ----------------------------------------------
#   GET /obiective -> count: 3
#   GET /obiective/2 -> nume: Laptop nou
#   GET /obiective/99 -> status: 404
#   GET /aproape-gata (prag implicit 80) -> ['Vacanta', 'Fond urgente']
#
# =============================================================

from fastapi import FastAPI, HTTPException

app = FastAPI(title="Buget - obiective (citire)")

obiective = [
    {"id": 1, "nume": "Vacanta",      "suma_tinta": 3000,  "suma_actuala": 2700},
    {"id": 2, "nume": "Laptop nou",   "suma_tinta": 5000,  "suma_actuala": 1000},
    {"id": 3, "nume": "Fond urgente", "suma_tinta": 10000, "suma_actuala": 8000},
]


# ---- ZONA TA DE LUCRU ---------------------------------------
# TODO: GET /obiective
@app.get("/obiective")
def obiectivele():
    return obiective

# TODO: GET /obiective/{obiectiv_id}  (cu 404)
@app.get("/obiective/{obiectiv_id}")
def un_obiectiv(obiectiv_id: int):
    for obiectiv in obiective:
        if obiectiv["id"] == obiectiv_id:
            return obiectiv
    raise HTTPException(status_code=404, detail="Obiectivul nu exista")

# TODO: GET /aproape-gata  (query param prag, default 80, filtru pe procent)
@app.get("/aproape-gata")
def aproape_gata(prag: float = 80):

    if prag < 80:
        return None
    else:
        return [obiectiv for obiectiv in obiective if obiectiv["suma_actuala"] / obiectiv["suma_tinta"] * 100 >= prag]



# ---- COD DE TEST (nu trebuie sa-l modifici) -----------------
from fastapi.testclient import TestClient
c = TestClient(app)

print("GET /obiective -> count:", len(c.get("/obiective").json()))              # 3
print("GET /obiective/2 -> nume:", c.get("/obiective/2").json()["nume"])        # Laptop nou
print("GET /obiective/99 -> status:", c.get("/obiective/99").status_code)       # 404
print("GET /aproape-gata ->",
      [o["nume"] for o in c.get("/aproape-gata").json()])   # ['Vacanta', 'Fond urgente']