# OOP  -  POLIMORFISM
# =============================================================
# Cuvantul vine din greaca:  poli = multe,  morphe = forme.
# In OOP inseamna: ACEEASI INTERFATA, dar IMPLEMENTARI DIFERITE.
#
# Concret: scrii UN cod care lucreaza pe un obiect fara sa-i pese de
# tipul exact, atat timp cat obiectul are metodele asteptate. Ii dai
# obiecte de tipuri diferite, fiecare se comporta in stilul lui - dar
# codul tau ramane neschimbat.
#
# In sesiunea 18 am vazut un gust de polimorfism (o lista de Email/SMS
# tratate uniform). Acum mergem in profunzime.
#
# In Python polimorfismul apare in 3 forme:
#   1) prin MOSTENIRE      (override de metode - sesiunea 18)
#   2) prin DUCK TYPING    ("daca se comporta ca X, il tratam ca X")
#   3) prin OPERATOR OVERLOADING (metode "dunder": __add__, __eq__, ...)
#
# De ce ai nevoie ca sa intelegi acest fisier (recap):
#   - clase, metode, __init__, __str__/__repr__ (sesiunea 17)
#   - mostenire si override (sesiunea 18)
#   - sorted(), len(), operatorul  in
# =============================================================
from datetime import datetime


# =============================================================
# PARTEA 1 - CE ESTE POLIMORFISMUL
# =============================================================


# 1. PROBLEMA: un lant de if-uri pe "tip"
# -------------------------------------------------------------
# Vrem sa procesam plati facute pe canale diferite. Naiv, verificam
# tipul cu if/elif:


def descrie_plata(modalitate_plata, suma):
    if modalitate_plata == "card":
        return "Plata cu cardul"
    elif modalitate_plata == "paypal":
        return "Plata cu PayPal"
    elif modalitate_plata == "transfer":
        return "Plata prin transfer bancar"
    else:
        return "Modalitate de plata nevalida"


print(descrie_plata("card", 100))


# Enervant: la FIECARE canal nou (Revolut, cripto, ramburs) trebuie sa
# adaugi inca un elif, in fiecare functie care lucreaza cu plati. Codul
# creste si se rupe usor.
# SOLUTIA POLIMORFICA: fiecare canal e un OBIECT care stie SINGUR sa se
# descrie. Codul care le foloseste nu mai are niciun if.


# 2. POLIMORFISM PRIN MOSTENIRE  (recap din sesiunea 18)
# -------------------------------------------------------------
# Mai multe clase mostenesc dintr-o baza si suprascriu aceeasi metoda.
# Poti scrie cod general care merge pe orice subclasa.

class Notificare:
    def __init__(self, destinatar, mesaj):
        self.destinatar = destinatar
        self.mesaj = mesaj

    def trimite(self):
        return f"Generica- Mesaj trimisa catre {self.destinatar} cu textul {self.mesaj}"

class Email(Notificare):
    def trimite(self):
        return f"Email- Mesaj trimisa catre {self.destinatar} cu textul {self.mesaj}"

class SMS(Notificare):
    def trimite(self):
        return f"SMS- Mesaj trimisa catre {self.destinatar} cu textul {self.mesaj}"


notificari = [
    Email("mihai@gmail.com", "Hello"),
    SMS("mihai@gmail.com", "Hello"),
    Email("george@gmail.com", "Hello"),
]

def trimite_notificare(notificari):
    for n in notificari:
        n.trimite()



# [EMAIL -> ana@site.ro] comanda confirmata
# [SMS -> 0722] cod: 4821

# 3. DUCK TYPING  -  polimorfism FARA radacina comuna
# -------------------------------------------------------------
# Python nu verifica TIPUL, ci daca obiectul are metoda ceruta. Nu e
# nevoie ca toate clasele sa mosteneasca dintr-o baza comuna!

class PlataCard:
    def plateste(self, suma):
        return f"Plata cu cardul: {suma} lei"

class PlataPayPal:
    def plateste(self, suma):
        return f"Plata cu PayPal: {suma} lei"

class PlataTransfer:
    def plateste(self, suma):
        return f"Plata prin transfer bancar: {suma} lei"


def proceseaza_plata(metoda, suma):
    for m in metoda:
        print(m.plateste(suma))

proceseaza_plata([PlataCard(), PlataPayPal(), PlataTransfer()], 100)

# platit 100 lei cu cardul
# platit 100 lei prin PayPal
# platit 100 lei prin transfer bancar
# Un canal nou = o clasa noua cu  plateste(). ZERO if-uri de modificat.


# 4. POLIMORFISMUL E DEJA IN LIMBAJ  (len, +, ==, print)
# -------------------------------------------------------------
# len, +, ==, for, in, print sunt polimorfice: acelasi apel, dar
# Python cheama "sub capota" o metoda potrivita pentru fiecare tip.

print(len("python"))    # 6 string stie sa raspunda la len()
print(len([1, 2, 3]))  # 3  list stie sa raspunda la len()
print("ana" + "maria") # anamaria -> concatenare
print(1 == 1.0)        # True  (float == int)
print(1 == "1")        # False (int == str)


# Aceste metode "sub capota" au nume speciale (__len__, __add__, ...).
# In PARTEA 2 le implementam SI NOI, ca obiectele noastre sa se
# integreze in aceleasi mecanisme.


# =============================================================
# PARTEA 2 - DUNDER METHODS PE CLASELE NOASTRE
# =============================================================
# "dunder" = double underscore = nume care incep si se termina cu __
# Le-am folosit deja: __init__, __str__, __repr__. Sunt zeci, si ne
# lasa sa spunem lui Python ce inseamna ==, <, +, len(), in pe
# obiectele noastre.


# 5. __eq__  -  ce inseamna "egal" pentru obiectele tale
# -------------------------------------------------------------
# PROBLEMA: implicit, doua obiecte sunt "egale" doar daca sunt EXACT
# acelasi obiect in memorie. Doua produse cu acelasi cod ar iesi
# "diferite", desi pentru noi sunt acelasi produs.
print("Punctul 5")

class Produs:
    def __init__(self, cod, nume):
        self.cod = cod
        self.nume = nume

    def __eq__(self, alt):
        if not isinstance(alt, Produs): # daca alt nu este un obiect de tip Produs va returna NotImplemented
            return NotImplemented
        return self.nume == alt.nume # sunt egale deci au acelasi cod

    def __repr__(self):
        return f"Produs({self.cod}, {self.nume})"

print(Produs(1, "produs1") == Produs(1, "produs2"), '1')  # True
print(Produs(2, "produs1") == Produs(3, "produs1"), '2')  # False
print(Produs(1, "produs1") == "produs1")

# Cand scrii obiect1 == obiect2, python apeleaza automat obiect1.__eq__(obiect2)

# Nota: daca definesti __eq__ si vrei sa pui obiectele in set/dict,
# defineste si __hash__. (Detaliu avansat - revenim mai tarziu.)


# 6. __lt__  +  sorted()  -  sortare pe obiecte
# -------------------------------------------------------------
# Daca implementezi  __lt__  ("less than", <), Python stie sa
# compare obiectele tale, deci  sorted()  merge automat.

class Angajat:
    def __init__(self, nume, salariu, zile_de_concediu):
        self.nume = nume
        self.salariu = salariu
        self.zile_de_concediu = zile_de_concediu

    def __lt__(self, alt):
        return self.zile_de_concediu < alt.zile_de_concediu

    def __repr__(self):
        return f"Angajat({self.nume}, {self.salariu}, {self.zile_de_concediu})"

echipa = [Angajat("ana", 1000, 21), Angajat("george", 2000, 25), Angajat("maria", 500, 7)]
print(sorted(echipa))


# Fara __lt__, sorted(echipa) ar da TypeError: "not supported between
# instances of 'Angajat'".


# 7. __add__ / __sub__  -  aritmetica pe obiecte (o clasa Bani)
# -------------------------------------------------------------
# Implementand __add__ / __sub__ putem folosi  +  si  -  pe obiectele
# noastre. Caz real: o suma de bani cu moneda, care refuza sa adune
# monede diferite.

class Bani:
    def __init__(self, valoare, moneda):
        self.valoare = valoare
        self.moneda = moneda


    def __add__(self, alt):
        if self.moneda != alt.moneda:
            raise ValueError("Nu poti aduna bani de diferite monede")
        return Bani(self.valoare + alt.valoare, self.moneda)

    def __sub__(self, alt):
        if self.moneda != alt.moneda:
            raise ValueError("Nu poti scade bani de diferite monede")
        return Bani(self.valoare - alt.valoare, self.moneda)

    def __str__(self):
        return f"{self.valoare} {self.moneda}"

print(Bani(10, "lei") + Bani(20, "lei"))
# print(Bani(10, "eur") + Bani(20, "usd"))


a = 5
b = 6
suma = a + b
print(type(a))


# =============================================================
# PARTEA 3 - UNELTE / CAZURI AVANSATE
# =============================================================


# 8. UN CONTAINER PROPRIU  -  __len__, __contains__, __getitem__, __iter__
# -------------------------------------------------------------
# Cu aceste 4 dunder-uri, obiectul tau se comporta ca o lista: merge
# len(), operatorul  in, indexarea [i]  si bucla  for. Caz real: un
# playlist care tine melodii, dar are si nume + reguli proprii.

class Playlist:

    def __init__(self, nume):
        self.nume = nume   # atribut de instanta public
        self._melodii = [] # atribut de instanta protejat


    def adauga(self, titlu):
        self._melodii.append(titlu)

    def __len__(self):
        return len(self._melodii)

    def __contains__(self, titlu):
        return titlu in self._melodii

    def __getitem__(self, i):
        return self._melodii[i]

    def __iter__(self):
        return iter(self._melodii)

    def __repr__(self):
        return f"Playlist({self.nume})"


p = Playlist("playlist1")
p.adauga("titlu1")
p.adauga("titlu2")
print(len(p))                   # 2        (__len__)
print("titlu1" in p)            # True     (__contains__)
print(p[1])                     # titlu2   (__getitem__)
for titlu in p:                 # for titlu in p:  (__iter__)
    print(titlu)



# 9. __call__  -  obiectul se comporta ca o FUNCTIE
# -------------------------------------------------------------
# Cu __call__ poti "apela" un obiect ca pe o functie:  obiect(...).
# Util cand vrei o functie care isi tine niste setari (stare) in ea.


class TarifLivrare:
    def __init__(self, tarif_per_km):
        self.tarif_per_km = tarif_per_km

    def __call__(self, distanta_km):
        return self.tarif_per_km * distanta_km


livrare_oras = TarifLivrare(10)     # 10 lei per km
livrare_tara = TarifLivrare(5)      # 5 lei per km
print(livrare_oras(10))             # 100
print(livrare_tara(10))             # 50



# livrare_oras e un OBIECT, dar il folosim ca pe o functie.


# 10. @functools.total_ordering  -  toate comparatiile dintr-una
# -------------------------------------------------------------
# Daca vrei toate comparatiile (<, <=, >, >=) dar nu vrei sa scrii 4
# metode, defineste doar  __eq__  si  __lt__, iar decoratorul
# total_ordering le genereaza pe restul automat.

import functools

@functools.total_ordering
class Versiune:
    def __init__(self, numar, data):
        self.numar = numar
        self.data = data

    def __eq__(self, alt):
        return self.numar == alt.numar or self.data == alt.data

    def __lt__(self, alt):
        return self.numar < alt.numar and  self.data < alt.data


    def __repr__(self):
        return f"Versiune({self.numar})"


print(Versiune(1, "12-12-2026") == Versiune(2, "12-12-2026"))    # False (definit de noi)
print(Versiune(1, "12-12-2026") < Versiune(2, "12-12-2026"))     # True (definit de noi)
print(Versiune(5, datetime.now().date()) >= Versiune(3, datetime.now().date()))     # True (generat automat)

print(datetime.now().date())


set_date ={1, 2, 3, True, "ana"}
print(hash(1))
print(hash(True))

print(len(set_date))
# =============================================================
# RECAP / GRESELI FRECVENTE
# =============================================================
# POLIMORFISM = aceeasi interfata, comportamente diferite. Il obtii:
#   1) prin MOSTENIRE + override   (Notificare -> Email / SMS)
#   2) prin DUCK TYPING            (orice obiect cu metoda plateste())
#   3) prin OPERATOR OVERLOADING   (dunder methods pe clasele tale)
#
# Dunder methods utile:
#   - __eq__          ->  ==            (ce inseamna "egal")
#   - __lt__          ->  <  si sorted()
#   - __add__/__sub__ ->  +  si  -
#   - __len__         ->  len(obiect)
#   - __contains__    ->  x in obiect
#   - __getitem__     ->  obiect[i]
#   - __iter__        ->  for x in obiect
#   - __call__        ->  obiect(...)
#
# Greseli frecvente:
#   - sa crezi ca polimorfismul cere OBLIGATORIU mostenire. Duck typing
#     (obiecte fara radacina comuna, dar cu aceeasi metoda) e adesea
#     mai simplu si mai flexibil.
#   - sa uiti  return NotImplemented  in __eq__ cand comparatia nu are
#     sens (obiect vs string) - altfel primesti rezultate ciudate.
#   - sa definesti __eq__ dar sa pui obiectul in set/dict fara __hash__.
#   - sa reimplementezi lant de if pe  type(x) ==  in loc sa lasi
#     fiecare obiect sa-si faca treaba (polimorfism).
#
# =============================================================
# CONCLUZIE (sablon de retinut)
# =============================================================
# class X:
#     def __eq__(self, alt): ...       # ==
#     def __lt__(self, alt): ...       # <  (+ sorted)
#     def __add__(self, alt): ...      # +
#     def __len__(self): ...           # len(x)
#     def __contains__(self, v): ...   # v in x
#     def __getitem__(self, i): ...    # x[i]
#     def __iter__(self): ...          # for _ in x
#     def __call__(self, ...): ...     # x(...)
#
# In sesiunea urmatoare: ABSTRACTIZAREA - cum definim explicit o
# "interfata" pe care subclasele SUNT OBLIGATE sa o implementeze
# (modulul abc, @abstractmethod).
# =============================================================


# Incapsulare:
# Este primul principial al OOP-ului prin care datele(atributele) si comportamentele(metode) opereaze asupra lor
# fiind grupate intr-o singura unitate(clasa/obiect). Accesul direct la date se va realiza pe baza unor atribute publice,
# protejate si private

# Incapsularea protejeaza si organizeaza datele din interiorul unui obiect

# Mostenirea
# Este principiul al doilea al OOP-ului si se raporteaza la modul in care o clasa copil poate mosteni de la o clasa
# parinte toate atributele, metodele si chiar sa adauge si altele

# Definirea de clase noi pe baza claselor deja definite, fiecare mostenind atributele si metodele.

# Polimorfismul
# Clasele pot avea metode cu aceeasi denumire dar cu comportament diferit

# permite tratarea uniforma a obiectivelor diferinte si definirea de noi comportamente pentru acestea