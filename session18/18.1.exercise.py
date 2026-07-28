# EXERCITIUL 1  -  PRODUS FIZIC vs PRODUS DIGITAL (mostenire de baza)
# =============================================================
#
# CONTEXT (caz real)
# ------------------
# Intr-un magazin online ai produse fizice (au un pret) si produse
# digitale (au acelasi pret, dar in plus o dimensiune de descarcare
# in MB). Un ProdusDigital ESTE UN Produs - are tot ce are un produs,
# plus ceva specific. Exact cazul pentru MOSTENIRE: pui la comun ce e
# comun si adaugi in copil doar diferenta.
#
#
# CE AI DE FACUT
# --------------
# --- Clasa Produs (parintele) ---
# 1. __init__(self, nume, pret): salveaza nume si pret.
# 2. descriere(self): intoarce  f"{nume} - {pret} lei".
#
# --- Clasa ProdusDigital (copilul, mosteneste din Produs) ---
# 3. __init__(self, nume, pret, dimensiune_mb):
#    - apeleaza  super().__init__(nume, pret)  ca sa NU rescrii
#      setarea lui nume si pret
#    - adauga  self.dimensiune_mb = dimensiune_mb
# 4. descriere(self): EXTINDE metoda parintelui:
#    - ia textul de la parinte cu  super().descriere()
#    - adauga la coada  f" (digital, {dimensiune_mb} MB)"
#
#
# CERINTE
# -------
#   - ProdusDigital mosteneste din Produs:  class ProdusDigital(Produs)
#   - folosesti  super().__init__(...)  (nu rescrii self.nume = ...)
#   - descriere() din copil apeleaza  super().descriere()  (extindere)
#
#
# OUTPUT ASTEPTAT (din codul de test de mai jos)
# ----------------------------------------------
#   carte - 45 lei
#   ebook - 39 lei (digital, 12 MB)
#   e digital un Produs? True
#   e carte un ProdusDigital? False
#
#
# INDICII
# -------
#   - mostenire:  class ProdusDigital(Produs):
#   - init parinte:  super().__init__(nume, pret)
#   - extindere:  baza = super().descriere(); return baza + " (...)"
#   - verificare tip:  isinstance(obiect, Clasa)
# =============================================================


# ---- ZONA TA DE LUCRU ---------------------------------------

class Produs:
    def __init__(self, nume, pret):
        # TODO: salveaza nume si pret
        self.nume = nume
        self.pret = pret

    def descriere(self):
        # TODO: "nume - pret lei"
        return f"{self.nume} - {self.pret} lei"


class ProdusDigital(Produs):
    def __init__(self, nume, pret, dimensiune_mb):
        # TODO: super().__init__(...) + self.dimensiune_mb
        super().__init__(nume, pret)
        self.dimensiune_mb = dimensiune_mb

    def descriere(self):
        # TODO: super().descriere() + " (digital, X MB)"
        baza = super().descriere()
        return f"{baza} (digital, {self.dimensiune_mb})"


# ---- COD DE TEST (nu trebuie sa-l modifici) -----------------
carte = Produs("carte", 45)
ebook = ProdusDigital("ebook", 39, 12)

print(carte.descriere())        # carte - 45 lei
print(ebook.descriere())        # ebook - 39 lei (digital, 12 MB)

print("e digital un Produs?", isinstance(ebook, Produs))       # True
print("e carte un ProdusDigital?", isinstance(carte, ProdusDigital))  # False