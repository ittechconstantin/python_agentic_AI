# OPERATORII DIN PYTHON
# =============================================================
# Operatorii sunt simboluri speciale care efectueaza operatii
# asupra unor valori numite OPERANZI.
# Exemplu: in expresia  5 + 3, simbolul "+" este operatorul,
# iar 5 si 3 sunt operanzii.
# =============================================================


# 1. OPERATORI ARITMETICI
# -------------------------------------------------------------
# Sunt folositi pentru a efectua operatii matematice.
#
#   +    adunare
#   -    scadere
#   *    inmultire
#   /    impartire (rezultat float, intotdeauna)
#   //   impartire intreaga (catul intreg)
#   %    modulo (restul impartirii)
#   **   ridicare la putere

print("Adunare           ",   5 + 3)
print("Scadere           ",   5 - 3)
print("Inmultire         ",   5 * 3)
print("Impartire         ",   10 / 2)
print("Impartire intreaga",   10 // 2)
print("Modulo            ",   5 % 3)
print("Ridicare la putere",   5 ** 3)  # 5 * 5 * 5

# Aplicatii utile pentru % si //:
#   - a % 2 ne arata daca un numar este par (rest 0) sau impar (rest 1)
#   - a // n imparte un numar in grupe egale (ex: minute -> ore)

minute = 135
ore = minute // 60  # 2 ore
minute_ramase = minute % 60 # 15 minute ramase
print(f"{minute} minute = {ore} ore si {minute_ramase} minute")

# 2. OPERATORI DE COMPARARE
# -------------------------------------------------------------
# Compara doua valori si returneaza un BOOLEAN (True / False).
#
#   ==   egal
#   !=   diferit
#   >    mai mare
#   <    mai mic
#   >=   mai mare sau egal
#   <=   mai mic sau egal

x = 7
y = 10

print(x == y) # False
print(x != y) # True
print(x > y)  # False
print(x < y)  # True
print(x >= y) # False
print(x <= y) # True

# Atentie: "==" verifica egalitatea de valoare, "=" face atribuire.


# 3. OPERATORI LOGICI
# -------------------------------------------------------------
# Combina expresii booleene.
#
#   and  -> True doar daca AMBELE conditii sunt True
#   or   -> True daca CEL PUTIN UNA dintre conditii este True
#   not  -> inverseaza valoarea booleana

# Tabela de adevar pentru AND:
#   True  and True  -> True
#   True  and False -> False
#   False and True  -> False
#   False and False -> False

# Tabela de adevar pentru OR:
#   True  or True  -> True
#   True  or False -> True
#   False or True  -> True
#   False or False -> False

varsta = 25
are_permis = True

print(varsta >= 18 and are_permis)  # True
print(varsta < 18 or are_permis)    # True
print(not are_permis)               # False


# 4. OPERATORI DE ATRIBUIRE
# -------------------------------------------------------------
# Atribuie valori variabilelor. Variantele compuse (+=, -=, etc.)
# sunt scurtaturi pentru "ia valoarea curenta, aplica operatia,
# pune rezultatul inapoi in variabila".

scor = 10

scor += 5    # echivalent cu scor = scor + 5   -> 15
scor -= 2    # echivalent cu scor = scor - 2   -> 13
scor *= 2    # echivalent cu scor = scor * 2   -> 26
scor //= 2   # echivalent cu scor = scor // 2  -> 13
scor %= 5    # echivalent cu scor = scor % 5   -> 3
scor **= 2   # echivalent cu scor = scor ** 2  -> 9
print(scor)


# 5. OPERATORI DE APARTENENTA (membership)
# -------------------------------------------------------------
# Verifica daca o valoare se afla intr-o secventa (string, lista).
#
#   in       -> True daca valoarea EXISTA in secventa
#   not in   -> True daca valoarea NU exista in secventa

email = 'ana@gmail.com'
print("@" in email)          # True
print("yahoo" not in email)  # True


# 6. OPERATORI DE IDENTITATE
# -------------------------------------------------------------
# Verifica daca DOUA variabile fac referire la ACELASI obiect
# din memorie (NU doar daca au aceeasi valoare).
#
#   is        -> True daca este acelasi obiect in memorie
#   is not    -> opusul

a = None
print(a is None)     # True (folosim "is" cu None, True, False)
print(a is not None) # False


# 7. PRECEDENTA OPERATORILOR
# -------------------------------------------------------------
# Operatorii nu se evalueaza de la stanga la dreapta intotdeauna.
# Exista o ordine (similar cu matematica):
#
#   1.  **                     (putere)
#   2.  *  /  //  %            (inmultire, impartire, modulo)
#   3.  +  -                   (adunare, scadere)
#   4.  <  <=  >  >=  ==  !=   (comparari)
#   5.  not
#   6.  and
#   7.  or
#
# Folositi PARANTEZE () cand vreti sa fortati o ordine clara.

rezultat = 2 + 3 * 4  # 14, NU 20 ( mai intai se face inmultirea)
rezultat_paranteze = (2 + 3) * 4 # 20
print(rezultat, rezultat_paranteze)

print(1 > 4 or 13 > 4 and 15 > 13)