# EXERCITII LISTE
# =============================================================
# Foloseste DOAR ce am invatat pana acum: variabile, tipuri,
# print(), operatori, string-uri si tot ce e in 3.list.py.
# =============================================================


# 1. Crearea unei liste
# ---------------------
# Creeaza o lista numita `fructe` cu valorile:
# "mar", "para", "banana", "capsuna".
# Afiseaza lista intreaga.

# Solutie:

print("\n--- Exercitiul 1 ---")
fructe = ["mar", "para", "banana", "capsuna"]
print(fructe)


# 2. Accesarea elementelor
# ------------------------
# Folosind lista de mai sus, afiseaza:
#   - primul fruct
#   - al treilea fruct
#   - ultimul fruct (folosind index negativ)

# Solutie:

print("\n--- Exercitiul 2 ---")
print(fructe[0])
print(fructe[2])
print(fructe[-1])

# 3. Slicing
# ----------
# Avem  numere = [10, 20, 30, 40, 50, 60, 70, 80].
# Afiseaza:
#   - primele 3 elemente
#   - ultimele 3 elemente
#   - elementele de la indexul 2 pana la 5 (inclusiv 4, exclusiv 5)

# Solutie:

print("\n--- Exercitiul 3 ---")
numere = [10, 20, 30, 40, 50, 60, 70, 80]
print(numere[:3])
print(numere[-3:])
print(numere[2:5])

# 4. Modificarea unui element
# ---------------------------
# Avem  fructe = ["mar", "para", "banana"].
# Inlocuieste "para" cu "kiwi" si afiseaza lista actualizata.

# Solutie:

print("\n--- Exercitiul 4 ---")
fructe = ["mar", "para", "banana"]
fructe[1] = "kiwi"
print(fructe)

# 5. Adaugare la final - append()
# -------------------------------
# Avem  cumparaturi = ["paine", "lapte"].
# Adauga la final "branza" si "iaurt", apoi afiseaza lista.

# Solutie:

print("\n--- Exercitiul 5 ---")
cumparaturi = ["paine", "lapte"]
cumparaturi_doi = ["branza", "iaurt"]
lista_cumparaturi = cumparaturi + cumparaturi_doi
print(lista_cumparaturi)

# 6. Adaugare cu extend()
# -----------------------
# Avem  lista_a = ["Python", "Java"]   si   lista_b = ["GO", "Rust"].
# Adauga toate elementele din lista_b la finalul listei_a folosind .extend().
# Afiseaza rezultatul.

# Solutie:

print("\n--- Exercitiul 6 ---")
lista_a = ["Python", "Java"]
lista_b = ["GO", "Rust"]
lista_a.extend(lista_b)
print(lista_a)

# 7. Insert la o pozitie
# ----------------------
# Avem  numere = [1, 2, 4, 5].
# Insereaza valoarea 3 pe pozitia corecta (intre 2 si 4) folosind .insert().
# Afiseaza lista finala.

# Solutie:

print("\n--- Exercitiul 7 ---")
numere = [1, 2, 4, 5]
numere.insert(2, 3)
print(numere)

# 8. Stergere cu remove()
# -----------------------
# Avem  animale = ["caine", "pisica", "oaie", "vaca", "pisica"].
# Sterge prima aparitie a "pisica" si afiseaza lista.

# Solutie:

print("\n--- Exercitiul 8 ---")
animale = ["caine", "pisica", "oaie", "vaca", "pisica"]
animale.remove("pisica")
print(animale)

# 9. Stergere cu pop()
# --------------------
# Avem  numere = [10, 20, 30, 40, 50].
# Foloseste .pop() pentru a extrage ULTIMUL element.
# Afiseaza valoarea extrasa SI lista ramasa.

# Solutie:

print("\n--- Exercitiul 9 ---")
numere = [10, 20, 30, 40, 50]
ultimul_element = numere.pop(-1)
print(ultimul_element)
print(numere)

# 10. Lungimea listei
# -------------------
# Avem  oameni = ["Ana", "Maria", "Ion", "Vlad", "George"].
# Calculeaza si afiseaza cati oameni sunt in lista.

# Solutie:

print("\n--- Exercitiul 10 ---")
oameni = ["Ana", "Maria", "Ion", "Vlad", "George"]
print(len(oameni))

# 11. Verificare apartenenta cu  in
# ---------------------------------
# Avem  fructe = ["mar", "para", "banana"].
# Afiseaza True / False pentru:
#   - exista "mar" in lista
#   - exista "kiwi" in lista
#   - "banana" NU este in lista

# Solutie:

print("\n--- Exercitiul 11 ---")
fructe = ["mar", "para", "banana"]
print("mar" in fructe)
print("kiwi" in fructe)
print("banana" not in fructe)

# 12. Concatenare si repetare
# ---------------------------
# Avem  a = [1, 2, 3]   si   b = [4, 5, 6].
# Afiseaza:
#   - lista combinata a + b
#   - lista a repetata de 3 ori

# Solutie:

print("\n--- Exercitiul 12 ---")
a = [1, 2, 3]
b = [4, 5, 6]
print(a + b)
print(a * 3)

# 13. Min, max, sum, media
# ------------------------
# Avem  note = [8, 9, 7, 10, 6, 8].
# Afiseaza:
#   - cea mai mica nota
#   - cea mai mare nota
#   - suma notelor
#   - media notelor (cu 2 zecimale, folosind f-string)

# Solutie:

print("\n--- Exercitiul 13 ---")
note = [8, 9, 7, 10, 6, 8]
print(min(note))
print(max(note))
print(sum(note))
media = sum(note) / len(note)
print(f"Media este de {media:.2f}")

# 14. Sortare
# -----------
# Avem  preturi = [99.99, 19.5, 250, 49.9, 5.0].
# Sorteaza lista crescator (cu .sort()) si afiseaz-o.
# Apoi sorteaza descrescator si afiseaza din nou.

# Solutie:

print("\n--- Exercitiul 14 ---")
preturi = [99.99, 19.5, 250, 49.9, 5.0]
preturi.sort()
print(preturi)
print(preturi[::-1])

# 15. Inversare
# -------------
# Avem  litere = ["a", "b", "c", "d", "e"].
# Inverseaza ordinea cu .reverse() si afiseaza lista.

# Solutie:

print("\n--- Exercitiul 15 ---")
litere = ["a", "b", "c", "d", "e"]
litere.reverse()
print(litere)