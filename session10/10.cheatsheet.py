# RECAPITULARE - CONTROL FLOW (if / for / while)
# =============================================================
# In sesiunea 6 am recapitulat TIPURILE DE DATE (str, list,
# tuple, set, dict). Acum recapitulam CONTROLUL EXECUTIEI:
# decizii cu  if  si bucle cu  for  /  while.
#
# Acest fisier este un CATALOG DE PATTERN-URI - sabloane pe
# care le vei folosi tot timpul cand scrii cod. Daca le
# recunosti, scrii cod mai rapid si mai clar.
# =============================================================


# 1. RECAP RAPID -  if / elif / else
# -------------------------------------------------------------
nota = 7

if nota >= 9:
    print("excelent")
elif nota >= 7:
    print("bine")
elif nota >= 5:
    print("suficient")
else:
    print("insuficient")

# Ternara - cand vrei o VALOARE pe baza unei conditii:
status = "promovat" if nota >= 5 else "picat"
print(status)


# 2. RECAP RAPID -  for
# -------------------------------------------------------------
# Pentru CAND stii pe ce iterezi:
for x in [1, 2, 3]:        print(x)
for c in "Python":          print(c)
for k, v in {"a": 1, "b": 2}.items():    print(k, v)
for i in range(5):           print(i)
for i, val in enumerate(["ana", "horia"], start=1):
    print(i, val)
for n, p in zip(["paine", "lapte"], [4.5, 7.99]):
    print(n, p)


# 3. RECAP RAPID -  while
# -------------------------------------------------------------
# Pentru CAND stii cand sa te opresti, dar nu cati pasi vor fi:
n = 10
while n > 0:
    n -= 1
print("done")

# `while True + break` - cand iesirea e in mijloc:
i = 0
while True:
    if i >= 3:
        break
    i += 1


# 4.  break  /  continue  /  else  pe bucle
# -------------------------------------------------------------
# break    -> iesire IMEDIATA din bucla
# continue -> sare la URMATOAREA iteratie
# else     -> ruleaza DACA bucla s-a terminat normal (fara break)

for x in [1, 2, 3, 4]:
    if x == 3:
        break
    print(x)                  # 1 2

for x in [1, 2, 3, 4]:
    if x % 2 == 0:
        continue
    print(x)                  # 1 3

for x in [1, 2, 3]:
    if x == 99:
        break
else:
    print("nu a fost gasit 99")


# =============================================================
# CATALOG DE PATTERN-URI
# =============================================================


# 5.  PATTERN: ACUMULATOR  (sum, count, product, total)
# -------------------------------------------------------------
note = [9, 7, 8, 10, 6]

# Suma
total = 0
for n in note:
    total += n
print(total)
# echivalent:  total = sum(note)

# Produs
produs = 1
for n in [2, 3, 5]:
    produs *= n
print(produs)            # 30


# 6.  PATTERN: NUMARARE CONDITIONATA
# -------------------------------------------------------------
# Numara cate elemente respecta o conditie.

note = [9, 4, 8, 10, 5, 6, 3, 9]
peste_7 = 0
for n in note:
    if n > 7:
        peste_7 += 1
print(peste_7)           # 4
# echivalent:  sum(1 for n in note if n > 7)


# 7.  PATTERN: CAUTARE  (search)  - cu break
# -------------------------------------------------------------
# Mergem prin lista pana gasim primul element care indeplineste
# conditia. Daca il gasim -> break. Daca nu -> ramura else.

useri = [{"nume": "ana", "rol": "user"},
         {"nume": "horia", "rol": "admin"},
         {"nume": "geo", "rol": "user"}]

gasit = None
for u in useri:
    if u["rol"] == "admin":
        gasit = u
        break
print(gasit)


# 8.  PATTERN: FILTRARE  (collect)
# -------------------------------------------------------------
# Pastram doar elementele care respecta o conditie.

cuvinte = ["python", "go", "rust", "java", "c"]

# Stil clasic:
scurte = []
for c in cuvinte:
    if len(c) <= 4:
        scurte.append(c)

# Stil pythonic - list comprehension:
scurte = [c for c in cuvinte if len(c) <= 4]
print(scurte)


# 9.  PATTERN: TRANSFORMARE  (map)
# -------------------------------------------------------------
# Aplicam o operatie pe fiecare element si construim o lista noua.

emailuri = ["  ANA@X.COM ", "Horia@x.com", "  GEO@x.com"]

# Stil clasic:
curate = []
for e in emailuri:
    curate.append(e.strip().lower())

# Stil pythonic:
curate = [e.strip().lower() for e in emailuri]
print(curate)


# 10.  PATTERN: MAX / MIN MANUAL
# -------------------------------------------------------------
# Cand criteriul de comparatie nu e standard (ex: cel mai lung cuvant).

cuvinte = ["python", "go", "javascript", "c"]
cel_mai_lung = ""
for c in cuvinte:
    if len(c) > len(cel_mai_lung):
        cel_mai_lung = c
print(cel_mai_lung)        # javascript

# Echivalent cu max si key:
print(max(cuvinte, key=len))


# 11.  PATTERN: FREQUENCY COUNTER
# -------------------------------------------------------------
# Numara cate aparitii are fiecare element. Utilizat la log-uri,
# voturi, cuvinte intr-un text.

loguri = ["INFO", "ERROR", "INFO", "WARN", "INFO", "ERROR"]
freq = {}
for n in loguri:
    freq[n] = freq.get(n, 0) + 1
print(freq)            # {'INFO': 3, 'ERROR': 2, 'WARN': 1}

# Apoi gasesti maxim cu max + key=lambda:
top = max(freq, key=lambda k: freq[k])
print(f"top: {top} ({freq[top]})")


# 12.  PATTERN: GROUP BY  (dict de liste)
# -------------------------------------------------------------
# Grupam elemente pe categorii.

produse = [("laptop", "tech"), ("mar", "fructe"),
           ("mouse", "tech"), ("para", "fructe")]

grupat = {}
for nume, cat in produse:
    if cat not in grupat:
        grupat[cat] = []
    grupat[cat].append(nume)
print(grupat)


# 13.  PATTERN: FLATTEN  (2D -> 1D)
# -------------------------------------------------------------
# Aplatizam o lista de liste intr-o singura lista.

matrice = [[1, 2, 3], [4, 5], [6, 7, 8]]

flat = []
for rand in matrice:
    for v in rand:
        flat.append(v)
print(flat)            # [1, 2, 3, 4, 5, 6, 7, 8]

# Cu comprehension:
flat = [v for rand in matrice for v in rand]
print(flat)


# 14.  PATTERN: ITERATIE PARALELA  (zip)
# -------------------------------------------------------------
# Combinam doua sau mai multe colectii index-cu-index.

nume = ["ana", "horia", "geo"]
varste = [28, 30, 40]

for n, v in zip(nume, varste):
    print(f"{n} - {v} ani")


# 15.  PATTERN: ITERATIE 2D  (matrice cu indecsi)
# -------------------------------------------------------------
# Cand vrei sa stii pozitia (linie, coloana) intr-o matrice.

grid = [
    ["a", "b", "c"],
    ["d", "e", "f"],
    ["g", "h", "i"],
]

for i, rand in enumerate(grid):
    for j, valoare in enumerate(rand):
        print(f"({i},{j}) = {valoare}")


# 16.  PATTERN: WHILE NUMERIC  (cifre, convergenta)
# -------------------------------------------------------------
# `while` straluceste cand lucram cu numere prin operatii.

# Suma cifrelor:
n = 12345
suma = 0
while n > 0:
    suma += n % 10
    n //= 10
print(suma)            # 15

# Cati pasi pana la 1:
n = 1000
pasi = 0
while n > 1:
    n //= 2
    pasi += 1
print(pasi)            # 9

# CMMDC (Euclid):
a, b = 252, 105
while b != 0:
    a, b = b, a % b
print(a)               # 21


# 17.  PATTERN: SENTINEL  (oprire la o valoare speciala)
# -------------------------------------------------------------
evenimente = ["INFO", "INFO", "WARN", "STOP", "INFO"]
i = 0
while i < len(evenimente) and evenimente[i] != "STOP":
    print(evenimente[i])
    i += 1


# 18.  PATTERN: PROCESARE COADA  (while + pop)
# -------------------------------------------------------------
# Cand procesarea unui element poate ADAUGA elemente noi in coada,
# `for` nu mai e potrivit. Folosim `while + pop`.

queue = ["task1", "task2", "task3"]
while queue:
    task = queue.pop(0)
    print(f"procesez {task}")


# 19.  PATTERN: VALIDARE INTRARI / EARLY RETURN
# -------------------------------------------------------------
# Verificam in ordine; daca o regula pica -> mesaj clar si oprire.
email = "ana@@x"
valid = True

if "@" not in email:
    print("lipseste @")
    valid = False
elif email.count("@") > 1:
    print("prea multi @")
    valid = False
elif "." not in email:
    print("lipseste .")
    valid = False

if valid:
    print("ok")


# =============================================================
# COMPREHENSIONS  -  TABEL COMPACT
# =============================================================
# list comp:    [<expr> for x in iter if cond]
# set comp:     {<expr> for x in iter if cond}
# dict comp:    {<key>: <val> for x in iter if cond}
#
# Echivalente cu pattern-urile FILTER / TRANSFORM / FREQUENCY.

print([n ** 2 for n in range(5)])                # [0, 1, 4, 9, 16]
print([n for n in range(20) if n % 3 == 0])      # [0, 3, 6, 9, 12, 15, 18]

print({c.lower() for c in "Hello World" if c.isalpha()})    # litere unice mici

print({n: n ** 2 for n in range(5)})              # {0:0, 1:1, 2:4, 3:9, 4:16}


# =============================================================
# CAND ALEGEM CE  -  GHID DE DECIZIE
# =============================================================
#
# A) Vreau sa iau o decizie?
#       -> if / elif / else
#       -> ternara (A if cond else B) cand vrei doar o valoare
#
# B) Iterez pe o colectie cunoscuta?
#       -> for ... in ...
#
# C) Iterez de un numar fix de ori?
#       -> for i in range(N)
#
# D) Stiu ca trebuie sa repet, dar nu cati pasi?
#       -> while
#
# E) Iesirea din bucla e in mijloc?
#       -> while True + break
#
# F) Vreau o lista construita prin filtrare/transformare?
#       -> list comprehension     (in loc de for + .append)
#
# G) Lucrez cu cifrele unui numar / convergenta numerica?
#       -> while
#
# H) Procesez o coada care creste in interior?
#       -> while + pop
#
# Reguli:
#   - daca poti scrie un for natural, foloseste FOR (mai sigur).
#   - foloseste WHILE doar daca for nu se potriveste.
#   - prefera comprehension-ul cand are sub 1 linie de logica.


# =============================================================
# CAPCANE DE EVITAT
# =============================================================
#
# 1. BUCLA INFINITA in while
#       i = 0
#       while i < 10:
#           print(i)        # NU am uitat sa fac i += 1 !
#
# 2. MODIFICARE LISTA IN TIMPUL ITERATIEI
#       lista = [1, 2, 3, 4]
#       for x in lista:
#           if x == 2:
#               lista.remove(x)     # comportament imprevizibil!
#       Rezolvare: itereaza pe o COPIE  ->  for x in lista[:]
#       sau construieste o lista NOUA cu comprehension.
#
# 3. CONFUZIE  =  vs  ==
#       in if foloseste mereu ==, nu =
#
# 4. INDENTARE GRESITA
#       Python foloseste indentarea ca delimitator de bloc.
#       Mai bine 4 spatii peste tot, NU mixe cu tab-uri.
#
# 5. continue intr-un while fara incrementare
#       i = 0
#       while i < 10:
#           if i % 2 == 0:
#               continue       # i nu se mai incrementeaza -> infinit!
#           i += 1
#       Rezolvare: incrementeaza ÎNAINTE de continue.


# =============================================================
# CONCLUZIE
# =============================================================
# Cu  if + for + while + comprehensions  acoperi 95% din
# nevoile de control flow. Restul de 5% (functii, exceptii,
# clase) construim peste aceste baze.
#
# Recunoaste pattern-urile - le vei folosi tot tipul:
#   ACUMULATOR / NUMARARE / CAUTARE / FILTRARE / TRANSFORMARE
#   MAX-MIN / FREQUENCY / GROUP BY / FLATTEN / ZIP
#   SENTINEL / WHILE-NUMERIC / WHILE-COADA / VALIDARE
# =============================================================