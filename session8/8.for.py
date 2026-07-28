# INSTRUCTIUNEA  for  IN PYTHON
# =============================================================
# `for` ne permite sa REPETAM un bloc de cod pentru fiecare
# element dintr-o colectie. Pana acum, daca aveam o lista de
# 100 elemente, trebuia sa scriem manual 100 linii. Acum
# scriem o singura "regula" care se aplica la fiecare element.
#
# Cand folosim `for`?
#   - parcurgere de log-uri / fisiere / linii
#   - aplicam o validare pe fiecare email / IP
#   - calcule cumulative (totaluri, medii, contoare)
#   - construim raporturi din date
#   - iteram cheie cu cheie intr-un dict
#
# `for` se foloseste pe ITERABILE: list, tuple, set, dict, str,
# range, etc. - tot ce putem "parcurge element cu element".
# =============================================================


# 1. SINTAXA DE BAZA
# -------------------------------------------------------------
# Forma:
#   for <variabila> in <iterabil>:
#       <bloc - se executa pentru fiecare element>
#
# La fiecare iteratie, <variabila> primeste valoarea
# urmatoare din iterabil.

fructe = ['mar', 'para', 'banana']
for fruct in fructe:
    print(fruct.upper())
print('AI TERMINAT!')

# Numele variabilei e la alegerea ta. Daca ai o lista de useri,
# variabila se cheama natural "user", "item", "u" etc.


# 2. for PE STRING - itereaza CARACTER cu CARACTER
# -------------------------------------------------------------
limbaj  = 'python'
nr_vocale = 0
for caracter in limbaj:
    if caracter in ('a','e','i','o','u','A','E','I','O','U'):
        nr_vocale += 1

print(f"Textul {limbaj} are {nr_vocale} vocale.")


# 3. for PE TUPLE
# -------------------------------------------------------------
porturi = (80, 22, 8000, 8001)
for port in porturi:
    print(f"Portul {port} este deschis.")


# 4. for PE SET (fara ordine garantata!)
# -------------------------------------------------------------
ip_blocate = {'192.168.1.1', '192.168.1.2', '192.168.1.3'}
for ip in ip_blocate:
    print(f"IP-ul {ip} este blocat.")


# 5. for PE DICT - implicit itereaza CHEILE
# -------------------------------------------------------------
config = {
    'host': 'localhost',
    'port': 8080,
    'debug': False,
    'timeout': 30
}
# Iterare pe chei:
for element in config:
    print(element)             # afiseze DOAR CHEILE

for element in config.keys():
    print(element)


# Iterare pe valori:
for element in config:
    print(config[element])    # afiseaza DOAR VALORILE

for element in config.values():
    print(element)

# Iterare pe perechi (cheie, valoare) - cel mai folosit:

for cheie, valoare in config.items():
    print(f"{cheie} = {valoare}")


# 6. range()  -  generator de numere
# -------------------------------------------------------------
# range NU este o lista, ci un "iterabil leneses". Daca vrem
# sa il vedem ca lista, il convertim cu list().
#
# Forme:
#   range(stop)              ->  0, 1, ..., stop-1
#   range(start, stop)        ->  start, start+1, ..., stop-1
#   range(start, stop, step)  ->  cu pas

# range cu un argument:
for i in range(5):
    print(i)
# range cu start si stop:
for i in range(1, 5):
    print(i)

# range cu pas:
for i in range(0, 10, 2):
    print(i)

# Pas negativ - numara descrescator:
for i in range(10, 0 , -1):
    print(i)


# Trimit email la primii 10 de useri
for i in range(10):
    print(f"Mail-ul a fost trimit pentru user {i}")


lista_useri = ['ana', 'maria', 'george', 'horia', 'clara']

for user in range(len(lista_useri)):
    print(f"Mail-ul a fost trimit pentru user {lista_useri[user]}")


# 7. enumerate()  -  itereaza si stii indexul
# -------------------------------------------------------------
# Cand avem nevoie SI de pozitia elementului, NU folosim range(len(...)).
# Folosim enumerate() - returneaza perechi (index, valoare).

useri = ["ana", "horia", "george"]

# Stil clasic, dar mai putin pythonic
for i in range(len(useri)):
    print(f"Userul {i} este {useri[i]}")

# Stil pythonic - cu enumerate:

for index, user in enumerate(useri):
    print(f"Userul {index} este {user}")


# enumerate cu start (de la 1, ca o lista numerotata):

for index, user in enumerate(useri, start=1):
    print(f"Userul {index} este {user}")


useri = {
    'ana': 25,
    'george': 30,
    'clara': 28,
    'maria': 22,
}
for index, user in enumerate(useri.items()):
    print(f"Userul {index} are {user[1]} ani.")


# 8. zip()  -  itereaza prin DOUA (sau mai multe) liste in paralel
# -------------------------------------------------------------
# zip "imperecheaza" elementele de pe acelasi index.
# Se opreste la cea mai SCURTA lista.

produse = ['margarine', 'farina', 'cereale', 'banane']
cantitati = [2, 1, 3, 5]

print(list(zip(produse, cantitati)))
for produs, cantitate in zip(produse, cantitati):
    print(f"Am {cantitate} produse  la pretul {produs}.")


# Cu 3 liste:
nume = ['ana', 'maria', 'george']
prenume = ['popescu', 'marius', 'constantin']
roluri = ['admin', 'user', 'user']

print(list(zip(nume, prenume, roluri)))

for n, p, r, in zip(nume, prenume, roluri):
    print(f"Userul {n} {p} are rolul {r}.")



# 9. break  -  iesim din bucla mai devreme
# -------------------------------------------------------------
# Folosit cand am gasit ce cautam si nu mai are rost sa continuam.

emailuri = ['a@gmail.com', 'b@gmail.com','spam@gmail.com', 'c@gmail.com']

for email in emailuri:
    print(email)
    if 'spam' in email:
        print("Am detectat o adresa spam")
        break       # iesim din program. nu mai verificam restul de elemente din lista



# 10. continue  -  sarim peste iteratia curenta
# -------------------------------------------------------------
# Sare la urmatorul element, fara a executa restul blocului.

numere = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for numar in numere:
    if numar % 2 == 0:
        continue
    else:
        print(numar)


# 11. for / else  -  ramura "else" pe bucla
# -------------------------------------------------------------
# Blocul `else` ruleaza DACA bucla s-a terminat NORMAL
# (fara break). Util pentru "am cautat tot, nu am gasit".

emailuri = ['a@gmail.com', 'b@gmail.com', 'c@gmail.com']
for email in emailuri:
    print(email)
else:
    print("Am cautat prin toata lista")



# 12. NESTED for  -  bucle imbricate (matrice / grid)
# -------------------------------------------------------------
# Pentru fiecare iteratie a buclei externe, bucla interna ruleaza
# COMPLET. Folosit pentru matrice, combinatii, tabele.

matrice = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

for rand in matrice:
    for valoare in rand:
        print(valoare)

# 13. LIST COMPREHENSION  -  pe scurt
# -------------------------------------------------------------
# Pattern-urile de "filter" si "transform" sunt asa de des intalnite,
# incat Python ofera o sintaxa scurta:
#
#   [<expresie>  for <var> in <iterabil>]
#   [<expresie>  for <var> in <iterabil>  if <conditie>]

patrate = [i** 2 for i in range(1,6)]
print(patrate)

emailuri = ['a@gmail.com', 'b@gmail.com', 'c@yahoo.com']

# varianta 1
emailuri_gmail = [email for email in emailuri if '@gmail.com' in email]
print(emailuri_gmail)


# varianta 2
emailuri_gmail = []
for email in emailuri:
    if '@gmail.com' in email:
        emailuri_gmail.append(email)

print(emailuri_gmail)

# Echivalente:
# - list(map(lambda n: n**2, range(1, 6)))   ==   [n**2 for n in range(1, 6)]


# =============================================================
# CONCLUZIE
# =============================================================
# `for` ne lasa sa parcurgem ELEMENT cu ELEMENT orice colectie:
#
#     for x in iterabil:
#         ...
#
# - Pe dict, foloseste  .items()  ca sa ai (cheie, valoare).
# - Foloseste  range()  cand vrei numere; foloseste  enumerate()
#   cand vrei si indexul; foloseste  zip()  pentru iteratie paralela.
# - Foloseste  break  ca sa iesi devreme,  continue  ca sa sari peste.