# EXERCITIUL 2  -  PIPELINE DE PROCESARE COMENZI (flux)
# =============================================================
#
# CONTEXT (caz real)
# ------------------
# Lucrezi la un magazin online. Iti vine un FLUX de comenzi si vrei
# venitul total, dar cu doua reguli:
#   - iei in calcul DOAR comenzile platite
#   - aplici un discount (ex: 10%) la fiecare suma
#
# Vrei sa procesezi totul "in flux", cate o comanda pe rand, fara sa
# construiesti liste intermediare uriase. Solutia: un PIPELINE de
# generatori legati in lant:
#       comenzi  ->  doar_platite  ->  cu_discount  ->  sum
# Fiecare etapa primeste elemente de la cea de dinainte si le da mai
# departe, una cate una.
#
#
# CE AI DE FACUT
# --------------
# 1. Scrie un generator  doar_platite(stream)  care primeste un flux
#    de comenzi (dictionare) si da mai departe DOAR pe cele cu
#    c["platita"] == True.
#
# 2. Scrie un generator  cu_discount(stream, procent)  care, pentru
#    fiecare comanda primita, da (yield) suma DUPA discount:
#       suma * (1 - procent / 100)
#
# 3. Leaga-le intr-un pipeline si calculeaza venitul total:
#       total = sum( cu_discount( doar_platite( comenzi() ), 10 ) )
#    Afiseaza:  total cu discount: <total>
#
#
# CERINTE
# -------
#   - foloseste `yield` in ambii generatori
#   - NU construi liste intermediare (lasa datele sa "curga")
#   - foloseste sum(...) direct pe pipeline (e tot lazy)
#
#
# OUTPUT ASTEPTAT
# ---------------
#   total cu discount: 315.0
#
#   Explicatie: comenzile platite au sumele 200, 100, 50.
#   Cu 10% discount: 180 + 90 + 45 = 315.0
#
#
# INDICII
# -------
#   - fiecare comanda e un dict cu cheile: "id", "platita", "suma"
#   - un generator de filtrare: for c in stream: if conditie: yield c
#   - un generator de transformare: for c in stream: yield <ceva>(c)
# =============================================================


# ---- ZONA TA DE LUCRU ---------------------------------------

def comenzi():
    # Fluxul de comenzi (in realitate ar veni dintr-o baza de date)
    yield {"id": 1, "platita": True,  "suma": 200}
    yield {"id": 2, "platita": False, "suma": 150}
    yield {"id": 3, "platita": True,  "suma": 100}
    yield {"id": 4, "platita": True,  "suma": 50}


def doar_platite(stream):
    # TODO: da mai departe (yield) doar comenzile cu "platita" == True
    for comanda in stream:
        if comanda["platita"]:
            yield comanda


def cu_discount(stream, procent):
    # TODO: pentru fiecare comanda, yield suma dupa discount
    suma = 0
    for plata in stream:
        if plata["platita"]:
            suma = plata["suma"]
            yield suma * (1 - procent / 100)



# ---- COD DE TEST (nu trebuie sa-l modifici) -----------------
pipeline = cu_discount(doar_platite(comenzi()), 10)
total = sum(pipeline)
print(f"total cu discount: {total}")