# EXERCITII OPERATORI
# =============================================================
# Foloseste DOAR ce am invatat pana acum:
# variabile, tipuri (int, float, str, bool), conversie, print()
# si operatorii din 1.operators.py.
# =============================================================


# 1. Suma si diferenta
# --------------------
# Creeaza doua variabile `a = 17` si `b = 4`.
# Afiseaza suma, diferenta, produsul si catul lor (impartire normala).

# Solutie:
a = 17
b = 4
suma = a + b
scadere = a - b
produs = a * b
catul = a / b



# 2. Impartire intreaga si rest
# -----------------------------
# Avem 47 de bomboane si 5 copii.
# Calculeaza cate bomboane primeste fiecare copil
# si cate raman nedistribuite.

# Solutie:

bomboane = 47
copii = 5
per_copil = bomboane // copii
ramase = bomboane % copii
print(per_copil, ramase)


# 3. Numar par sau impar
# ----------------------
# Creeaza o variabila `numar = 23`.
# Afiseaza rezultatul expresiei  numar % 2 == 0.
# (rezultatul True inseamna par, False inseamna impar)

# Solutie:

numar = 23
print(numar % 2 == 0)

# 4. Ridicare la putere
# ---------------------
# Calculeaza si afiseaza:
#   - 2 la puterea 10
#   - radacina patrata a lui 81 (folosind ** 0.5)

# Solutie:

print(2 ** 10)
print( 81 ** 0.5)

# 5. Comparatii intre numere
# --------------------------
# Avem `pret_produs = 120` si `buget = 100`.
# Afiseaza rezultatele expresiilor:
#   - pret_produs > buget
#   - pret_produs == buget
#   - pret_produs <= buget * 1.5

# Solutie:

pret_produs = 120
buget = 100
print(pret_produs > buget)
print(pret_produs == buget)
print(pret_produs <= buget * 1.5)

# 6. Operator de atribuire compusa
# --------------------------------
# Pleaca de la `scor = 0`.
# Aplica pe rand:
#   scor += 10
#   scor += 25
#   scor *= 2
#   scor -= 15
# Afiseaza scorul final.

# Solutie:

scor = 0
scor += 10
scor += 25
scor *= 2
scor -= 15
print(scor)

# 7. Operatori logici
# -------------------
# Avem `varsta = 22` si `are_buletin = True`.
# Afiseaza rezultatele:
#   varsta >= 18 and are_buletin
#   varsta < 18 or are_buletin
#   not are_buletin

# Solutie:

varsta = 22
are_buletin = True
print(varsta >=18 and are_buletin)
print(varsta < 18 or are_buletin)
print(not are_buletin)

# 8. Egalitate intre tipuri
# -------------------------
# Creeaza  a = 5  si  b = 5.0  (unul int, celalalt float).
# Afiseaza  a == b.
# (Ce concluzie tragem? Egalitatea compara valoarea, nu tipul.)

# Solutie:

a = 5
b = 5.0
print(a == b)

# 9. Conversie + operator
# -----------------------
# Avem `numar_text = "42"`.
# Converteste-l in intreg, aduna-i 8 si afiseaza rezultatul.

# Solutie:

numar_text = 42
numar_int = int(numar_text)
print(numar_int + 8)

# 10. Operatorul `in` pe text
# ---------------------------
# Avem  email = "ana.popescu@gmail.com".
# Verifica si afiseaza:
#   - daca textul contine "@"
#   - daca textul contine ".com"
#   - daca textul NU contine "yahoo"

# Solutie:

email ="ana.popescu@gmail.com"
print("@" in email)
print(".com" in email)
print("yahoo" not in email)