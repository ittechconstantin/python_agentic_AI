# EXERCITIUL 4  -  CONT BANCAR CU COMISION SI ISTORIC
# =============================================================
#
# CONTEXT (caz real)
# ------------------
# La o banca, un cont nu doar tine un sold - el trebuie sa:
#   - refuze operatiile invalide (depuneri negative, retrageri peste
#     fonduri) ca soldul sa NU ajunga niciodata intr-o stare gresita;
#   - retina un ISTORIC al tranzactiilor (pentru extrasul de cont);
#   - aplice un COMISION fix la fiecare retragere (regula bancii,
#     aceeasi pentru toate conturile -> atribut de clasa).
#
# Combinam: incapsulare (soldul ascuns, modificat doar prin metode),
# atribut de clasa (comisionul comun), o lista de istoric si un
# @property read-only.
#
#
# CE AI DE FACUT
# --------------
# Scrie o clasa  ContBancar  cu:
#
# 1. atribut de CLASA  COMISION_RETRAGERE = 1  (1 leu, fix, la retragere)
#
# 2. __init__(self, titular, sold_initial):
#    - salveaza titular (public)
#    - pune soldul in  self._sold  (ascuns, conventie)
#    - initializeaza  self._istoric = []  (lista de texte)
#
# 3. depune(self, suma):
#    - daca  suma <= 0, arunca  ValueError("suma invalida")
#    - creste soldul cu suma
#    - adauga in istoric textul:  f"depunere: +{suma}"
#
# 4. retrage(self, suma):
#    - daca  suma <= 0, arunca  ValueError("suma invalida")
#    - total_necesar = suma + COMISION_RETRAGERE
#    - daca  total_necesar > sold, arunca  ValueError("fonduri insuficiente")
#    - scade din sold suma SI comisionul
#    - adauga in istoric:
#         f"retragere: -{suma} (comision -{ContBancar.COMISION_RETRAGERE})"
#
# 5. property  sold  (DOAR getter): intoarce self._sold
#
# 6. property  nr_tranzactii  (DOAR getter): cate operatii sunt in istoric
#
# 7. property  istoric  (DOAR getter): intoarce o COPIE a listei
#    (list(self._istoric)) - ca nimeni din afara sa nu modifice
#    istoricul intern direct
#
# 8. __str__(self):
#       ContBancar(Ana, sold=998 lei)
#
#
# CERINTE
# -------
#   - soldul real sta in  self._sold  si se schimba DOAR prin depune/retrage
#   - comisionul se ia din atributul de clasa (ContBancar.COMISION_RETRAGERE)
#   - sold, nr_tranzactii, istoric sunt property-uri read-only (fara setter)
#   - property istoric intoarce o COPIE, nu lista interna
#
#
# OUTPUT ASTEPTAT (din codul de test de mai jos)
# ----------------------------------------------
#   ContBancar(Ana, sold=998 lei)
#   sold: 998
#   tranzactii: 3
#   - depunere: +500
#   - retragere: -300 (comision -1)
#   - retragere: -200 (comision -1)
#   refuzat: suma invalida
#   refuzat: fonduri insuficiente
#   istoricul intern nu a fost afectat: 3
#
#
# INDICII
# -------
#   - atribut de clasa: il scrii direct in corpul clasei, il citesti cu
#     ContBancar.COMISION_RETRAGERE
#   - istoric: self._istoric.append(text)
#   - copie a listei: list(self._istoric)
#   - nr_tranzactii: len(self._istoric)
# =============================================================


# ---- ZONA TA DE LUCRU ---------------------------------------

class ContBancar:
    # TODO: atribut de clasa COMISION_RETRAGERE = 1
    COMISION_RETRAGERE = 1

    def __init__(self, titular, sold_initial):
        # TODO: titular, self._sold, self._istoric = []
        self.titular = titular
        self._sold = sold_initial
        self._istoric = []

    def depune(self, suma):
        # TODO: valideaza suma > 0, creste soldul, adauga in istoric
        if suma <= 0:
            raise ValueError("suma invalida")
        self._sold = self._sold + suma
        self._istoric.append(f"depunere: +{suma}")


    def retrage(self, suma):
        # TODO: valideaza suma > 0 si fondurile (suma + comision), scade, log
        if suma <= 0:
            raise ValueError("suma invalida")
        total_necesar = suma + ContBancar.COMISION_RETRAGERE
        if total_necesar > self.sold:
            raise ValueError("fonduri insuficiente")
        self._sold -= (suma + ContBancar.COMISION_RETRAGERE)
        self._istoric.append (f"retragere: -{suma} (comision -{ContBancar.COMISION_RETRAGERE})")


    @property
    def sold(self):
        # TODO: intoarce self._sold
        return self._sold

    @property
    def nr_tranzactii(self):
        # TODO: cate operatii sunt in istoric
        return len(self._istoric)

    @property
    def istoric(self):
        # TODO: intoarce o COPIE a listei de istoric
        return list(self._istoric)

    def __str__(self):
        # TODO: ContBancar(titular, sold=... lei)
        return f"ContBancar({self.titular}, sold={self.sold} lei)"


# ---- COD DE TEST (nu trebuie sa-l modifici) -----------------
cont = ContBancar("Ana", 1000)
cont.depune(500)                # sold 1500
cont.retrage(300)               # -300 -1 comision -> 1199
cont.retrage(200)               # -200 -1 comision -> 998

print(cont)                     # ContBancar(Ana, sold=998 lei)
print("sold:", cont.sold)       # sold: 998
print("tranzactii:", cont.nr_tranzactii)   # tranzactii: 3
for linie in cont.istoric:
    print("-", linie)

# operatii care trebuie refuzate:
try:
    cont.depune(-5)
except ValueError as e:
    print(f"refuzat: {e}")      # refuzat: suma invalida

try:
    cont.retrage(100000)
except ValueError as e:
    print(f"refuzat: {e}")      # refuzat: fonduri insuficiente

# property istoric intoarce o COPIE: modificarea ei nu strica obiectul
copie = cont.istoric
copie.append("HACK")
print("istoricul intern nu a fost afectat:", cont.nr_tranzactii)   # 3