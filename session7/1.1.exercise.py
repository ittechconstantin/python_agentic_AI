# EXERCITII LAMBDA / MAP / FILTER / ZIP
# =============================================================
# Toate exercitiile sunt rezolvate FARA if / for / while.
# Folosim: lambda, map, filter, zip, sorted, max, min, sum, list, dict.
#
# De facut:
# - Sesiunea 3 -> fisierul 3.2 -> exercitiile 13, 14
# - Sesiunea 4 -> fisierul 4.2 -> exercitiile 8, 9, 11, 12, 13
# - Sesiunea 5 -> fisierul 5.2 -> exercitiile 3, 8, 10
# =============================================================

# 1. Lambda - dublul unui numar
# -----------------------------
# Defineste o lambda numita `dublu` care primeste x si returneaza 2*x.
# Apeleaz-o pentru 7 si pentru 12 si afiseaza rezultatele.

# Solutie:

print("\n--- Exercitiul 1 ---")
dublu = lambda x : x *2
print(dublu(5))

# 2. Lambda - patratul unui numar
# -------------------------------
# Defineste o lambda  `patrat`  care intoarce x*x.
# Afiseaza patratul lui 9.

# Solutie:

print("\n--- Exercitiul 2 ---")
patrat = lambda x : x*x
print(patrat(9))

# 3. Lambda - suma a doua numere
# ------------------------------
# Defineste o lambda  `adun`  care primeste a si b si intoarce a+b.
# Afiseaza adun(15, 27).

# Solutie:

print("\n--- Exercitiul 3 ---")
adun = lambda a, b : a + b
print(adun(15, 27))

# 4. Lambda - mesaj de salut
# --------------------------
# Defineste o lambda  `salut`  care primeste un nume si intoarce
# string-ul "Salut, <nume>!". Apeleaz-o cu "Ana".

# Solutie:

print("\n--- Exercitiul 4 ---")
salut = lambda nume: "Salut, " + nume
print(salut("Ana"))

# 5. Map - dublam o lista
# -----------------------
# Avem  numere = [1, 2, 3, 4, 5].
# Construieste cu map + lambda o lista cu fiecare numar dublat.

# Solutie:

print("\n--- Exercitiul 5 ---")
numere = [1, 2, 3, 4, 5]
lista_noua = list(map(lambda x: x * 2, numere))
print(lista_noua)

# 6. Map - patrate
# ----------------
# Avem  numere = [1, 2, 3, 4, 5, 6].
# Construieste lista patratelor lor.

# Solutie:

print("\n--- Exercitiul 6 ---")
numere = [1, 2, 3, 4, 5, 6]
patratele = list(map(lambda x: x ** 2, numere))
print(patratele)

# 7. Map - preturi cu TVA (21%)
# -----------------------------
# Avem  preturi = [100, 200, 350, 1000].
# Construieste o lista cu preturile + 21% TVA (rotunjite la 2 zecimale).

# Solutie:

print("\n--- Exercitiul 7 ---")
preturi = [100, 200, 350, 1000]
preturi_cu_TVA = list(map(lambda x:x * 1.21, preturi))
print(preturi_cu_TVA)

# 8. Map - nume la majuscule
# --------------------------
# Avem  nume = ["ana", "vlad", "maria", "george"].
# Construieste o lista cu toate numele scrise cu majuscule.

# Solutie:

print("\n--- Exercitiul 8 ---")
nume = ["ana", "vlad", "maria", "george"]
lista_majuscule = list(map(lambda x:x.upper(), nume))
print(lista_majuscule)

# 9. Map - string-uri la int
# --------------------------
# Avem  texte = ["7", "42", "100", "3"].
# Construieste o lista cu valorile lor intregi.
# Sugestie: nu e nevoie de lambda - poti folosi direct int.

# Solutie:

print("\n--- Exercitiul 9 ---")
texte = ["7", "42", "100", "3"]
valori_intregi = list(map(lambda x: int(x), texte))
print(valori_intregi)

# 10. Map - lungimea fiecarui cuvant
# ----------------------------------
# Avem  cuvinte = ["mar", "banana", "ou", "ananas"].
# Construieste o lista cu lungimea fiecarui cuvant.

# Solutie:

print("\n--- Exercitiul 10 ---")
cuvinte = ["mar", "banana", "ou", "ananas"]
lista_lungime = list(map(lambda x:len(x), cuvinte))
print(lista_lungime)

# 11. Filter - numere pare
# ------------------------
# Avem  numere = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10].
# Construieste o lista doar cu numerele pare.

# Solutie:

print("\n--- Exercitiul 11 ---")
numere = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista_numere_noi = list(filter(lambda x:x%2==0, numere))
print(lista_numere_noi)

# 12. Filter - preturi peste un prag
# ----------------------------------
# Avem  preturi = [50, 120, 79, 200, 30, 500, 99].
# Construieste o lista doar cu preturile peste 100.

# Solutie:

print("\n--- Exercitiul 12 ---")
preturi = [50, 120, 79, 200, 30, 500, 99]
lista_preturi_noi = list(filter(lambda x:x > 100, preturi))
print(lista_preturi_noi)

# 13. Filter - cuvinte lungi
# --------------------------
# Avem  cuvinte = ["Ana", "Vlad", "Ox", "Maria", "Bo", "Cristina"].
# Construieste o lista doar cu cuvintele de lungime cel putin 4.

# Solutie:

print("\n--- Exercitiul 13 ---")
cuvinte = ["Ana", "Vlad", "Ox", "Maria", "Bo", "Cristina"]
lista_cea_noua = list(filter(lambda x: len(x)>=4, cuvinte))
print(lista_cea_noua)

# 14. Filter - utilizatori activi (lista de dict-uri)
# ---------------------------------------------------
# Avem  useri = [
#       {"nume": "Ana",   "activ": True},
#       {"nume": "Vlad",  "activ": False},
#       {"nume": "Maria", "activ": True},
#       {"nume": "Paul",  "activ": False},
#   ]
# Construieste o lista doar cu utilizatorii activi.

# Solutie:

print("\n--- Exercitiul 14 ---")
useri = [
      {"nume": "Ana",   "activ": True},
      {"nume": "Vlad",  "activ": False},
      {"nume": "Maria", "activ": True},
      {"nume": "Paul",  "activ": False},
  ]
utilizatori_activi = list(filter(lambda x: x["activ"], useri))
print(utilizatori_activi)

# 15. Filter - emailuri valide (contin @)
# ---------------------------------------
# Avem  inputuri = ["ana@x.com", "vlad", "maria@y.org", "x@", "george@z.net"].
# Construieste o lista doar cu textele care contin "@".

# Solutie:

print("\n--- Exercitiul 15 ---")
inputuri = ["ana@x.com", "vlad", "maria@y.org", "x@", "george@z.net"]
lista_inputuri = list(filter(lambda x:"@" in x, inputuri))
print(lista_inputuri)

# 16. Zip - nume si varste -> lista de tupluri
# --------------------------------------------
# Avem:
#   nume   = ["Ana", "Vlad", "Maria"]
#   varste = [30, 28, 35]
# Construieste o lista de tupluri (nume, varsta).

# Solutie:

print("\n--- Exercitiul 16 ---")
nume   = ["Ana", "Vlad", "Maria"]
varste = [30, 28, 35]
lista_tupluri = list(zip(nume, varste))
print(lista_tupluri)

# 17. Zip - construim un dict din doua liste
# ------------------------------------------
# Folosind aceleasi liste de mai sus, construieste un dict
# {nume: varsta} si afiseaza varsta Mariei.

# Solutie:

print("\n--- Exercitiul 17 ---")
dict_tupluri = dict(zip(nume, varste))
print(dict_tupluri)
print(dict_tupluri["Maria"])