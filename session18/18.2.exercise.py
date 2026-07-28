# EXERCITIUL 2  -  STATE DE PLATA POLIMORFICE (mostenire + polimorfism)
# =============================================================
#
# CONTEXT (caz real)
# ------------------
# La final de luna calculezi salariile. Ai tipuri diferite de angajati:
#   - platiti la ora (ore x tarif),
#   - cu salariu fix lunar,
#   - manageri (salariu fix + un bonus).
# Vrei sa poti pune TOTI angajatii intr-o lista si sa aduni salariile
# cu un singur "for", fara if-uri gen  if tip == "ora": ...
#
# Solutia: o clasa de baza  Angajat  cu metoda  salariu(), pe care
# fiecare subclasa o suprascrie in felul ei. Codul care aduna nu stie
# ce tip e fiecare - le trateaza uniform (POLIMORFISM).
#
#
# CE AI DE FACUT
# --------------
# --- Angajat (parintele) ---
# 1. __init__(self, nume): salveaza nume.
# 2. salariu(self): intoarce  0  (va fi suprascrisa de copii).
#
# --- AngajatOra(Angajat) ---
# 3. __init__(self, nume, ore, tarif): super().__init__(nume) + ore, tarif.
# 4. salariu(self): intoarce  ore * tarif.
#
# --- AngajatFix(Angajat) ---
# 5. __init__(self, nume, salariu_lunar): super().__init__(nume) + salariu_lunar.
# 6. salariu(self): intoarce  salariu_lunar.
#
# --- Manager(AngajatFix) ---   (mosteneste din AngajatFix!)
# 7. __init__(self, nume, salariu_lunar, bonus):
#      super().__init__(nume, salariu_lunar) + self.bonus.
# 8. salariu(self): EXTINDE - ia salariul de la parinte cu
#    super().salariu()  si aduna  bonus.
#
# --- Functie separata (nu metoda) ---
# 9. total_salarii(angajati): primeste o lista de angajati si intoarce
#    suma tuturor  salariu()-urilor  (polimorfic).
#
#
# CERINTE
# -------
#   - fiecare copil apeleaza  super().__init__(...)
#   - Manager mosteneste din AngajatFix si foloseste  super().salariu()
#   - total_salarii NU face if-uri pe tip: doar  a.salariu()  pe fiecare
#
#
# OUTPUT ASTEPTAT (din codul de test de mai jos)
# ----------------------------------------------
#   Ion: 8000
#   Ana: 6000
#   Horia: 10000
#   total salarii: 24000
#
#
# INDICII
# -------
#   - polimorfism:  sum(a.salariu() for a in angajati)
#   - extindere in Manager:  return super().salariu() + self.bonus
#   - Manager(AngajatFix) - lantul e Manager -> AngajatFix -> Angajat
# =============================================================


# ---- ZONA TA DE LUCRU ---------------------------------------

class Angajat:
    def __init__(self, nume):
        # TODO
        self.nume = nume

    def salariu(self):
        # TODO: 0 (de suprascris)
        return 0


class AngajatOra(Angajat):
    def __init__(self, nume, ore, tarif):
        # TODO: super().__init__(nume) + ore, tarif
        super().__init__(nume)
        self.ore = ore
        self.tarif = tarif

    def salariu(self):
        # TODO: ore * tarif
        return self.ore * self.tarif


class AngajatFix(Angajat):
    def __init__(self, nume, salariu_lunar):
        # TODO: super().__init__(nume) + salariu_lunar
        super().__init__(nume)
        self.salariu_lunar = salariu_lunar

    def salariu(self):
        # TODO: salariu_lunar
        return self.salariu_lunar


class Manager(AngajatFix):
    def __init__(self, nume, salariu_lunar, bonus):
        # TODO: super().__init__(nume, salariu_lunar) + bonus
        super().__init__(nume, salariu_lunar)
        self.bonus = bonus

    def salariu(self):
        # TODO: super().salariu() + bonus
        return super().salariu() + self.bonus


def total_salarii(angajati):
    # TODO: suma salariilor (polimorfic, fara if-uri pe tip)
    return sum(a.salariu() for a in angajati)


# ---- COD DE TEST (nu trebuie sa-l modifici) -----------------
echipa = [
    AngajatOra("Ion", 160, 50),     # 160 * 50 = 8000
    AngajatFix("Ana", 6000),        # 6000
    Manager("Horia", 8000, 2000),   # 8000 + 2000 = 10000
]
for a in echipa:
    print(f"{a.nume}: {a.salariu()}")

print("total salarii:", total_salarii(echipa))   # 24000