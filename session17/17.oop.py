# OOP IN PYTHON
# =============================================================
# OOP = Object-Oriented Programming = Programare Orientata pe Obiecte.
#
# Pana acum am scris cod PROCEDURAL: date pe de o parte (variabile,
# liste, dictionare) si functii pe de alta parte, care primesc datele
# ca argumente si intorc un rezultat.
#
# In OOP grupam DATELE + COMPORTAMENTUL care lucreaza pe ele intr-un
# singur loc, numit OBIECT. Un obiect "ContBancar" tine soldul (data)
# SI stie sa faca depunere/retragere (comportament) - la un loc.
#
# Analogie: o CLASA e o MATRITA.
# Un OBIECT (instanta) e o prajitura concreta, coapta din acea reteta.
# Dintr-o singura reteta scoti oricate prajituri, fiecare separata.
#
# DE CE OOP?
#   - Modeleaza natural realitatea: un User, o Comanda, un Cont.
#   - Reduce repetitia: definesti "matrita" o singura data, creezi
#     cate obiecte vrei din ea.
#   - INCAPSULARE: datele sunt modificate DOAR prin metode controlate,
#     nu poate oricine sa strice soldul "de mana".
#
# Termeni-cheie (revenim la fiecare mai jos, cu exemple):
#   - CLASA     = matrita / definitia (nu e un obiect "viu")
#   - INSTANTA  = un obiect concret, creat din clasa
#   - ATRIBUT   = o "variabila" care traieste in obiect (date)
#   - METODA    = o "functie" definita in clasa, primeste self
#   - self      = referinta la obiectul curent (instanta pe care lucrezi)
# =============================================================
# PARTEA 1 - BAZELE
# =============================================================


# 1. PROBLEMA: fara clase, datele care "merg impreuna" se imprastie
# -------------------------------------------------------------
# Vrem sa reprezentam conturi bancare. Fara OOP tinem soldul intr-o
# variabila si scriem functii separate. Nimic nu leaga soldul de
# functiile lui - trebuie sa pasezi mereu totul de mana.

sold_ana = 1000

def depunere(sold, suma):
    return sold + suma

def retragere(sold, suma):
    return sold - suma

sold_ana = depunere(sold_ana, 500)
print(sold_ana)
sold_ana = retragere(sold_ana, 200)
print(sold_ana)

# Enervant si periculos:
#   - trebuie sa pasezi soldul la fiecare apel si sa-l reasignezi;
#   - daca ai 100 de conturi, ai 100 de variabile razlete;
#   - nimic nu impiedica pe cineva sa faca  sold_ana = -99999.
# SOLUTIA: legam datele de comportament intr-o CLASA.


# 2. PRIMA CLASA  -  definitie si instanta
# -------------------------------------------------------------
# Definim o clasa cu:  class NumeClasa:
# Conventie: numele claselor se scriu in PascalCase (ContBancar).

class Cont:
    pass                 # deocamandata clasa este goala

# Cream o INSTANTA apeland clasa ca pe o functie:

c = Cont()
print(c)
print(type(c))


# `Cont` e matrita. `c` e un obiect concret facut din ea.


# 3. CONSTRUCTORUL  __init__  -  umplem obiectul cu date la creare
# -------------------------------------------------------------
# PROBLEMA: putem lipi atribute pe un obiect "de mana"...

c.titular = "Ana"
c.sold = 1000
print(c.titular)
print(c.sold)

# ... dar e usor sa uiti sa setezi ceva, si fiecare obiect ar arata
# altfel. Vrem ca ORICE cont sa aiba, garantat, titular si sold.
#
# SOLUTIA: metoda speciala  __init__  ("constructor"). Se apeleaza
# AUTOMAT la crearea obiectului. Primul parametru e mereu `self` =
# obiectul proaspat creat, pe care punem atributele.

class Cont:
    def __init__(self, titlular, sold):
        self.titular = titlular  # atribut de instanta
        self.sold = sold         # atribut de instanta


# La  Cont("Ana", 1000)  Python creeaza obiectul si apeleaza
# __init__(obiect, "Ana", 1000). Pe `self` NU il dai tu, il pune Python.

cont_ana = Cont("Ana", 1000)
cont_ion = Cont("Ion", 50)
print(cont_ana.titular, cont_ana.sold)
print(cont_ion.titular, cont_ion.sold)

# Doua obiecte separate, fiecare cu datele lui. Asta e puterea matritei.


# 4. METODE  -  comportament care lucreaza pe self
# -------------------------------------------------------------
# O METODA e o functie definita in clasa. Primeste mereu `self`, ca
# sa aiba acces la atributele obiectului. Aici mutam depune/retrage
# INAUNTRUL clasei, langa datele pe care le modifica.

class Cont:

    def __init__(self, titular, sold):
        self.titular = titular
        self.sold = sold

    def depune(self, suma):
        self.sold += suma

    def retrage(self, suma):
        self.sold -= suma


cont = Cont("Ana", 1000)
cont.depune(500)
cont.retrage(1000)
print(cont.sold)

print(type(cont))

lista = [1, 2, 3, 4]

print(type(lista))

# Observa: nu mai pasam soldul de mana. Metoda il stie prin self.


# 5. self, mai clar  -  fiecare obiect isi vede propriile date
# -------------------------------------------------------------
# `self` NU e un cuvant magic, e doar numele (prin conventie) al
# primului parametru = obiectul pe care s-a apelat metoda.

a = Cont("George", 100)
b = Cont("Florin", 1000)
a.depune(1000)
print(a.sold) # accesam atributul sold din obiectul Cont

# Acelasi cod, doua obiecte, rezultate diferite - fiindca self difera.

# 6. __str__  -  cum arata obiectul cand il afisezi
# -------------------------------------------------------------
# PROBLEMA: print(cont) da "<__main__.Cont object at 0x...>" - inutil.
# SOLUTIA: metoda speciala __str__ intoarce un text "pentru oameni".

class Cont:

    def __init__(self, titular, sold):
        self.titular = titular
        self.sold = sold

    def depune(self, suma):
        self.sold += suma

    def retrage(self, suma):
        self.sold -= suma

    def __str__(self):
        return f"Contul {self.titular} are soldul {self.sold}"

a = Cont("Horia", 100)
print(a)


# =============================================================
# PARTEA 2 - CAZURI REALE
# =============================================================


# 7. __repr__  -  reprezentarea "tehnica" (debug, log-uri, liste)
# -------------------------------------------------------------
# __str__  = pentru utilizator (afisare frumoasa).
# __repr__ = pentru programator (debug). E ce vezi cand pui obiectul
#            intr-o LISTA si o afisezi, sau in consola interactiva.
# Regula practica: __repr__ ar trebui sa arate cum ai RECREA obiectul.

class Cont:

    def __init__(self, titular, sold):
        self.titular = titular
        self.sold = sold

    def depune(self, suma):
        self.sold += suma

    def retrage(self, suma):
        self.sold -= suma

    def __str__(self):
        return f"Contul {self.titular} are soldul {self.sold}"

    def __repr__(self):
        return f"Contul {self.titular} -  soldul {self.sold}"


x = Cont("Ioana", 1000)
print(x)           # Contul Ioana are soldul 1000 (__str__)
print([x])         # [Cont('Ioana', 1000)         (__repr__)

# Daca definesti doar __repr__, el e folosit si ca fallback pentru print.

lista_conturi = []
lista_conturi.append(Cont("Dan", 1000))
lista_conturi.append(Cont("Florin", 100))
lista_conturi.append(Cont("Andreea", 5000))

print(lista_conturi)

for cont in lista_conturi:
    cont.depune(100)
    print(cont.titular, cont.sold)


# 8. ATRIBUT DE CLASA vs ATRIBUT DE INSTANTA
# -------------------------------------------------------------
# Atribut de INSTANTA (self.x): propriu fiecarui obiect, difera.
# Atribut de CLASA: definit direct in corpul clasei, PARTAJAT de toate
# instantele. Bun pentru constante (cota TVA) sau contoare comune.


class ProdusTva:
    cota_TVA = 0.21   # atribut de clasa

    def __init__(self, name, price_without_tva, discount = 10, *args, **kwargs):
        self.nume = name                       # atribut de instanta
        self.pret_fara_tva= price_without_tva  # atribut de instanta
        self.discount= discount                # atribut de instanta

    def pret_cu_tva(self):
        return self.pret_fara_tva * (1 + ProdusTva.cota_TVA)

    def pret_cu_discount(self):
        pass

p1 = ProdusTva("laptop", 3000)
p2 = ProdusTva("mouse", 500, 10)

print(p1.pret_cu_tva())
print(p2.pret_cu_tva())
print(ProdusTva.cota_TVA)



# 9. CONTOR DE INSTANTE  (atribut de clasa care creste la fiecare obiect)
# -------------------------------------------------------------
# Caz real: vrem un ID unic, crescator, pentru fiecare comanda creata.


class Comanda:
    _nr_total = 0     # cate comenzi au fost adaugate

    def __init__(self, descriere):
        Comanda._nr_total += 1    # creste cu o unitate
        self.descriere = descriere
        self.id = Comanda._nr_total


    def __str__(self):
        return f"Comanda cu numarul #{self.id}: {self.descriere}"



c1 = Comanda("laptop")
c2 = Comanda("Mouse")
c3 = Comanda("Trackpad")
print(c1)
print(c2)
print(c3)
print(f"Total comenzi este: {Comanda._nr_total}")


# 10. OBIECTE CARE CONTIN ALTE OBIECTE  (compunere)
# -------------------------------------------------------------
# In realitate obiectele se combina: un Cos contine mai multe Produse.
# Un atribut poate fi o lista de alte obiecte.



class Cos:

    def __init__(self):
        self.produse = []

    def adauga(self, produs):
        self.produse.append(produs)

    def total(self):
        return sum(p for p in self.produse)

    def __str__(self):
        return f"Cos cu {len(self.produse)} produse are totalul de: {self.total()} lei"


cos = Cos()
cos.adauga(1000)
cos.adauga(300)
cos.adauga(500)
print(cos)



# =============================================================
# PARTEA 3 - INCAPSULARE (ascunderea si protejarea datelor)
# =============================================================
# INCAPSULARE = obiectul isi ascunde detaliile interne si ofera doar
# o "usa de acces" controlata. Scop: nimeni sa nu poata pune obiectul
# intr-o stare invalida (un sold negativ, o parola goala).


# 11. PROBLEMA: atribute total publice = oricine strica orice
# -------------------------------------------------------------

class Cont:

    def __init__(self, sold):
        self.sold = sold


cn = Cont(1000)
cn.sold = -99999      # nimeni nu ma opreste sa fac o prostie
print(cn.sold)        # -99999

# Vrem: soldul sa poata fi modificat DOAR prin metode care valideaza.


# 12. _protected si __private  -  conventie si name mangling
# -------------------------------------------------------------
# In Python nu exista "private" strict ca in alte limbaje. Avem:
#   - nume normal:  public - oricine il foloseste.
#   - _nume  (un underscore): "PROTECTED" - conventie. Inseamna "nu
#     umbla la asta din afara". Python NU te opreste, dar e semnal clar.
#   - __nume (doua underscore-uri): declanseaza "name mangling" -
#     Python il redenumeste intern in _NumeClasa__nume, ca sa fie greu
#     de atins din greseala si sa nu se ciocneasca la mostenire.


class ContPrivat:

    def __init__(self, sold):
        self.__sold = sold      # atribut privat


    def sold_curent(self):
        return self.__sold


c = ContPrivat(1000)
print(c.sold_curent())             # 1000
# print(c.__sold)                  # asa il ascunde Python fara a-l putea accesa
# print(c.ContPrivat.__sold, '???')  # asa il ascunde Python fara a-l putea accesa


# Concluzie: __private nu e securitate, e "gard" impotriva accidentelor.


# 13. GETTER / SETTER cu @property  -  varianta Pythonic
# -------------------------------------------------------------
# PROBLEMA: ca sa validam, am putea scrie get_sold() / set_sold().
# Dar atunci codul devine  cont.set_sold(500)  in loc de  cont.sold = 500
# - urat si ne-Pythonic.
#
# SOLUTIA: @property. Definesti o METODA, dar o folosesti ca pe un
# ATRIBUT (fara paranteze). @property = getter-ul. @x.setter = setter-ul,
# unde punem VALIDAREA.

class ContBancar:

    def __init__(self, titular, sold_initial):
        self.titular = titular       # atribut de instanta public
        self.__sold = sold_initial   # atribut de instanta privat

    @property                  # GETTER -> se apeleaza cont_nou.sold
    def sold(self):
        return self.__sold

    @sold.setter                # SETTER -> se apeleaza cont_nou.sold = X
    def sold(self, valoare):
        if valoare < 0:
            raise ValueError("Valoarea nu poate fi negativa")
        self.__sold = valoare

    def depunere(self, suma):
        if suma <= 0:
            raise ValueError("Suma depusa trebuie sa fie pozitiva")
        self.sold = self.sold + suma

    def retragere(self, suma):
        if suma > self.sold:
            raise ValueError("Fonduri insuficiente")
        self.sold -= suma


    def __str__(self):
        return f"Contul lui {self.titular} are soldul {self.sold} lei"


cont_nou = ContBancar("Costel", 3000)
print(cont_nou.sold)
cont_nou.depunere(500)
print(cont_nou.sold)
cont_nou.retragere(600)
print(cont_nou.sold)

# Validarea prinde greselile in loc sa strice tacut obiectul:

try:
    cont_nou.sold = -50
except ValueError as e:
    print(e)


# 14. @property doar-citire  -  valoare CALCULATA, fara setter
# -------------------------------------------------------------
# Daca definesti @property FARA setter, atributul devine read-only.
# Perfect pentru valori derivate din altele (nu le stochezi, le calculezi).


class Angajat:

    def __init__(self, nume, salariu_brut):
        self.nume = nume
        self.salariu_brut = salariu_brut

    @property
    def salariu_net(self):
        return round(self.salariu_brut * 0.52,2)



a = Angajat("Florin", 5000)
print(a.salariu_net)
a.salariu_brut = 6000
print(a.salariu_net)



# =============================================================
# RECAP / GRESELI FRECVENTE
# =============================================================
# - CLASA = matrita, INSTANTA = obiect concret creat din ea.
# - __init__ ruleaza automat la creare; pune atributele pe `self`.
# - `self` = obiectul curent; e primul parametru al oricarei metode
#   (nu il dai tu la apel, il pune Python).
# - Metodele traiesc langa datele lor - asa OOP-ul are sens.
# - __str__ pentru afisare "umana"; __repr__ pentru debug/liste.
# - Atribut de CLASA (in corpul clasei) = partajat de toate instantele
#   (constante, contoare). Atribut de INSTANTA (self.x) = propriu.
#
# INCAPSULARE:
#   - public:    nume        - oricine il foloseste
#   - protected: _nume       - conventie: "nu umbla din afara"
#   - private:   __nume       - name mangling (gard anti-accident)
#   - @property + @x.setter  - getter/setter Pythonic, cu VALIDARE
#   - @property fara setter  - atribut read-only / valoare calculata
#
# Greseli frecvente:
#   - sa uiti `self` ca prim parametru al metodei -> TypeError.
#   - sa apelezi metoda fara paranteze:  cont.depune  (nu o executa!).
#   - sa crezi ca __private e securitate reala (e doar mangling).
#   - sa pui toate atributele publice si sa validezi "pe ici pe colo"
#     in loc sa treci totul prin setter/metode.
#   - sa confunzi atribut de clasa cu cel de instanta:  self.COTA = ...
#     creeaza un atribut NOU pe obiect, nu modifica pe cel de clasa.
#
# =============================================================
# CONCLUZIE (sablon de retinut)
# =============================================================
# class NumeClasa:
#     CONST = ...                    # atribut de clasa (partajat)
#
#     def __init__(self, x):
#         self._x = x                # atribut de instanta (ascuns)
#
#     @property
#     def x(self):                   # getter:  obiect.x
#         return self._x
#
#     @x.setter
#     def x(self, val):              # setter:  obiect.x = val  (+ validare)
#         if val < 0:
#             raise ValueError("...")
#         self._x = val
#
#     def metoda(self):              # comportament pe self
#         return self._x
#
#     def __str__(self):
#         return "..."               # cum apare la print
#
# =============================================================