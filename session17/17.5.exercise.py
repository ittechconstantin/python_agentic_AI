# EXERCITIUL 5  -  GESTIUNE DE STOC INTR-O MAGAZIE
# =============================================================
#
# CONTEXT (caz real)
# ------------------
# Administrezi stocul unei magazii. Fiecare produs are un pret si o
# cantitate. Ai nevoie de un obiect Magazie care:
#   - tine evidenta produselor (nume -> pret, cantitate);
#   - stie sa vanda (scade stocul) si refuza operatiile imposibile
#     (produs inexistent, stoc insuficient);
#   - calculeaza valoarea totala a stocului;
#   - avertizeaza care produse au scazut sub un prag de reaprovizionare
#     (acelasi prag pentru toata magazia -> atribut de clasa).
#
# Acesta e un exercitiu "de sinteza": un dictionar ca atribut de
# instanta, un atribut de clasa (pragul), metode cu validare,
# property-uri read-only si __str__.
#
#
# CE AI DE FACUT
# --------------
# Scrie o clasa  Magazie  cu:
#
# 1. atribut de CLASA  PRAG_MINIM = 5
#    (un produs cu cantitate STRICT sub 5 e "stoc scazut")
#
# 2. __init__(self, nume):
#    - salveaza nume (public)
#    - initializeaza  self._stoc = {}   (dict: nume_produs -> dict cu
#      cheile "pret" si "cant")
#
# 3. adauga_produs(self, nume, pret, cantitate):
#    - daca  pret <= 0, arunca  ValueError("pret invalid")
#    - daca  cantitate < 0, arunca  ValueError("cantitate invalida")
#    - salveaza:  self._stoc[nume] = {"pret": pret, "cant": cantitate}
#
# 4. vinde(self, nume, cantitate):
#    - daca  nume  nu e in stoc, arunca  ValueError("produs inexistent")
#    - daca  cantitate > stocul disponibil, arunca
#         ValueError("stoc insuficient")
#    - altfel scade  cantitate  din stocul acelui produs
#
# 5. property  valoare_totala  (DOAR getter):
#    - suma  pret * cant  pe toate produsele
#
# 6. produse_sub_prag(self):
#    - intoarce o LISTA cu numele produselor a caror cantitate e
#      STRICT sub PRAG_MINIM (in ordinea in care au fost adaugate)
#
# 7. __str__(self):
#       Magazie Depozit 1: 3 produse, valoare 51237 lei
#    (numarul de produse = cate produse DISTINCTE sunt in stoc)
#
#
# CERINTE
# -------
#   - stocul sta in  self._stoc  (dict ascuns), modificat doar prin metode
#   - pragul se ia din atributul de clasa (Magazie.PRAG_MINIM)
#   - valoare_totala e property read-only (calculat, nu stocat)
#   - dictionarul pastreaza ordinea de inserare (deci lista sub prag e
#     in ordinea adaugarii)
#
#
# OUTPUT ASTEPTAT (din codul de test de mai jos)
# ----------------------------------------------
#   Magazie Depozit 1: 3 produse, valoare 51237 lei
#   valoare dupa vanzari: 41037
#   sub prag: ['mouse', 'monitor']
#   refuzat: stoc insuficient
#   refuzat: produs inexistent
#   refuzat: pret invalid
#
#
# INDICII
# -------
#   - exista in stoc:   if nume not in self._stoc: raise ...
#   - stoc disponibil:  self._stoc[nume]["cant"]
#   - valoare:  sum(p["pret"] * p["cant"] for p in self._stoc.values())
#   - sub prag:  [nume for nume, p in self._stoc.items()
#                 if p["cant"] < Magazie.PRAG_MINIM]
#   - nr produse distincte:  len(self._stoc)
# =============================================================


# ---- ZONA TA DE LUCRU ---------------------------------------

class Magazie:
    # TODO: atribut de clasa PRAG_MINIM = 5
    PRAG_MINIM = 5

    def __init__(self, nume):
        # TODO: nume + self._stoc = {}
        self.nume = nume
        self._stoc = {}

    def adauga_produs(self, nume, pret, cantitate):
        # TODO: valideaza pret > 0 si cantitate >= 0, apoi salveaza in _stoc
        if pret <= 0:
            raise ValueError(f"pret invalid")
        if cantitate < 0:
            raise ValueError(f"cantitate invalida")
        self._stoc[nume] = {"pret": pret, "cant": cantitate}


    def vinde(self, nume, cantitate):
        # TODO: verifica ca exista si ca ai stoc, apoi scade cantitatea
        if nume not in self._stoc:
            raise ValueError(f"produs inexistent")
        if cantitate > self._stoc[nume]["cant"]:
            raise ValueError(f"stoc insuficient")
        self._stoc[nume]["cant"] -= cantitate

    @property
    def valoare_totala(self):
        # TODO: suma pret * cant pe toate produsele
        return sum(p["pret"] * p["cant"] for p in self._stoc.values())

    def produse_sub_prag(self):
        # TODO: lista numelor cu cantitate STRICT sub PRAG_MINIM
        return [nume for nume, p in self._stoc.items() if p["cant"] < Magazie.PRAG_MINIM]

    def __str__(self):
        # TODO: Magazie <nume>: <n> produse, valoare <valoare> lei
        return f"Magazie {self.nume}: {len(self._stoc)} produse, valoare {m.valoare_totala}"


# ---- COD DE TEST (nu trebuie sa-l modifici) -----------------
m = Magazie("Depozit 1")
m.adauga_produs("laptop", 4500, 10)   # 10 * 4500 = 45000
m.adauga_produs("mouse", 79, 3)      #  3 *   79 =   237
m.adauga_produs("monitor", 1200, 5)   #  5 * 1200 =  6000
print(m)                        # Magazie Depozit 1: 3 produse, valoare 51237 lei

m.vinde("laptop", 2)            # laptop -> 8 bucati
m.vinde("monitor", 1)           # monitor -> 4 bucati
print("valoare dupa vanzari:", m.valoare_totala)   # 41037

# sub prag (cant < 5): mouse (3), monitor (4)
print("sub prag:", m.produse_sub_prag())   # sub prag: ['mouse', 'monitor']

# operatii care trebuie refuzate:
try:
    m.vinde("laptop", 100)
except ValueError as e:
    print(f"refuzat: {e}")      # refuzat: stoc insuficient

try:
    m.vinde("tastatura", 1)
except ValueError as e:
    print(f"refuzat: {e}")      # refuzat: produs inexistent

try:
    m.adauga_produs("gratis", -5, 3)
except ValueError as e:
    print(f"refuzat: {e}")      # refuzat: pret invalid