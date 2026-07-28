# EXERCITIUL 3  -  IERARHIE DE CONTURI BANCARE (capstone mostenire)
# =============================================================
#
# CONTEXT (caz real)
# ------------------
# Continuam contul bancar din sesiunea 17, dar acum avem TIPURI de
# cont care se comporta diferit la retragere:
#   - Cont          - contul de baza: nu poti retrage mai mult decat ai.
#   - ContEconomii  - are dobanda; poti "aplica dobanda" ca sa creasca.
#   - ContCurent    - permite "descoperire" (overdraft): poti intra pe
#                     minus, dar doar pana la o limita negociata.
#
# Toate sunt conturi (au titular, sold, depunere/retragere), deci pun
# la comun logica in  Cont  si SPECIALIZEAZA in subclase prin override.
# La final le tratam polimorfic: o lista de conturi, un singur for.
#
#
# CE AI DE FACUT
# --------------
# --- Cont (parintele) ---
# 1. __init__(self, titular, sold): salveaza titular; pune soldul in
#    self._sold (ascuns).
# 2. property  sold  (DOAR getter): intoarce self._sold.
# 3. depune(self, suma): daca suma <= 0 -> ValueError("suma invalida");
#    altfel creste soldul.
# 4. retrage(self, suma): daca  suma > sold -> ValueError("fonduri
#    insuficiente"); altfel scade din sold.
# 5. __str__(self):  f"Cont {titular}: {sold} lei"
#
# --- ContEconomii(Cont) ---
# 6. atribut de CLASA  DOBANDA = 0.10  (10%).
# 7. aplica_dobanda(self): creste soldul cu  round(sold * DOBANDA)
#    (rotunjit la intreg).
# 8. __str__(self): EXTINDE - super().__str__() + " (economii)".
#
# --- ContCurent(Cont) ---
# 9. __init__(self, titular, sold, limita_descoperire):
#    super().__init__(titular, sold) + self.limita_descoperire.
# 10. retrage(self, suma): OVERRIDE - permite sold negativ, dar nu sub
#     -limita_descoperire. Adica daca  suma > sold + limita_descoperire
#     -> ValueError("peste limita de descoperire"); altfel scade.
# 11. __str__(self): super().__str__() + " (curent)".
#
#
# CERINTE
# -------
#   - subclasele apeleaza  super().__init__(...)  si  super().__str__()
#   - ContEconomii foloseste atributul de clasa DOBANDA
#   - ContCurent SUPRASCRIE retrage (regula diferita de descoperire)
#   - la final tratam conturile polimorfic (un singur for pe __str__)
#
#
# OUTPUT ASTEPTAT (din codul de test de mai jos)
# ----------------------------------------------
#   dupa dobanda: 1100
#   sold curent dupa retragere: -200
#   refuzat (curent): peste limita de descoperire
#   refuzat (baza): fonduri insuficiente
#   --- toate conturile ---
#   Cont Ana: 1100 lei (economii)
#   Cont Ion: -200 lei (curent)
#   Cont Maria: 5000 lei
#
#
# INDICII
# -------
#   - dobanda:  self._sold += round(self._sold * ContEconomii.DOBANDA)
#   - overdraft:  if suma > self._sold + self.limita_descoperire: raise ...
#   - extindere __str__:  return super().__str__() + " (economii)"
#   - accesezi self._sold direct din subclasa (e acelasi obiect)
# =============================================================


# ---- ZONA TA DE LUCRU ---------------------------------------

class Cont:
    def __init__(self, titular, sold):
        # TODO: titular + self._sold
        self.titular = titular
        self._sold = sold

    @property
    def sold(self):
        # TODO: self._sold
        return self._sold

    def depune(self, suma):
        # TODO: valideaza > 0, creste soldul
        if suma <= 0:
            raise ValueError("suma invalida")
        self._sold += suma

    def retrage(self, suma):
        # TODO: valideaza fonduri, scade din sold
        if suma > self._sold:
            raise ValueError("fonduri insuficiente")
        self._sold -= suma

    def __str__(self):
        # TODO: "Cont <titular>: <sold> lei"
        return f"Cont {self.titular}: {self._sold} lei"


class ContEconomii(Cont):
    # TODO: atribut de clasa DOBANDA = 0.10
    DOBANDA = 0.10

    def aplica_dobanda(self):
        # TODO: creste soldul cu round(sold * DOBANDA)
        self._sold += round(self._sold * ContEconomii.DOBANDA)

    def __str__(self):
        # TODO: super().__str__() + " (economii)"
        return super().__str__() + f" (economii)"


class ContCurent(Cont):
    def __init__(self, titular, sold, limita_descoperire):
        # TODO: super().__init__(...) + limita_descoperire
        super().__init__(titular, sold)
        self.limita_descoperire = limita_descoperire

    def retrage(self, suma):
        # TODO: permite minus pana la -limita_descoperire
        if suma > self._sold + self.limita_descoperire:
            raise ValueError("peste limita de descoperire")
        self._sold -= suma

    def __str__(self):
        # TODO: super().__str__() + " (curent)"
        return super().__str__() + f" (curent)"


# ---- COD DE TEST (nu trebuie sa-l modifici) -----------------
econ = ContEconomii("Ana", 1000)
econ.aplica_dobanda()               # 1000 + 10% = 1100
print("dupa dobanda:", econ.sold)   # dupa dobanda: 1100

curent = ContCurent("Ion", 500, 300)   # poate cobora pana la -300
curent.retrage(700)                 # 500 - 700 = -200 (in limita)
print("sold curent dupa retragere:", curent.sold)   # -200

try:
    curent.retrage(200)             # ar duce la -400, sub limita -300
except ValueError as e:
    print(f"refuzat (curent): {e}") # peste limita de descoperire

baza = Cont("Test", 100)
try:
    baza.retrage(500)               # contul de baza nu permite minus
except ValueError as e:
    print(f"refuzat (baza): {e}")   # fonduri insuficiente

# polimorfism: o lista de conturi diferite, un singur for:
print("--- toate conturile ---")
conturi = [econ, curent, Cont("Maria", 5000)]
for c in conturi:
    print(c)