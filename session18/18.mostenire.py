# OOP  -  MOSTENIREA  (Inheritance)
# =============================================================
# In sesiunea 17 am invatat sa construim CLASE proprii (atribute,
# metode, __init__, incapsulare). Acum invatam sa construim o clasa
# NOUA pornind de la una EXISTENTA: copilul primeste "din oficiu"
# atributele si metodele parintelui, si adauga sau inlocuieste doar
# ce e diferit.
#
# DE CE mostenire?
#   - NU rescrii acelasi cod in mai multe clase (principiul DRY:
#     "Don't Repeat Yourself").
#   - Modeleaza relatia "ESTE UN": un Manager ESTE UN Angajat, un
#     Admin ESTE UN User, un ContEconomii ESTE UN ContBancar.
#   - Permite SPECIALIZARE: copilul schimba doar ce e diferit.
#   - Sta la baza POLIMORFISMULUI (acelasi cod pe tipuri diferite).
#
# Termeni (ii folosim tot fisierul):
#   - clasa PARINTE  = superclasa = clasa de BAZA   (Angajat)
#   - clasa COPIL    = subclasa                       (Manager)
#   - "subclasa MOSTENESTE de la superclasa"
#
# De ce ai nevoie ca sa intelegi acest fisier (recap din sesiunea 17):
#   - class, __init__, self, metode
#   - atribute de instanta vs atribute de clasa
#   - __str__ / __repr__
# =============================================================


# =============================================================
# PARTEA 1 - BAZELE
# =============================================================


# 1. PROBLEMA: doua clase inrudite = acelasi cod copiat de doua ori
# -------------------------------------------------------------
# Avem angajati si manageri. Un manager E un angajat, dar in plus
# conduce o echipa. Fara mostenire, copiem tot ce e comun:

class AngajatV1:

    def __init__(self, nume, salariu):
        self.nume = nume
        self.salariu = salariu

    def prezinta(self):
        return f"{self.nume} are salariul {self.salariu} RON"

class ManagerV1:
    def __init__(self, nume, salariu):
        self.nume = nume
        self.salariu = salariu

    def prezinta(self):
        return f"{self.nume} are salariul {self.salariu} RON"


# Enervant si periculos: daca schimbi formatul din prezinta(), trebuie
# sa-l schimbi in AMBELE clase. La 5 tipuri de angajati = cosmar.
# SOLUTIA: Manager MOSTENESTE de la Angajat ce e comun.


# 2. SINTAXA  -  class Copil(Parinte):  copilul primeste TOT
# -------------------------------------------------------------
# Punem parintele intre paranteze. Copilul mosteneste automat atribute
# si metode, chiar daca nu scrie nimic in plus.

class Angajat:

    def __init__(self, nume, salariu):
        self.nume = nume
        self.salariu = salariu

    def prezinta(self):
        return f"{self.nume} are salariul {self.salariu} RON"


class Manager(Angajat):
    pass

m = Manager("Ana", 5000)
print(m.nume)


# Manager nu are propriul __init__ / prezinta - le foloseste pe ale lui Angajat.


# 3. super().__init__  -  copilul adauga atribute proprii
# -------------------------------------------------------------
# Managerul are in plus o echipa. Ii dam propriul __init__, dar NU
# rescriem initializarea parintelui - o apelam cu super().__init__(...).
# `super()` inseamna "parintele meu".


class Manager(Angajat):
    def __init__(self, nume, salariu, echipa):
        super().__init__(nume, salariu)
        self.echipa = echipa

m = Manager("Ioana", 6000, ["Maria", 'Ion', 'George'])
print(m.nume, m.salariu, m.echipa)
print(m.prezinta())

# Fara super().__init__ ar trebui sa rescriem self.nume = nume etc. - exact
# duplicarea pe care voiam sa o evitam.


# 4. METODE NOI  in copil  (pe langa cele mostenite)
# -------------------------------------------------------------
# Copilul poate avea metode care nu exista in parinte.
class Manager(Angajat):
    def __init__(self, nume, salariu, echipa):
        super().__init__(nume, salariu)
        self.echipa = echipa

    def raport_echipa(self):
        return f"{self.nume} conduce echipa de {len(self.echipa)}"

m = Manager("Ioana", 6000, ["Maria", 'Ion', 'George'])
print(m.nume, m.salariu, m.echipa)
print(m.prezinta())
print(m.raport_echipa())


# 5. OVERRIDE  -  copilul REDEFINESTE o metoda a parintelui
# -------------------------------------------------------------
# Daca metoda parintelui nu se potriveste, o rescriem in copil. Cand
# obiectul e de tip copil, se foloseste versiunea copilului.

class Manager(Angajat):

    def prezinta(self):
        return f"{self.nume} este un manager cu salariul de {self.salariu}"

m = Manager("Dan", 1000)
print(m.prezinta())

# Acelasi apel .prezinta(), rezultat diferit, in functie de TIPUL obiectului.


# =============================================================
# PARTEA 2 - CAZURI REALE
# =============================================================


# 6. EXTINDERE cu super().metoda()  -  completezi, nu inlocuiesti
# -------------------------------------------------------------
# De multe ori NU vrei sa arunci logica parintelui, ci sa o COMPLETEZI.
# Atunci apelezi super().metoda() si adaugi la rezultat. Caz real:
# useri si admini pe un site.

class User:

    def __init__(self, nume, email):
        self.nume = nume
        self.email = email

    def descriere(self):
        return f"{self.nume} are email-ul {self.email}"

    def poate(self, actiune):
        return actiune == "citeste"


class Admin(User):

    def descriere(self):
        baza = super().descriere() # ia descrierea de la User
        return baza + "[ADMIN]"    # concateneaza cu "[ADMIN]"

    def poate(self, actiune):
        return True                # adminul poate orice


u = User("Ana", 'ana@gmail.com')
a = Admin("Cristian", "cristian@gmail.com")

print(u.descriere())
print(a.descriere())
print(u.poate("scrie"))
print(u.poate("citeste"))



# 7. isinstance() si issubclass()  -  verificari de tip
# -------------------------------------------------------------
# isinstance(obiect, Clasa) -> True daca obiectul e de acel tip SAU
#                              al unui descendent.
# issubclass(A, B)          -> True daca A e subclasa lui B.

print(isinstance(u, User))    #True
print(isinstance(a, User))    #True, un Admin ESTE UN USER
print(issubclass(Admin, User))#True
print(issubclass(User, Admin))#False



# 8. POLIMORFISM  -  acelasi cod, obiecte de tipuri diferite
# -------------------------------------------------------------
# PROBLEMA: vrem sa trimitem notificari pe canale diferite (email,
# SMS, push) fara if-uri lungi gen  if tip == "email": ...
# SOLUTIA: o clasa de baza cu o metoda comuna, subclase care o
# suprascriu. Codul care le foloseste NU stie/nu-i pasa ce tip e
# fiecare - le trateaza uniform.


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

for n in notificari:
    n.trimite()


# [EMAIL catre ana@site.ro] comanda confirmata
# [SMS catre 0722...] cod livrare: 4821
# [EMAIL catre ion@site.ro] factura atasata
# ASTA e polimorfismul: un singur "for", comportamente diferite.


# 9. ATRIBUTE DE CLASA se mostenesc (si pot fi "umbrite")
# -------------------------------------------------------------
# Un atribut de clasa din parinte e vizibil in copil. Daca copilul
# defineste unul cu acelasi nume, il "umbreste" doar pentru el.

class AngajatConcediu:
    ZILE_CONCEDIU = 21     # REGULA STANDARD


class ManagerConcediu(AngajatConcediu):
    ZILE_CONCEDIU = 26     # managerii au mai multe zile(umbrite)

class StagiarConcediu(AngajatConcediu):
    pass

print(AngajatConcediu.ZILE_CONCEDIU)
print(ManagerConcediu.ZILE_CONCEDIU)
print(StagiarConcediu.ZILE_CONCEDIU)



# 10. object  -  parintele TUTUROR claselor; __str__ se mosteneste
# -------------------------------------------------------------
# Orice clasa mosteneste implicit din  object  (de aceea o clasa goala
# are deja __init__, __str__ etc.). Si un __str__ definit in parinte se
# mosteneste in copil daca acesta nu il rescrie.

class Produs:
    def __init__(self, nume, pret):
        self.nume = nume
        self.pret = pret

    def __str__(self):
        return f"{self.nume} are pretul {self.pret} RON"

class ProdusDigital(Produs):
    pass

print(ProdusDigital("ebook", 100))

# =============================================================
# PARTEA 3 - UNELTE / CAZURI AVANSATE
# =============================================================


# 11. LANT super()  -  fiecare nivel completeaza rezultatul
# -------------------------------------------------------------
# Cand parintele SI copilul au aceeasi metoda si fiecare apeleaza
# super(), se executa TOT lantul, de sus in jos. Caz real: un raport
# care se construieste in straturi.

class Raport:
    def genereaza(self):
        print("date de baza")

class RaportFinanciar(Raport):
    def genereaza(self):
        super().genereaza()            # intai ia partea parintelui
        print("secitunea financiara")  # apoi partea proprie

class RezumatExecutiv(Raport):
    def genereaza(self):
        super().genereaza()
        print("rezumat executiv")

# - date de baza
# - sectiune financiara
# - rezumat executiv

RezumatExecutiv().genereaza()

# 12. MOSTENIRE MULTIPLA si MIXIN-uri
# -------------------------------------------------------------
# O clasa poate avea MAI MULTI parinti. Cel mai curat mod de folosire:
# "mixin"-uri = clase mici care adauga o capabilitate reutilizabila.

class Salvabil:
    def salveaza(self):
        return f"SALVEAZA"

class Notificabil:
    def notifica(self):
        return f"NOTIFICA"

    def salveaza(self):
        return f"SALVEAZA"

class Document(Salvabil, Notificabil):
    def __init__(self, nume_fisier):
        self.nume = nume_fisier


d = Document("contracte.pdf")
print(d.salveaza())
print(d.notifica())


# 13. MRO  -  ordinea in care Python cauta metodele
# -------------------------------------------------------------
# Cand exista mai multi parinti, Python cauta metoda intr-o ordine
# fixa: "Method Resolution Order". O vezi cu  Clasa.__mro__.

print(Document.__mro__)

# (<class '__main__.Document'>, <class '__main__.Salvabil'>,
#  <class '__main__.Notificabil'>, <class 'object'>)
# Cauta metoda in aceasta ordine si o foloseste pe prima gasita.


# 14. "ESTE UN" (mostenire) vs "ARE UN" (compunere)
# -------------------------------------------------------------
# Greseala clasica: sa mostenesti cand relatia nu e "ESTE UN".
# O Masina NU "este un" Motor - ea "ARE UN" Motor. Aici NU folosim
# mostenire, ci COMPUNERE: un obiect tine alt obiect ca atribut.

class Motor:

    def __init__(self, cai_putere):
        self.cai_putere = cai_putere

    def porneste(self):
        return f"Motor de {self.cai_putere} CP a pornit"


class Masina:

    def __init__(self, marca, cai_putere):
        self.marca = marca
        self.motor =  Motor(cai_putere)

    def porneste(self):
        return f"{self.marca}: {self.motor.porneste()}"

masina = Masina("Audi", 200)
print(masina.porneste())


# Regula: "ESTE UN" -> mostenire.  "ARE UN" -> compunere.


# =============================================================
# RECAP / GRESELI FRECVENTE
# =============================================================
# - class Copil(Parinte):  copilul mosteneste TOATE atributele si
#   metodele parintelui.
# - super().__init__(...)  in copil = ruleaza initializarea parintelui,
#   ca sa nu rescrii self.nume = ... etc.
# - OVERRIDE = rescrii o metoda in copil (o inlocuiesti).
# - EXTINDERE = super().metoda() + cod nou (o completezi).
# - isinstance / issubclass = verifici tipul / relatia de mostenire.
# - POLIMORFISM = acelasi cod (un for) peste obiecte de tipuri diferite
#   care au aceeasi metoda; fiecare se comporta in felul lui.
# - Atributele de clasa se mostenesc; copilul le poate "umbri".
# - object e radacina tuturor claselor.
#
# Greseli frecvente:
#   - sa uiti super().__init__(...) -> atributele parintelui lipsesc
#     si primesti AttributeError cand le folosesti.
#   - sa folosesti mostenire pentru "ARE UN" (Masina din Motor) in loc
#     de compunere.
#   - ierarhii prea adanci (5-6 niveluri) = greu de urmarit; prefera
#     ierarhii plate sau compunere.
#   - override total cand voiai doar sa extinzi (uiti super()).
#
# =============================================================
# CONCLUZIE (sablon de retinut)
# =============================================================
# class Parinte:
#     def __init__(self, x):
#         self.x = x
#     def metoda(self):
#         return "..."
#
# class Copil(Parinte):
#     def __init__(self, x, y):
#         super().__init__(x)        # init la parinte
#         self.y = y                 # ce e specific copilului
#
#     def metoda(self):
#         baza = super().metoda()    # extindere (optional)
#         return baza + " + extra"
#
# In sesiunea urmatoare: continuam cu POLIMORFISM si ABSTRACTIZARE -
# cum definim o "interfata" comuna pe care mai multe clase o respecta.
# =============================================================