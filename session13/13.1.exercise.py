# 10 EXERCITII
# =============================================================

import random


# 1. GHICESTE NUMARUL
# ----------------------
# Calculatorul alege un numar 1-100, tu ghicesti, el iti spune daca e
# prea mare sau prea mic. Scrie  indiciu(ghicit, secret)  care intoarce
# mesajul potrivit.

# Solutie:

def indiciu(ghicit, secret):
    if ghicit < secret:
        return "Prea mic! Mai incearca"

    if ghicit > secret:
        return "Prea mare! Mai incearca"

    return "Bravo, ai ghicit numarul!"

secret = random.randint(1, 100)
print(secret)
#
# while True:
#     ghicit = int(input("Ghiceste un numar: "))
#     print(indiciu(ghicit, secret))
#     if ghicit == secret:
#         break


# 2.  PIATRA - FOARFECA - HARTIE
# -------------------------------
# Joci impotriva calculatorului. Scrie  castigator(tu, calculator)  care
# intoarce "Castigi!", "Pierzi!" sau "Egal!".
# Reguli: piatra bate foarfeca, foarfeca bate hartie, hartie bate piatra.

# Solutie:

# def castigator(tu, calculator):
#     bate = {'piatra': 'foarfeca', 'foarfeca': 'hartie', 'hartie': 'piatra'}
#     if tu == calculator:
#         return "EGAL!"
#
#     if bate[tu] == calculator:
#         return "Castigi!"
#     else:
#         return "Pierzi!"
#
#
# tu = input("Piatra, foarfeca sau hartie?:  ")
# calculator = random.choice(['piatra', 'foarfeca', 'hartie'])
# print(castigator(tu, calculator))


# 3. WORDLE simplu
# -------------------
# Ghicesti un cuvant; pentru fiecare litera primesti: 🟩 corecta pe locul
# corect, 🟨 exista dar in alta parte, ⬜ nu exista. Scrie
# feedback(ghicit, secret)  care intoarce sirul de patratele colorate.

# Solutie:

def feedback(ghicit, secret):
    rezultat = ''
    for i, litera in enumerate(ghicit):
        if litera == secret[i]:
            rezultat += '🟩'
        elif litera in secret:
            rezultat += '🟨'
        else:
            rezultat += '⬜';
    return rezultat

# print(feedback("python", "python"))


# secret = random.choice(['casa', 'mere', 'pere'])
# ghicit = input("Ghiceste un cuvant (4 litere): ")
# print(feedback(ghicit, secret))



# 4. COD OTP de verificare (2FA)
# ---------------------------------
# La login pe doua etape primesti un cod de 6 cifre prin SMS. Scrie
# genereaza_otp()  (cod de 6 cifre, cu zerouri in fata daca e nevoie) si
# verifica_otp(introdus, corect)  care confirma daca au fost tastate bine.

# Solutie:
def genereaza_otp():
    return f"{random.randint(0, 999999):06d}"   # mereu 6 cifre: 000123

def verifica_otp(introdus, corect):
    return introdus == corect

# cod = genereaza_otp()
# print("Cod trimis prin SMS:", cod)                  # ex: 048217 (variaza)
# print("Verificare corecta:", verifica_otp(cod, cod))   # True


# 5. CAPTCHA matematic  ("dovedeste ca nu esti robot")
# -------------------------------------------------------
# Inainte de trimiterea formularului ceri un calcul simplu. Scrie
# genereaza_captcha()  care intoarce o intrebare (text) SI raspunsul corect,
# si  verifica_captcha(raspuns, corect)  care confirma.

# Solutie:

def genereaza_captcha():
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    return f"{a} + {b} = ", a + b

rezultat = genereaza_captcha()


def verifica_captcha(raspuns, corect):
    return raspuns == corect

# intrebare, raspuns = genereaza_captcha()
# raspuns = int(input(intrebare))
# print(verifica_captcha(raspuns, raspuns))


# 6. VOTURI ca pe Reddit  (closure + nonlocal)
# ------------------------------------------------
# Fiecare postare are un scor care creste la upvote si scade la downvote.
# Scrie  creeaza_postare()  care intoarce o functie  voteaza(sus=True):
# fiecare apel modifica scorul si il intoarce. `nonlocal` tine minte scorul.

# Solutie:

def creeaza_postare():
    scor =0

    def voteaza(sus=True):
        nonlocal scor
        scor += 1 if sus else -1
        return scor
    return voteaza


print("Varianta 1")
postare = creeaza_postare()
print(postare())
print(postare(False))
print(postare())
print(postare(True))

print('Incepe varianta 2')

punctaj = 0

def creeaza_postare(punctaj, sus=True):
    if sus:
        punctaj += 1
    else:
        punctaj -= 1

    return punctaj

punctaj = creeaza_postare(punctaj)
print(punctaj)  # 1

punctaj = creeaza_postare(punctaj)
print(punctaj)  # 2

punctaj = creeaza_postare(punctaj, False)
print(punctaj)  # 1

punctaj = creeaza_postare(punctaj)
print(punctaj)  # 2