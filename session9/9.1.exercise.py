# EXERCITII  while
# =============================================================
# Foloseste DOAR ce am invatat pana acum: variabile, tipuri,
# print(), operatori, string-uri, liste, dictionare, tupluri,
# set-uri, if/elif/else, for, si tot ce e in 9.while.py.
# =============================================================


# 1. Numara de la 1 la 10 cu while
# --------------------------------
# Foloseste while pentru a afisa numerele de la 1 la 10 inclusiv.

# Solutie:

print("\n--- Exercitiul 1 ---")
i = 1
while i <= 10:
    print(i, end=" ")
    i+=1

# 2. Countdown de la 10 la 1
# --------------------------
# Foloseste while pentru a afisa numerele de la 10 la 1, descrescator.
# Dupa bucla afiseaza "Lansare!".

# Solutie:

print("\n--- Exercitiul 2 ---")
i = 10
while i > 0:
    print(i)
    i -=1
print("Lansare")
# 3. Suma numerelor de la 1 la 100
# --------------------------------
# Calculeaza suma numerelor de la 1 la 100 cu while si afiseaza-o.

# Solutie:

print("\n--- Exercitiul 3 ---")
i=0
suma = 0
while i < 100:
    suma += i
    i += 1
print(suma)

# 4. Numere pare sub 20
# ---------------------
# Afiseaza toate numerele pare de la 0 la 20 inclusiv, folosind while.

# Solutie:

print("\n--- Exercitiul 4 ---")
i = -1
while i < 20:
    i += 1
    if i % 2 == 0:
        print(i, end=" ")

# 5. Suma cifrelor unui numar
# ---------------------------
# Avem  n = 8473.
# Foloseste while pentru a calcula suma cifrelor lui n.
# (Sugestie:  cifra = n % 10; n //= 10;  pana cand n == 0)

# Solutie:

print("\n--- Exercitiul 5 ---")
n = 8473
sume = 0
cifra = 0
while n > 0:
    cifra = n % 10
    sume = cifra + sume
    n //= 10
print(sume)

# while n > 0:
#     # cifra += n % 10
#     ultima_cifra = n % 10
#     cifra = cifra + ultima_cifra
#     if n //= 10
# print(cifra)

# 6. Numara cifrele unui numar
# ----------------------------
# Avem  n = 1234567.
# Calculeaza cate cifre are folosind while (NU folosi len(str(n))).

# Solutie:

print("\n--- Exercitiul 6 ---")
n = 9564984
numar_cifra = 0
while n > 0:
    n //= 10
    numar_cifra += 1
print(numar_cifra)

# 7. Inversare cifrelor unui numar
# --------------------------------
# Avem  n = 12345.
# Construieste numarul cu cifrele inversate (54321) folosind while.

# Solutie:

print("\n--- Exercitiul 7 ---")
n = 12345
numar_inversat = 0
while n > 0:
    numar_inversat = numar_inversat * 10 + n % 10
    n = n // 10
print(numar_inversat)

# 8. while True + break
# ---------------------
# Avem  numere = [3, 7, 9, 12, 15, 18].
# Foloseste while True pentru a gasi PRIMUL numar divizibil cu 4
# si sparge (break) imediat ce l-ai gasit. Afiseaza valoarea si indexul.

# Solutie:

print("\n--- Exercitiul 8 ---")
numerele = [3, 7, 9, 12, 15, 18]
i = 0
while True:
    if i >= len(numerele):
        break
    if numerele[i] % 4 == 0:
        print(f"Am gasit PRIMUL numar divizibil cu 4! Acesta este {numerele[i]} aflat la indexul {numerele.index(numerele[i])}")
        break
    i += 1

# 9. Continue in while
# --------------------
# Afiseaza numerele de la 1 la 10, dar SARI peste multiplii de 3.
# (Atentie: incrementeaza i ÎNAINTE de continue!)

# Solutie:

print("\n--- Exercitiul 9 ---")
i = 0
while i < 10:
    i += 1
    if i % 3 == 0:
        continue
    print(i, end=" ")

# 10. Procesare coada (lista pana se goleste)
# -------------------------------------------
# Avem  job_queue = ["build", "test", "deploy", "notify"].
# Foloseste while pentru a "extrage" job-urile cu .pop(0) pana se goleste,
# afisand mesajul:
#   "rulez build, ramase 3"

# Solutie:

print("\n--- Exercitiul 10 ---")
job_queue = ["build", "test", "deploy", "notify"]
i=0
while i < len(job_queue):
    if job_queue[i] == job_queue[i]:
        print(f"rulez {job_queue.pop(i)} ramase {len(job_queue)}")
        continue
    else:
        i += 1

# 11. Cea mai mare putere a lui 2 sub un prag
# -------------------------------------------
# Avem  prag = 500.
# Calculeaza cea mai mare putere a lui 2 (1, 2, 4, 8, ...) care
# este STRICT mai mica decat pragul. Afiseaza valoarea.

# Solutie:

print("\n--- Exercitiul 11 ---")
prag = 500
putere = 1
variabila = 2
while variabila**putere < prag:
    if variabila**(putere + 1) > prag:
        break
    putere += 1
print(variabila**putere)

# 12. Fibonacci sub 100
# ---------------------
# Afiseaza termenii sirului Fibonacci care sunt < 100.
# (Pleci de la a=0, b=1; in fiecare pas afisezi a si recalculezi
#  a, b = b, a + b)

# Solutie:

print("\n--- Exercitiul 12 ---")
a, b=0, 1
while a < 100:
    print(a, end=" ")
    a, b = b, a + b

# 13. Numar de incercari pana la succes
# -------------------------------------
# Avem o lista cu raspunsuri pre-incarcate, simuland incercari:
#   raspunsuri = [False, False, False, True, False]
# Foloseste while pentru a numara cate incercari ai facut PANA AI
# AVUT succes (True). Daca nu se ajunge la True, afiseaza "esuat".

# Solutie:

print("\n--- Exercitiul 13 ---")
raspunsuri = [False, False, False, True, False]
incercari=0
while True:
    if incercari >= len(raspunsuri):
        print(f"Am avut {raspunsuri.index(True)} incercari")
        break
    if raspunsuri[incercari] >= len(raspunsuri):
        print("esuat")
        break
    incercari += 1

# 14. Indexare manuala cu while in loc de for
# -------------------------------------------
# Avem  cuvinte = ["python", "go", "java", "rust"].
# Foloseste while (NU for) pentru a afisa fiecare cuvant cu indexul:
#   "0: python"
#   "1: go"
#   ...

# Solutie:

print("\n--- Exercitiul 14 ---")
cuvinte = ["python", "go", "java", "rust"]
index = 0
while index < len(cuvinte):
    print(f"{index} : {cuvinte[index]}")
    index += 1

# 15. Suma pana la depasirea unui prag
# ------------------------------------
# Avem  numere = [10, 25, 8, 17, 30, 12, 5, 9].
# Aduna numerele in ordine; OPRESTE-TE de indata ce suma DEPASESTE 50.
# Afiseaza:
#   - cate numere ai adunat
#   - suma finala

# Solutie:

print("\n--- Exercitiul 15 ---")
numerre = [10, 25, 8, 17, 30, 12, 5, 9]
suma = 0
index = 0
while suma < 50:
        suma += numerre[index]
        index += 1
print(f"Am adunat {index} numere")
print(f"Suma finala este {suma}")



# print(f"Am adunat un numar total de {numerre.index(n)} numere")
# print(f"Suma finala este de {suma}")

# 16. while/else - cautare cu fallback
# ------------------------------------
# Avem  emailuri = ["a@x.com", "b@x.com", "c@x.com", "d@x.com"].
# Cauta primul email care contine "spam":
#   - daca il gasesti -> afiseaza-l si break
#   - daca nu (else pe while) -> afiseaza "lista curata"

# Solutie:

print("\n--- Exercitiul 16 ---")

emailuri = ["a@x.com", "b@x.com", "c@x.com", "d@x.com"]
t = 0
while t < len(emailuri):
    if "spam" in emailuri[t]:
        print(t)
        break
    else:
        t += 1
else:
    print("lista curata")