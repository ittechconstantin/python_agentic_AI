# PROGRAMARE PROCEDURALA  vs  PROGRAMARE ORIENTATA PE OBIECTE (OOP)
# =============================================================
# Ai parcurs acum intregul arc OOP: clase (17), mostenire (18),
# polimorfism (19), abstractizare (20) si SOLID (21). Inainte sa
# mergi mai departe, hai sa te intorci la intrebarea de la inceput:
# cu ce ai castigat, mai exact, fata de stilul PROCEDURAL pe care il
# stiai deja din sesiunile 1-16 (date pe o parte, functii pe alta
# parte, care primesc datele ca argumente si intorc un rezultat)?
#
# Fisierul asta rezolva ACEEASI problema in DOUA stiluri, ca sa vezi
# diferenta cu ochii tai, nu doar in teorie.
#
# Nu e "OOP e mai bun" - e "iata ce castigi si ce pierzi cu fiecare".
#
# De ce ai nevoie ca sa intelegi acest fisier (recap):
#   - functii, dicturi, liste, bucle for (sesiunile 3, 4, 8, 11)
#   - clase, self, __init__ (sesiunea 17)
# =============================================================


# #############################################################
# PARTEA 1  -  STIL PROCEDURAL: date (dict) + functii separate
# #############################################################
# Un cont bancar e un dict cu doua chei. Fiecare "actiune" (depunere,
# retragere, afisare) e o FUNCTIE separata, care primeste dict-ul ca
# argument si il modifica.

def creeaza_cont(titular, sold_initial):
    return {"titular": titular, "sold": sold_initial}


def depune(cont, suma):
    cont["sold"] += suma


def retrage(cont, suma):
    if suma > cont["sold"]:
        print(f"  refuzat: {cont['titular']} nu are {suma} lei disponibili")
        return
    cont["sold"] -= suma


def afiseaza_cont(cont):
    print(f"  {cont['titular']}: {cont['sold']} lei")


print("1) Stil PROCEDURAL")
cont_ana = creeaza_cont("Ana", 1000)
cont_ion = creeaza_cont("Ion", 500)

depune(cont_ana, 200)
retrage(cont_ion, 100)
afiseaza_cont(cont_ana)   #   Ana: 1200 lei
afiseaza_cont(cont_ion)   #   Ion: 400 lei


# PROBLEMA cu stilul asta, pe masura ce codul creste:
# -------------------------------------------------------------
# 1. NIMIC nu leaga datele de functiile care le folosesc - poti apela
#    din greseala depune(cont_ion, ...) cu datele lui Ana, sau poti
#    modifica soldul DIRECT, ocolind orice validare:
cont_ion["sold"] = -9999   # nimeni nu opreste asta - "retrage" e ocolit
print(f"  (bug demonstrat) sold Ion dupa modificare directa: {cont_ion['sold']}")
cont_ion["sold"] = 400     # il reparam manual, ca sa continuam exemplul

# 2. Daca adaugi o functie NOUA (ex: transfera(cont_sursa, cont_dest,
#    suma)), trebuie sa-ti amintesti SINGUR sa refolosesti validarea
#    din retrage() - nimic nu te obliga. Usor sa uiti si sa introduci
#    un bug (transfer care lasa soldul negativ).
print()


# #############################################################
# PARTEA 2  -  ACELASI LUCRU, IN STIL OOP
# #############################################################
# O CLASA grupeaza datele (titular, sold) SI comportamentul (depune,
# retrage, afiseaza) intr-un singur loc. Detaliile lui `class`/`self`/
# `__init__` le inveti in 17.oop.py - aici ne uitam doar la REZULTAT,
# ca sa il compari cu Partea 1.

class ContBancar:
    def __init__(self, titular, sold_initial):
        self.titular = titular
        self.sold = sold_initial

    def depune(self, suma):
        self.sold += suma

    def retrage(self, suma):
        if suma > self.sold:
            print(f"  refuzat: {self.titular} nu are {suma} lei disponibili")
            return
        self.sold -= suma

    def afiseaza(self):
        print(f"  {self.titular}: {self.sold} lei")


print("2) Stil OOP")
cont_ana_oop = ContBancar("Ana", 1000)
cont_ion_oop = ContBancar("Ion", 500)

cont_ana_oop.depune(200)
cont_ion_oop.retrage(100)
cont_ana_oop.afiseaza()   #   Ana: 1200 lei
cont_ion_oop.afiseaza()   #   Ion: 400 lei
print()


# #############################################################
# PARTEA 3  -  COMPARATIE DIRECTA
# #############################################################
#                     PROCEDURAL                  OOP
#  -----------------  ------------------------    ------------------------
#  date + comportament  separate (dict + functii)  impreuna (in clasa)
#  apelare               depune(cont, 200)          cont.depune(200)
#  cine poate modifica   oricine, direct             prin metode (poti
#  datele?                (cont["sold"] = ...)       adauga protectie -
#                                                     vezi INCAPSULARE
#                                                     in 17.oop.py)
#  cont nou               creeaza_cont(...)           ContBancar(...)
#  10 conturi diferite    10 dicturi + ACELEASI       10 obiecte, aceleasi
#  (economii, curent...)  functii cu if-uri pt fiecare metode, comportament
#                         caz special                diferit prin MOSTENIRE
#                                                     (sesiunea 18)
#
# Observatie cheie: in Partea 1, `cont_ana` si `cont_ion` sunt DOAR
# date - "stiu" ca sunt conturi doar pentru ca noi, programatorii, ne
# amintim sa le tratam asa. In Partea 2, `cont_ana_oop` e un OBIECT -
# STIE singur cum sa se depuna/retraga, indiferent cine il foloseste.


# #############################################################
# PARTEA 4  -  CAND ALEGI CE
# #############################################################
# FOLOSESTE STIL PROCEDURAL cand:
#   - transformi date dintr-o forma in alta (citesti un CSV, calculezi
#     ceva, scrii alt fisier) - un "pipeline" de functii e mai simplu
#     decat sa inventezi clase pentru fiecare pas.
#   - scriptul e mic si de unica folosinta.
#
# FOLOSESTE OOP cand:
#   - modelezi ceva cu STARE care se schimba in timp si IDENTITATE
#     proprie (un Cont, un User, o Comanda - "acest obiect anume").
#   - ai MULTE operatii legate de acelasi tip de date (un cont bancar
#     are depune/retrage/transfera/afiseaza_extras - toate "apartin"
#     conceptului de cont).
#   - ai nevoie sa PROTEJEZI datele (incapsulare) sau sa ai VARIANTE
#     ale aceluiasi lucru care se comporta diferit (mostenire,
#     polimorfism - sesiunile 18-19).
#
# In practica, un proiect real COMBINA ambele: clase pentru entitatile
# cu stare (Cont, User), functii simple pentru calcule/transformari
# fara stare (ex: formateaza_data(data)).


# =============================================================
# RECAP
# =============================================================
# - PROCEDURAL: date (dict/lista) + functii separate care le primesc
#   ca argument. Simplu pentru scripturi si transformari de date.
# - OOP: date + comportament grupate intr-o CLASA; fiecare OBIECT stie
#   singur cum sa se comporte. Util cand modelezi "lucruri" cu stare si
#   identitate proprie, si cand ai nevoie de protectie/variante.
# - Nu e o alegere "pe viata" - acelasi proiect foloseste des ambele
#   stiluri, in parti diferite.
# - Ai invatat stilul OOP in detaliu de-a lungul sesiunilor 17-21:
#   `self`/`__init__` (17), mostenirea (18), polimorfismul (19),
#   abstractizarea (20) si SOLID (21) - ghidurile care te ajuta sa
#   STRUCTUREZI bine clasele pe masura ce un proiect creste.
# =============================================================