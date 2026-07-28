# EXERCITIUL 1  -  PRIMA TA CLASA: UN SENZOR DE TEMPERATURA
# =============================================================
#
# CONTEXT (caz real)
# ------------------
# Lucrezi la o platforma de monitorizare (IoT). Fiecare senzor din
# hala trimite citiri de temperatura. Vrei sa modelezi un senzor ca
# un OBIECT care isi tine singur numele si istoricul citirilor si stie
# sa raspunda la intrebari despre ele (ultima citire, media, maximul).
#
# Pana acum ai fi tinut asta in variabile razlete (o lista aici, un
# nume acolo) si functii separate. Acum le grupam intr-o clasa: DATE
# (numele, citirile) + COMPORTAMENT (adauga citire, media) la un loc.
#
#
# CE AI DE FACUT
# --------------
# Scrie o clasa  Senzor  cu:
#
# 1. __init__(self, nume): primeste numele senzorului si il salveaza
#    in  self.nume. Initializeaza  self.citiri  cu o lista GOALA.
#
# 2. adauga_citire(self, temp): adauga temperatura  temp  la lista
#    self.citiri.
#
# 3. ultima(self): intoarce ultima citire adaugata. Daca nu exista
#    nicio citire, intoarce  None.
#
# 4. media(self): intoarce media citirilor, rotunjita la 2 zecimale.
#    Daca nu exista citiri, intoarce  0.0  (ca sa nu impartim la zero).
#
# 5. maxima(self): intoarce cea mai mare citire (sau None daca nu-s).
#
# 6. __str__(self): intoarce un text de forma:
#       Senzor hala-1: 3 citiri, media 22.5, max 25
#    (daca nu-s citiri:  Senzor hala-1: 0 citiri)
#
#
# CERINTE
# -------
#   - foloseste  class  si  __init__  cu  self
#   - citirile stau intr-un atribut LISTA de instanta (self.citiri)
#   - fiecare metoda lucreaza pe  self, nu pe variabile globale
#
#
# OUTPUT ASTEPTAT (din codul de test de mai jos)
# ----------------------------------------------
#   Senzor hala-1: 0 citiri
#   ultima: 25
#   media: 22.67
#   maxima: 25
#   Senzor hala-1: 3 citiri, media 22.67, max 25
#   senzor gol -> ultima: None media: 0.0
#
#
# INDICII
# -------
#   - lista goala:  self.citiri = []
#   - ultimul element:  self.citiri[-1]
#   - media:  sum(self.citiri) / len(self.citiri)
#   - rotunjire:  round(x, 2)
#   - maxim:  max(self.citiri)
#   - ATENTIE la cazul "lista goala" inainte de [-1], max() sau impartire
# =============================================================


# ---- ZONA TA DE LUCRU ---------------------------------------

class Senzor:
    def __init__(self, nume):
        # TODO: salveaza numele si porneste cu o lista goala de citiri
        self.nume = nume
        self.citire = []

    def adauga_citire(self, temp):
        # TODO: adauga temp in self.citiri
        self.citire.append(temp)

    def ultima(self):
        # TODO: ultima citire sau None daca nu-s citiri
        if not self.citire:
            return None
        return self.citire[-1]

    def media(self):
        # TODO: media rotunjita la 2 zecimale, sau 0.0 daca nu-s citiri
        if not self.citire:
            return 0.0
        return round(sum(self.citire)/len(self.citire), 2)

    def maxima(self):
        # TODO: cea mai mare citire sau None daca nu-s citiri
        if not self.citire:
            return None
        return max(self.citire)

    def __str__(self):
        # TODO: textul descris in enunt
        if not self.citire:
            return f"Senzor {self.nume}: 0 citiri"
        return f"Senzor {self.nume}: {len(self.citire)} citiri, media {self.media()}, max {self.maxima()} "


# ---- COD DE TEST (nu trebuie sa-l modifici) -----------------
s = Senzor("hala-1")
print(s)                        # Senzor hala-1: 0 citiri

s.adauga_citire(24)
s.adauga_citire(19)
s.adauga_citire(25)             # citiri: [24, 19, 25]
print("ultima:", s.ultima())    # ultima: 25
print("media:", s.media())      # media: 22.67
print("maxima:", s.maxima())    # maxima: 25
print(s)                        # Senzor hala-1: 3 citiri, media 22.67, max 25

gol = Senzor("hala-2")
print("senzor gol -> ultima:", gol.ultima(), "media:", gol.media())
