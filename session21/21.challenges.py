#  10 CHALLENGE-URI  -  SOLID (cazuri reale de dev)
# =============================================================


from abc import ABC, abstractmethod


# #############################################################
# CHALLENGE 1  (S - Single Responsibility)
# GENERATOR DE FACTURA CU 3 RESPONSABILITATI INTR-O CLASA
# #############################################################
#
# CONTEXT (caz real)
# ------------------
# O clasa `GeneratorFacturaNaiv` ar face TOT dintr-o data: calculeaza
# totalul comenzii, formateaza textul facturii SI "trimite" (simulat)
# emailul catre client. Trei motive diferite ca aceasta clasa sa se
# schimbe: (1) se schimba formula de calcul (ex: adaugam TVA), (2) se
# schimba formatul facturii (ex: trecem la HTML), (3) se schimba
# providerul de email. O modificare la format ar putea, din greseala,
# sa strice si calculul, pentru ca totul sta in aceeasi clasa.
#
# CE TREBUIE SA FACA SOLUTIA
# --------------------------
# 1. `FacturaCalculator` - primeste `linii` (lista de dicturi cu
#    `produs`/`pret`/`cantitate`) in `__init__` si are o metoda
#    `total()` care intoarce suma `pret * cantitate` pentru toate liniile.
# 2. `FacturaFormatter` - o metoda `formateaza(linii, total)` care
#    construieste un text cu o linie per produs si totalul la final.
# 3. `EmailSender` - o metoda `trimite(cui, continut)` care doar
#    afiseaza (simuleaza trimiterea reala).
#
# CERINTE
# -------
#   - fiecare clasa are DOAR o responsabilitate (calcul / formatare /
#     trimitere) - nici o clasa nu face 2 din cele 3.
#   - `FacturaFormatter` NU calculeaza nimic - primeste totalul deja
#     calculat, ca parametru.
#
# OUTPUT ASTEPTAT
# ---------------
#   1) [email catre client@test.com]
#      Factura:
#        Laptop x1 = 3000 lei
#        Mouse x2 = 160 lei
#      TOTAL: 3160 lei
# =============================================================


print("\n--- Exercitiul 1 ---")
class FacturaCalculator:
    def __init__(self, linii):
        self.linii = linii

    def total(self):
        return sum([linie['pret'] * linie['cantitate'] for linie in self.linii])

class FacturaFormatter:
    def formateaza(self, linii, total):
        text = "Factura: \n"
        for linie in linii:
            subtotal = linie['pret'] * linie['cantitate']
            text += f"{linie['produs']} cu cantitatea {linie['cantitate'] } costa {subtotal}\n"

        text += f"Total: {total}"
        return text

class EmailSender:
    def trimite(self, cui, continut):
        print(f"Email trimis {cui} cu urmatorul continut: {continut} ")



linii = [
    {'produs': 'Laptop', 'pret': 5000,'cantitate': 3},
    {'produs': 'Mouse', 'pret': 500,'cantitate': 6},
    {'produs': 'Desktop', 'pret': 100,'cantitate': 6},
]


calculator = FacturaCalculator(linii)
total_factura = calculator.total()

text_factura = FacturaFormatter().formateaza(linii, total_factura)
print(text_factura)

EmailSender().trimite("client@test.ro", text_factura)



# #############################################################
# CHALLENGE 2  (S - Single Responsibility)
# PROCESARE COMANDA: VALIDARE + STOC + LOGGING INTR-O SINGURA METODA
# #############################################################
#
# CONTEXT (caz real)
# ------------------
# La plasarea unei comenzi, o functie naiva ar verifica daca datele
# sunt valide, ar scadea din stoc SI ar scrie in log - toate in acelasi
# loc. Daca cineva schimba regula de validare, risca sa strice si
# logica de stoc de langa ea, desi n-are nicio legatura.
#
# CE TREBUIE SA FACA SOLUTIA
# --------------------------
# 1. `ValidatorComanda.valideaza(comanda)` - intoarce True doar daca
#    `cantitate > 0` si `produs_id` nu e None.
# 2. `ProcesatorStoc` - primeste `stoc` (dict `{produs_id: cantitate}`)
#    in `__init__`; `scade_stoc(comanda)` scade cantitatea ceruta si
#    intoarce stocul RAMAS pentru acel produs.
# 3. `Logger.info(mesaj)` - afiseaza mesajul cu prefixul `[INFO]`.
#
# CERINTE
# -------
#   - codul "de orchestrare" (verifica -> proceseaza -> logheaza) sta
#     in AFARA celor 3 clase, care raman independente una de alta.
#   - daca `valideaza` intoarce False, NU se atinge stocul - se
#     logheaza direct "Comanda invalida".
#
# OUTPUT ASTEPTAT (pentru stoc {"P1": 10}, comanda cantitate 3)
# ---------------------------------------------------------------
#   2) [INFO] Comanda procesata, stoc ramas: 7
# =============================================================

print("\n--- Exercitiul 2 ---")
class ValidatorComanda:

    def valideaza(self, comanda):
        return comanda['cantitate'] > 0 and comanda['produs_id'] is not None

class ProcesatorStoc:

    def __init__(self, stoc):
        self.stoc = stoc

    def scade_stoc(self,  comanda):
        self.stoc[comanda['produs_id']] -= comanda['cantitate']
        return self.stoc[comanda['produs_id']]

class Logger:
    def info(self, mesaj):
       print(f"[INFO]: {mesaj}")


stoc_curent = {'p1': 10}
comanda_noua = {'produs_id': "p1", 'cantitate': 3}


validator = ValidatorComanda().valideaza(comanda_noua)
procesator_stoc = ProcesatorStoc(stoc_curent)
procesator_stoc.scade_stoc(comanda_noua)
procesator_stoc.scade_stoc(comanda_noua)
log = Logger()
log.info('Comanda valida')

# #############################################################
# CHALLENGE 3  (O - Open/Closed)
# TAXE VAMALE PE CATEGORIE DE PRODUS
# #############################################################
#
# CONTEXT (caz real)
# ------------------
# Un sistem de import/export calculeaza taxa vamala in functie de
# categoria produsului. Varianta naiva ar fi un lant `if/elif` pe
# numele categoriei - la fiecare categorie noua (si vor mai veni),
# cineva trebuie sa MODIFICE aceeasi functie, riscand sa strice
# categoriile existente.
#
# CE TREBUIE SA FACA SOLUTIA
# --------------------------
# 1. O clasa abstracta `TaxaVamala(ABC)` cu o metoda abstracta
#    `aplica(self, valoare)` care intoarce SUMA taxei (nu valoarea cu
#    taxa inclusa).
# 2. `TaxaElectronice` (20%) si `TaxaTextile` (12%) - clasele
#    "existente".
# 3. O clasa NOUA, `TaxaAlimente` (5%), adaugata FARA sa atingeti restul.
# 4. O functie `calculeaza_taxa(taxa, valoare)` care aplica taxa si
#    rotunjeste la 2 zecimale.
#
# CERINTE
# -------
#   - NU exista niciun `if`/`elif` pe numele categoriei - fiecare
#     categorie e o clasa separata.
#   - adaugarea `TaxaAlimente` NU modifica nicio linie din
#     `TaxaElectronice`/`TaxaTextile`/`calculeaza_taxa`.
#
# OUTPUT ASTEPTAT (pentru valoare=1000)
# ---------------------------------------------------------------
#   3) Electronice: 200.0
#   3) Textile: 120.0
#   3) Alimente: 50.0
# =============================================================

print("\n--- Exercitiul 3 ---")
class TaxaVamala(ABC):

    @abstractmethod
    def aplica(self, valoare):
        ...

class TaxaElectronice(TaxaVamala):
    def aplica(self, valoare):
        return valoare * 0.2

class TaxaTextile(TaxaVamala):
    def aplica(self, valoare):
        return valoare * 0.12

class TaxaAlimente(TaxaVamala):
    def aplica(self, valoare):
        return valoare * 0.05

def calculeaza_taxa(taxa, valoare):
    return round(taxa.aplica(valoare), 2)

valoare = 1000
print(f"Electronice: {calculeaza_taxa(TaxaElectronice(), 1000)}")
print(f"Textile: {calculeaza_taxa(TaxaTextile(), 1000)}")
print(f"Alimente: {calculeaza_taxa(TaxaAlimente(), 1000)}")

# #############################################################
# CHALLENGE 4  (O - Open/Closed)
# BONUS DE PERFORMANTA PE DEPARTAMENT
# #############################################################
#
# CONTEXT (caz real)
# ------------------
# HR calculeaza bonusul anual dupa departamentul angajatului. Cu un
# `if/elif` pe numele departamentului, adaugarea unui departament nou
# (ex: Marketing) ar insemna sa MODIFICATI aceeasi functie folosita
# deja pentru toate celelalte departamente - risc de bug pe cod care
# functiona deja.
#
# CE TREBUIE SA FACA SOLUTIA
# --------------------------
# 1. O clasa abstracta `Bonus(ABC)` cu metoda abstracta
#    `calculeaza(self, salariu)`.
# 2. `BonusVanzari` (15%) si `BonusSuport` (8%) - departamentele
#    "existente".
# 3. O clasa NOUA, `BonusDevelopment` (10%), adaugata fara sa atingeti
#    codul existent.
# 4. O functie `bonus_final(bonus, salariu)` care calculeaza si
#    rotunjeste la 2 zecimale.
#
# CERINTE
# -------
#   - fiecare departament e o clasa separata, fara `if`/`elif` pe nume.
#
# OUTPUT ASTEPTAT (pentru salariu=4000)
# ---------------------------------------------------------------
#   4) Vanzari: 600.0
#   4) Suport: 320.0
#   4) Development: 400.0
# =============================================================

print("\n--- Exercitiul 4 ---")

class Bonus(ABC):
    @abstractmethod
    def calculeaza(self, salariu):
        ...
class BonusVanzari(Bonus):
    def calculeaza(self, salariu):
        return salariu * 0.15

class BonusSport(Bonus):
    def calculeaza(self, salariu):
        return salariu * 0.08

class BonusDevelopment(Bonus):
    def calculeaza(self, salariu):
        return salariu * 0.10
def bonus_final(bonus, salariu):
    return round(bonus.calculeaza(salariu), 2)

salariu = 4000
print(f"{bonus_final(BonusVanzari(), salariu)}")
print(f"{bonus_final(BonusSport(), salariu)}")
print(f"{bonus_final(BonusDevelopment(), salariu)}")

# #############################################################
# CHALLENGE 5  (L - Liskov Substitution)
# CONT DE ECONOMII CARE RUPE PROMISIUNEA DE RETRAGERE
# #############################################################
#
# CONTEXT (caz real)
# ------------------
# `Cont.retrage(suma)` PROMITE ca intoarce soldul ramas (un numar). O
# subclasa naiva `ContEconomiiNaiv` (nu permite retrageri) ridica o
# exceptie in loc sa respecte contractul. Orice cod care proceseaza o
# LISTA de conturi (indiferent de tip) se rupe brusc cand da peste un
# cont de economii - desi codul acela nu stia (si n-ar trebui sa stie)
# ca exista tipuri "speciale" de conturi.
#
# CE TREBUIE SA FACA SOLUTIA
# --------------------------
# 1. `Cont` - `__init__(self, sold)`; `retrage(self, suma)` scade suma
#    din sold si intoarce noul sold.
# 2. `ContEconomii(Cont)` - "refuza" retragerea, dar politicos: NU
#    modifica soldul si NU ridica nicio exceptie, doar intoarce soldul
#    NESCHIMBAT (tot un numar, exact ce promite parintele).
# 3. O functie `proceseaza_retrageri(conturi, suma)` care aplica
#    `retrage(suma)` pe fiecare cont dintr-o lista si aduna rezultatele
#    intr-o lista noua.
#
# CERINTE
# -------
#   - `ContEconomii.retrage` NU arunca nicio exceptie.
#   - `proceseaza_retrageri` merge IDENTIC pe o lista amestecata de
#     `Cont` si `ContEconomii`, fara `try/except` in jurul ei.
#
# OUTPUT ASTEPTAT (Cont(1000) si ContEconomii(500), suma=100)
# ---------------------------------------------------------------
#   5) [900, 500]
# =============================================================

print("\n--- Exercitiul 5 ---")
class Cont:
    def __init__(self, sold):
        self.sold = sold

    def retrage(self, suma):
        self.sold -= suma
        return self.sold

class ContEconomii(Cont):
    def retrage(self, suma):
        return self.sold

def proceseaza_retrageri(conturi, suma):
    return list(c.retrage(suma) for c in conturi)

c1 = Cont(1000)

c2 = ContEconomii(500)

print(proceseaza_retrageri([c1, c2], 100))

# #############################################################
# CHALLENGE 6  (L - Liskov Substitution)
# JURNAL DE AUDIT: COMPOZITIE IN LOC DE MOSTENIRE GRESITA
# #############################################################
#
# CONTEXT (caz real)
# ------------------
# Un jurnal de audit trebuie sa fie "doar adaugare" - din motive legale,
# intrarile NU se pot sterge. Varianta naiva ar mosteni direct din
# `list` (ca sa "fure" gratis `append`), dar apoi ar trebui sa
# SUPRASCRIE `remove`/`clear` ca sa arunce eroare - ceea ce inseamna ca
# `ListaNaiv` promite (prin faptul ca E o lista) ca poate face orice
# face o lista, dar de fapt RUPE acea promisiune la unele metode. Orice
# cod generic care primeste "o lista" si incearca `.remove(...)` se
# rupe pe surprinse.
#
# CE TREBUIE SA FACA SOLUTIA
# --------------------------
# 1. In loc sa mosteniti `list`, scrieti `AuditLog` ca o clasa NOUA
#    (compozitie, nu mostenire) care tine intern o lista privata
#    `self._intrari`.
# 2. `adauga(self, item)` - adauga in lista interna.
# 3. `toate(self)` - intoarce o COPIE a listei (ca cine o citeste sa nu
#    poata modifica direct originalul).
#
# CERINTE
# -------
#   - `AuditLog` NU mosteneste `list` si NU are (si nu promite) nicio
#     metoda de stergere - deci nu poate rupe o promisiune pe care n-a
#     facut-o niciodata. Asta e adevarata lectie de LSP: daca nu poti
#     respecta INTREGUL contract al parintelui, nu mosteni din el doar
#     ca sa reutilizezi cateva metode.
#
# OUTPUT ASTEPTAT
# ---------------
#   6) ['user logat', 'comanda plasata']
# =============================================================

print("\n--- Exercitiul 6 ---")
class AuditLog:
    def __init__(self):
        self._intrari = []

    def adauga(self, item):
        return self._intrari.append(item)

    def toate(self):
        return self._intrari[:]

a1 = AuditLog()
a1.adauga('user logat')
a1.adauga('comanda plasata')
print(a1.toate())

# #############################################################
# CHALLENGE 7  (I - Interface Segregation)
# PLUGIN-URI PENTRU UN EDITOR DE TEXT
# #############################################################
#
# CONTEXT (caz real)
# ------------------
# Un editor de text suporta plugin-uri: unele doar formateaza textul,
# altele si verifica ortografia. O interfata NAIVA `PluginEditor` ar
# cere TUTUROR plugin-urilor sa implementeze `formateaza` SI
# `verifica_ortografie` SI `exporta_pdf` - un plugin simplu (doar
# formatare) ar fi obligat sa "implementeze" cele 2 metode pe care nu
# le poate face, de obicei aruncand `NotImplementedError`.
#
# CE TREBUIE SA FACA SOLUTIA
# --------------------------
# 1. Doua interfete MICI, separate: `PoateFormata(ABC)` cu
#    `formateaza(self, text)`, si `PoateVerificaOrtografia(ABC)` cu
#    `verifica_ortografie(self, text)`.
# 2. `PluginFormatare` - implementeaza DOAR `PoateFormata`
#    (`formateaza` = `text.strip().capitalize()`).
# 3. `PluginComplet` - implementeaza AMBELE interfete (mosteneste din
#    ambele clase abstracte).
# 4. O functie `foloseste_formatare(plugin, text)` care cere DOAR
#    `formateaza` (nu conteaza daca pluginul stie si ortografie).
#
# CERINTE
# -------
#   - `PluginFormatare` NU are (si nu trebuie sa aiba)
#     `verifica_ortografie` - nu e obligat sa implementeze ce nu
#     foloseste.
#   - `foloseste_formatare` merge la fel de bine pe `PluginFormatare`
#     SI pe `PluginComplet`.
#
# OUTPUT ASTEPTAT
# ---------------
#   7) Salut lume
#   7) Text corect
# =============================================================

print("\n--- Exercitiul 7 ---")
class PoateFormata(ABC):
    @abstractmethod
    def formateaza(self, text):...

class PoateVerificaOrtografia(ABC):
    @abstractmethod
    def verifica_ortografie(self, text):...

class PluginFormatare(PoateFormata):
    def formateaza(self, text):
        print(f"7) {text.strip().capitalize()}")

class PluginComplet(PoateFormata, PoateVerificaOrtografia):
    def formateaza(self, text):
        print(f"7) {text.strip().capitalize()}")
    def verifica_ortografie(self, text):
        print(f"7) {text.strip().capitalize()}")

def foloseste_formatare(plugin, text):
    plugin.formateaza(text)

foloseste_formatare(PluginComplet(), "Salut lume")
foloseste_formatare(PluginFormatare(), "Text corect")

# #############################################################
# CHALLENGE 8  (I - Interface Segregation)
# DISPOZITIVE SMART HOME
# #############################################################
#
# CONTEXT (caz real)
# ------------------
# O casa inteligenta are dispozitive diferite: un bec (doar pornit/
# oprit) si un termostat (pornit/oprit SI regleaza temperatura). O
# interfata uriasa `DispozitivSmart` care ar cere TUTUROR sa aiba
# `seteaza_temperatura` ar obliga becul sa "implementeze" o metoda care
# nu are niciun sens pentru el.
#
# CE TREBUIE SA FACA SOLUTIA
# --------------------------
# 1. `PoatePornit(ABC)` cu `porneste(self)` si `opreste(self)`.
# 2. `PoateReglaTemperatura(ABC)` cu `seteaza_temperatura(self, grade)`.
# 3. `BecSmart(PoatePornit)` - doar porneste/opreste.
# 4. `TermostatSmart(PoatePornit, PoateReglaTemperatura)` - toate 3
#    metodele.
# 5. O functie `comuta(dispozitiv)` care apeleaza doar `porneste()`.
#
# CERINTE
# -------
#   - `BecSmart` NU are `seteaza_temperatura` - nu e nevoie.
#   - `comuta` merge la fel pe `BecSmart` SI pe `TermostatSmart`.
#
# OUTPUT ASTEPTAT
# ---------------
#   8) bec pornit
#   8) termostat pornit
#   8) seteaza la 21C
# =============================================================

print("\n--- Exercitiul 8 ---")
class PoatePornit(ABC):
    @abstractmethod
    def porneste(self):...
    def opreste(self):...

class PoateReglaTemperatura(ABC):
    @abstractmethod
    def seteaza_temperatura(self, grade):...

class BecSmart(PoatePornit):
    def porneste(self):
        print("8) bec pornit")

    def opreste(self):
        print("8) bec oprit")

class TermostatSmart(PoatePornit, PoateReglaTemperatura):
    def porneste(self):
        print("8) termostat pornit")
    def opreste(self):
        print("8) termostat oprit")
    def seteaza_temperatura(self, grade):
        print("8) seteaza la {grade}C")

def comuta(dispozitiv):
    dispozitiv.porneste()

BecSmart().porneste()
TermostatSmart().porneste()
TermostatSmart().seteaza_temperatura(21)

# #############################################################
# CHALLENGE 9  (D - Dependency Inversion)
# SERVICIU DE COMENZI CU LOGGER INJECTAT
# #############################################################
#
# CONTEXT (caz real)
# ------------------
# `ServiciuComenziNaiv` isi creeaza SINGUR, in `__init__`, un
# `FileLogger` concret - "cablat" direct in cod. Rezultatul: nu puteti
# testa serviciul fara sa scrieti efectiv intr-un fisier/consola, si nu
# puteti schimba usor logger-ul (ex: pentru un serviciu extern de
# monitorizare) fara sa modificati `ServiciuComenzi` insusi.
#
# CE TREBUIE SA FACA SOLUTIA
# --------------------------
# 1. O clasa abstracta `Logger(ABC)` cu metoda abstracta
#    `scrie(self, mesaj)`.
# 2. `FileLogger(Logger)` - `scrie` afiseaza mesajul cu prefixul
#    `[fisier]` (simuleaza scrierea reala).
# 3. `LoggerFals(Logger)` - pentru teste: retine mesajele intr-o lista
#    `self.mesaje`, in loc sa le afiseze.
# 4. `ServiciuComenzi` - PRIMESTE `logger` ca parametru in `__init__`
#    (nu il creeaza singur); `plaseaza(comanda)` scrie in logger
#    `"comanda plasata: {comanda}"`.
#
# CERINTE
# -------
#   - `ServiciuComenzi.__init__` NU instantiaza niciun logger concret -
#     il primeste gata creat, din afara.
#   - aceeasi clasa `ServiciuComenzi` functioneaza atat cu
#     `FileLogger`, cat si cu `LoggerFals`, fara nicio modificare.
#
# OUTPUT ASTEPTAT
# ---------------
#   9) [fisier] comanda plasata: CMD-1
#   9) ['comanda plasata: CMD-2']
# =============================================================

print("\n--- Exercitiul 9 ---")
class Logger(ABC):
    @abstractmethod
    def scrie(self, mesaj):...

class FileLogger(Logger):
    def scrie(self, mesaj):
        print(f"[fisier] {mesaj}")
class LoggerFalse(Logger):
    def __init__(self):
        self.mesaje = []

    def scrie(self, mesaj):
        self.mesaje.append(mesaj)

class ServiciuComenzi:
    def __init__(self, logger):
        self.logger = logger

    def plaseaza(self,comanda):
        self.logger.scrie(f"comanda plasata: {comanda}")


ServiciuComenzi(FileLogger()).plaseaza("CMD -1")
fals = LoggerFalse()
ServiciuComenzi(fals).plaseaza("CMD -2")
print(fals.mesaje)


# #############################################################
# CHALLENGE 10  (D - Dependency Inversion)
# SERVICIU DE RAPOARTE CU SURSA DE DATE INJECTATA
# #############################################################
#
# CONTEXT (caz real)
# ------------------
# Un serviciu de raportare naiv si-ar citi singur datele direct dintr-un
# fisier CSV hardcodat in cod. Cand sursa de date se schimba (trece pe
# un API, sau pe o baza de date), trebuie sa modificati serviciul
# insusi - desi calculul raportului (suma) nu are nicio legatura cu DE
# UNDE vin numerele.
#
# CE TREBUIE SA FACA SOLUTIA
# --------------------------
# 1. O clasa abstracta `SursaDate(ABC)` cu metoda abstracta
#    `citeste(self)` care intoarce o lista de numere.
# 2. `SursaCSVSimulata` si `SursaAPISimulata` - ambele primesc o lista
#    de valori in `__init__` si o intorc identic la `citeste()`
#    (simuleaza doua surse diferite, cu acelasi contract).
# 3. `RaportService` - PRIMESTE `sursa` in `__init__`; `total()`
#    intoarce suma valorilor citite din sursa.
#
# CERINTE
# -------
#   - `RaportService` nu stie NIMIC despre CSV/API - lucreaza doar cu
#     `SursaDate` (abstractia).
#   - aceeasi clasa `RaportService` produce rezultatul corect pentru
#     ambele surse, fara nicio modificare intre ele.
#
# OUTPUT ASTEPTAT
# ---------------
#   10) 600
#   10) 100
# =============================================================

print("\n--- Exercitiul 10 ---")
class SursaDate(ABC):
    @abstractmethod
    def citeste(self):...

class SursaCSVSimulata(SursaDate):
    def __init__(self, date):
        self.date = date

    def citeste(self):
        return self.date

class SursaAPISimulata(SursaDate):
    def __init__(self, date):
        self.date = date

    def citeste(self):
        return self.date

class RaportService:
    def __init__(self, sursa):
        self.sursa = sursa

    def total(self):
        return sum(self.sursa.citeste())

csv= SursaCSVSimulata([100, 200, 300])
api = SursaAPISimulata([20, 30, 50])

rap1 = RaportService(csv)
rap2 = RaportService(api)

print(f"10) {rap1.total()}")
print(f"10) {rap2.total()}")