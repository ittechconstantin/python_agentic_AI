# PRINCIPIILE  S O L I D
# =============================================================
# ROLUL LUI SOLID, mai exact:
# Intr-un script mic (un exercitiu, 20-30 de linii), clasele si
# mostenirea nu prea au cum sa strice ceva - totul incape "in cap"
# dintr-o privire. Dar cand un proiect CRESTE (mai multe clase, mai
# multi oameni care lucreaza pe el, luni sau ani de modificari),
# acelasi tip de cod OOP poate deveni fragil: o schimbare mica intr-un
# loc strica pe neasteptate ceva ce parea neasociat in alt loc,
# testarea devine grea (ai nevoie de jumatate din sistem ca sa testezi
# o bucata), iar adaugarea unei functionalitati noi te obliga sa umbli
# prin cod care deja functiona si risca sa il strici.
#
# SOLID NU e cod nou de invatat, ci 5 GHIDURI care iti spun CUM sa
# structurezi clasele si relatiile dintre ele, ca o schimbare sa ramana
# CAT MAI LOCALA - cand modifici sau adaugi ceva, sa afectezi cat mai
# putin din restul codului. Fiecare litera ataca un alt tip concret de
# fragilitate (vezi exemplele PROBLEMA -> SOLUTIE de mai jos pentru
# fiecare).
#
#   S  -  Single Responsibility  (o singura responsabilitate)
#   O  -  Open / Closed          (deschis la extindere, inchis la modificare)
#   L  -  Liskov Substitution    (subclasa tine promisiunea parintelui)
#   I  -  Interface Segregation  (interfete mici, nu una uriasa)
#   D  -  Dependency Inversion   (depinzi de abstractii, nu de concret)
#
# NU sunt reguli absolute, ci INDICII care te ajuta sa recunosti un
# design slab si sa-l imbunatatesti (sa REFACTORIZEZI) - nu legi pe
# care le respecti orbeste. Pe un script mic, aplicarea lor "cu forta"
# e adesea inutila (over-engineering); cu cat proiectul creste, cu atat
# conteaza mai mult.
#
# Structura fisierului: pentru fiecare litera aratam intai o varianta
# NAIVA (de ce e enervanta) si apoi SOLUTIA.
#
# De ce ai nevoie ca sa intelegi acest fisier (recap):
#   - clase, metode, mostenire, polimorfism (sesiunile 17-19)
#   - clase abstracte: ABC + @abstractmethod (sesiunea 20)
# =============================================================

from abc import ABC, abstractmethod


# =============================================================
# S  -  SINGLE RESPONSIBILITY PRINCIPLE  (SRP)
# =============================================================
# "O clasa ar trebui sa aiba O SINGURA responsabilitate = un singur
#  motiv sa se schimbe."


# PROBLEMA (naiv): o clasa care face TOTUL
# -------------------------------------------------------------
class RaportNaiv:
    def __init__(self, angajati):
        self.angajati = angajati

    def total_salarii(self):
        return sum(a["salariu"] for a in self.angajati)

    def salveaza_in_db(self):       # responsabilitate 2: stocare
        print("[db] salvat")

    def trimite_email(self, cui):   # responsabilitate 3: email
        print(f"[email] trimis la {cui}")

    def formateaza_html(self):      # responsabilitate 4: prezentare
        return "<html>...</html>"

# Clasa are 4 "motive diferite sa se schimbe": cineva schimba formula de
# calcul al salariilor, altcineva schimba baza de date folosita, altcineva
# schimba textul emailului, altcineva schimba aspectul HTML-ului. Toate
# patru modificarile ating ACELASI fisier si ACEEASI clasa, desi n-au
# nicio legatura una cu alta.
#
# De ce e o problema, concret:
#   - Doi colegi lucreaza in paralel - unul la email, altul la baza de
#     date. Amandoi modifica ACELASI fisier -> conflicte la merge in Git,
#     desi treaba lor nu are nicio legatura.
#   - Cu cat clasa se modifica mai des (din 4 motive, nu unul), cu atat
#     creste riscul sa strici din GRESEALA o parte care functiona deja -
#     ex: redenumesti un atribut in timp ce "faci curat" la HTML, fara sa
#     observi ca acelasi atribut e folosit si de total_salarii().


# SOLUTIA: o clasa = o responsabilitate
# -------------------------------------------------------------
class Raport:
    def __init__(self, angajati):
        self.angajati = angajati

    def total_salarii(self):
        return sum(a["salariu"] for a in self.angajati)

class RaportRepo:                   # doar stocare
    def salveaza(self, raport):
        print("[db] salvat raport")

class EmailService:                 # doar trimitere email
    def trimite(self, cui, continut):
        print(f"[email] -> {cui}: {continut}")

class HTMLFormatter:                # doar prezentare
    def render(self, raport):
        return f"<html>total: {raport.total_salarii()}</html>"

r = Raport([{"salariu": 100}, {"salariu": 200}])
RaportRepo().salveaza(r)                                    # [db] salvat raport
EmailService().trimite("ana@x.com", HTMLFormatter().render(r))
# [email] -> ana@x.com: <html>total: 300</html>


# =============================================================
# O  -  OPEN / CLOSED PRINCIPLE  (OCP)
# =============================================================
# "Codul sa fie DESCHIS pentru extindere, dar INCHIS pentru modificare."
# Cand adaugi o varianta noua, adaugi COD NOU (o clasa), nu editezi
# codul existent. In Python: prin polimorfism.


# PROBLEMA (naiv): un lant de if pe "tip"
# -------------------------------------------------------------
def pret_final_naiv(produs):
    if produs["tip"] == "carte":
        return produs["pret"] * 0.9        # reducere
    elif produs["tip"] == "electronic":
        return produs["pret"] * 1.19       # cu TVA
    elif produs["tip"] == "alimente":
        return produs["pret"] * 1.05
    return produs["pret"]
    # La FIECARE tip nou trebuie sa MODIFIC aceasta functie existenta,
    # nu doar sa adaug ceva langa ea.
    #
    # De ce e o problema, concret: ca sa adaugi "alimente", editezi o
    # functie care deja functiona pentru "carte" si "electronic". Un
    # elif pus gresit, o linie mutata din greseala - si rupi un calcul
    # care mergea bine de multa vreme, doar ca sa adaugi un caz nou.


# SOLUTIA: fiecare politica de pret intr-o clasa
# -------------------------------------------------------------
class PoliticaPret(ABC):
    @abstractmethod
    def aplica(self, pret_baza):
        ...

class Carte(PoliticaPret):
    def aplica(self, pret_baza):
        return pret_baza * 0.9

class Electronic(PoliticaPret):
    def aplica(self, pret_baza):
        return pret_baza * 1.19

# Un tip NOU = o clasa noua. NU atingem cele existente:
class Cosmetice(PoliticaPret):
    def aplica(self, pret_baza):
        return pret_baza * 1.10

def pret_final(politica, pret_baza):
    return round(politica.aplica(pret_baza), 2)

print(pret_final(Carte(), 100))         # 90.0
print(pret_final(Electronic(), 100))    # 119.0
print(pret_final(Cosmetice(), 100))     # 110.0  (adaugat fara sa modificam nimic)


# =============================================================
# L  -  LISKOV SUBSTITUTION PRINCIPLE  (LSP)
# =============================================================
# "O subclasa trebuie sa poata fi folosita IN LOCUL parintelui, fara
#  surprize." Daca metoda parintelui PROMITE ceva (ex: intoarce un
#  numar), subclasa trebuie sa tina promisiunea - nu sa arunce eroare.


# PROBLEMA (naiv): o subclasa care RUPE contractul
# -------------------------------------------------------------
class AngajatNaiv:
    def __init__(self, nume, salariu):
        self.nume = nume
        self.salariu = salariu

    def bonus_anual(self):
        return self.salariu * 0.1          # promite: intoarce un numar

class PartTimeNaiv(AngajatNaiv):
    def bonus_anual(self):
        raise ValueError("part-time nu are bonus")   # rupe promisiunea!

def total_bonusuri_naiv(angajati):
    return sum(a.bonus_anual() for a in angajati)

try:
    total_bonusuri_naiv([AngajatNaiv("Ana", 5000), PartTimeNaiv("Ion", 3000)])
except ValueError as e:
    print(f"crapa: {e}")                    # crapa: part-time nu are bonus
# total_bonusuri_naiv e scris pentru "orice Angajat", fara sa stie ca
# exista PartTime. Cand lista contine si un PartTime, .bonus_anual()
# arunca eroare pe neasteptate - desi codul apelant n-a facut nimic
# gresit, doar a primit tipul "gresit" de Angajat. Ca sa nu mai crape,
# ar trebui sa verifice manual tipul fiecarui angajat inainte
# (if isinstance(a, PartTime): ...) - exact ce voia mostenirea sa evite:
# sa poti trata TOATE subclasele la fel, fara conditii speciale.


# SOLUTIA: subclasa respecta contractul (intoarce un numar, ex 0)
# -------------------------------------------------------------
class Angajat:
    def __init__(self, nume, salariu):
        self.nume = nume
        self.salariu = salariu

    def bonus_anual(self):
        return self.salariu * 0.1

class PartTime(Angajat):
    def bonus_anual(self):
        return 0                            # tine promisiunea: tot un numar

def total_bonusuri(angajati):
    return sum(a.bonus_anual() for a in angajati)

print(total_bonusuri([Angajat("Ana", 5000), PartTime("Ion", 3000)]))   # 500.0
# Acum orice Angajat (inclusiv PartTime) e substituibil fara surprize.

# =============================================================
# I  -  INTERFACE SEGREGATION PRINCIPLE  (ISP)
# =============================================================
# "Nu forta clientii sa depinda de metode pe care nu le folosesc."
# Mai bine mai multe interfete MICI decat una uriasa pe care fiecare
# implementator e obligat sa o "rezolve" toata.


# PROBLEMA (naiv): o interfata uriasa
# -------------------------------------------------------------
class Multifunctionala(ABC):
    @abstractmethod
    def printeaza(self, doc): ...
    @abstractmethod
    def scaneaza(self, doc): ...
    @abstractmethod
    def trimite_fax(self, doc): ...

class ImprimantaIeftinaNaiv(Multifunctionala):
    def printeaza(self, doc):
        print(f"print: {doc}")
    def scaneaza(self, doc):
        raise NotImplementedError           # nu stie sa scaneze
    def trimite_fax(self, doc):
        raise NotImplementedError           # nici fax
# ImprimantaIeftinaNaiv PROMITE (prin faptul ca mosteneste din
# Multifunctionala) ca stie sa scaneze si sa trimita fax - dar de fapt
# arunca eroare la amandoua. Oricine primeste un obiect "Multifunctionala"
# si ii cere sa scaneze se asteapta sa functioneze, la fel ca la
# PartTime.bonus_anual() de mai sus (Liskov Substitution) - doar ca aici
# cauza e o interfata prea MARE (cere prea multe metode), nu o subclasa
# prost gandita.


# SOLUTIA: interfete mici, combinate dupa nevoie
# -------------------------------------------------------------
class PoatePrinta(ABC):
    @abstractmethod
    def printeaza(self, doc): ...

class PoateScana(ABC):
    @abstractmethod
    def scaneaza(self, doc): ...

class ImprimantaSimpla(PoatePrinta):        # doar ce stie sa faca
    def printeaza(self, doc):
        print(f"print: {doc}")

class Multifunctionala2(PoatePrinta, PoateScana):
    def printeaza(self, doc):
        print(f"MFP print: {doc}")
    def scaneaza(self, doc):
        print(f"MFP scan: {doc}")

def trimite_la_print(dispozitiv, doc):      # cere DOAR PoatePrinta
    dispozitiv.printeaza(doc)

trimite_la_print(ImprimantaSimpla(), "raport.pdf")     # print: raport.pdf
trimite_la_print(Multifunctionala2(), "raport.pdf")    # MFP print: raport.pdf


# =============================================================
# D  -  DEPENDENCY INVERSION PRINCIPLE  (DIP)
# =============================================================
# "Modulele importante NU depind direct de detalii concrete; ambele
#  depind de o ABSTRACTIE." Practic: nu instantia singur clasa concreta
#  inauntru - PRIMESTE-o din afara (prin ABC/parametru).


# PROBLEMA (naiv): serviciul isi creeaza singur baza de date
# -------------------------------------------------------------
class MySQLNaiv:
    def query(self, sql):
        print(f"[mysql] {sql}")

class ServiciuUserNaiv:
    def __init__(self):
        self.db = MySQLNaiv()               # CABLAT - nu il poti schimba/testa

    def gaseste(self, id):
        self.db.query(f"SELECT * FROM users WHERE id={id}")
# Doua probleme concrete:
#   - Ca sa scrii un test pentru ServiciuUserNaiv, ai nevoie de un MySQL
#     real, pornit, cu date - un test care ar trebui sa dureze
#     milisecunde acum depinde de o baza de date intreaga.
#   - Daca vrei sa treci de la MySQL la alta baza de date, trebuie sa
#     modifici ServiciuUserNaiv direct (linia self.db = MySQLNaiv()) -
#     clasa care ar trebui sa se ocupe doar de "gaseste un user" e
#     legata "in dur" de o tehnologie anume.


# SOLUTIA: primeste o abstractie  Database  din afara
# -------------------------------------------------------------
class Database(ABC):
    @abstractmethod
    def query(self, sql):
        ...

class MySQL(Database):
    def query(self, sql):
        print(f"[mysql] {sql}")

class DatabaseFals(Database):               # pentru teste: tine in memorie
    def __init__(self):
        self.apeluri = []

    def query(self, sql):
        self.apeluri.append(sql)

class ServiciuUser:
    def __init__(self, db):
        self.db = db                        # primit din afara (injectat)

    def gaseste(self, id):
        self.db.query(f"SELECT * FROM users WHERE id={id}")

# in productie:
ServiciuUser(MySQL()).gaseste(42)           # [mysql] SELECT * FROM users WHERE id=42

# in teste: aceeasi clasa, alt "db" - putem inspecta ce s-a apelat
fals = DatabaseFals()
ServiciuUser(fals).gaseste(42)
print(fals.apeluri)                         # ['SELECT * FROM users WHERE id=42']


# =============================================================
# RECAP  -  CHECKLIST PRACTIC
# =============================================================
#   S  Clasa are mai multe motive sa se schimbe?  -> imparte-o.
#   O  Ca sa adaugi o varianta modifici un if/elif?  -> foloseste o clasa noua.
#   L  Subclasa arunca / se comporta altfel decat promite parintele?
#         -> nu e un subtip potrivit; regandeste ierarhia.
#   I  Interfata obliga la metode nefolosite?  -> sparge-o in interfete mici.
#   D  Clasa isi instantiaza singura dependinta concreta (DB, email)?
#         -> primeste-o din afara, ca abstractie (injectie de dependente).
#
# Greseli frecvente:
#   - sa aplici SOLID "cu forta" pe un script de 20 de linii (over-engineering).
#     Principiile conteaza pe masura ce codul creste.
#   - sa confunzi SRP cu "o clasa = o metoda". Responsabilitate != metoda.
#   - sa rupi LSP mostenind doar ca sa reutilizezi cod ("are-un" vs "este-un",
#     vezi sesiunea 18).
#
# =============================================================
# CONCLUZIE
# =============================================================
# SOLID iti da o LIMBA COMUNA pentru design: poti spune "asta incalca
# SRP" sau "ar trebui inversata dependenta", iar colegii inteleg imediat.
# Nu sunt reguli rigide - sunt semnale pentru cand merita sa refactorizezi.
# =============================================================