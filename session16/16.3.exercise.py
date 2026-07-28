# EXERCITIUL 3  -  FLUX INFINIT + GENERATOR CU STARE
# =============================================================
#
# CONTEXT (caz real)
# ------------------
# Doua nevoi reale dintr-o aplicatie de facturare:
#
#   A) NUMERE DE FACTURA: ai nevoie de un "robinet" care da numere de
#      factura unice, la nesfarsit: FACT-0001, FACT-0002, FACT-0003...
#      Nu stii de la inceput cate vei emite, deci o lista nu merge -
#      ai nevoie de un flux INFINIT din care iei cate ai nevoie.
#
#   B) TOTAL CUMULATIV: pe masura ce intra sume pe un extras de cont,
#      vrei sa vezi soldul DUPA fiecare operatiune (totalul de pana
#      acum). Un generator poate tine STARE intre yield-uri (o variabila
#      locala care "supravietuieste"), deci e perfect pentru asta.
#
#
# CE AI DE FACUT
# --------------
# A) Scrie un generator INFINIT  numar_factura()  care da pe rand:
#       "FACT-0001", "FACT-0002", "FACT-0003", ...
#    (numarul are mereu 4 cifre, completat cu zerouri in fata).
#    Apoi ia primele 5 cu  itertools.islice  si afiseaza-le ca lista.
#
# B) Scrie un generator  total_cumulativ(stream)  care, pentru fiecare
#    suma primita, da (yield) TOTALUL de pana atunci (suma curenta +
#    tot ce a fost inainte). Tine un acumulator intr-o variabila locala.
#    Afiseaza  list(total_cumulativ([10, 20, 30, 40])).
#
#
# CERINTE
# -------
#   - la A) foloseste  while True  (flux infinit) si  itertools.islice
#     ca sa iei exact 5 (NU folosi break manual aici)
#   - la B) variabila acumulator se declara INAINTE de bucla, ca sa
#     "tina minte" intre yield-uri
#
#
# OUTPUT ASTEPTAT
# ---------------
#   ['FACT-0001', 'FACT-0002', 'FACT-0003', 'FACT-0004', 'FACT-0005']
#   [10, 30, 60, 100]
#
#
# INDICII
# -------
#   - format cu zerouri in fata:  f"FACT-{n:04d}"   (04d = 4 cifre)
#   - islice(generator, 5)  ia primele 5 elemente dintr-un flux infinit
#   - total cumulativ pentru [10,20,30,40]:
#       10 -> 10
#       20 -> 30   (10+20)
#       30 -> 60   (30+30)
#       40 -> 100  (60+40)
# =============================================================

from itertools import islice


# ---- ZONA TA DE LUCRU ---------------------------------------

def numar_factura():
    # TODO: flux INFINIT: FACT-0001, FACT-0002, ... (while True + yield)
    n = 1
    while True:
        yield f"FACT-{n:04d}"
        n += 1



def total_cumulativ(stream):
    # TODO: pentru fiecare valoare, yield totalul de pana acum
    #       (acumulator declarat inainte de bucla)
    total = 0
    for i in stream:
        total += i
        yield total


# ---- COD DE TEST (nu trebuie sa-l modifici) -----------------
print(list(islice(numar_factura(), 5)))
print(list(total_cumulativ([10, 20, 30, 40])))
