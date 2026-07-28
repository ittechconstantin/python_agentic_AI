# EXERCITII TUPLURI
# =============================================================
# Combinam tupluri cu liste, dictionare si string-uri.
# Toate exercitiile sunt rezolvate FARA  if / for / while.
# =============================================================


# 1. Lista de inregistrari (lista de tupluri)
# -------------------------------------------
# Construieste o lista cu 3 useri, fiecare tuplu de forma:
#   (nume, email, varsta)
# Afiseaza:
#   - numarul total de useri
#   - email-ul celui de-al doilea user
#   - varsta ultimului user

# Solutie:

print("\n--- Exercitiul 1 ---")
lista = [("ana", "ana@example.com", 30),
         ("george", "george@example.com", 45),
         ("horia", "horia@example.com", 55)]
print(len(lista))
print(lista[1][1])
print(lista[2][2])

# 2. Unpacking dintr-o inregistrare
# ---------------------------------
# Folosind lista de mai sus, despacheteaza primul user in
# 3 variabile (nume, email, varsta) si afiseaza un mesaj
# cu f-string:  "horia (30) - horia@example.com"

# Solutie:

print("\n--- Exercitiul 2 ---")
nume, email, varsta = lista[0]
print(f"{nume} ({varsta}) - {email}")

# 3. Sortarea unei liste de tupluri dupa al doilea element
# --------------------------------------------------------
# Avem inventar de produse:
#   produse = [("laptop", 4500), ("mouse", 79), ("monitor", 1200), ("tastatura", 199)]
# Sorteaza descrescator dupa pret folosind:
#   sorted(produse, key=lambda p: p[1], reverse=True)
# Afiseaza lista sortata si primul produs (cel mai scump).

# Solutie:

print("\n--- Exercitiul 3 ---")
produse = [("laptop", 4500), ("mouse", 79), ("monitor", 1200), ("tastatura", 199)]
produse_noi = sorted(produse, key=lambda p: p[1], reverse=True)
print(produse_noi)
print(max(produse, key=lambda p: (p[1])))

# 4. Sortare versiuni semantice
# -----------------------------
# Avem versiuni ale unei aplicatii ca tupluri (major, minor, patch):
#   versiuni = [(1, 2, 0), (1, 0, 9), (2, 0, 0), (1, 2, 5), (1, 2, 1)]
# Sorteaza-le crescator (Python sorteaza tuplurile lexicografic in mod natural).
# Afiseaza lista sortata si CEA MAI RECENTA versiune (ultima dupa sortare).

# Solutie:

print("\n--- Exercitiul 4 ---")
versiuni = [(1, 2, 0), (1, 0, 9), (2, 0, 0), (1, 2, 5), (1, 2, 1)]
versiuni_sortate = sorted(versiuni)
print(versiuni_sortate)
print(versiuni_sortate[::-1])

# 5. Tuplu ca CHEIE intr-un dict (coordonate -> valoare)
# ------------------------------------------------------
# Construieste un dict  `harta`  cu chei tupluri (x, y) si valori string:
#   (0, 0) -> "start"
#   (1, 0) -> "drum"
#   (1, 1) -> "comoara"
#   (2, 1) -> "iesire"
# Afiseaza:
#   - ce se afla la (1, 1)
#   - lista cheilor (toate coordonatele)
#   - cate locatii are harta

# Solutie:

print("\n--- Exercitiul 5 ---")
harta = {(0, 0) : ("start"),
         (1,0) : ("drum"),
         (1,1) : ("comoara"),
         (2,1) : ("iesire")}
print(harta[(1, 1)])
print(list(harta.keys()))
print(len(harta.keys()))

# 6. Cheie compusa (tara, oras) -> populatie
# ------------------------------------------
# Construieste:
#   populatii = {
#       ("RO", "Cluj"):       325000,
#       ("RO", "Bucuresti"): 1716000,
#       ("DE", "Berlin"):    3700000,
#       ("DE", "Munchen"):   1488000,
#   }
# Afiseaza:
#   - populatia Bucurestiului
#   - populatia totala (folosind sum pe valori)
#   - populatia maxima

# Solutie:

print("\n--- Exercitiul 6 ---")
populatii = {
      ("RO", "Cluj"):       325000,
      ("RO", "Bucuresti"): 1716000,
      ("DE", "Berlin"):    3700000,
      ("DE", "Munchen"):   1488000,
  }
print(populatii[("RO", "Bucuresti")])
print(sum(populatii.values()))
print(max(populatii.values()))

# 7. Unpacking cu  *  (rest)
# --------------------------
# Avem  log_line = ("2026-05-09", "ERROR", "auth", "user", "not", "found").
# Despacheteaza-l in:
#   data, nivel, *mesaj
# Apoi afiseaza:
#   - data
#   - nivelul
#   - mesajul reasamblat ca un singur string (cu " " intre cuvinte)
# Sugestie: " ".join(mesaj)

# Solutie:

print("\n--- Exercitiul 7 ---")
log_line = ("2026-05-09", "ERROR", "auth", "user", "not", "found")
data, nivel, *mesaj = log_line
print(data)
print(nivel)
mesaj_reasamblat = " ".join(mesaj)
print(f"{mesaj_reasamblat}")

# 8. Construirea unui dict din 2 tupluri paralele
# -----------------------------------------------
# Avem doua tupluri:
#   chei    = ("host", "port", "debug", "timeout")
#   valori  = ("localhost", 8080, True, 30)
# Construieste un dict folosind:
#   dict(zip(chei, valori))
# Afiseaza dict-ul si valoarea cheii "port".

# Solutie:

print("\n--- Exercitiul 8 ---")
chei    = ("host", "port", "debug", "timeout")
valori  = ("localhost", 8080, True, 30)
dict_nou = dict(zip(chei, valori))
print(dict_nou)
print(dict_nou["port"])

# 9. Calcul de statistici dintr-o lista de tupluri
# -------------------------------------------------
# Avem rezultatele unor request-uri (url, durata_ms):
#   masuratori = [
#       ("/login",   120),
#       ("/home",     85),
#       ("/profile", 240),
#       ("/logout",   45),
#   ]
# Afiseaza:
#   - durata maxima
#   - durata minima
#   - durata medie (cu 2 zecimale)
# Sugestie: extrage doar duratele cu  list(map(lambda r: r[1], masuratori))

# Solutie:

print("\n--- Exercitiul 9 ---")
masuratori = [
      ("/login",   120),
      ("/home",     85),
      ("/profile", 240),
      ("/logout",   45),
  ]
print(max(masuratori, key=lambda p: p[1]))
print(min(masuratori, key=lambda p: p[1]))
durate = list(map(lambda r: r[1], masuratori))
print(f"{(sum(durate) / len(durate)):.2f}")