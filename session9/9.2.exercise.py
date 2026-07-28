# EXERCITII  while
# =============================================================
# Mini-scenarii care folosesc while pentru iteratii bazate pe
# CONDITII (nu pe colectii), combinate cu liste, dictionare,
# string-uri si if/elif/else.
# =============================================================



# 1. Simulare ATM cu retry
# ------------------------
# Avem  parola_corecta = "1234"  si o lista de incercari (simuleaza
# tastari): tentative = ["0000", "1111", "1234", "9999"]
# Permitem maxim 3 incercari. Foloseste while:
#   - daca pin-ul e corect -> "acces permis"  + break
#   - dupa 3 incercari gresite -> "card blocat"
# Afiseaza si numarul de incercari folosite.

# Solutie:

print("\n--- Exercitiul 1 ---")
parola_corecta = "1234"
tentativele = ["0000", "1111", "1234", "9999"]
max_incercari = 3
i = 0
acces = False
while i<len(tentativele) and i<max_incercari:
    if tentativele[i] == parola_corecta:
        acces = True
        break
    i += 1

if acces:
    print("Acces permis")
else:
    print("Cardul este blocat")

# 2. Joc simplu - "ghiceste numarul"  (cu lista predefinita de incercari)
# -----------------------------------------------------------------------
# Avem  secret = 42  si o lista de incercari: tentative = [10, 80, 50, 40, 42, 99].
# Foloseste while pentru a parcurge tentativele in ordine:
#   - "prea mic"  daca tentativa < secret
#   - "prea mare" daca tentativa > secret
#   - "corect!"   daca tentativa == secret -> break
# La final afiseaza cate tentative au fost necesare.

# Solutie:

print("\n--- Exercitiul 2 ---")
secret = 42
tentative = [10, 80, 50, 40, 42, 99]
tentativa = 0
while tentativa < len(tentative):
    if secret > tentative[tentativa]:
        print("prea mic")
        break
    if secret < tentative[tentativa]:
        print("prea mare")
        break
    if secret == tentative[tentativa]:
        print("corect")
        break
    else:
        tentativa += 1
print(f"Au fost necesare un numar de {tentative.index(secret)} tentative.")

# 3. Procesare buffer pana se goleste (simulare retele)
# -----------------------------------------------------
# Avem un buffer de pachete:
#   buffer = [120, 50, 80, 200, 30, 90, 60, 110]
# Dimensiunea maxima a unei "ferestre" de transmitere este 250.
# Pentru fiecare grupa, ia pachete pana cand ai > 250 (sau s-a golit
# buffer-ul) si afiseaza:
#   "fereastra X: 3 pachete, 250 bytes"
# (Foloseste 2 while imbricate sau un while care reseteaza acumulatorul
#  cand se umple fereastra.)

# Solutie:

print("\n--- Exercitiul 3 ---")
buffer = [120, 50, 80, 200, 30, 90, 60, 110]
ferestra = 1
acumulat = 0
contor = 0
while buffer:
    pachet = buffer[0]
    if acumulat + pachet > 250:
        print(f"Fereastra {ferestra}: {contor}, {acumulat} bytes")
        ferestra += 1
        acumulat = 0
        contor = 0
    else:
        buffer.pop(0)
        acumulat+=pachet
        contor+=1

# 4. Tăiere repetată a unui string pana ramane "miez"
# ----------------------------------------------------
# Avem  text = "###Salut Python!!!".
# Vrem sa indepartam toate caracterele "#" de la inceput
# si "!" de la sfarsit folosind while:
#   while text.startswith("#"):
#       text = text[1:]
#   while text.endswith("!"):
#       text = text[:-1]
# Afiseaza string-ul curat.

# Solutie:

print("\n--- Exercitiul 4 ---")
text = "###Salut Python!!!"
while text.startswith("#"):
      text = text[1:]
      while text.endswith("!"):
            text = text[:-1]
print(text)

# 5. Convertor Romana - din arabe in romane (numere mici)
# --------------------------------------------------------
# Avem  n = 49.
# Construieste un dict cu valorile romane (in ordine descrescatoare):
#   romane = [(50, "L"), (40, "XL"), (10, "X"), (9, "IX"),
#             (5, "V"), (4, "IV"), (1, "I")]
# Foloseste while pentru a scadea cea mai mare valoare care incape,
# concatenand simbolul corespunzator. Afiseaza string-ul rezultat.

# Solutie:

print("\n--- Exercitiul 5 ---")
romane = [(50, "L"), (40, "XL"), (10, "X"), (9, "IX"),
            (5, "V"), (4, "IV"), (1, "I")]
n = 49
i=0
numar_roman = ""
while n > 0:
    if romane[i][0] <= n:
        numar_roman += romane[i][1]
        n -= romane[i][0]
    else:
        i+= 1
print(numar_roman)

# 6. Cresterea unei investitii (capitalizare)
# --------------------------------------------
# Avem  capital = 1000  si  rata = 0.05  (5% pe an).
# Cati ani sunt necesari ca acel capital sa devina >= 2000?
# Foloseste while:  capital *= (1 + rata)  si numara anii.
# Afiseaza numarul de ani si capitalul final cu 2 zecimale.

# Solutie:

print("\n--- Exercitiul 6 ---")
capital = 1000
rata = 0.05
ani = 0
while  capital <= 2000:
        capital *= (1 + rata)
        ani += 1
print(f"Numarul de ani :{ani} Capitalul {capital:.2f}")

# 7. Procesare log pana la primul ERROR (combinare for/while)
# ------------------------------------------------------------
# Avem  loguri = [
#       "INFO: start",
#       "INFO: connect",
#       "WARN: slow",
#       "INFO: query",
#       "ERROR: timeout",
#       "INFO: ignored1",
#       "INFO: ignored2",
#   ]
# Foloseste while pentru a procesa loguri pana la primul "ERROR" inclusiv.
# Pentru fiecare log:
#   - daca incepe cu "INFO" -> "info: <restul>"
#   - daca incepe cu "WARN" -> "warn: <restul>"
#   - daca incepe cu "ERROR" -> "error: <restul>" + iesire (break)

# Solutie:

print("\n--- Exercitiul 7 ---")
loguri = [
      "INFO: start",
      "INFO: connect",
      "WARN: slow",
      "INFO: query",
      "ERROR: timeout",
      "INFO: ignored1",
      "INFO: ignored2",
  ]
# restul = 0
# while restul < len(loguri):
#     if "INFO" in loguri:
#         print(loguri[restul])

# 8. Anagrame - verificare cu while
# ----------------------------------
# Avem  a = "listen"  si  b = "silent".
# Verifica daca cele doua string-uri sunt ANAGRAME (au aceleasi
# litere, in alta ordine), folosind while pentru a "consuma"
# litera cu litera dintr-o lista convertita.
# Pasi:
#   - converteste b in lista de caractere
#   - parcurge fiecare litera din a (cu while + index):
#       - daca exista in lista b -> .remove() acea litera
#       - altfel -> NU sunt anagrame
#   - la final, daca lista b e goala -> sunt anagrame

# Solutie:

print("\n--- Exercitiul 8 ---")
a = "listen"
b = "silent"
restul = 0
b = list(b)
i = 0
while i < len(a):
        if a[i] in b:
            b.remove(a[i])
            i += 1
        else:
            print("Nu sunt anagrame")
            break
else:
    if b == []:
        print("Sunt anagrame")
    else:
        print("Nu sunt anagrame")
