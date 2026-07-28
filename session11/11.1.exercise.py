# EXERCITII FUNCTII
# =============================================================
# Foloseste DOAR ce am invatat pana acum: variabile, tipuri,
# operatori, string-uri, liste, dict-uri, set-uri, tupluri,
# if/elif/else, for, while, si tot ce e in 11.functions.py.
# (Nu folosim *args / **kwargs - sesiunea urmatoare.)
# =============================================================


# 1. Functie care saluta
# ----------------------
# Defineste o functie  saluta()  care printeaza "Salut, lume!".
# Apoi cheama-o.

# Solutie:

print("\n--- Exercitiul 1 ---")
def saluta():
    print("Salut, lume!")
saluta()

# 2. Functie cu un parametru
# --------------------------
# Defineste  saluta_pe(nume)  care printeaza "Salut, <nume>!".
# Cheam-o pentru "Ana" si pentru "Horia".

# Solutie:

print("\n--- Exercitiul 2 ---")
def saluta_pe(nume):
    print(f"Salut, {nume}!")

saluta_pe("Ana")
saluta_pe("Horia")

# 3. Suma a doua numere - return
# ------------------------------
# Defineste  aduna(a, b)  care RETURNEAZA suma. Foloseste-o pentru
# a calcula 3+5 si afiseaza rezultatul.

# Solutie:

print("\n--- Exercitiul 3 ---")
def aduna(a, b):
    return a + b
print(aduna(3, 5))

# 4. Patratul unui numar
# ----------------------
# Defineste  patrat(x)  care returneaza  x ** 2.
# Afiseaza patratul lui 7.

# Solutie:

print("\n--- Exercitiul 4 ---")
def patrat(x):
    return x ** 2
print(patrat(7))

# 5. Cubul unui numar (lambda)
# ----------------------------
# Defineste  cub  ca o LAMBDA care intoarce  x ** 3.
# Afiseaza cubul lui 4.

# Solutie:

print("\n--- Exercitiul 5 ---")
cub=lambda x: x**3
print(cub(4))

# 6. Verifica par sau impar
# -------------------------
# Defineste  este_par(n)  care returneaza  True / False
# in functie de paritate. Testeaza pe 4 si pe 7.

# Solutie:

print("\n--- Exercitiul 6 ---")
def este_par(n):
    if n % 2 == 0:
        return True
    return False
print(este_par(6))
print(este_par(7))

# 7. Maximul a 2 numere
# ---------------------
# Defineste  maxim(a, b)  care returneaza valoarea mai mare
# (FARA sa folosesti max()).

# Solutie:

print("\n--- Exercitiul 7 ---")
def maxim (a, b):
    max = 0
    if a > b:
        max = a
    else:
        max = b
    return max
print(maxim(5, 6))

# 8. Aria unui dreptunghi cu default
# ----------------------------------
# Defineste  aria(lung, lat=1)  care returneaza  lung * lat.
# Cheam-o cu un singur argument (lat va fi 1) si cu doua.

# Solutie:

print("\n--- Exercitiul 8 ---")
def aria(lung, lat=1):
    return lung * lat
print(aria(8))
print(aria(8, 2))

# 9. Salutare cu mesaj configurabil
# ---------------------------------
# Defineste  saluta(nume, mesaj="Salut")  care printeaza:
#   "<mesaj>, <nume>!"
# Cheam-o:
#   - saluta("Ana")
#   - saluta("Horia", "Buna seara")
#   - saluta(nume="Geo", mesaj="Hi")

# Solutie:

print("\n--- Exercitiul 9 ---")
def salutare(nume, mesaj="Salut"):
    print(f"{mesaj}, {nume}!")
salutare("Ana")
salutare("Horia", "Buna seara")
salutare(nume="Geo", mesaj="Hi")

#Aici am definit altfel functia deoarece am definit-o mai sus cu acelasi nume si nu voiam sa se suprascrie valorile

# 10. Suma cifrelor
# -----------------
# Defineste  suma_cifrelor(n)  care returneaza suma cifrelor lui n.
# Sugestie: foloseste un while cu  % 10  si  // 10.

# Solutie:

print("\n--- Exercitiul 10 ---")
def suma_cifrelor(n):
    suma = 0
    while n > 0:
        cifra = n % 10
        suma = cifra + suma
        n //= 10
    return suma
print(suma_cifrelor(238))

# 11. Factorial
# -------------
# Defineste  factorial(n)  care returneaza  1 * 2 * 3 * ... * n.
# Pentru n = 0 returneaza 1.

# Solutie:

print("\n--- Exercitiul 11 ---")
def factorial(n):
    factor = 1
    for i in range(1, n+1):
        factor *= i
    if n == 0:
        return 1
    return factor
print(factorial(0))

# 12. Verifica daca un numar este prim
# ------------------------------------
# Defineste  este_prim(n) -> bool.
# (n trebuie sa fie >= 2 si sa nu se imparta exact la nici un 2..n-1)

# Solutie:

print("\n--- Exercitiul 12 ---")
def este_prim(n) -> bool:
    if n >= 2:
        for i in range(2, n):
            if n % i == 0:
                return False
        else:
            return True
    else:
        return False
print(este_prim(19))

# 13. Min si max simultan (return tuplu)
# --------------------------------------
# Defineste  min_max(numere)  care returneaza un TUPLU (min, max).
# Apeleaz-o si despacheteaza in 2 variabile.

# Solutie:

print("\n--- Exercitiul 13 ---")
def min_max(numere):
    return tuple([min(numere), max(numere)])
print(min_max([15,3]))

# 14. Validare email
# ------------------
# Defineste  email_valid(email) -> bool.
# Reguli:
#   - exact UN @
#   - cel putin un . (in domeniu, nu e necesar sa verifici pozitia)
#   - cel putin 5 caractere

# Solutie:

print("\n--- Exercitiul 14 ---")
def email_valid(email) ->bool:
    if email.count("@") == 1 and email.count(".") >= 1 and len(email) > 5:
        return True
    else:
        return False
print(email_valid("johnn_python@yahoo.com"))

# 15. Functii intr-un dict (calculator simplu)
# --------------------------------------------
# Defineste functii  add, sub, mul, div  (cele de baza).
# Pune-le intr-un dict cu cheile "+", "-", "*", "/".
# Apeleaza dict-ul pentru semn = "*", a = 6, b = 7. Afiseaza rezultatul.

# Solutie:

print("\n--- Exercitiul 15 ---")
def functii(add, sub, mul, div):
    return {"+": a + b,
            "-": a - b,
            "*": a * b,
            "/": a / b}
print(functii("*", a = 6, b = 7))
