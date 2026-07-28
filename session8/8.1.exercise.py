# EXERCITII  for
# =============================================================
# Foloseste DOAR ce am invatat pana acum: variabile, tipuri,
# print(), operatori, string-uri, liste, dictionare, tupluri,
# set-uri, if/elif/else, si tot ce e in 8.for.py.
# (NU folosim while - urmeaza in sesiunea urmatoare.)
# =============================================================


# 1. Afiseaza fiecare element dintr-o lista
# -----------------------------------------
# Avem  fructe = ["mar", "para", "banana", "capsuna"].
# Afiseaza fiecare fruct pe cate o linie.

# Solutie:

print("\n--- Exercitiul 1 ---")
fructe = ["mar", "para", "banana", "capsuna"]
for fruct in fructe:
    print(fruct)

# 2. Suma unei liste cu for
# -------------------------
# Avem  numere = [3, 7, 1, 8, 2, 5].
# Foloseste un acumulator pentru a calcula suma.
# (Stim ca exista sum(), aici exersam pattern-ul.)

# Solutie:

print("\n--- Exercitiul 2 ---")
numere = [3, 7, 1, 8, 2, 5]
suma = 0
for numar in numere:
    suma += numar
print(suma)

# 3. range() de la 1 la 10
# ------------------------
# Afiseaza numerele de la 1 la 10 (inclusiv 10).

# Solutie:

print("\n--- Exercitiul 3 ---")
for i in range(1,11):
    print(i)

# 4. Numere pare cu range si pas
# ------------------------------
# Afiseaza toate numerele pare de la 0 la 20 inclusiv,
# folosind range cu pas 2.

# Solutie:

print("\n--- Exercitiul 4 ---")
for n in range(0, 21, 2):
    print(n)

# 5. Numara descrescator
# ----------------------
# Afiseaza numerele de la 10 la 1 (in ordine descrescatoare).

# Solutie:

print("\n--- Exercitiul 5 ---")
for a in range(10, 0, -1):
    print(a)

# 6. Itereaza pe un string
# ------------------------
# Avem  text = "Python".
# Afiseaza fiecare litera pe cate o linie.

# Solutie:

print("\n--- Exercitiul 6 ---")
text = "Python"
for litera in text:
    print(litera)

# 7. Itereaza pe un dict
# ----------------------
# Avem  config = {"host": "localhost", "port": 8080, "debug": True}.
# Afiseaza fiecare pereche cheie:valoare folosind .items() in formatul:
#   "host = localhost"

# Solutie:

print("\n--- Exercitiul 7 ---")
config = {"host": "localhost", "port": 8080, "debug": True}
for cheie, valoare in config.items():
    print(f"{cheie} = {valoare}")

# 8. enumerate - lista numerotata
# -------------------------------
# Avem  cumparaturi = ["paine", "lapte", "branza", "iaurt"].
# Afiseaza ca o lista numerotata, incepand de la 1:
#   "1. paine"
#   "2. lapte"
#   ...

# Solutie:

print("\n--- Exercitiul 8 ---")
cumparaturi = ["paine", "lapte", "branza", "iaurt"]
for index, cumparat in enumerate(cumparaturi, start=1):
    print(f"{index}. {cumparat}")

# 9. zip - parcurgere paralela
# ----------------------------
# Avem:
#   produse = ["laptop", "mouse", "tastatura"]
#   preturi = [4500, 79, 199]
# Afiseaza:  "laptop: 4500 lei",  "mouse: 79 lei",  ...

# Solutie:

print("\n--- Exercitiul 9 ---")
produse = ["laptop", "mouse", "tastatura"]
preturi = [4500, 79, 199]
for produse, preturi in zip(produse, preturi):
    print(f"{produse}: {preturi} lei")

# 10. Numarare conditionata
# -------------------------
# Avem  note = [9, 4, 8, 10, 5, 6, 3, 9, 7].
# Numara cati studenti au promovat (nota >= 5) si afiseaza:
#   "Promovati: X"
#   "Picati:    Y"

# Solutie:

print("\n--- Exercitiul 10 ---")
note = [9, 4, 8, 10, 5, 6, 3, 9, 7]
promovati = 0
picati = 0
for nota in note:
    if nota >=5:
        promovati += 1
    else:
        picati += 1
print(f"Promovati: {promovati}")
print(f"Picati: {picati}")

# 11. Maxim manual cu for
# -----------------------
# Avem  preturi = [120, 35, 899, 49, 1200, 17].
# Calculeaza pretul maxim FARA sa folosesti max().
# Pleaca de la prima valoare ca "ipoteza" si compara restul.

# Solutie:

print("\n--- Exercitiul 11 ---")
preturi = [120, 35, 899, 49, 1200, 17]
maxim = preturi[0]
for pret in preturi:
    if pret > maxim:
        maxim = pret
        print(f"Maximum: {maxim}")
    else:
        print(f"Maximum: {pret}")
        break


# ipoteza, *restul = preturi
# if ipoteza >= restul[0] and ipoteza > restul[1] and ipoteza > restul[2] and ipoteza > restul[3] and ipoteza > restul[4]:
#     print(ipoteza)
# elif ipoteza <= restul[0] and restul[0] > restul[1] and restul[0] > restul[2] and restul[0] > restul[3] and restul[0] > restul[4]:
#     print(restul[0])
# elif ipoteza >= restul[0] and restul[0] < restul[1] and restul[1]>restul[2] and restul[2]>restul[3] and restul[3]>restul[4]:
#     print(restul[1])
# elif ipoteza >= restul[0] and restul[0] < restul[1] and restul[1]<restul[2] and restul[2]>restul[3] and restul[3]>restul[4]:
#     print(restul[2])
# elif ipoteza >= restul[0] and restul[0] < restul[1] and restul[1]>restul[2] and restul[2]<restul[3] and restul[3]>restul[4]:
#     print(restul[3])
# else:
#     print(restul[4])
#Aici am codat mai mult, dar nu stiam altfel

# 12. break la prima aparitie
# ---------------------------
# Avem  emailuri = ["a@x.com", "b@x.com", "spam@x.com", "c@x.com", "d@x.com"].
# Iesi din bucla la primul email care contine "spam" si afiseaza-l.

# Solutie:

print("\n--- Exercitiul 12 ---")
emailuri = ["a@x.com", "b@x.com", "spam@x.com", "c@x.com", "d@x.com"]
for email in emailuri:
    if "spam" in email:
        print(email)
        break


# 13. continue - sari peste valori invalide
# -----------------------------------------
# Avem  valori = [10, -3, 7, 0, -5, 8, 2].
# Calculeaza suma DOAR a valorilor pozitive (> 0). Foloseste continue
# pentru valorile <= 0.

# Solutie:

print("\n--- Exercitiul 13 ---")
valori = [10, -3, 7, 0, -5, 8, 2]
suma = 0
for valoare in valori:
    if valoare > 0:
        suma += valoare
    elif valoare <= 0:
        suma -= 0
        continue

print(suma)

# 14. Construire lista cu .append()
# ---------------------------------
# Avem  numere = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10].
# Construieste o lista NOUA `patrate` cu patratul fiecarui numar.

# Solutie:

print("\n--- Exercitiul 14 ---")
numere = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista_noua = []
for i in numere:
    formula = i**2
    lista_noua.append(formula)
print(lista_noua)

# 15. List comprehension simpla
# -----------------------------
# Rezolva exercitiul 14 pe O SINGURA LINIE folosind list comprehension.

# Solutie:

print("\n--- Exercitiul 15 ---")
print([i**2 for i in numere])


# 16. List comprehension cu filtru
# --------------------------------
# Avem  numere = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10].
# Folosind list comprehension construieste lista patratelor
# DOAR pentru numerele pare.

# Solutie:

print("\n--- Exercitiul 16 ---")
numere = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista_patrate = [i**2 for i in numere if i%2==0]
print(lista_patrate)

# 17. Iterare pe set
# ------------------
# Avem  servicii = {"nginx", "postgres", "redis", "rabbitmq"}.
# Afiseaza fiecare serviciu cu prefixul "[OK] ":
#   "[OK] nginx"
#   "[OK] postgres"
#   ...

# Solutie:

print("\n--- Exercitiul 17 ---")
servicii = {"nginx", "postgres", "redis", "rabbitmq"}
status = "[OK]"
for serviciu in servicii:
    print(f"{status} {serviciu}")

# 18. Inversare lista cu for
# --------------------------
# Avem  lista = [1, 2, 3, 4, 5].
# Construieste o lista NOUA cu elementele in ordine inversa,
# FARA sa folosesti .reverse() sau slicing [::-1].
# Sugestie: foloseste range(len(lista)-1, -1, -1).

# Solutie:

print("\n--- Exercitiul 18 ---")
lista = [1, 2, 3, 4, 5]
inversa = []
for l in range(len(lista)-1, -1, -1):
                  inversa.append(lista[l])
                  break


# 19. Iterare pe matrice (nested for)
# -----------------------------------
# Avem  matrice = [[1, 2, 3], [4, 5, 6], [7, 8, 9]].
# Afiseaza toate valorile pe O SINGURA linie, despartite cu spatiu.
# (Sugestie: print(val, end=" ") in interior, print() la final.)

# Solutie:

print("\n--- Exercitiul 19 ---")
matrice = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]
for rand in matrice:
    for valoare in rand:
        print(valoare, end=" ")
print()

# 20. Tabela inmultirii (cu nested for)
# -------------------------------------
# Afiseaza tabela inmultirii pentru numarul 3 (3*1=3, 3*2=6, ..., 3*10=30).
# Foloseste range(1, 11) pentru valorile inmultite.

# Solutie:

print("\n--- Exercitiul 20 ---")
for i in range(1,11):
    print(f"{3}*{i}={3*i}")

