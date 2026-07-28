# EXERCITIUL 2  -  INCAPSULARE: UN UTILIZATOR CU DATE VALIDATE
# =============================================================
#
# CONTEXT (caz real)
# ------------------
# La inregistrarea pe un site, datele unui utilizator trebuie sa fie
# mereu VALIDE: email-ul sa contina "@", varsta sa fie intre 0 si 120.
# Daca lasi atributele "publice", oricine poate face  user.varsta = -5
# si obiectul ajunge intr-o stare imposibila.
#
# Solutia OOP e INCAPSULAREA: tii datele reale ascunse (self._email,
# self._varsta) si le expui prin  @property  +  @setter, unde pui
# VALIDAREA. Din afara pare un atribut normal (user.varsta = 30), dar
# in spate trece prin verificari.
#
#
# CE AI DE FACUT
# --------------
# Scrie o clasa  Utilizator  cu:
#
# 1. __init__(self, nume, email, varsta):
#    - salveaza  nume  ca atribut public normal
#    - seteaza email si varsta PRIN property-uri (self.email = email,
#      self.varsta = varsta) ca sa treaca prin validare inca de la creare
#
# 2. property  email  (getter) + setter:
#    - getter: intoarce self._email
#    - setter: daca in valoare NU apare "@", arunca
#         ValueError("email invalid")
#      altfel salveaza in self._email
#
# 3. property  varsta  (getter) + setter:
#    - getter: intoarce self._varsta
#    - setter: daca valoarea nu e intre 0 si 120 (inclusiv), arunca
#         ValueError("varsta invalida")
#      altfel salveaza in self._varsta
#
# 4. property  este_major  (DOAR getter, fara setter):
#    - intoarce True daca varsta >= 18, altfel False
#
# 5. __str__(self):
#       Utilizator(Ana, ana@site.ro, 30 ani)
#
#
# CERINTE
# -------
#   - datele reale stau in  self._email  si  self._varsta  (ascunse)
#   - validarea sta in SETTER-e, nu imprastiata prin cod
#   - in __init__ folosesti  self.email = ...  (NU self._email = ...)
#     ca sa treaca prin validare de la inceput
#   - este_major nu are setter (e read-only, calculat din varsta)
#
#
# OUTPUT ASTEPTAT (din codul de test de mai jos)
# ----------------------------------------------
#   Utilizator(Ana, ana@site.ro, 30 ani)
#   major? True
#   dupa update: 17
#   major acum? False
#   refuzat: email invalid
#   refuzat: varsta invalida
#   creare refuzata: email invalid
#
#
# INDICII
# -------
#   - getter:      @property
#                  def varsta(self): return self._varsta
#   - setter:      @varsta.setter
#                  def varsta(self, val): ...
#   - "@" in email:   if "@" not in valoare: raise ValueError(...)
#   - interval:    if not (0 <= val <= 120): raise ValueError(...)
#   - property fara setter = read-only (este_major)
# =============================================================


# ---- ZONA TA DE LUCRU ---------------------------------------

class Utilizator:
    def __init__(self, nume, email, varsta):
        self.nume = nume
        self.email = email
        self.varsta = varsta

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, valoare):
        if "@" not in valoare:
            raise ValueError(f"email invalid")
        self._email = valoare

    @property
    def varsta(self):
        return self._varsta

    @varsta.setter
    def varsta(self, valoare):
        if  not (0 <= valoare <= 120):
            raise ValueError(f"varsta invalida")
        self._varsta = valoare

    @property
    def este_major(self):
        # TODO: True daca varsta >= 18
        return True if self.varsta >= 18 else False

    def __str__(self):
        # TODO: Utilizator(nume, email, varsta ani)
        return f"{self.nume} {self.email} {self.varsta}"


# ---- COD DE TEST (nu trebuie sa-l modifici) -----------------

u = Utilizator("Ana", "ana@site.ro", 30)
print(u)                        # Utilizator(Ana, ana@site.ro, 30 ani)
print("major?", u.este_major)   # major? True

u.varsta = 17                   # trece prin setter (valid)
print("dupa update:", u.varsta) # dupa update: 17
print("major acum?", u.este_major)   # major acum? False

# validari care trebuie sa refuze:
try:
    u.email = "fara-arond"
except ValueError as e:
    print(f"refuzat: {e}")      # refuzat: email invalid

try:
    u.varsta = 200
except ValueError as e:
    print(f"refuzat: {e}")      # refuzat: varsta invalida

# validarea trebuie sa functioneze SI la creare:
try:
    Utilizator("Ion", "ion-fara-arond", 40)
except ValueError as e:
    print(f"creare refuzata: {e}")   # creare refuzata: email invalid