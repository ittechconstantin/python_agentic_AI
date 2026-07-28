# EXERCITII *args / **kwargs / SCOPE
# =============================================================
# =============================================================


# 1. Bon de cumparaturi cu oricate produse
# ----------------------------------------
# La casa de marcat nu stii dinainte cate produse cumpara clientul.
# Defineste  bon(*preturi)  care primeste ORICATE preturi si intoarce
# un dict cu:
#   "produse" (cate au fost), "total" (suma lor), "media" (pretul mediu)
# Daca nu se scaneaza nimic, toate sunt 0 (atentie sa nu imparti la 0).
# Testeaza cu 3 produse si cu zero produse.

# Solutie:

print("\n--- Exercitiul 1 ---")

def bon(*produse, **preturi):
    return print((f"{produse}, {sum(preturi)}, {sum(preturi) / len(produse)}"))

bon("paine", "lapte", "oua", 90, 87,55)
# 2. Profil de client cu campuri optionale
# ----------------------------------------
# La inregistrare un client da NUMELE (obligatoriu) si, optional, orice
# alte detalii (email, telefon, oras...).
# Defineste  creeaza_profil(nume, **detalii)  care intoarce un dict cu
# numele + toate detaliile extra primite.
# Testeaza cu un client care da doar numele si unul care da mai multe.

# Solutie:

print("\n--- Exercitiul 2 ---")
def creeaza_profil(nume, **detalii):
        return f"{nume}: {detalii}"
        email = detalii.get("email", "")
        telefon = detalii.get("telefon", 0)
        oras = detalii.get("oras", "")
        # if len(detalii) != 0:
        #     print(f"Clientul cu numele {nume} are emailul '{email}', numarul de telefon :{telefon} si e situat in  orasul {oras}")

print(creeaza_profil("Ionel"))
print(creeaza_profil("Claudiu", email = "claudiu@gmail.com", telefon = "0745678921", oras = "Bistrita"))

# 3. Tabela de scor - cine castiga?
# ----------------------------------
# La un joc, fiecare jucator are un scor. Defineste
#   castigator(**scoruri)
# care primeste perechi de forma  jucator=scor  si intoarce numele
# jucatorului cu scorul cel mai mare.
# Daca nu primeste niciun jucator, intoarce None.
# Sugestie:  max(scoruri, key=lambda nume: scoruri[nume]).

# Solutie:

print("\n--- Exercitiul 3 ---")
def castigator(**scoruri):
    if len(scoruri) > 0:
        return max(scoruri, key=lambda nume: scoruri[nume])
    else:
        return None
print(castigator(Ioana=56, Costel=43,Ionut=89, Doru=90))
print(castigator())

#Nu am inteles exact cum sa fac acest exercitiu, acesta e ceea ce am incercat

# 4. Setarile aplicatiei: valori implicite + ce schimba userul
# ------------------------------------------------------------
# O aplicatie are setari implicite, dar userul poate suprascrie unele.
# Defineste  setari(**modificari)  care porneste de la un dict de valori
# implicite si aplica peste el modificarile primite (restul raman default).
# Testeaza fara modificari si cu cateva modificari.

# Solutie:

print("\n--- Exercitiul 4 ---")
def setari(user,**modificari):

    setari_implicite = {
    'status': 'user',
    'port': 8080,
    'settings': 'standard',
    'os': 'Windows'
}

    status = modificari.get("status", "user")
    port = modificari.get("port", "8080")
    settings = modificari.get("settings", "standard")
    os= modificari.get("os", "Windows")
    print(f"{user} este {status} si are acces la portul {port} cu setarile {settings}, ruland sistemul {os}")

setari("John",status="admin",port=1273, settings='high', os='Linux')
setari("Vasile")

# 5. Total vanzari pe ziua curenta (variabila globala)
# ----------------------------------------------------
# Vrei sa tii minte cat ai vandut pana acum, intr-o variabila GLOBALA.
# Defineste:
#   total_vanzari = 0   (in afara functiei)
#   inregistreaza_vanzare(suma) -> adauga suma la total si intoarce noul total
# Pentru ca REASIGNEZI variabila globala (total = total + ...), ai nevoie
# de cuvantul `global` la inceputul functiei (altfel -> UnboundLocalError).

# Solutie:

print("\n--- Exercitiul 5 ---")
total_vanzari = 0
def inregistreaza_vanzare(suma):
    global total_vanzari
    total_vanzari += suma
    print(total_vanzari)
inregistreaza_vanzare(100)

# inregistreaza_vanzare(12, 50, 45)

# 6. Comanda la restaurant (normal + *args + **kwargs impreuna)
# -------------------------------------------------------------
# Defineste  comanda(masa, *feluri, **optiuni)  unde:
#   masa    -> numarul mesei (obligatoriu)
#   feluri  -> oricate preparate (pozitionale)
#   optiuni -> detalii care pot lipsi (livrare, observatii...)
# Functia printeaza un rezumat al comenzii.
# Atentie la ORDINEA in semnatura: parametri normali -> *args -> **kwargs.

# Solutie:

print("\n--- Exercitiul 6 ---")
def comanda(masa, *feluri, **optiuni):
    print(f"Comanda de la {masa}")
    for fel in feluri:
        print(f"  -{fel}")

    print("Optiuni")
    for cheie, valoare in optiuni.items():
        print(f"  -{cheie}: {valoare}")

comanda("Masa 8", "supa", "ciolan", livrare="Felul 1, apoi felul 2", observatii="Mancare perisabila")

# 7. Pipeline de curatare a unui text (slug pentru un titlu)
# ----------------------------------------------------------
# Vrei sa transformi un titlu intr-un "slug" pentru URL, trecandu-l prin
# mai multi pasi, in ordine.
# Defineste  proceseaza(text, *pasi)  care aplica pe rand fiecare functie
# din "pasi", fiecare primind rezultatul celei dinainte.
# Testeaza cu: elimina spatiile de la capete, litere mici, spatiile -> "-".

# Solutie:

print("\n--- Exercitiul 7 ---")

f'voleiplajapenisip.ro'
def proceseaza(text, *pasi):
    for pas in pasi:
        if pas ==  'strip':
            text = text.strip()
        elif pas == 'lower':
            text = text.lower()
        elif pas == 'split':
            text = text.split(' ')
            text = ''.join(text)
            text = text.split('-')
            text = ''.join(text)
    print(text)
proceseaza(f'Volei-plaja PE nisip.ro', 'strip', 'lower', 'split')

# 8. Uneste mai multe liste de invitati
# -------------------------------------
# Organizezi un eveniment si primesti mai multe liste de invitati de la
# persoane diferite. Defineste  invitati_unici(*liste)  care primeste
# ORICATE liste de nume si intoarce o singura lista, sortata si FARA
# dubluri (acelasi nume nu apare de doua ori).
# Sugestie: aduna totul intr-un set, apoi sorted(...).

# Solutie:

print("\n--- Exercitiul 8 ---")
def invitati_unici(*liste):
    lista_completa = set()
    for i in liste:
        lista_completa.update(i)
    lista_completa = list(lista_completa)
    lista_completa = sorted(lista_completa)
    print(lista_completa)

lista1 = ['Ion', 'Gheorghe', 'Maria', 'Ionel', 'Ion']
lista2 = ['Ionut', 'Ion', 'Gheorghe', 'Ioana', 'Ionel']
lista3 = ['Ionel', 'Maria', 'Marius', 'Marian', 'Marcel']

invitati_unici(lista1, lista2, lista3)

# 9. Validarea unui formular cu mai multe reguli
# ----------------------------------------------
# La un formular ai mai multe reguli de verificat pentru aceeasi valoare.
# Fiecare regula e o FUNCTIE care intoarce (True, "") daca trece, sau
# (False, "mesaj de eroare") daca pica.
# Defineste  verifica(valoare, *reguli)  care intoarce lista mesajelor de
# eroare (lista goala daca totul e ok).
# Apoi scrie 3 reguli pentru o parola: lungime, cifra, litera mare.

# Solutie:

print("\n--- Exercitiul 9 ---")
def verifica(valoare, *reguli):
    lista_mesaje = []
    for regula in reguli:
        if regula == 'lungime':
            tuplu = regula1(valoare)
            if tuplu[0] is False:
                lista_mesaje.append(tuplu[1])
        elif regula == 'cifra':
            tuplu = regula2(valoare)
            if tuplu[0] is False:
                lista_mesaje.append(tuplu[1])
        elif regula == 'litera_mare':
            tuplu = regula3(valoare)
            if tuplu[0] is False:
                lista_mesaje.append(tuplu[1])
    return lista_mesaje


def regula1(lungime):
    if len(lungime) > 12:
        return (True, "")
    else:
        return (False, "Lungime prea mica")

def regula2(cifra):
    cifra_gasita = False
    for i in cifra:
        if i >= '0' and i <= '9':
            cifra_gasita = True
            break
    if cifra_gasita is True:
        return (True, "")
    else:
        return (False, "Nu contine cifra")

def regula3(litera_mare):
    litera_gasita = False
    for i in litera_mare:
        if i >= 'A' and i <= 'Z':
            litera_gasita = True
            break
    if litera_gasita is True:
        return (True, "")
    else:
        return (False, "Nu contine litera mare")


# reguli = lungime, cifra, litera mare

parola1 = '1234'
parola2 = '12abc34ABC678'
print(verifica(parola1, 'lungime', 'cifra', 'litera_mare'))
print(verifica(parola2, 'lungime', 'cifra', 'litera_mare'))

# 10. Numara vizitatorii UNICI ai unui site
# -----------------------------------------
# Vrei sa stii cati vizitatori UNICI a avut site-ul (acelasi IP nu se
# numara de doua ori). Tii un set cu IP-urile deja vazute.
# Defineste:
#   viziteaza(ip)     -> True daca e prima oara cand vezi acest IP, altfel False
#   nr_vizitatori()   -> cati vizitatori unici sunt pana acum
# Pentru .add() pe set NU ai nevoie de "global" (modifici lista in-place).

# Solutie:

print("\n--- Exercitiul 10 ---")
def viziteaza(ip):
    vizitator_unic = True
    if ip in ip_uri:
        vizitator_unic = False
    ip_uri.add(ip)
    return vizitator_unic

def nr_vizitatori():
    return len(ip_uri)

ip_uri = {'192.168.1.1', '111.12.54.98', '192.168.1.2', '192.168.1.4', '192.169.1.5'}

print(f"Esti la prima vizita ? Daca {viziteaza('192.168.1.101')}, atunci inseamna ca acum avem {nr_vizitatori()} vizitatori unici!")
print(f"Esti la prima vizita ? Daca {viziteaza('192.168.1.102')}, atunci inseamna ca acum avem {nr_vizitatori()} vizitatori unici!")
print(f"Esti la prima vizita ? Daca {viziteaza('192.168.1.103')}, atunci inseamna ca acum avem {nr_vizitatori()} vizitatori unici!")