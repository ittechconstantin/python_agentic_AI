# EXERCITII FUNCTII
# =============================================================

# 1. Factura cu TVA
# -----------------
# Esti la casa unui magazin si trebuie sa generezi o factura.
# Defineste mai intai o functie ajutatoare:
#   pret_cu_tva(pret, cota=21)  -> pretul cu TVA adaugat
#     (ex: 100 lei cu TVA 21% -> 121 lei)
# Apoi functia principala:
#   genereaza_factura(produse, cota=21) -> dict
# unde "produse" este o LISTA de tupluri (nume, pret_bucata, cantitate).
# Pentru fiecare produs aduni in subtotal:  pret_bucata * cantitate.
# La final functia returneaza un dict cu cheile:
#   "subtotal" (suma fara TVA)
#   "tva"      (cat reprezinta TVA-ul)

#   "total"    (subtotal + TVA, folosind pret_cu_tva)
# Testeaza pe un cos cu cafea, lapte si paine.

# Solutie:

print("\n--- Exercitiul 1 ---")
def pret_cu_tva(pret, cota=21):
    return pret * (100 +cota)/100

def genereaza_factura(produse, cota=21):
    subtotal = 0
    for nume, pret_bucata, cantitate in produse:
        subtotal += pret_bucata * cantitate
    total = pret_cu_tva(subtotal, cota)
    return {
        'subtotal': subtotal,
        'tva': total - subtotal,
        'total': total
    }

# Testare
cos = [
    ("cafea", 10, 2),
    ("lapte", 20, 1),
    ("paine", 5, 3),
]
print(genereaza_factura(cos))


# 2. Nota de plata la restaurant (bacsis + impartire)
# ---------------------------------------------------
# Ati iesit in grup la restaurant. Defineste:
#   bacsis(suma, procent=10)        -> cat reprezinta bacsisul
#   total_de_plata(suma, procent=10)-> suma + bacsis
#   de_persoana(suma, nr_persoane, procent=10)
#       -> cat plateste fiecare (total de plata impartit egal)
# Functiile mai mari le folosesc pe cele mici.
# Testeaza pentru o nota de 240 lei, 4 persoane, bacsis 15%.

# Solutie:

print("\n--- Exercitiul 2 ---")
def bacsis(suma, procent=10):
    return suma * procent / 100

def total_de_plata(suma, procent=10):
    return suma + bacsis(suma, procent)

def de_persoana(suma, nr_persoane, procent=10):
    return total_de_plata(suma, procent) / nr_persoane

print(f"Total BACSIS: {bacsis(240)}")
print(f"Total de plata CU BACSIS: {total_de_plata(240)}")
print(f"De fiecare persoana: {de_persoana(240, 4)}")


# 3. Costul unei calatorii cu masina
# ----------------------------------
# Planifici un drum cu masina si vrei sa stii cat te costa combustibilul,
# impartit intre prieteni.
# Defineste functiile ajutatoare:
#   litri_necesari(distanta, consum)
#       -> cati litri arde masina  (consum = litri la 100 km)
#          formula: distanta / 100 * consum
#   cost_combustibil(litri, pret_litru)
#       -> litri * pret_litru
# Apoi functia principala:
#   cost_pe_persoana(distanta, consum, pret_litru, persoane)
#       -> costul total al drumului impartit la numarul de persoane
# Testeaza: 450 km, consum 7 l/100km, 7.5 lei/litru, 3 persoane.

# Solutie:

print("\n--- Exercitiul 3 ---")
def litri_necesari(distanta, consum):
    return distanta /100 * consum

def  cost_combustibil(litri, pret_litru):
    return litri * pret_litru
def cost_pe_persoana(distanta, consum, pret_litru, persoane):
    litri = litri_necesari(distanta, consum)
    cost = cost_combustibil(litri, pret_litru)
    return cost / persoane

print(cost_pe_persoana(450 , 7, 7.5 , 3))

# 4. Indicele de masa corporala (IMC)
# -----------------------------------
# IMC-ul iti spune daca ai o greutate normala fata de inaltime.
# Formula: IMC = greutate / inaltime ** 2
#   (greutate in kilograme, inaltime in metri)
# Defineste functiile ajutatoare:
#   imc(greutate, inaltime)  -> valoarea IMC
#   categorie(valoare):
#       - "subponderal"    daca IMC < 18.5
#       - "normal"         daca IMC < 25
#       - "supraponderal"  daca IMC < 30
#       - "obezitate"      in rest
# Apoi functia principala:
#   raport_imc(greutate, inaltime)
#       -> un string de forma:  "IMC: 22.86 -> normal"
# Testeaza pentru o persoana de 70 kg si 1.75 m.

# Solutie:

print("\n--- Exercitiul 4 ---")
def imc (greutate, inaltime):
    return greutate / inaltime ** 2

def categorie(valoare):
    if valoare < 18.5:
        return "subponderal"
    elif valoare < 25:
        return "normal"
    elif valoare < 30:
        return "supraponderal"
    else:
        return "obezitate"
def raport_imc(greutate, inaltime):
    indice_masa = imc(greutate, inaltime)
    categorie_imc = categorie(indice_masa)

    return f"IMC: {indice_masa:.2f} -> {categorie_imc}"

print(raport_imc(70, 1.75))

# 5. Bugetul lunar
# ----------------
# Vrei sa vezi cat reusesti sa economisesti intr-o luna.
# Cheltuielile sunt intr-un dict {categorie: suma}, ex:
#   {"chirie": 1500, "mancare": 900, "transport": 200}
# Defineste functiile ajutatoare:
#   total_cheltuieli(cheltuieli) -> suma tuturor cheltuielilor
#   economii(venit, cheltuieli)  -> venit - total cheltuieli
# Apoi functia principala:
#   raport_buget(venit, cheltuieli)
# care printeaza:
#   - totalul cheltuielilor
#   - cati bani raman (economiile)
#   - ce procent din venit ai economisit
# Testeaza pentru un venit de 4000 lei.

# Solutie:

print("\n--- Exercitiul 5 ---")
def total_cheltuieli(cheltuieli):
    return sum(cheltuieli.values())
def economii(venit, cheltuieli):
    return venit - total_cheltuieli(cheltuieli)

def raport_buget(venit, cheltuieli):
    total = total_cheltuieli(cheltuieli)
    ramas = economii(venit, cheltuieli)
    procent = ramas / venit * 100
    print(f"Cheltuieli total: {total}, am economisit: {ramas}, procent economisit din procent: {procent}")

cheltuieli = {"chirie": 1500, "mancare": 900, "transport": 200}
raport_buget(venit = 4000, cheltuieli = cheltuieli)

# 6. Generator de username (cu numar daca e ocupat)
# -------------------------------------------------
# La crearea unui cont generam un username din numele complet.
# Defineste:
#   genereaza_username(nume_complet, existente)
# care primeste un nume ("Ana Popescu") si un set de username-uri
# deja folosite. Returneaza un username de forma "ana.popescu".
# Daca este DEJA folosit, adauga un numar incremental pana gaseste
# unul liber: "ana.popescu1", "ana.popescu2"...
# Foloseste un while.

# Solutie:

print("\n--- Exercitiul 6 ---")
def genereaza_username(nume_complet, existente):
    user = nume_complet.lower().split()
    baza = f"{user[0]}.{user[1]}"
    if baza in existente:
        return baza
    else:
        i = 1
        while f"{baza}{i}" in existente:
            i += 1
        return f"{baza}{i}"

used_username = {"ana.popescu1", "ana.popescu2"}
print(genereaza_username("Ana Popescu", used_username))

# 7. Validarea unei comenzi online
# --------------------------------
# Un produs din cos arata asa:
#   {"nume": str, "pret": float, "cantitate": int}
# Defineste:
#   produs_valid(produs) -> bool
# Reguli:
#   - "nume" trebuie sa fie un string ne-vid
#   - "pret" >= 0
#   - "cantitate" >= 1
# Apoi:
#   produse_valide(cos) -> lista doar cu produsele care trec validarea
# Testeaza pe un cos care contine si produse gresite.

# Solutie:

print("\n--- Exercitiul 7 ---")
produs1 = {"nume": 'Lapte', "pret": 12.99, "cantitate": 2}
produs2 = {"nume": 'Paine', "pret": 5.99, "cantitate": 1}
produs3 = {"nume": 'Oua', "pret": 10.99, "cantitate": 10}
produs4 = {"nume": '', "pret": 0, "cantitate": 3}
produs5 = {"nume": 'lemn', "pret": 10.99, "cantitate": 0}


cos = (produs1, produs2, produs3, produs4, produs5)

def produs_valid(produs):
    if len(produs["nume"]) != 0 and produs["pret"] >= 0 and produs["cantitate"] >= 1:
        return True
    else:
        return False

def produse_valide(cos):
    produse_valide = []
    for produs in cos:
        if produs_valid(produs) is True:
            produse_valide.append(produs)
    return produse_valide


cos = produse_valide(cos)
print(cos)

# 8. Monitorizare servere (health check)
# --------------------------------------
# Defineste:
#   stare_server(server) -> str
# care primeste un dict {cpu, ram, disk, online} si returneaza:
#   - "DOWN"   daca serverul e offline
#   - "CRITIC" daca cpu, ram SAU disk >= 90
#   - "WARN"   daca cpu, ram SAU disk >= 70
#   - "OK"     in rest
# Apoi:
#   raport_servere(servere)
# care primeste un dict {nume_server: dict_resurse} si printeaza
# pentru fiecare:  "<nume>: <stare>"

# Solutie:

# def stare_server(server) -> str:
# dictul = {'cpu', 'ram', 'disk', 'online'}
#
# if 'online' in dictul is False:
#     return "DOWN"
# elif 'cpu' or 'ram' or 'disk' >= 90:
#     return "CRITIC"
# elif 'cpu' or 'ram' or 'disk' >= 70:
#     return "CRITIC"


# 9. Comanda online cu transport gratuit
# ---------------------------------------
# Multe magazine ofera transport gratuit daca depasesti un prag.
# Regula: daca valoarea produselor este >= 200 lei, transportul e 0 lei;
# altfel se adauga o taxa de 20 lei.
# Defineste functiile ajutatoare:
#   valoare_produse(cos)          -> suma preturilor din cos (lista de preturi)
#   cost_transport(total, prag=200, taxa=20)
#       -> 0 daca total >= prag, altfel taxa
# Apoi functia principala:
#   total_comanda(cos, prag=200, taxa=20)
#       -> valoarea produselor + transportul
# Bonus, tot o functie:
#   cat_mai_lipseste(cos, prag=200)
#       -> cati lei mai trebuie pana la transport gratuit (0 daca deja se aplica)
# Testeaza pe doua cosuri: unul sub prag si unul peste prag.

# Solutie:

# def valoare_produse(cos):
#     sum(total_comanda(cos))
#
# def cost_transport(total, prag=200, taxa=20)
#
# def total_comanda(cos, prag=200, taxa=20):
#     if prag < 200:
#         cos + taxa
#
# def cat_mai_lipseste(cos, prag=200):
#     if prag < 200:
#         prag - cos
#
# if valoare_produse >= 200 lei:
#     transport = 0
# else:
#     transport = 20

# 10. Card de fidelitate (puncte + nivel client)
# ----------------------------------------------
# La fiecare cumparatura clientul primeste puncte. Defineste:
#   puncte_castigate(suma)  -> 1 punct pentru fiecare 10 lei (rotunjit in jos)
#   nivel_client(puncte):
#       - "GOLD"   daca puncte >= 500
#       - "SILVER" daca puncte >= 200
#       - "BRONZE" in rest
# Apoi functia principala:
#   actualizeaza_card(card, suma) -> dict actualizat
# unde "card" este {"nume": str, "puncte": int}. Functia adauga punctele
# castigate la cumparatura curenta si recalculeaza nivelul, returnand
# un dict {"nume", "puncte", "nivel"}.
# Testeaza adaugand o cumparatura de 1500 lei la un card cu 380 puncte.

# Solutie:

# def puncte_castigate(suma) ->
#
# def nivel_client(puncte):
#     if puncte >= 500:
#         return "GOLD"
#     elif puncte >= 200:
#         return "SILVER"
#     else:
#         return "Bronze"
#
# def actualizeaza_card(card, suma):
#     card = {"nume": str, "puncte": int}