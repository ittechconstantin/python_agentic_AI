# EXERCITIUL 1  -  INVENTAR DE JOC (dunder de baza)
# =============================================================
#
# CONTEXT (caz real)
# ------------------
# Intr-un joc RPG, inventarul tine "stive" de iteme identice (5 sageti,
# 3 potiuni etc). Vrei ca obiectul StocItem sa se comporte "natural":
#   - sa il poti aduna cu  +  (combini doua stive DIN ACELASI item);
#   - sa il poti compara cu  ==  (doua stive egale);
#   - sa arate frumos la  print.
# Pentru asta implementam metodele "dunder": __add__, __eq__, __str__.
# La fel ca la  Bani  din lectie (care refuza sa adune RON cu EUR),
# StocItem refuza sa combine doua iteme DIFERITE.
#
#
# CE AI DE FACUT
# --------------
# Scrie o clasa  StocItem  cu:
#
# 1. __init__(self, nume, cantitate): salveaza numele itemului si cantitatea.
#
# 2. __str__(self): intoarce  f"{cantitate}x {nume}".
#
# 3. __eq__(self, alt): doua stive sunt egale daca au ACELASI nume SI
#    ACEEASI cantitate.
#    - daca  alt  NU e un StocItem, intoarce  NotImplemented
#    - altfel compara  (self.nume, self.cantitate) == (alt.nume, alt.cantitate)
#
# 4. __add__(self, alt): daca  alt  are ACELASI nume, intoarce un StocItem
#    NOU cu cantitatile insumate. Daca numele difera, ridica
#    ValueError("nu poti combina iteme diferite").

# =============================================================


# ---- ZONA TA DE LUCRU ---------------------------------------

class StocItem:
    def __init__(self, nume, cantitate):
        # TODO: salveaza nume si cantitate
        self.nume = nume
        self.cantitate = cantitate

    def __str__(self):
        # TODO: "Xx nume"
        return f"{self.cantitate}x {self.nume}"

    def __eq__(self, alt):
        # TODO: egal daca acelasi nume SI aceeasi cantitate (NotImplemented altfel)
        if not isinstance(alt, StocItem):
            return NotImplemented
        return (self.nume, self.cantitate) == (alt.nume, alt.cantitate)

    def __add__(self, alt):
        # TODO: daca acelasi nume, StocItem nou cu cantitatile insumate;
        #       altfel ValueError("nu poti combina iteme diferite")
        if self.nume != alt.nume:
            raise ValueError("nu poti combina iteme diferite")
        return StocItem(self.nume, self.cantitate + alt.cantitate)


# ---- COD DE TEST (nu trebuie sa-l modifici) -----------------
s1 = StocItem("Potiune de viata", 5)
s2 = StocItem("Potiune de viata", 3)
s3 = StocItem("Sageata", 10)

print(s1)                       # 5x Potiune de viata
print(s1 + s2)                  # 8x Potiune de viata

print("egale?", StocItem("Sageata", 10) == StocItem("Sageata", 10))  # True
print("diferite?", s1 == s3)                          # False
print("vs text:", s1 == "5x Potiune de viata")         # False

try:
    s1 + s3
except ValueError as e:
    print(f"refuzat: {e}")      # refuzat: nu poti combina iteme diferite