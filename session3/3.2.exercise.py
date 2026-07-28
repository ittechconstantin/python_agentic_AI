# EXERCITII LISTE
# =============================================================
# Exercitii in care combinam mai multe operatii pe liste,
# slicing, sortare si interactiunea cu string-uri.
# =============================================================


# 1. Topul a 3 cei mai mari din lista
# -----------------------------------
# Avem  scoruri = [55, 89, 23, 100, 67, 91, 78, 42].
# Sorteaza descrescator si afiseaza primele 3 valori (top 3).

# Solutie:

print("\n--- Exercitiul 1 ---")
scoruri = [55, 89, 23, 100, 67, 91, 78, 42]
scoruri.sort(reverse=True)
print(scoruri)
print(scoruri[0:3])

# 2. Cel mai scurt si cel mai lung cuvant
# ---------------------------------------
# Avem  cuvinte = ["mar", "elefant", "casa", "programare", "pix"].
# Sorteaza dupa LUNGIMEA cuvantului (sugestie: foloseste
# parametrul `key` la sorted, ex: sorted(cuvinte, key=len) ).
# Afiseaza primul (cel mai scurt) si ultimul (cel mai lung).

# Solutie:

print("\n--- Exercitiul 2 ---")
cuvinte = ["mar", "elefant", "casa", "programare", "pix"]
cuvinte_noi = sorted(cuvinte, key=len)
print(cuvinte_noi)
print(F"Cel mai scurt : {cuvinte_noi[0]}")
print(F"Cel mai lung : {cuvinte_noi[-1]}")

# 3. Eliminare duplicate
# ----------------------
# Avem  cu_duplicate = [1, 2, 2, 3, 4, 4, 4, 5, 1, 6].
# Construieste o lista FARA duplicate folosind:
#   list(set(cu_duplicate))
# Afiseaza rezultatul.
# (atentie: ordinea poate sa nu se mai pastreze)

# Solutie:

print("\n--- Exercitiul 3 ---")
cu_duplicate = [1, 2, 2, 3, 4, 4, 4, 5, 1, 6]
lista_fara_duplicate = list(set(cu_duplicate))
print(lista_fara_duplicate)

# 4. Inversare prin slicing vs reverse()
# --------------------------------------
# Avem  numere = [1, 2, 3, 4, 5].
# Construieste:
#   - o COPIE inversata folosind slicing  [::-1]
#   - aplica .reverse() pe lista originala
# Afiseaza ambele variante.

# Solutie:

print("\n--- Exercitiul 4 ---")
numere = [1, 2, 3, 4, 5]
print(numere[::-1])
numere.reverse()
print(numere[::-1])

# 5. Inlocuire prin slicing
# -------------------------
# Avem  lista = [10, 20, 30, 40, 50, 60, 70].
# Inlocuieste elementele de la indexul 2 pana la 5
# (i.e. 30, 40, 50) cu lista [99, 99, 99].
# Sugestie:  lista[2:5] = [99, 99, 99]
# Afiseaza lista finala.

# Solutie:

print("\n--- Exercitiul 5 ---")
lista = [10, 20, 30, 40, 50, 60, 70]
lista[2:5] = [99, 99, 99]
print(lista)

# 6. Statistici pentru note
# -------------------------
# Avem  note = [9, 7, 8, 10, 6, 5, 9, 8, 7].
# Calculeaza si afiseaza, cu f-string:
#   - numarul de note
#   - nota minima
#   - nota maxima
#   - media (2 zecimale)
#   - de cate ori apare nota 9

# Solutie:

print("\n--- Exercitiul 6 ---")
note = [9, 7, 8, 10, 6, 5, 9, 8, 7]
print(f"Numar de note este : {len(note)}")
print(f"Nota minima este : {min(note)}")
print(f"Nota maxima este : {max(note)}")
print(f"Media este : {(sum(note)/len(note)):.2f}")
print(f"Nota 9 apare de : {note.count(9)}")

# 7. Cos de cumparaturi - total
# -----------------------------
# Avem doua liste paralele:
#   produse  = ["paine", "lapte", "cafea", "branza"]
#   preturi  = [4.5,    7.99,    23.0,    15.5]
# Afiseaza totalul cosului folosind sum() si construieste un
# mesaj de tipul:
#   "Cos: 4 produse, total 50.99 lei"

# Solutie:

print("\n--- Exercitiul 7 ---")
produse  = ["paine", "lapte", "cafea", "branza"]
preturi  = [4.5,    7.99,    23.0,    15.5]
print(f"Cos: {len(produse)} produse, total {sum(preturi)} lei")

# 8. Adaugare conditionala in lista
# ---------------------------------
# Pleaca de la  lista = [1, 2, 3].
# Adauga la final  numarul 4 daca nu este deja in lista
# (foloseste  in / not in  si .append()).
# Apoi incearca sa adaugi 2 - dar doar daca nu este deja prezent.
# Afiseaza lista finala.

# Solutie:

print("\n--- Exercitiul 8 ---")
lista = [1, 2, 3]
print(4 not in lista)
lista.append(4)
print(2 not in lista)
print(lista)

# 9. Din string in lista de cuvinte si invers
# -------------------------------------------
# Pleaca de la  text = "Python este un limbaj de programare".
# - Imparte in cuvinte (.split()) -> lista
# - Sorteaza lista alfabetic
# - Re-uneste cu " | " ca separator (.join())
# Afiseaza string-ul final.

# Solutie:

print("\n--- Exercitiul 9 ---")
text = "Python este un limbaj de programare"
cuvinte = text.split()
cuvinte.sort()
cuvinte_de_final = " | ".join(cuvinte)
print(cuvinte_de_final)

# 10. Cele mai lungi cuvinte
# --------------------------
# Avem  cuvinte = ["python", "java", "go", "rust", "javascript", "c"]
# - Sorteaza dupa lungime, descrescator
#   (sugestie:  sorted(cuvinte, key=len, reverse=True) )
# - Afiseaza primele 3.

# Solutie:

print("\n--- Exercitiul 10 ---")
cuvintele = ["python", "java", "go", "rust", "javascript", "c"]
cuvintelele_noi = (sorted(cuvinte, key=len, reverse=True))
print(cuvintelele_noi[0:3])

# 11. Combinare doua liste sortate
# --------------------------------
# Avem  a = [1, 5, 8]  si  b = [2, 3, 9, 10].
# Construieste o lista noua  c  care contine elementele din ambele,
# sortata crescator. Afiseaz-o.

# Solutie:

print("\n--- Exercitiul 11 ---")
a = [1, 5, 8]
b = [2, 3, 9, 10]
c = a+b
print(sorted(c))

# 12. Lista 2D - acces in matrice
# -------------------------------
# Avem o matrice 3x3:
#   matrice = [
#       [1, 2, 3],
#       [4, 5, 6],
#       [7, 8, 9],
#   ]
# Afiseaza:
#   - elementul din coltul stanga-sus
#   - elementul din mijloc
#   - elementul din coltul dreapta-jos
#   - intregul rand al doilea
# (sugestie: matrice[rand][coloana])

# Solutie:

print("\n--- Exercitiul 12 ---")
matrice = [
           [1, 2, 3],
           [4, 5, 6],
           [7, 8, 9],
           ]


print(matrice[0][0])
print(matrice[1][1])
print(matrice[2][2])
print(matrice[1])

# 13. Lista de string-uri -> lista de lungimi
# -------------------------------------------
# Avem  cuvinte = ["mar", "elefant", "casa", "programare"].
# Fara loop, foloseste functia map cu len si conversie list:
#   list(map(len, cuvinte))
# Afiseaza lista cu lungimile fiecarui cuvant.

# Solutie:

print("\n--- Exercitiul 13 ---")
calomfir = ["mar", "elefant", "casa", "programare"]
noul_calomfire = list(map(len, calomfir))
print(noul_calomfire)

# 14. Curatare nume
# -----------------
# Avem  nume = ["  ana  ", "MARIA", "ion", "  GEORGE  "].
# Vrem o lista  nume_curate  in care fiecare nume:
#   - este fara spatii la capete
#   - are doar prima litera majuscula
# Sugestie - foloseste o expresie cu map si .strip().title():
#   list(map(lambda n: n.strip().title(), nume))
# Afiseaza rezultatul.

# Solutie:

print("\n--- Exercitiul 14 ---")
norii = ["  ana  ", "MARIA", "ion", "  GEORGE  "]
mai_nou = list(map(lambda n: n.strip().title(), norii))
print(mai_nou)

# 15. Mutare element de la sfarsit la inceput
# -------------------------------------------
# Avem  lista = ["a", "b", "c", "d", "e"].
# Muta ultimul element pe prima pozitie folosind .pop() si .insert(),
# astfel incat lista sa devina ["e", "a", "b", "c", "d"].
# Afiseaza lista finala.

# Solutie:

print("\n--- Exercitiul 15 ---")
lista = ["a", "b", "c", "d", "e"]
ultimul = lista.pop()
lista.insert(0, ultimul)
print(lista)
