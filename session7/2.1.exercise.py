# =============================================================
# EXERCITII  if / elif / else  -  NIVEL INCEPATOR
# =============================================================
# Foloseste DOAR ce am invatat pana acum: variabile, tipuri,
# print(), operatori, string-uri, liste, dictionare, tupluri,
# set-uri, si tot ce e in 7.if.py.
# (NU folosim for / while - inca nu le-am invatat.)
# =============================================================


# 1. Major sau minor
# ------------------
# Avem  varsta = 20.
# Daca varsta >= 18 -> afiseaza "major", altfel "minor".

# Solutie:

print("\n--- Exercitiul 1 ---")
varsta = 20
if varsta >= 18:
    print("major")
else:
    print("minor")

# 2. Promovat sau picat
# ---------------------
# Avem  nota = 7.
# Daca nota >= 5 -> "Promovat", altfel "Picat".

# Solutie:

print("\n--- Exercitiul 2 ---")
nota = 7
if nota>= 5:
    print("Promovat")
else:
    print("Picat")

# 3. Par sau impar
# ----------------
# Avem  nr = 13.
# Foloseste % pentru a verifica daca este par sau impar.
# Afiseaza "par" sau "impar".

# Solutie:

print("\n--- Exercitiul 3 ---")
nr = 13
if nr % 2 == 0:
    print("par")
else:
    print("impar")

# 4. Pozitiv, negativ sau zero
# ----------------------------
# Avem  x = -5.
# Afiseaza "pozitiv", "negativ" sau "zero" in functie de valoare.

# Solutie:

print("\n--- Exercitiul 4 ---")
x = -5
if x > 0:
    print("pozitiv")
elif x < 0:
    print("negativ")
else:
    print("zero")

# 5. Cel mai mare dintre 2 numere
# -------------------------------
# Avem  a = 12  si  b = 25.
# Afiseaza valoarea cea mai mare. Foloseste un if/else.
# (Stim ca exista max(), dar aici exersam if-ul.)

# Solutie:

print("\n--- Exercitiul 5 ---")
a = 12
b = 25
if a > b:
    print(a)
else:
    print(b)

# 6. Cel mai mare dintre 3 numere
# -------------------------------
# Avem  a = 10, b = 25, c = 17.
# Afiseaza cel mai mare folosind if / elif / else.6
# Solutie:

print("\n--- Exercitiul 6 ---")
a = 10
b = 25
c = 17
if a > b and a > c:
    print(a)
elif b > a and b > c:
    print(b)
elif c > a and c > b:
    print(c)

# 7. Categorii de varsta
# ----------------------
# Avem  varsta = 70.
# Afiseaza:
#   - "copil"     daca varsta < 13
#   - "adolescent" daca varsta < 18
#   - "adult"     daca varsta < 65
#   - "senior"    altfel

# Solutie:

print("\n--- Exercitiul 7 ---")
varsta = 70
if varsta <13:
    print("copil")
elif varsta < 18:
    print("adolescent")
elif varsta < 65:
    print("adult")
else:
    print("senior")

# 8. Categorisire status HTTP
# ---------------------------
# Avem  cod = 503.
# Afiseaza categoria:
#   1xx -> "informational"
#   2xx -> "success"
#   3xx -> "redirect"
#   4xx -> "client error"
#   5xx -> "server error"
# (Sugestie: foloseste cod < 200, cod < 300, etc.)

# Solutie:

print("\n--- Exercitiul 8 ---")
cod = 503
if cod < 200:
    print("informational")
elif cod < 300:
    print("success")
elif cod < 400:
    print("redirect")
elif cod < 500:
    print("client error")
elif cod < 600:
    print("server error")

# 9. Reducere in functie de pret
# ------------------------------
# Avem  pret = 120.
# Aplica:
#   - 0%   daca pret < 50
#   - 5%   daca pret < 100
#   - 10%  daca pret < 200
#   - 20%  altfel
# Calculeaza si afiseaza pretul final cu 2 zecimale.

# Solutie:

print("\n--- Exercitiul 9 ---")
pret = 120
if pret < 50:
    print(f"{(pret * 1.00):.2f}")
elif pret < 100:
    print(f"{(pret * 0.95):.2f}")
elif pret < 200:
    print(f"{(pret * 0.90):.2f}")
else:
    print(f"{(pret * 0.80):.2f}")

# 10. Validare parola
# -------------------
# Avem  parola = "abc12".
# Daca parola are macar 8 caractere -> "OK", altfel "Prea scurta".

# Solutie:

print("\n--- Exercitiul 10 ---")
parola = "abc12"
if len(parola) >= 8:
    print("OK")
else:
    print("Prea scurta")

# 11. Email pare valid?
# ---------------------
# Avem  email = "ana@example.com".
# Daca contine "@" SI ".", afiseaza "valid". Altfel "invalid".

# Solutie:

print("\n--- Exercitiul 11 ---")
email = "ana@example.com"
if "@" and "." in email:
    print("valid")
else:
    print("invalid")

# 12. Acces pe baza de permisiuni
# -------------------------------
# Avem  permisiuni = {"read", "write"}.
# Daca "delete" este in set -> "poti sterge", altfel "nu poti sterge".

# Solutie:

print("\n--- Exercitiul 12 ---")
permisiuni = {"read", "write"}
if "delete" in permisiuni:
    print("poti sterge")
else:
    print("nu poti sterge")

# 13. Acces pe rol (chained elif)
# -------------------------------
# Avem  user = {"username": "ana", "rol": "editor"}.
# Afiseaza:
#   - "acces complet" daca rolul este "admin"
#   - "poate edita"   daca rolul este "editor"
#   - "doar citire"   daca rolul este "user"
#   - "rol necunoscut" altfel

# Solutie:

print("\n--- Exercitiul 13 ---")
user = {"username": "ana", "rol": "editor"}
if ["rol"] == "admin":
    print("acces complet")
elif ["rol"] == "editor":
    print("poate edita")
elif ["rol"] == "user":
    print("doar citire")
else:
    print("rol necunoscut")

# 14. Lista goala?
# ----------------
# Avem  cos = [].
# Daca lista este goala -> "Cos gol", altfel afiseaza
# numarul de produse din cos.
# (Sugestie: poti folosi truthiness:  if cos:  ...)

# Solutie:

print("\n--- Exercitiul 14 ---")
cos = []
if cos == []:
    print("Cos gol")
else:
    print(len(cos))

# 15. Dict cu valoare default daca lipseste cheia
# -----------------------------------------------
# Avem  config = {"host": "localhost"}.
# Daca exista cheia "port" -> afiseaza valoarea ei.
# Altfel -> afiseaza "Port nesetat - folosesc 8080".

# Solutie:

print("\n--- Exercitiul 15 ---")
config = {"host": "localhost"}
if "port" in config:
    print(config["port"])
else:
    print("Port nesetat - folosesc 8080")

# 16. Expresia ternara
# --------------------
# Avem  varsta = 17.
# Foloseste expresia ternara pentru a construi un mesaj:
#   "Esti major" sau "Esti minor"
# si afiseaza-l intr-un singur print.

# Solutie:

print("\n--- Exercitiul 16 ---")
varsta = 17
status = print("Esti major" if varsta >= 18 else "Esti minor")




# 17. Ternara pentru valoare
# --------------------------
# Avem  scor = 88.
# Foloseste expresia ternara pentru a stoca in variabila `medalie`:
#   - "aur"    daca scor >= 90
#   - "argint" altfel
# Afiseaza medalia.

# Solutie:

print("\n--- Exercitiul 17 ---")
scor = 88
medalie = print("aur" if scor >= 90 else "argint")

# 18. Verificare None
# -------------------
# Avem  rezultat = None.
# Daca rezultat este None -> "necalculat", altfel afiseaza valoarea.
# (Sugestie: foloseste  is None / is not None)

# Solutie:

print("\n--- Exercitiul 18 ---")
rezultat = None
if rezultat is None:
    print("necalculat")
elif rezultat is not None:
    print(rezultat)

# 19. Cinema dupa varsta
# ----------------------
# Avem  varsta = 12  si  film_tip = "horror".
# Reguli:
#   - daca filmul este "kids"   -> oricine poate intra
#   - daca filmul este "general" -> minim 6 ani
#   - daca filmul este "horror" -> minim 16 ani
# Afiseaza "permis" sau "interzis".

# Solutie:

print("\n--- Exercitiul 19 ---")
varsta = 12
film_tip = "horror"
if film_tip == "kids":
    print("permis")
elif film_tip == "general" and varsta >= 6 :
    print("permis")
elif film_tip == "horror" and varsta >= 16 :
    print("permis")
else:
    print("interzis")

# 20. Recomandare imbracaminte
# ----------------------------
# Avem  temperatura = 5.
# Afiseaza:
#   - "geaca groasa + fular"  daca <= 0
#   - "geaca"                 daca <= 10
#   - "bluza lunga"           daca <= 20
#   - "tricou"                altfel

# Solutie:

print("\n--- Exercitiul 20 ---")
temperatura = 5
if temperatura <= 0:
    print("geaca groasa + fular")
elif temperatura <= 10:
    print("geaca")
elif temperatura <= 20:
    print("bluza lunga")
else:
    print("tricou")