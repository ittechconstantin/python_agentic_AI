# INSTRUCTIUNEA  while  IN PYTHON
# =============================================================
# `while` ne permite sa repetam un bloc de cod ATATA TIMP CAT
# o conditie este adevarata. Spre deosebire de `for`, NU stim
# in avans de cate ori se va repeta - asta depinde de cum se
# schimba conditia in interiorul buclei.
#
# Cand folosim `while` in loc de `for`?
#   - cand NU stim numarul de iteratii (depinde de un eveniment)
#   - cand asteptam ca o conditie sa se schimbe (ex. retry pana
#     reuseste, citire pana la o valoare-stop, convergenta numerica)
#   - cand iteram pe ceva care nu este "natural iterabil"
#     (ex: cifrele unui numar, un buffer care se goleste)
#   - simulari pas cu pas (game loop, state machine)
#
# Regula de aur:
#     for    -> stim CE iteram (lista, range, dict, etc.)
#     while  -> stim CAND ne oprim (o conditie devine False)
# =============================================================


# 1. SINTAXA DE BAZA
# -------------------------------------------------------------
# Forma:
#   while conditie:
#       <bloc - se executa cat timp conditia este True>
#
# IMPORTANT:
#   - inainte de while INITIALIZAM variabile pe care le folosim in conditie
#   - in interior trebuie sa MODIFICAM ceva ce influenteaza conditia,
#     altfel obtinem o BUCLA INFINITA (programul nu se mai opreste)

i = 1
while i < 5:
    print(i)
    i += 5


# 2. while  vs  for  -  acelasi rezultat, doua stiluri
# -------------------------------------------------------------
# Numaram de la 0 la 4:

# cu for:
for i in range(0, 5):
    print(i)

# cu while:
i = 1
while i < 5:
    print(i)
    i += 5


# Cand se stie numarul de iteratii, FOR este alegerea naturala.


# 3. PATTERN: COUNTDOWN
# -------------------------------------------------------------
n = 5
while n > 0:
    print(n)
    n -= 1

print("Lansare!")

# 4. PATTERN: SENTINEL  (ne oprim cand atingem o valoare speciala)
# -------------------------------------------------------------
# Avem o lista de evenimente; ne oprim la "STOP".

evenimente = ['Warning', 'Error', 'Info', 'Stop', 'Info']

i = 0
while evenimente[i] != 'Stop':
    print(evenimente[i])
    i += 1

print(f"Au fost procesate un numar de {i} evenimente din {len(evenimente)}")



# 5. while  cu  break  -  iesire devreme
# -------------------------------------------------------------
# Acelasi efect ca la for: break opreste bucla imediat.

numere = [1, 3, 5, 8, 11, 14]

i = 0
while i < len(numere):  # ATATA TIMP CAT MAI AM ELEMENTE IN LISTA
    if numere[i] % 2 == 0:
        print(f"Am identificat un numar par! Acela este: {numere[i]}")
        break
    else:
        i += 1


# 6. while  cu  continue
# -------------------------------------------------------------
# Sare la urmatoarea iteratie. ATENTIE: trebuie sa modificam
# variabila de control INAINTE de continue, altfel bucla infinita!

i = 0
while i < 10:
    i += 1
    if i % 2 == 0:
        continue
    print(i)                # 1 3 5 7 9



# 7. while  /  else
# -------------------------------------------------------------
# La fel ca for/else: blocul `else` ruleaza DACA bucla s-a oprit
# normal (conditia a devenit False), NU prin break.

emailuri = ['a@gmail.com', 'b@gmail.com', 'c@gmail.com']

i = 0
while i < len(emailuri):
    if 'spam' in emailuri[i]:
        print("Spam gasit!")
        break
    else:
        i += 1
else:
    print("Nu am gasit spam")



# 8. while True + break  -  bucla "fara conditie", controlata din interior
# -------------------------------------------------------------
# Stil util cand conditia de iesire e mai naturala in mijlocul
# buclei (ex: dupa o validare). NU uita break-ul, altfel bucla
# este infinita.


scoruri = [10, 25, 80, 99, 99, 7]
i = 0

while True:
    if i >= len(scoruri):
        break
    if scoruri[i] >= 100:
        print(f"Am depasit pragul de 100 de puncte")
        break

    i+=1


# 9. CAPCANA: BUCLA INFINITA
# -------------------------------------------------------------
# Daca uitam sa modificam variabila din conditie, programul
# se blocheaza. Exemplu (NU rula):
#

# i = 0
# while i < 5:
#     print(i)    i nu se schimba

# Cum evitam:
#   - mereu intreaba-te: "ce face conditia sa devina falsa?"
#   - asigura-te ca acea variabila se actualizeaza in interior




# 10. PATTERN: CRESTERE PANA LA UN PRAG  (Fibonacci)
# -------------------------------------------------------------
# Generam termenii Fibonacci cat timp sunt < 100.

# 0, 1, 1,        2,        3, 5, 8, 13, 21, 34, 55, 89, 144, ...

a, b = 0, 1
while a < 100:
    print(a, end=" ")
    a, b = b, a + b

    # temp = a
    # a = b
    # b = temp + b

# 11. WHILE  vs  FOR  -  RECAPITULARE
# -------------------------------------------------------------
# Folosesti FOR cand:
#   - ai o colectie cunoscuta (lista, dict, string, range)
#   - stii in avans cate iteratii sunt
#   - vrei sa parcurgi simplu fiecare element
#
# Folosesti WHILE cand:
#   - bucla depinde de o CONDITIE care se schimba dinamic
#   - numarul iteratiilor NU este cunoscut in avans
#   - lucrezi cu numere prin operatii (cifre, convergenta)
#   - procesezi un buffer / o coada care se goleste
#   - astepti un eveniment ("retry pana reuseste")
#
# Daca lista pe care iterezi NU se schimba si stii cati pasi
# vrei -> folosesti for (mai citibil si mai sigur).
# Daca conditia e altceva decat "am terminat lista" -> while.



# =============================================================
# CONCLUZIE
# =============================================================
# `while`:
#     while conditie:
#         ...
#
# - Cere INITIALIZARE inainte si MODIFICARE in interior
#   (altfel: bucla infinita).
# - break / continue / else functioneaza ca la for.
# - while True + break = pattern util cand iesirea e in mijloc.
# - Folosit pentru: countdown, sentinel, retry, convergenta,
#   procesare pe coada, manipulare cifre, simulari pas cu pas.
# - Daca poti folosi for in mod natural -> foloseste for.
#   Daca nu - while.
# =============================================================