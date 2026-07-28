# EXERCITII OPERATORI
# =============================================================
# Combina mai multi operatori, conversii si formatari
# pentru a rezolva mici probleme reale.
# =============================================================
from bisect import bisect
from operator import and_

# 1. Media a trei note
# --------------------
# Ai notele: nota1 = 8, nota2 = 9, nota3 = 7.
# Calculeaza media aritmetica si afiseaza-o cu f-string,
# in formatul:  "Media este: 8.0"

# Solutie:

print("\n--- Exercitiul 1 ---")
nota1 = 8
nota2 = 9
nota3 = 7

media = (nota1 + nota2 + nota3) / 3
print(f"Media este: {media}")

# 2. Pretul cu TVA si discount
# ----------------------------
# Pret produs:    pret = 250 (lei)
# TVA:            21 %
# Discount:       10 %
# Calculeaza pretul final dupa aplicarea TVA, iar apoi
# a discountului. Afiseaza rezultatul.

# Solutie:

print("\n--- Exercitiul 2 ---")
pret = 250
pret_cu_TVA = pret * 1.21
print(pret_cu_TVA)
Discount = pret * 0.1
print(Discount)
pret_cu_discount = pret_cu_TVA - Discount
print(pret_cu_discount)

# 3. Conversie de timp
# --------------------
# Ai un total de  total_secunde = 7384.
# Calculeaza cate ORE, MINUTE si SECUNDE reprezinta
# (foloseste // si %) si afiseaza in formatul "2h 3m 4s".

# Solutie:

print("\n--- Exercitiul 3 ---")
total_secunde = 7384
minute = total_secunde // 60
ore = minute // 60
secunde = total_secunde % 60

print(f"{ore}h {minute}m {secunde}s")

# 4. Conversie temperatura
# ------------------------
# Avem  celsius = 36.6.
# Aplica formula:  F = C * 9/5 + 32
# Afiseaza rezultatul cu un text descriptiv.

# Solutie:

print("\n--- Exercitiul 4 ---")
C = 36.6
F = C * 9 / 5 + 32
print(f"Daca temperatura in grade Celsius este de {C}, atunci inseamna ca temperatura in grade Fahrenheit este de {F}.")

# 5. An bisect
# ------------
# Ai variabila  an = 2024.
# Un an este bisect daca:
#   (este divizibil cu 4 SI nu este divizibil cu 100)
#   SAU este divizibil cu 400.
# Afiseaza rezultatul (True / False) folosind doar
# operatori (fara if).

# Solutie:

print("\n--- Exercitiul 5 ---")
an = 2024
if an % 4 == 0 and an % 100 != 0 or an % 400 == 0:
    print("True")
else:
    print("False")
    #Aici am folosit if deoarce am invatat deja functia, plus ca e mai usor cu if :)

# 6. Verificare interval
# ----------------------
# Avem  varsta = 27.
# Verifica daca varsta este in intervalul [18, 65]
# (inclusiv ambele capete) folosind operatori logici.
# Afiseaza rezultatul.

# Solutie:

print("\n--- Exercitiul 6 ---")
varsta = 27
interval = [18, 65]
print(varsta>=interval[0] and varsta<=interval[1])

# 7. Distanta dintre doua puncte
# ------------------------------
# Avem doua puncte:  (x1, y1) = (1, 2)  si  (x2, y2) = (4, 6).
# Calculeaza distanta dintre ele cu formula:
#   d = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
# Afiseaza rezultatul.

# Solutie:

print("\n--- Exercitiul 7 ---")
(x1, y1) = (1, 2)
(x2, y2) = (4, 6)
d = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
print(d)

# 8. Calcul BMI
# -------------
# Greutatea: kg = 78,    Inaltimea: m = 1.80
# Calculeaza indicele de masa corporala:  BMI = kg / (m ** 2)
# Afiseaza valoarea cu 2 zecimale folosind f-string:
#   f"{bmi:.2f}"

# Solutie:

print("\n--- Exercitiul 8 ---")
kg = 78
m = 1.80
BMI = kg / (m ** 2)
print(f"X are indicele BMI de {BMI:.2f}")

# 9. Pret pe produs
# -----------------
# La un magazin am cumparat 7 produse cu un cost total
# de 152 lei. Calculeaza pretul mediu pe produs (float)
# si afiseaza-l cu 2 zecimale.

# Solutie:

print("\n--- Exercitiul 9 ---")
total_produse = 7
total_cost = 152
pretul_mediu = total_cost / total_produse
print(f"Pretul mediu pe produs este de {pretul_mediu:.2f}")

# 10. Cifra unitatilor si zecilor
# -------------------------------
# Avem  numar = 4729.
# Foloseste % si // pentru a obtine:
#   - cifra unitatilor (ex: 9)
#   - cifra zecilor    (ex: 2)
#   - cifra sutelor    (ex: 7)
# Afiseaza fiecare valoare.

# Solutie:

print("\n--- Exercitiul 10 ---")
numar = 4729
print(numar % 10)
cifra_zecilor = numar % 100
print(cifra_zecilor // 10)
cifra_sutelor = numar // 100
print(cifra_sutelor % 10)

# 11. Aplicare succesiva de reduceri
# ----------------------------------
# Pret = 1000 lei. Aplica 3 reduceri succesive de 10%, 5%, 8%.
# Foloseste operatorul *= pentru a obtine pretul final.
# Afiseaza valoarea cu 2 zecimale.

# Solutie:

print("\n--- Exercitiul 11 ---")
pret = 1000
pret *= 0.90
pret *= 0.95
pret *= 0.92
print(f"Pretul final este de {pret:.2f}")

# 12. Cont bancar simplu
# ----------------------
# Pleaca de la  sold = 0.
# Realizeaza operatiile:
#   - depunere de 500
#   - retragere de 120
#   - depunere de 300
#   - dobanda de 2% (sold *= 1.02)
# Foloseste operatorii compusi (+=, -=, *=) si afiseaza soldul final
# cu 2 zecimale folosind f-string.

# Solutie:

print("\n--- Exercitiul 12 ---")
sold = 0
sold += 500
sold -= 120
sold += 300
sold *= 1.02
print(f"Soldul final este de {sold:.2f}")