# EXERCITII SET-URI
# =============================================================
# Foloseste DOAR ce am invatat pana acum: variabile, tipuri,
# print(), operatori, string-uri, liste, dictionare, tupluri,
# si tot ce e in 1.set.py
# (NU folosim if / for / while - inca nu le-am invatat.)
# =============================================================


# 1. Crearea unui set
# -------------------
# Creeaza un set numit  `tehnologii`  cu valorile:
#   "Python", "Go", "SQL", "Docker"
# Afiseaza set-ul si lungimea lui.

# Solutie:

tehnologii = {"Python", "Go", "SQL", "Docker"}
print(tehnologii)
print(len(tehnologii))

# 2. Set gol
# ----------
# Creeaza un set GOL si afiseaza tipul lui.
# (Atentie:  {}  inseamna dict gol, NU set gol!)

# Solutie:

set_gol = set()
print(type(set_gol))

# 3. Duplicate ignorate automat
# -----------------------------
# Creeaza un set din lista:
#   ["INFO", "ERROR", "INFO", "WARN", "INFO", "ERROR"]
# Afiseaza set-ul rezultat si lungimea lui.

# Solutie:

set_valori = {"INFO", "ERROR", "INFO", "WARN", "INFO", "ERROR"}
print(set_valori)
print(type(set_valori))

# 4. Adaugare cu .add()
# ---------------------
# Pleaca de la  permisiuni = {"read"}.
# Adauga "write", apoi inca o data "read" (NU se va dubla),
# apoi "delete". Afiseaza set-ul final.

# Solutie:

permisiuni = {"read"}
permisiuni.add("write")
permisiuni.add("read")
permisiuni.add("delete")
print(permisiuni)

# 5. .update() cu mai multe elemente
# ----------------------------------
# Pleaca de la  porturi = {80, 443}.
# Adauga deodata 22, 8080 si 80 (duplicat) folosind .update().
# Afiseaza set-ul.

# Solutie:

porturi = {80, 443}
porturi.update({22, 8080, 80})
print(porturi)

# 6. .discard() vs .remove()
# --------------------------
# Avem  emailuri = {"a@x.com", "b@x.com", "c@x.com"}.
# - sterge "b@x.com" cu .remove()
# - apoi incearca sa stergi "z@x.com" cu .discard() (nu exista, dar
#   nu da eroare)
# Afiseaza set-ul final.

# Solutie:

emailuri = {"a@x.com", "b@x.com", "c@x.com"}
emailuri.remove("b@x.com")
emailuri.discard("z@x.com")
print(emailuri)

# 7. Apartenenta: in / not in
# ---------------------------
# Avem  ip_blocate = {"10.0.0.5", "10.0.0.7", "10.0.0.13"}.
# Afiseaza True / False pentru:
#   - "10.0.0.5" este blocat
#   - "10.0.0.1" este blocat
#   - "10.0.0.1" NU este blocat

# Solutie:

ip_blocate = {"10.0.0.5", "10.0.0.7", "10.0.0.13"}
print("10.0.0.5" in ip_blocate)
print("10.0.0.1" in ip_blocate)
print("10.0.0.1" not in ip_blocate)

# 8. Deduplicare unei liste
# --------------------------
# Avem o lista de useri logati (cu duplicate):
#   useri = ["ana", "horia", "ana", "george", "horia", "ana", "vlad"]
# Construieste o LISTA unica si sortata alfabetic.
# Sugestie:  sorted(set(useri))

# Solutie:

useri = ["ana", "horia", "ana", "george", "horia", "ana", "vlad"]
lista_unica = sorted(set(useri))

# 9. .pop() si .clear()
# ----------------------
# Avem  servicii = {"nginx", "postgres", "redis"}.
# - extrage un element ALEATOR cu .pop() si afiseaza-l
# - afiseaza set-ul ramas
# - apoi goleste set-ul cu .clear() si afiseaza-l

# Solutie:

servicii = {"nginx", "postgres", "redis"}
servicii.pop()
print(servicii)
servicii.clear()
print(servicii)

# 10. Conversie  string -> set  (litere unice)
# --------------------------------------------
# Avem  text = "abracadabra".
# Construieste setul cu literele DISTINCTE din text si
# afiseaza:
#   - set-ul
#   - cate litere distincte sunt

# Solutie:

text = "abracadabra"
print(set(text))
print(len(text))