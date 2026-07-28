# TEMA PENTRU ACASA 2  -  TRAFIC WEB ZILNIC (un dunder nou: __radd__)
# =============================================================
#
# CONTEXT (caz real)
# ------------------
# Site-ul tau primeste un numar de cereri HTTP in fiecare zi. Vrei sa:
#   - aduni traficul din doua zile cu  +   (ai vazut asta la Bani, in
#     lectie);
#   - inmultesti traficul unei zile "medii" cu 30, ca sa faci o ESTIMARE
#     pentru o luna (TraficZilnic(1200) * 30 -> TraficZilnic(36000));
#   - folosesti  sum(lista_de_trafic)  ca sa aduni traficul unei
#     saptamani intregi dintr-o data, fara bucla scrisa de mana.
#
# Aici e ideea NOUA fata de lectie:  sum(lista)  incepe intern cu
# 0 + primul_element. Daca ai definit doar __add__, Python incearca
# 0 + TraficZilnic(1200) - dar int-ul 0 nu stie sa se adune cu un
# TraficZilnic, deci arunca eroare INAINTE sa apuce sa incerce varianta
# ta. Solutia: mai definesti __radd__ ("reflected add" - "aduna-ma pe
# mine cand sunt in DREAPTA unui plus care altfel ar esua").
#
#
# CE AI DE FACUT
# --------------
# Scrie o clasa  TraficZilnic  cu:
#
# 1. __init__(self, cereri): salveaza numarul de cereri HTTP dintr-o zi.
#
# 2. __repr__(self):  f"TraficZilnic({cereri} cereri)"   (asa apare la
#    print/sum)
#
# 3. __add__(self, alt): intoarce un TraficZilnic NOU cu
#    self.cereri + alt.cereri.
#
# 4. __radd__(self, alt): intoarce un TraficZilnic NOU cu
#    self.cereri + alt   (alt e un NUMAR aici, de obicei 0 - vine de
#    la  sum(), care porneste cu  0 + primul_trafic).
#
# 5. __mul__(self, zile): intoarce un TraficZilnic NOU cu
#    self.cereri * zile  (zile e un numar, ex. 30 pentru estimare lunara).

# =============================================================


# ---- ZONA TA DE LUCRU ---------------------------------------

class TraficZilnic:
    def __init__(self, cereri):
        # TODO: salveaza cereri
        self.cereri = cereri

    def __repr__(self):
        # TODO: "TraficZilnic(cereri cereri)"
        return f"TraficZilnic({self.cereri} cereri)"

    def __add__(self, alt):
        # TODO: TraficZilnic nou cu cererile insumate
        return TraficZilnic(self.cereri + alt.cereri)

    def __radd__(self, alt):
        # TODO: TraficZilnic nou cu self.cereri + alt (alt e un numar)
        return TraficZilnic(self.cereri + alt)

    def __mul__(self, zile):
        # TODO: TraficZilnic nou cu cererile inmultite cu zile
        return TraficZilnic(self.cereri * zile)


# ---- COD DE TEST (nu trebuie sa-l modifici) -----------------
luni = TraficZilnic(1200)
marti = TraficZilnic(1500)
print("luni + marti:", luni + marti)  luni.__add__(marti)             # TraficZilnic(2700 cereri)

estimare_lunara = TraficZilnic(1200) * 30
print("estimare pe 30 de zile:", estimare_lunara)  # TraficZilnic(36000 cereri)

saptamana = [TraficZilnic(1200), TraficZilnic(1500), TraficZilnic(900)]
print("total saptamanal (sum):", sum(saptamana))   # TraficZilnic(3600 cereri)
