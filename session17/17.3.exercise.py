# EXERCITIUL 3  -  SISTEM DE COMENZI (tot ce am invatat, la un loc)
# =============================================================
#
# CONTEXT (caz real)
# ------------------
# Construiesti backend-ul unui magazin online. Ai nevoie de:
#   - PRODUSE (au nume si pret; pretul trebuie sa fie mereu pozitiv);
#   - COMENZI care CONTIN mai multe produse cu cantitati (compunere:
#     un obiect Comanda tine o lista de alte obiecte / linii);
#   - fiecare comanda primeste automat un ID unic, crescator
#     (contor partajat = atribut de clasa);
#   - totalul comenzii sa fie CALCULAT, nu stocat "de mana"
#     (property read-only), ca sa nu ramana niciodata desincronizat.
#
# Acest exercitiu combina: __init__, self, metode, atribut de clasa
# (contor), compunere (obiecte in obiecte), incapsulare (@property +
# validare) si __str__ / __repr__.
#
#
# CE AI DE FACUT
# --------------
# --- Clasa Produs ---
# 1. __init__(self, nume, pret):
#    - salveaza nume (public)
#    - seteaza pretul PRIN property (self.pret = pret) ca sa valideze
# 2. property  pret  (getter) + setter:
#    - setter: daca pretul <= 0, arunca  ValueError("pret invalid")
#      altfel salveaza in self._pret
# 3. __repr__(self):  Produs('laptop', 4500)
#
# --- Clasa Comanda ---
# 4. atribut de CLASA  _contor = 0  (cate comenzi s-au creat vreodata)
# 5. __init__(self, client):
#    - creste contorul si atribuie un  self.id  unic (1, 2, 3, ...)
#    - salveaza  client
#    - initializeaza  self._linii = []  (lista de linii ale comenzii)
# 6. adauga(self, produs, cantitate):
#    - daca  cantitate <= 0, arunca  ValueError("cantitate invalida")
#    - adauga in self._linii o pereche (produs, cantitate)
# 7. property  total  (DOAR getter):
#    - suma  pret * cantitate  pe toate liniile
# 8. property  nr_produse  (DOAR getter):
#    - suma cantitatilor (cate bucati in total)
# 9. __str__(self):
#       Comanda #1 (Ana): 3 produse, total 9079 lei
#
#
# CERINTE
# -------
#   - id-ul se genereaza din atributul de clasa  _contor  (NU il dai tu)
#   - liniile stau in  self._linii  (ascuns); nu expune lista direct
#   - total si nr_produse sunt CALCULATE (property read-only), nu stocate
#   - pretul produsului e validat in setter
#
#
# OUTPUT ASTEPTAT (din codul de test de mai jos)
# ----------------------------------------------
#   Produs('laptop', 4500)
#   refuzat produs: pret invalid
#   Comanda #1 (Ana): 3 produse, total 9079 lei
#   nr produse: 3
#   total: 9079
#   Comanda #2 (Ion): 1 produse, total 79 lei
#   id comanda 1: 1
#   id comanda 2: 2
#   refuzat: cantitate invalida
#
#
# INDICII
# -------
#   - contor:   Comanda._contor += 1 ; self.id = Comanda._contor
#   - linii:    self._linii.append((produs, cantitate))
#   - total:    sum(p.pret * c for (p, c) in self._linii)
#   - bucati:   sum(c for (p, c) in self._linii)
#   - pretul unui produs dintr-o linie:  p.pret  (e un obiect Produs)
# =============================================================


# ---- ZONA TA DE LUCRU ---------------------------------------

class Produs:
    def __init__(self, nume, pret):
        self.nume = nume
        # TODO: seteaza pretul prin property (cu validare)
        self.pret = pret

    @property
    def pret(self):
        # TODO: intoarce self._pret
        return self._pret

    @pret.setter
    def pret(self, valoare):
        # TODO: valideaza > 0, apoi salveaza in self._pret
        if valoare < 0:
            raise ValueError("pret invalid")
        self._pret = valoare

    def __repr__(self):
        # TODO: Produs('nume', pret)
        return f"Produs('{self.nume}', {self.pret})"


class Comanda:
    # TODO: atribut de clasa _contor = 0
    _contor = 0

    def __init__(self, client):
        # TODO: id unic din contor, salveaza client, lista goala _linii
        Comanda._contor += 1
        self._client = client
        self.id = Comanda._contor
        self._linii = []

    def adauga(self, produs, cantitate):
        # TODO: valideaza cantitate > 0, apoi adauga (produs, cantitate)
        if cantitate <= 0:
            raise ValueError("cantitate invalida")
        self._linii.append((produs, cantitate))

    @property
    def total(self):
        # TODO: suma pret * cantitate pe toate liniile
        return sum(p.pret * c for (p,c) in self._linii)

    @property
    def nr_produse(self):
        # TODO: suma cantitatilor
        return sum(cantitati for produs, cantitati in self._linii)

    def __str__(self):
        # TODO: Comanda #<id> (<client>): <nr> produse, total <total> lei
        return f"Comanda #{self.id}: ({self._client}):{self.nr_produse} produse, total: {self.total}"


# ---- COD DE TEST (nu trebuie sa-l modifici) -----------------
laptop = Produs("laptop", 4500)
mouse  = Produs("mouse", 79)
print(repr(laptop))             # Produs('laptop', 4500)

# pret invalid la creare:
try:
    Produs("gratis", 0)
except ValueError as e:
    print(f"refuzat produs: {e}")    # refuzat produs: pret invalid

c1 = Comanda("Ana")
c1.adauga(laptop, 2)            # 2 x 4500 = 9000
c1.adauga(mouse, 1)            # 1 x 79   =   79
print(c1)                       # Comanda #1 (Ana): 3 produse, total 9079 lei
print("nr produse:", c1.nr_produse)  # nr produse: 3
print("total:", c1.total)       # total: 9079

c2 = Comanda("Ion")
c2.adauga(mouse, 1)
print(c2)                       # Comanda #2 (Ion): 1 produse, total 79 lei

# id-urile sunt unice si crescatoare:
print("id comanda 1:", c1.id)   # id comanda 1: 1
print("id comanda 2:", c2.id)   # id comanda 2: 2

# cantitate invalida:
try:
    c2.adauga(laptop, 0)
except ValueError as e:
    print(f"refuzat: {e}")      # refuzat: cantitate invalida