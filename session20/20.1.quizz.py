# QUIZ INTERVIU  -  SESIUNEA 20  (OOP: CLASE, INCAPSULARE,
#                    MOSTENIRE, POLIMORFISM, ABSTRACTIZARE - 17-20)
# =============================================================
# Pe baza a tot ce s-a predat in 17.oop.py, 18.mostenire.py,
# 19.polimorfism.py si 20.abstractizare.py.
# Fiecare intrebare contine:
#   - o SECVENTA DE COD (de tip "ce afiseaza? / ce eroare apare?")
#   - 4 variante A/B/C/D
#   - EXPLICATIE obligatorie dupa raspuns (afisata si cand
#     raspunzi corect — la interviu conteaza sa stii DE CE)
#
# Gotcha-urile clasice din sesiunile 17-19:
#   CLASE & self (17):
#     - fiecare instanta are propriile atribute (self = obiectul curent)
#     - metoda apelata FARA paranteze = obiect metoda, nu rezultatul
#     - __str__ lipsa -> reprezentarea implicita urata din object
#     - __repr__ e folosit cand obiectul e intr-o lista/container
#     - self.ATRIBUT_CLASA = ... creeaza un atribut NOU de instanta,
#       nu modifica atributul de clasa
#   INCAPSULARE (17):
#     - __private -> name mangling (_NumeClasa__nume), NU securitate reala
#     - _protected e doar conventie, Python nu opreste nimic
#     - @property se foloseste FARA paranteze; cu paranteze -> TypeError
#     - setter-ul valideaza INAINTE sa schimbe starea (raise oprit)
#     - @property fara setter = read-only, AttributeError la scriere
#   MOSTENIRE (18):
#     - class Copil(Parinte): pass -> mosteneste TOT
#     - uiti super().__init__(...) -> atributele parintelui lipsesc
#     - override inlocuieste, super().metoda() extinde
#     - isinstance/issubclass: copilul ESTE parinte, parintele NU e copil
#     - atribut de clasa mostenit, poate fi umbrit de copil
#   POLIMORFISM (19):
#     - aceeasi metoda apelata pe tipuri diferite -> comportamente diferite
#     - duck typing: nu conteaza mostenirea, conteaza doar metoda existenta
#     - __eq__, __lt__, __add__, __len__/__contains__, __call__
#   ABSTRACTIZARE (20) - RUNDA NOUA, GOTCHA-URI REALE DE INTERVIU:
#     - @abstractmethod verifica DOAR ca numele e suprascris, NU ca
#       raman o metoda apelabila - un ATRIBUT cu acelasi nume "bifeaza"
#       cerinta la fel de bine (capcana rar cunoscuta, chiar si de
#       programatori cu experienta)
#     - o metoda abstracta POATE avea cod real in corp (nu doar ...);
#       subclasa il poate refolosi cu super().metoda_abstracta()
#     - ordinea decoratorilor CONTEAZA: @property deasupra,
#       @abstractmethod dedesubt - invers, AttributeError la
#       DEFINIREA clasei, inainte sa apuci sa creezi vreun obiect
#     - TREBUIE implementate TOATE metodele abstracte; lipseste una
#       singura -> clasa ramane abstracta in intregime
#     - o clasa abstracta poate avea __init__ CONCRET (comun) - daca
#       subclasa isi rescrie __init__ si uita super().__init__(...),
#       obiectul TOT se creeaza (are toate metodele abstracte
#       implementate), dar atributele parintelui lipsesc pana le
#       accesezi
#
# Cum se ruleaza:
#   python3 20.0.quiz_interviu.py
#
# Apasa Q oricand pentru iesire.
# =============================================================


# =============================================================
# BANCA DE INTREBARI
# =============================================================
# Fiecare intrebare e un DICT cu:
#   runda       (int)    1..4
#   categorie   (str)
#   puncte      (int)    1 / 2 / 3 — dificultate
#   cod         (str)    secventa de cod (triple-quoted)
#   intrebare   (str)    intrebarea propriu-zisa
#   optiuni     (dict)   {"A": ..., "B": ..., "C": ..., "D": ...}
#   corect      (str)    "A" / "B" / "C" / "D"
#   explicatie  (str)    DE CE — afisata mereu dupa raspuns

intrebari = [
    # ---------- RUNDA 1: CLASE, OBIECTE & self ----------
    {"runda": 1, "categorie": "apel-fara-paranteze", "puncte": 3,
     "cod": 'class Cont:\n    def __init__(self, sold):\n        self.sold = sold\n    def afiseaza(self):\n        return f"sold: {self.sold}"\n\nc = Cont(200)\nprint(c.afiseaza)',
     "intrebare": "Ce afiseaza? (atentie: lipsesc parantezele)",
     "optiuni": {"A": "sold: 200", "B": "<bound method ...> (metoda, neapelata)",
                 "C": "None", "D": "TypeError"},
     "corect": "B",
     "explicatie": "Greseala clasica: `c.afiseaza` FARA paranteze e doar REFERINTA la metoda (bound method), nu o executie. Trebuie `c.afiseaza()` ca sa obtii rezultatul."},

    {"runda": 1, "categorie": "repr-in-lista", "puncte": 2,
     "cod": 'class Produs:\n    def __init__(self, nume, pret):\n        self.nume = nume\n        self.pret = pret\n    def __str__(self):\n        return f"{self.nume} - {self.pret} lei"\n    def __repr__(self):\n        return f"Produs({self.nume!r}, {self.pret})"\n\np = Produs("mouse", 79)\nprint(p)\nprint([p])',
     "intrebare": "Ce afiseaza cele doua print-uri?",
     "optiuni": {"A": "ambele folosesc __str__", "B": "primul __str__, al doilea __repr__",
                 "C": "ambele folosesc __repr__", "D": "primul __repr__, al doilea __str__"},
     "corect": "B",
     "explicatie": "print(p) direct pe obiect foloseste __str__ ('mouse - 79 lei'). Dar cand obiectul e INTR-O LISTA, Python afiseaza fiecare element cu __repr__ -> [Produs('mouse', 79)]."},

    {"runda": 1, "categorie": "atribut-clasa-umbrit-per-instanta", "puncte": 3,
     "cod": 'class ProdusTva:\n    COTA_TVA = 0.19\n    def seteaza_cota_gresit(self, noua_cota):\n        self.COTA_TVA = noua_cota   # greseala!\n\np1 = ProdusTva()\np2 = ProdusTva()\np1.seteaza_cota_gresit(0.05)\nprint(p1.COTA_TVA, p2.COTA_TVA, ProdusTva.COTA_TVA)',
     "intrebare": "Ce afiseaza?",
     "optiuni": {"A": "0.05 0.05 0.05", "B": "0.05 0.19 0.19",
                 "C": "0.19 0.19 0.19", "D": "0.05 0.19 0.05"},
     "corect": "B",
     "explicatie": "self.COTA_TVA = ... NU modifica atributul de CLASA, ci creeaza un atribut NOU de instanta pe p1, care il umbreste doar pentru p1. p2 si clasa insasi raman la 0.19."},

    {"runda": 1, "categorie": "atribut-clasa-mutabil-shared", "puncte": 3,
     "cod": 'class Cos:\n    produse = []   # atribut de CLASA (nu in __init__!)\n    def adauga(self, produs):\n        self.produse.append(produs)\n\nc1 = Cos()\nc2 = Cos()\nc1.adauga("mar")\nc1.adauga("paine")\nprint(c1.produse, c2.produse, Cos.produse)',
     "intrebare": "Ce afiseaza? (atentie: produse e definit la nivel de CLASA, nu in __init__)",
     "optiuni": {"A": "[\'mar\', \'paine\'] [] []", "B": "[\'mar\', \'paine\'] [\'mar\', \'paine\'] [\'mar\', \'paine\']",
                 "C": "[] [] [\'mar\', \'paine\']", "D": "TypeError, produse e read-only"},
     "corect": "B",
     "explicatie": "SPRE DEOSEBIRE de o REASIGNARE (self.x = ...), care creeaza un atribut nou de instanta, .append() MUTEAZA lista existenta IN LOC - iar acea lista e UNA SINGURA, definita la nivel de clasa, impartita de TOATE instantele. c1.adauga(...) modifica aceeasi lista pe care o vede si c2. Compara cu intrebarea de mai sus (COTA_TVA, care folosea =): liste/dicturi ca atribute de clasa se comporta radical diferit fata de numere/stringuri."},

    {"runda": 1, "categorie": "init-returneaza-non-none", "puncte": 2,
     "cod": 'class Config:\n    def __init__(self):\n        return 5\n\nc = Config()',
     "intrebare": "Ce se intampla la ultima linie?",
     "optiuni": {"A": "c devine 5", "B": "TypeError: __init__() should return None, not \'int\'",
                 "C": "c e un Config normal, 5 e ignorat tacut", "D": "SyntaxError la definirea clasei"},
     "corect": "B",
     "explicatie": "__init__ are un singur job: sa initializeze obiectul, NU sa intoarca o valoare. Python impune asta strict: orice return diferit de None (implicit sau explicit) intr-un __init__ arunca TypeError, la CREAREA obiectului."},


    # ---------- RUNDA 2: INCAPSULARE — private, protejat, @property ----------
    {"runda": 2, "categorie": "property-setter-valideaza", "puncte": 3,
     "cod": 'class ContBancar:\n    def __init__(self, sold_initial):\n        self._sold = sold_initial\n    @property\n    def sold(self):\n        return self._sold\n    @sold.setter\n    def sold(self, valoare):\n        if valoare < 0:\n            raise ValueError("sold negativ")\n        self._sold = valoare\n\nc = ContBancar(1000)\ntry:\n    c.sold = -50\nexcept ValueError as e:\n    print(f"refuzat: {e}")\nprint(c.sold)',
     "intrebare": "Ce afiseaza?",
     "optiuni": {"A": "refuzat: sold negativ / -50", "B": "refuzat: sold negativ / 1000",
                 "C": "-50", "D": "1000"},
     "corect": "B",
     "explicatie": "c.sold = -50 trece prin SETTER, care valideaza si arunca ValueError INAINTE sa modifice _sold. except o prinde -> 'refuzat: sold negativ'. Soldul real ramane 1000."},

    {"runda": 2, "categorie": "property-readonly", "puncte": 3,
     "cod": 'class Angajat:\n    def __init__(self, salariu_brut):\n        self.salariu_brut = salariu_brut\n    @property\n    def salariu_net(self):\n        return round(self.salariu_brut * 0.585, 2)\n\na = Angajat(5000)\na.salariu_net = 9999',
     "intrebare": "Ce se intampla?",
     "optiuni": {"A": "salariu_net devine 9999", "B": "AttributeError, nu are setter",
                 "C": "ValueError", "D": "nimic, e ignorat"},
     "corect": "B",
     "explicatie": "@property definit FARA @salariu_net.setter face atributul READ-ONLY. Orice incercare de a-l seta direct arunca AttributeError. Perfect pentru valori calculate, nu stocate."},


    # ---------- RUNDA 3: MOSTENIRE ----------
    {"runda": 3, "categorie": "super-init-lipsa", "puncte": 3,
     "cod": 'class Angajat:\n    def __init__(self, nume, salariu):\n        self.nume = nume\n        self.salariu = salariu\n\nclass Manager(Angajat):\n    def __init__(self, nume, salariu, echipa):\n        self.echipa = echipa   # uita super().__init__(...)\n\nm = Manager("Ana", 8000, ["Ion"])\nprint(m.nume)',
     "intrebare": "Ce se intampla?",
     "optiuni": {"A": "Ana", "B": "AttributeError, nume nu exista",
                 "C": "None", "D": "TypeError"},
     "corect": "B",
     "explicatie": "Manager isi rescrie __init__ FARA sa cheme super().__init__(nume, salariu). self.nume nu se seteaza niciodata -> AttributeError la m.nume. Greseala clasica: uiti super().__init__(...)."},

    {"runda": 3, "categorie": "extindere-super", "puncte": 3,
     "cod": 'class User:\n    def descriere(self):\n        return "user"\n\nclass Admin(User):\n    def descriere(self):\n        baza = super().descriere()\n        return baza + " [ADMIN]"\n\nprint(Admin().descriere())',
     "intrebare": "Ce afiseaza?",
     "optiuni": {"A": "user", "B": "[ADMIN]",
                 "C": "user [ADMIN]", "D": "AttributeError"},
     "corect": "C",
     "explicatie": "super().descriere() apeleaza explicit versiunea din PARINTE ('user'), la care Admin ADAUGA text — asta e EXTINDERE, nu inlocuire totala. Rezultat: 'user [ADMIN]'."},

    {"runda": 3, "categorie": "mro-mostenire-multipla", "puncte": 3,
     "cod": 'class A:\n    def hello(self):\n        return "A"\n\nclass B:\n    def hello(self):\n        return "B"\n\nclass C(A, B):\n    pass\n\nprint(C().hello())',
     "intrebare": "C mosteneste din AMBELE A si B, care au fiecare propria hello(). Ce afiseaza?",
     "optiuni": {"A": "A", "B": "B",
                 "C": "TypeError, metoda e ambigua", "D": "AB (le combina pe amandoua)"},
     "corect": "A",
     "explicatie": "La mostenire multipla, class C(A, B) cauta metoda in ORDINEA scrisa in paranteze — intai A, apoi B (asta se numeste MRO - Method Resolution Order). Cum A are deja hello(), Python o gaseste acolo si se opreste, nu mai ajunge la B. Daca ai scrie class C(B, A), raspunsul ar deveni 'B'."},


    # ---------- RUNDA 4: POLIMORFISM & DUNDER METHODS ----------
    {"runda": 4, "categorie": "truthiness-obiect-fara-bool", "puncte": 3,
     "cod": 'class Cos:\n    def __init__(self):\n        self.produse = []\n\nc = Cos()\nif c:\n    print("cosul e \'adevarat\'")\nelse:\n    print("cosul e \'fals\'")',
     "intrebare": "Cos NU are __bool__ sau __len__. Ce afiseaza? (atentie: produse e o lista GOALA)",
     "optiuni": {"A": "cosul e 'fals', pentru ca produse e o lista goala", "B": "cosul e 'adevarat', desi produse e gol",
                 "C": "TypeError, obiectul nu poate fi folosit intr-un if", "D": "AttributeError"},
     "corect": "B",
     "explicatie": "Truthiness pe o LISTA goala (if produse:) e falsa, dar aici verificam OBIECTUL c, nu produse direct. Fara __bool__ sau __len__ definite pe clasa, Python considera ORICE obiect custom 'adevarat' by default, INDIFERENT ce contine pe dinauntru. Ca sa faci if c: sa reflecte 'e gol sau nu', trebuie sa definesti explicit __len__ (sau __bool__)."},

    {"runda": 4, "categorie": "lt-lipsa-sorted", "puncte": 3,
     "cod": 'class Angajat:\n    def __init__(self, nume, salariu):\n        self.nume = nume\n        self.salariu = salariu\n    def __repr__(self):\n        return self.nume\n\necoo = [Angajat("Ana", 8000), Angajat("Ion", 5000)]\nprint(sorted(ecoo))',
     "intrebare": "Ce se intampla? (Angajat NU are __lt__)",
     "optiuni": {"A": "[Ion, Ana], sortat crescator dupa nume", "B": "[Ana, Ion], ordinea originala",
                 "C": "TypeError: '<' not supported between instances of 'Angajat'", "D": "[Ion, Ana], sortat dupa salariu"},
     "corect": "C",
     "explicatie": "sorted() are nevoie sa compare elementele cu <, adica __lt__. Fara __lt__ definit, Python nu stie cum sa compare doi Angajati -> TypeError."},


    # ---------- RUNDA 5: ABSTRACTIZARE (ABC) - GOTCHA-URI DE INTERVIU ----------
    {"runda": 5, "categorie": "abstractmethod-suprascris-cu-atribut", "puncte": 3,
     "cod": 'from abc import ABC, abstractmethod\n\nclass Raport(ABC):\n    @abstractmethod\n    def genereaza(self):\n        ...\n\nclass RaportSimplu(Raport):\n    genereaza = "raport gata facut"   # atribut, NU metoda!\n\nr = RaportSimplu()\nprint(r.genereaza)',
     "intrebare": "Ce se intampla la RaportSimplu()? (atentie: genereaza NU mai e metoda)",
     "optiuni": {"A": "TypeError, genereaza trebuie sa fie o metoda apelabila",
                 "B": "Se creeaza normal, print afiseaza 'raport gata facut'",
                 "C": "AttributeError la instantiere",
                 "D": "TypeError abia la print(r.genereaza)"},
     "corect": "B",
     "explicatie": "@abstractmethod verifica DOAR ca numele exista in clasa copil, NU ca ramane o metoda CALLABLE. Un atribut simplu cu acelasi nume 'bifeaza' cerinta la fel de bine - o capcana reala: poti crede ca ai implementat metoda, dar ai suprascris-o accidental cu o valoare fixa."},

    {"runda": 5, "categorie": "abstractmethod-cu-corp-apelabil-super", "puncte": 3,
     "cod": 'from abc import ABC, abstractmethod\n\nclass Notificare(ABC):\n    @abstractmethod\n    def formateaza(self, mesaj):\n        return f"[GENERIC] {mesaj}"\n\nclass Email(Notificare):\n    def formateaza(self, mesaj):\n        return super().formateaza(mesaj) + " (trimis pe email)"\n\nprint(Email().formateaza("Bun venit"))',
     "intrebare": "Ce afiseaza? (atentie: metoda abstracta ARE cod, nu doar ...)",
     "optiuni": {"A": "TypeError, nu poti apela super() pe o metoda abstracta",
                 "B": "[GENERIC] Bun venit (trimis pe email)",
                 "C": "Bun venit (trimis pe email)",
                 "D": "AttributeError"},
     "corect": "B",
     "explicatie": "@abstractmethod OBLIGA la override, dar NU interzice cod real in corpul metodei abstracte. Subclasa poate apela acel cod cu super().formateaza(...), exact ca la mostenirea normala - abstractmethod blocheaza doar instantierea directa a clasei abstracte, nu si super()."},

    {"runda": 5, "categorie": "ordine-decoratori-property-abstractmethod", "puncte": 2,
     "cod": 'from abc import ABC, abstractmethod\n\nclass Produs(ABC):\n    @abstractmethod\n    @property\n    def pret(self):\n        ...',
     "intrebare": "Ce se intampla la DEFINIREA clasei Produs (inainte sa creezi vreun obiect)?",
     "optiuni": {"A": "Nimic, clasa se defineste normal",
                 "B": "AttributeError, ordinea decoratorilor e inversata",
                 "C": "SyntaxError",
                 "D": "Devine o metoda abstracta obisnuita, fara property"},
     "corect": "B",
     "explicatie": "Ordinea CONTEAZA: trebuie @property DEASUPRA si @abstractmethod DEDESUBT. Scrisa invers, Python incearca sa marcheze un obiect property ca abstract si arunca AttributeError CHIAR LA DEFINIREA clasei, inainte sa apuci sa creezi vreun obiect."},

    {"runda": 5, "categorie": "implementare-partiala-tot-abstracta", "puncte": 2,
     "cod": 'from abc import ABC, abstractmethod\n\nclass ApiClient(ABC):\n    @abstractmethod\n    def conecteaza(self): ...\n    @abstractmethod\n    def trimite(self, date): ...\n    @abstractmethod\n    def deconecteaza(self): ...\n\nclass ClientPartial(ApiClient):\n    def conecteaza(self):\n        return "conectat"\n    def trimite(self, date):\n        return f"trimis {date}"\n    # a uitat deconecteaza()\n\nc = ClientPartial()',
     "intrebare": "Ce se intampla la ultima linie? (2 din 3 metode abstracte implementate)",
     "optiuni": {"A": "Merge, are majoritatea metodelor implementate",
                 "B": "TypeError, ClientPartial ramane tot abstracta (lipseste deconecteaza)",
                 "C": "AttributeError, dar doar cand apelezi deconecteaza()",
                 "D": "Warning la creare, dar obiectul se creeaza"},
     "corect": "B",
     "explicatie": "TREBUIE implementate TOATE metodele abstracte, nu doar majoritatea. Daca lipseste macar UNA, clasa RAMANE abstracta in intregime si TypeError apare la instantiere - nu la apelul metodei lipsa."},

    {"runda": 5, "categorie": "abstract-property-suprascrisa-cu-atribut", "puncte": 2,
     "cod": 'from abc import ABC, abstractmethod\n\nclass Senzor(ABC):\n    @property\n    @abstractmethod\n    def unitate(self):\n        ...\n\nclass SenzorSimplu(Senzor):\n    unitate = "kg"   # fara @property, doar un atribut normal\n\ns = SenzorSimplu()\nprint(s.unitate)',
     "intrebare": "Ce afiseaza? (atentie: SenzorSimplu NU foloseste @property)",
     "optiuni": {"A": "TypeError, subclasa trebuie neaparat @property",
                 "B": "kg",
                 "C": "<property object at ...>",
                 "D": "AttributeError"},
     "corect": "B",
     "explicatie": "La fel ca la intrebarea cu atributul in loc de metoda: verificarea abstractmethod cere doar ca numele sa fie suprascris, INDIFERENT daca il suprascrii cu @property, cu o metoda sau cu un atribut simplu. 'kg' e un string normal, accesat identic (s.unitate, fara paranteze) - functioneaza perfect, desi tehnic nu mai e un property."},

    {"runda": 5, "categorie": "abc-super-init-lipsa-combo", "puncte": 3,
     "cod": 'from abc import ABC, abstractmethod\n\nclass Procesator(ABC):\n    def __init__(self, nume):\n        self.nume = nume\n    @abstractmethod\n    def proceseaza(self, suma): ...\n\nclass Stripe(Procesator):\n    def __init__(self, nume, taxa):\n        self.taxa = taxa   # a uitat super().__init__(nume)\n    def proceseaza(self, suma):\n        return suma - self.taxa\n\ns = Stripe("stripe", 5)\nprint(s.proceseaza(100))\nprint(s.nume)',
     "intrebare": "Ce se intampla? (Procesator are __init__ CONCRET + o metoda abstracta)",
     "optiuni": {"A": "95, apoi AttributeError la print(s.nume)",
                 "B": "TypeError la crearea lui Stripe, nu are toate metodele",
                 "C": "95, apoi None",
                 "D": "AttributeError chiar la crearea lui Stripe"},
     "corect": "A",
     "explicatie": "Stripe IMPLEMENTEAZA proceseaza() (singura metoda abstracta), deci NU mai e abstracta - se creeaza fara probleme si proceseaza(100) merge (100-5=95). Dar __init__ suprascris UITA super().__init__(nume), deci self.nume nu se seteaza niciodata -> AttributeError abia la s.nume, mult DUPA ce obiectul parea sa functioneze normal."},
]


# =============================================================
# CONFIGURARE INITIALA
# =============================================================
punctaj_maxim = 0
for q in intrebari:
    punctaj_maxim += q["puncte"]

scor                  = 0
intrebari_corecte     = 0
categorii_stapanite   = set()
intrebari_gresite     = []
runda_curenta         = 0


print("=" * 62)
print("===   QUIZ INTERVIU JUNIOR PYTHON  -  OOP (17-20)   ===")
print("=" * 62)
print()
print("Fiecare intrebare are o secventa de COD si o EXPLICATIE")
print("dupa raspuns. Citeste codul cu atentie inainte sa raspunzi.")
print()

nume = input("Numele jucatorului (Enter -> 'Candidat'): ").strip()
if nume == "":
    nume = "Candidat"
print(f"\nSucces, {nume}!  Q + Enter = iesire devreme.\n")


# =============================================================
# MOTORUL QUIZ-ULUI
# =============================================================

i = 0
abandonat = False

while i < len(intrebari) and not abandonat:
    q = intrebari[i]

    # Antet de runda
    if q["runda"] != runda_curenta:
        runda_curenta = q["runda"]
        titluri = {
            1: "CLASE, OBIECTE & self",
            2: "INCAPSULARE — PRIVATE, PROTEJAT, @property",
            3: "MOSTENIRE",
            4: "POLIMORFISM & DUNDER METHODS",
            5: "ABSTRACTIZARE (ABC) — GOTCHA-URI DE INTERVIU",
        }
        print()
        print("=" * 62)
        print(f"  RUNDA {runda_curenta}:  {titluri[runda_curenta]}")
        print("=" * 62)
        print()

    # Afisam intrebarea cu codul
    print(f"Q{i + 1}  [{q['categorie']}, {q['puncte']}p]  -  {q['intrebare']}")
    print()
    print("    --- COD ---")
    for linie in q["cod"].split("\n"):
        print(f"    {linie}")
    print("    -----------")
    print()
    for litera in ("A", "B", "C", "D"):
        print(f"    {litera})  {q['optiuni'][litera]}")
    print()

    # Validare input
    raspuns = ""
    while True:
        raspuns = input("Raspunsul tau (A/B/C/D, Q=iesire): ").strip().upper()
        if raspuns in ("A", "B", "C", "D", "Q"):
            break
        print("  ! Alege A, B, C, D — sau Q ca sa iesi.")

    if raspuns == "Q":
        abandonat = True
        print("\n(ai iesit din quiz)\n")
        break

    # Verificare + AFISARE EXPLICATIE (mereu)
    corect = (raspuns == q["corect"])
    if corect:
        scor += q["puncte"]
        intrebari_corecte += 1
        categorii_stapanite.add(q["categorie"])
        print(f"  >>> CORECT! +{q['puncte']}p   (scor: {scor}/{punctaj_maxim})")
    else:
        intrebari_gresite.append({
            "nr": i + 1,
            "categorie": q["categorie"],
            "raspuns_dat": raspuns,
            "raspuns_corect": q["corect"],
        })
        print(f"  >>> Hmm, nu. Raspuns corect: {q['corect']}) {q['optiuni'][q['corect']]}")
        print(f"      (scor: {scor}/{punctaj_maxim})")

    # Explicatia se afiseaza MEREU (si la corect, si la gresit)
    print(f"  DE CE: {q['explicatie']}")
    print()
    i += 1


# =============================================================
# RAPORT FINAL
# =============================================================
print("=" * 62)
print(f"===          RAPORT INTERVIU  -  {nume}          ===")
print("=" * 62)

procent = (scor / punctaj_maxim * 100) if punctaj_maxim > 0 else 0
print(f"\n  scor:                {scor} / {punctaj_maxim} puncte  ({procent:.0f}%)")
print(f"  intrebari corecte:   {intrebari_corecte} / {i}")

# Evaluare in stil interviu
print()
if procent >= 85:
    print(f"  *** {nume}: profil JUNIOR SOLID — gata de proiecte reale.")
elif procent >= 65:
    print(f"  ** {nume}: profil JUNIOR DECENT — mai cizelam gotcha-urile.")
elif procent >= 45:
    print(f"  * {nume}: profil INCEPATOR — fundamentele sunt, ne trebuie practica.")
else:
    print(f"  {nume}: revizuiti materialul; aproape sigur reusiti la a doua iteratie.")

# Categorii stapanite
print()
print(f"  categorii stapanite ({len(categorii_stapanite)}):")
if categorii_stapanite:
    for cat in sorted(categorii_stapanite):
        print(f"    + {cat}")
else:
    print("    (inca niciuna)")

# Punctele slabe — categorii greșite
if intrebari_gresite:
    print()
    print(f"  zone slabe (de reluat inainte de interviu):")
    zone_slabe = set()
    for g in intrebari_gresite:
        zone_slabe.add(g["categorie"])
    for cat in sorted(zone_slabe):
        print(f"    - {cat}")

    print()
    print(f"  intrebari de revazut:")
    for g in intrebari_gresite:
        print(f"    Q{g['nr']}  [{g['categorie']}]  ai zis {g['raspuns_dat']}, corect {g['raspuns_corect']}")

print()
print("=" * 62)
print("Pregateste-te de interviu: relueaza intrebarile gresite,")
print("apoi reia quiz-ul. La interviu, EXPLICATIA conteaza la fel")
print("de mult cat raspunsul.")
print("=" * 62)