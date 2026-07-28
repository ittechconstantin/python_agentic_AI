# OOP  -  ABSTRACTIZAREA  (Abstract Base Classes)
# =============================================================
# Al patrulea si ultimul pilon OOP:
#   1) INCAPSULARE   (sesiunea 17)
#   2) MOSTENIRE     (sesiunea 18)
#   3) POLIMORFISM   (sesiunea 19)
#   4) ABSTRACTIZARE (sesiunea 20 - aici)
#
# Ce inseamna abstractizarea?
#   Definim un CONTRACT: "orice procesator de plata TREBUIE sa stie sa
#   proceseze si sa ramburseze". Contractul spune CE trebuie facut, nu
#   CUM. Fiecare subclasa (Stripe, PayPal) decide CUM.
#
# In sesiunea 19, cu duck typing, contractul era IMPLICIT ("orice
# obiect care are metoda plateste()"). Daca cineva uita metoda, aflai
# tarziu - abia cand o apelai (AttributeError la RUNTIME).
#
# Cu o Abstract Base Class (ABC) contractul devine EXPLICIT si
# VERIFICAT: daca o subclasa uita sa implementeze o metoda ceruta,
# primesti eroare INCA DE LA CREAREA obiectului, nu mai tarziu.
#
# De ce ai nevoie ca sa intelegi acest fisier (recap):
#   - clase, __init__, metode (sesiunea 17)
#   - mostenire, super() (sesiunea 18)
#   - polimorfism si duck typing (sesiunea 19)
# =============================================================
from abc import ABC, abstractmethod


# =============================================================
# PARTEA 1 - CE ESTE si DE CE
# =============================================================


# 1. PROBLEMA: o metoda "default" lasa bug-uri tacute
# -------------------------------------------------------------
# Vrem o baza comuna pentru procesatori de plata. Naiv, punem o
# metoda cu implementare default. Dar daca o subclasa UITA sa o
# rescrie, codul merge... si nu face nimic. Bug tacut.

class ProcesatorPlati:
    def proceseaza(self):
        return None             # default None



class Stripe(ProcesatorPlati):
    pass                       # am uitat sa implementez metoda proceseaza

p = Stripe()
print(p.proceseaza())          # None, nicio plata, nu am implementat nimic

# Am putea pune  raise NotImplementedError, dar atunci eroarea apare
# abia cand APELAM metoda - poate in productie, tarziu.
# VREM: eroare inca de la CREAREA obiectului incomplet. Asta face ABC.


# 2. SOLUTIA: ABC + @abstractmethod  -  contract verificat la CREARE
# -------------------------------------------------------------
# Din modulul standard `abc`:
#   - ABC             = clasa de baza pentru clase abstracte
#   - @abstractmethod = marcheaza o metoda drept OBLIGATORIU de implementat
# O clasa care mosteneste ABC si are metode abstracte NU poate fi
# instantiata direct.


class ProcesatorPlati(ABC):

    @abstractmethod
    def proceseaza(self, suma):
        pass

    @abstractmethod
    def rambursaza(self):
        pass


# Nu poti crea direct un obiect din clasa abstracta:
try:
    x = ProcesatorPlati()
except TypeError as e:
    print(e)


# 3. SUBCLASE CONCRETE  -  implementeaza TOATE metodele abstracte
# -------------------------------------------------------------
# O subclasa care implementeaza tot ce e abstract devine "concreta"
# si poate fi instantiata.

class Stripe(ProcesatorPlati):
    def proceseaza(self,suma):
        return "[Stripe] plata procesata in valoare de " + str(suma) + " lei"

    def rambursaza(self):
        return "[Stripe] rambursare efectuata"


class PayPal(ProcesatorPlati):
    def proceseaza(self, suma):
        return "[PayPal] plata procesata in valoare de " + str(suma) + " lei"

    def rambursaza(self):
        return "[PayPal] rambursare efectuata"

plata_online = Stripe()
print(plata_online.proceseaza(100))

plata_paypal = PayPal()
print(plata_paypal.proceseaza(200))


# 4. SUBCLASA INCOMPLETA  =  TOT ABSTRACTA
# -------------------------------------------------------------
# Daca o subclasa nu implementeaza TOATE metodele abstracte, ramane
# ea insasi abstracta - deci nu poate fi instantiata.

class TransferBancar(ProcesatorPlati):

    def proceseaza(self, suma):
        return "[Transfer Bancar] plata procesata in valoare de " + str(suma) + " lei"


# tr_bancar = TransferBancar()
# print(tr_bancar.proceseaza(100))


# =============================================================
# PARTEA 2 - CAZURI REALE
# =============================================================


# 5. ABC cu metode CONCRETE + abstracte  (parintele orchestreaza)
# -------------------------------------------------------------
# Puterea reala: parintele scrie logica COMUNA (concreta) si o
# construieste peste pasii abstracti pe care ii completeaza copiii.
# (In alte limbaje asta se numeste "template method".)


class Procesator(ABC):

    def __init__(self, comercitant):
        self.comercitant = comercitant   # atribut public comun tuturor

    @abstractmethod
    def proceseaza_plata(self, suma):
        pass

    def plateste_si_istoric(self, suma):
        rezultat = self.proceseaza_plata(suma)
        return f"{self.comercitant} -> {rezultat}"


class StripeV2(Procesator):
    def proceseaza_plata(self, suma):
        return f"[Stripe] plata procesata in valoare de {suma} lei"

class PayPalV2(Procesator):
    def proceseaza_plata(self, suma):
        return f"[PayPal] plata procesata in valoare de {suma} lei"

s = StripeV2("NIBIRU")
print(s.plateste_si_istoric(100))


# 6. @property ABSTRACTA  -  obligi subclasa sa ofere o valoare
# -------------------------------------------------------------
# Combinand @property cu @abstractmethod, ceri fiecarei subclase sa
# ofere un atribut calculat. Parintele il poate folosi in cod comun.


class Abonament(ABC):

    @property
    @abstractmethod
    def pret_unitar(self):
        pass

    def pret_anual(self):
        return self.pret_unitar * 12


class AbonamentBasic(Abonament):
    @property
    def pret_unitar(self):
        return 1000

class AbonamentPremium(Abonament):
    def pret_unitar(self):
        return 2000


obj1 = AbonamentBasic()
print(obj1.pret_unitar)

# cu @property:                                                 fara property
# 1. 1000 valoare, nu trebuie sa apelam metoda                1. <bound method.....
# 2. obj1.pret_unitar fara ()                                 2. obj1.pret_unitar() - trebuie paranteze
# 3. self.pret_unitar * 12                                    3. self.pret_unitar * 12 EROARE TypeError



# 7. isinstance / issubclass  -  "respecta obiectul contractul?"
# -------------------------------------------------------------
print(isinstance(StripeV2("Nibiru"), Procesator))  # True
print(isinstance(Stripe, Procesator))              # False

print(issubclass(PayPalV2, Procesator))            # True


# 8. POLIMORFISM SUB CONTRACT  -  cod care primeste garantat un Procesator
# -------------------------------------------------------------
# Acum poti scrie cod care lucreaza pe orice Procesator, stiind sigur
# ca metodele exista (contractul e garantat de ABC).


def raporteaza_palti(procesatori, suma):
    for procesator in procesatori:
        print(procesator.plateste_si_istoric(suma))

raporteaza_palti([StripeV2("Nibiru"), PayPalV2("BeachPlease")], 100)


# Nibiru -> [Stripe] plata procesata in valoare de 100 lei
# BeachPlease -> [PayPal] plata procesata in valoare de 100 lei

# =============================================================
# PARTEA 3 - AVANSAT si IMAGINE DE ANSAMBLU
# =============================================================


# 9. LANT DE ABSTRACTIZARE  (abstract -> abstract -> concret)
# -------------------------------------------------------------
# O clasa abstracta poate avea o subclasa care adauga ALTE metode
# abstracte. Ramane abstracta pana cand cineva implementeaza tot lantul.

class Storage(ABC):

    @abstractmethod
    def citeste(self):
        pass

    @abstractmethod
    def scrie(self):
        pass

class StorageCuStorage(Storage):

    @abstractmethod
    def sterge(self):
        pass


class StorageMemory(StorageCuStorage):
    def citeste(self):
        return "citeste din memorie"

    def scrie(self):
        return "scrie in memorie"

    def sterge(self):
        return "sterge din memorie"


obj = StorageMemory()
print(obj.citeste())

# 10. ABC vs DUCK TYPING  -  cand alegi fiecare
# -------------------------------------------------------------
# DUCK TYPING (sesiunea 19):
#   - simplu, fara import-uri; potrivit pentru scripturi mici / prototip
#   - contractul e implicit; daca uiti o metoda -> eroare TARZIU, la apel
#
# ABC:
#   - contract EXPLICIT, vizibil in cod; eroare DEVREME, la creare
#   - potrivit pentru echipe, biblioteci, framework-uri, sisteme de
#     plugin-uri - oriunde tu ceri altora sa "extinda" ceva
#
# Regula: script mic -> duck typing e destul. Design serios cu multe
# implementari -> ABC iti da un contract sigur.


# =============================================================
# RECAP  -  CEI 4 PILONI OOP (S17-S20)
# =============================================================
# 1) INCAPSULARE   - date + comportament impreuna; ascunzi detaliile,
#                    controlezi accesul (_protected, __private, @property).
# 2) MOSTENIRE     - "este-un"; copilul primeste de la parinte; super().
# 3) POLIMORFISM   - aceeasi interfata, comportamente diferite
#                    (mostenire / duck typing / dunder methods).
# 4) ABSTRACTIZARE - contract EXPLICIT cu ABC + @abstractmethod;
#                    separa CE trebuie facut de CUM.
#
# Greseli frecvente la abstractizare:
#   - sa uiti @abstractmethod -> metoda devine normala si nu mai obliga
#     nimic (subclasa o poate ignora fara eroare).
#   - sa crezi ca poti instantia o clasa abstracta (nu poti).
#   - sa abuzezi de ABC in scripturi mici, unde duck typing ar fi ajuns.
#   - sa pui in ABC doar metode abstracte cand aveai si logica comuna
#     de reutilizat (pune-o ca metoda concreta in ABC).
#
# =============================================================
# CONCLUZIE (sablon de retinut)
# =============================================================
# from abc import ABC, abstractmethod
#
# class Baza(ABC):
#     @abstractmethod
#     def face(self): ...             # CE trebuie facut (obligatoriu)
#
#     def orchestreaza(self):         # cod concret, reutilizabil
#         return self.face()
#
# class Concret(Baza):
#     def face(self):                 # CUM: decide subclasa
#         return "implementat"
#
# - clasa abstracta NU se poate instantia
# - subclasa care nu implementeaza tot ramane si ea abstracta
# - @abstractmethod + @property = property abstracta
# - ABC = contracte respectate; util in biblioteci si framework-uri
#
# Cu cei 4 piloni acoperiti, ai baza completa de OOP in Python.
# =============================================================