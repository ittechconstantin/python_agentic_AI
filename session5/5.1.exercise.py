# EXERCITII TUPLURI
# =============================================================
# Foloseste DOAR ce am invatat pana acum: variabile, tipuri,
# print(), operatori, string-uri, liste, dictionare,
# si tot ce e in 1.tuple.py.
# (NU folosim if / for / while - inca nu le-am invatat.)
# =============================================================


# 1. Crearea unui tuplu
# ---------------------
# Creeaza un tuplu  `server`  cu 3 elemente:
#   - host    -> "10.0.0.1"
#   - port    -> 8080
#   - online  -> True
# Afiseaza tuplul si tipul lui.

# Solutie:

print("\n--- Exercitiul 1 ---")
server = ("host", "10.0.0.1",
          "port", "8080",
          "online", True)
print(server)
print(type(server))

# 2. Tuplu cu un singur element
# -----------------------------
# Creeaza un tuplu  `singur`  care contine doar valoarea 42.
# (Atentie - virgula este obligatorie!)
# Afiseaza tuplul si tipul lui.

# Solutie:

print("\n--- Exercitiul 2 ---")
singur = (42,)
print(singur)
print(type(singur))

# 3. Accesarea elementelor
# ------------------------
# Avem  culoare = (255, 100, 50).
# Afiseaza:
#   - prima componenta (rosu)
#   - ultima componenta (folosind index negativ)

# Solutie:

print("\n--- Exercitiul 3 ---")
culoare = (255, 100, 50)
print(culoare[0])
print(culoare[-1])

# 4. Slicing pe tuplu
# -------------------
# Avem  versiuni = ("v1", "v2", "v3", "v4", "v5", "v6").
# Afiseaza:
#   - primele 3 versiuni
#   - ultimele 2 versiuni
#   - tuplul inversat

# Solutie:

print("\n--- Exercitiul 4 ---")
versiuni = ("v1", "v2", "v3", "v4", "v5", "v6")
print(versiuni[:3])
print(versiuni[-2:])
print(versiuni[::-1])

# 5. Unpacking
# ------------
# Avem  coord = (10, 20).
# Despacheteaza-l in doua variabile  x  si  y  si afiseaza-le.

# Solutie:

print("\n--- Exercitiul 5 ---")
coord = (10, 20)
x, y = coord
print(x, y)

# 6. Unpacking cu 3 variabile
# ---------------------------
# Avem  user_record = ("horia", "horia@example.com", "admin").
# Despacheteaza-l in  nume, email, rol  si afiseaza:
#   "horia (admin) - horia@example.com"  folosind f-string.

# Solutie:

print("\n--- Exercitiul 6 ---")
user_record = ("horia", "horia@example.com", "admin")
nume, email, role = user_record
print(f"{nume}, ({role}) - {email}")

# 7. Swap de variabile
# --------------------
# Pleaca de la  a = 5  si  b = 10.
# Schimba-le valorile intre ele PE O SINGURA LINIE folosind tuplu.
# Afiseaza-le dupa swap.

# Solutie:

print("\n--- Exercitiul 7 ---")
a = 5
b = 10
a, b = b, a
print(a, b)

# 8. count si index pe tuplu
# --------------------------
# Avem  log_levels = ("INFO", "ERROR", "INFO", "WARN", "INFO", "ERROR").
# Afiseaza:
#   - de cate ori apare "INFO"
#   - indexul primei aparitii a lui "WARN"

# Solutie:

print("\n--- Exercitiul 8 ---")
log_levels = ("INFO", "ERROR", "INFO", "WARN", "INFO", "ERROR")
print(log_levels.count("INFO"))
print(log_levels.index("WARN"))

# 9. Concatenare si repetare
# --------------------------
# Avem  a = (1, 2, 3)  si  b = (4, 5, 6).
# Afiseaza:
#   - tuplul combinat  a + b
#   - tuplul a repetat de 3 ori

# Solutie:

print("\n--- Exercitiul 9 ---")
a = (1, 2, 3)
b = (4, 5, 6)
print(a + b)
print(a * 3)

# 10. Apartenenta:  in / not in
# -----------------------------
# Avem  permisiuni = ("read", "write").
# Afiseaza True / False pentru:
#   - "read" exista
#   - "delete" exista
#   - "delete" NU exista

# Solutie:

print("\n--- Exercitiul 10 ---")
permisiuni = ("read", "write")
print("read" in permisiuni)
print("delete" in permisiuni)
print("delete" not in permisiuni)

# 11. min, max, sum
# -----------------
# Avem  porturi = (22, 80, 443, 8080, 3306).
# Afiseaza:
#   - cel mai mic port
#   - cel mai mare port
#   - suma porturilor

# Solutie:

print("\n--- Exercitiul 11 ---")
porturi = (22, 80, 443, 8080, 3306)
print(min(porturi))
print(max(porturi))
print(sum(porturi))

# 12. Conversii lista <-> tuplu
# -----------------------------
# Avem  lista = [10, 20, 30].
# - Converteste lista in tuplu si afiseaza
# - Apoi din tuplu inapoi in lista si afiseaza

# Solutie:

print("\n--- Exercitiul 12 ---")
lista = [10, 20, 30]
tpl = tuple(lista)
print(tpl)
lst = list(tpl)
print(lst)

# 13. Lungime si afisare cu f-string
# ----------------------------------
# Avem  rgb = (200, 100, 50).
# Afiseaza:
#   - cate componente are tuplul
#   - un mesaj de forma:  "RGB(200, 100, 50)"   folosind f-string

# Solutie:

print("\n--- Exercitiul 13 ---")
rgb = (200, 100, 50)
print(len(rgb))
print(f"RGB{rgb}")

# 14. Modificare imposibila (demonstrativ)
# ----------------------------------------
# Avem  coord = (10, 20).
# Decomenteaza linia de mai jos si vezi ce eroare apare.
# Apoi rezolva problema reasignand un TUPLU NOU variabilei `coord`,
# in care prima componenta este 99.
# Afiseaza tuplul nou.

# Solutie:

print("\n--- Exercitiul 14 ---")
coord = (10, 20)
# coord[0] = 99
coord =(99,  coord[-1])
print(coord)
