# EXERCITIUL 1  -  ANALIZA UNUI FISIER DE LOG MARE (lazy)
# =============================================================
#
# CONTEXT (caz real)
# ------------------
# Administrezi un server. Fisierul de log are milioane de linii si
# zeci de GB - NU il poti incarca tot in memorie. Vrei sa numeri
# cate erori au aparut si sa le vezi, citind fisierul O LINIE PE RAND
# (lazy), nu tot deodata.
#
# In viata reala, un fisier deschis e deja un generator de linii:
#       with open("server.log") as f:
#           for linie in f:        # o linie pe rand, NU tot fisierul
#               ...
# Aici simulam "liniile fisierului" cu un generator, ca exercitiul sa
# ruleze fara un fisier real pe disc - dar logica e identica.
#
#
# CE AI DE FACUT
# --------------
# 1. Scrie un generator  citeste_linii()  care da pe rand (yield)
#    liniile de log de mai jos (le ai gata, in zona de lucru).
#
# 2. Scrie un generator  doar_erori(linii)  care primeste un flux de
#    linii si da mai departe DOAR liniile care contin "ERROR".
#    (filtrare lazy: nu construieste nicio lista)
#
# 3. Folosind cele doua, FARA sa pui toate liniile intr-o lista:
#       - numara cate erori sunt si afiseaza:  numar erori: <N>
#       - afiseaza fiecare linie de eroare
#
#
# CERINTE
# -------
#   - foloseste `yield` (nu construi liste intermediare)
#   - pentru numarat, foloseste:  sum(1 for _ in doar_erori(...))
#   - retine: un generator se consuma O SINGURA DATA. Daca il parcurgi
#     o data ca sa numeri, trebuie sa-l RECREEZI ca sa-l parcurgi iar.
#
#
# OUTPUT ASTEPTAT
# ---------------
#   numar erori: 3
#   2026-01-01 ERROR conectare esuata la baza de date
#   2026-01-01 ERROR plata respinsa
#   2026-01-01 ERROR timeout serviciu extern
#
#
# INDICII
# -------
#   - "ERROR" in linie  -> True/False (verifici daca textul apare)
#   - doar_erori(citeste_linii()) e un PIPELINE: sursa -> filtru
#   - `_` e un nume de variabila "nu ma intereseaza valoarea"
# =============================================================


# ---- ZONA TA DE LUCRU ---------------------------------------

def citeste_linii():
    # Liniile "fisierului" (in realitate ar veni din open(...))
    yield "2026-01-01 INFO  start aplicatie"
    yield "2026-01-01 ERROR conectare esuata la baza de date"
    yield "2026-01-01 INFO  utilizator autentificat"
    yield "2026-01-01 WARN  raspuns lent"
    yield "2026-01-01 ERROR plata respinsa"
    yield "2026-01-01 INFO  raport generat"
    yield "2026-01-01 ERROR timeout serviciu extern"


def doar_erori(linii):
    # TODO: da mai departe (yield) doar liniile care contin "ERROR"
    for linie in linii:
        if "ERROR" in linie:
            yield linie


# ---- COD DE TEST (nu trebuie sa-l modifici) -----------------
nr = sum(1 for _ in doar_erori(citeste_linii()))
print("numar erori:", nr)

# le afisam (recreem generatorul, fiindca cel de sus s-a consumat)
for linie in doar_erori(citeste_linii()):
    print(linie)
