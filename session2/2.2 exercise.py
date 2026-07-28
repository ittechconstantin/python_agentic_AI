# EXERCITII STRING
# =============================================================
# Combina mai multe metode si slicing pentru rezultate utile.
# Ai voie sa folosesti DOAR ce am invatat pana acum.
# =============================================================
from operator import concat

# 1. Inversare string
# -------------------
# Pleaca de la  cuvant = "Programare".
# Afiseaza-l INVERSAT folosind slicing  [::-1].

# Solutie:
print("\n--- Exercitiul 1 ---")
cuvant = "Programare"
print(cuvant[::-1])

# 2. Verificare palindrom
# -----------------------
# Un palindrom este un cuvant care se citeste la fel
# si invers (ex: "ana", "cojoc").
# Avem  cuvant = "ana".
# Afiseaza  True  daca este palindrom (cuvant == cuvant inversat),
# fara if, doar cu o expresie booleana.

# Solutie:

print("\n--- Exercitiul 2 ---")
cuvant = "ana"
print(cuvant == cuvant[::-1])

# 3. Initialele unei persoane
# ---------------------------
# Avem  nume_complet = "horia daniel scurtu".
# Foloseste .split() si indexare pentru a construi initialele
# in formatul:  "H.D.S."
# (sugestie: ia primul caracter al fiecarui cuvant, .upper(),
#  apoi pune-le impreuna cu un "." intre)

# Solutie:

print("\n--- Exercitiul 3 ---")
nume_complet = "horia daniel scurtu"
cuvinte = nume_complet.split()
# print(cuvinte)
initiale = cuvinte[0][0] + "." + cuvinte[1][0] + "." + cuvinte[2][0] + "."
print(initiale.upper())

# 4. Extragere domeniu email
# --------------------------
# Avem  email = "ana.popescu@gmail.com".
# Foloseste .find() si slicing pentru a extrage doar domeniul
# (ex: "gmail.com"). Afiseaza rezultatul.

# Solutie:

print("\n--- Exercitiul 4 ---")
email = "ana.popescu@gmail.com"
arond = email.find("@")
print(arond)
terminatie = email[arond + 1:]
print(terminatie)

# 5. Numar de vocale
# ------------------
# Numara cate vocale (a, e, i, o, u) sunt in textul:
#   "Programarea in Python este distractiva"
# Sugestie: foloseste .lower() ca sa nu te incurci cu majuscule
# si aduna count() pentru fiecare vocala.

# Solutie:

print("\n--- Exercitiul 5 ---")
text = "Programarea in Python este distractiva"
text_nou = text.lower()
# print(text_nou)
vocale = text_nou.count("a") + text_nou.count("e") + text_nou.count("i") + text_nou.count("o") + text_nou.count("u")
print(vocale)

# 6. Cuvinte cu majuscula
# -----------------------
# Avem propozitia:  "salut, eu sunt ana si invat python"
# Transform-o astfel incat fiecare cuvant sa inceapa cu majuscula.
# (sugestie: foloseste .title())

# Solutie:

print("\n--- Exercitiul 6 ---")
propozitia = "salut, eu sunt ana si invat python"
print(propozitia.title())

# 7. Curatare si normalizare nume
# -------------------------------
# Avem  intrare = "   ANA-MARIA   POPESCU   "
# Vrem sa obtinem string-ul "Ana-Maria Popescu":
#   - fara spatii la inceput / sfarsit
#   - prima litera a fiecarui cuvant majuscula, restul mici
# Afiseaza rezultatul.

# Solutie:

print("\n--- Exercitiul 7 ---")
intrare = "   ANA-MARIA   POPESCU   "
text_intrare = intrare.strip().title()
# print(text_intrare)
text_final = text_intrare.replace("   ", " ")
print(text_final)

# 8. Mascarea unui numar de card
# ------------------------------
# Avem  card = "1234567812345678".
# Vrem sa afisam doar ultimele 4 cifre, restul inlocuite cu *.
# Format dorit:  "************5678"
# Foloseste slicing si concatenare cu * .

# Solutie:

print("\n--- Exercitiul 8 ---")
card = "1234567812345678"
cuvant_nou = "*"  + (len(card) - 4) + card[-4:]
print(cuvant_nou)


# 9. Verificare format email simpla
# ---------------------------------
# Avem  email = "ana@gmail.com".
# Construieste o expresie booleana care returneaza True daca:
#   - email-ul contine "@"
#   - SI se termina cu ".com"
#   - SI are mai mult de 5 caractere
# Afiseaza rezultatul.

# Solutie:

print("\n--- Exercitiul 9 ---")
email = "ana@gmail.com"
print("@" in email and email.endswith(".com") and len(email) > 5)

# 10. Bon fiscal cu f-string si aliniere
# --------------------------------------
# Avem:
#   produs1 = "Paine"; pret1 = 4.5
#   produs2 = "Lapte"; pret2 = 7.99
#   produs3 = "Cafea"; pret3 = 23.0
# Afiseaza sub forma de bon (folosind alinierea f-string-urilor),
# astfel incat numele produsului sa aiba 15 caractere si pretul
# sa fie aliniat la dreapta cu 8 caractere si 2 zecimale:
#   f"{produs1:<15}{pret1:>8.2f}"
# La final, afiseaza si totalul.

# Solutie:

print("\n--- Exercitiul 10 ---")
produs1 = "Paine"; pret1 = 4.5
produs2 = "Lapte"; pret2 = 7.99
produs3 = "Cafea"; pret3 = 23.0

Totalul = pret1 + pret2 + pret3

print(f"{produs1:<15}{pret1:>8.2f}")
print(f"{produs2:<15}{pret2:>8.2f}")
print(f"{produs3:<15}{pret3:>8.2f}")
print(f"{"Totalul":<15}{Totalul:>8.2f}")

# 11. Extragere extensie fisier
# -----------------------------
# Avem  fisier = "raport_anual_2026.pdf".
# Foloseste .find() (sau .rfind()) si slicing pentru a extrage
# doar extensia: "pdf". Afiseaza rezultatul.

# Solutie:

print("\n--- Exercitiul 11 ---")
fisier = "raport_anual_2026.pdf"
pozitie = fisier.find(".")
cuvantul_final = fisier[pozitie + 1:]
print(cuvantul_final)

# 12. Construire URL slug
# -----------------------
# Avem un titlu:  titlu = "Invata Python in 30 de Zile"
# Vrem sa construim un slug pentru URL: "invata-python-in-30-de-zile"
# Pasi:
#   - .lower()
#   - .replace(" ", "-")
# Afiseaza rezultatul.

# Solutie:

print("\n--- Exercitiul 12 ---")
titlu = "Invata Python in 30 de Zile"
titlu_final = titlu.lower().replace(" ", "-")
print(titlu_final)

# 13. Numarare cuvinte
# --------------------
# Avem  paragraf = "Python este simplu. Python este puternic. Python este peste tot."
# Calculeaza si afiseaza:
#   - cate cuvinte sunt in total (foloseste .split() si len())
#   - de cate ori apare cuvantul "Python"

# Solutie:

print("\n--- Exercitiul 13 ---")
paragraf = "Python este simplu. Python este puternic. Python este peste tot."
cuvinte = paragraf.split()
print(len(cuvinte))
print(cuvinte.count("Python"))

# 14. Inlocuiri multiple in lant
# ------------------------------
# Pleaca de la  text = "Imi place Java si Java este cool".
# Inlantuie .replace() astfel incat sa obtii:
#   "Imi place Python si Python este foarte cool"
# (doua replace-uri lipite unul de altul)

# Solutie:

print("\n--- Exercitiul 14 ---")
text = "Imi place Java si Java este cool"
print(text.replace("Java", "Python").replace("este", "este foarte"))

# 15. Capitalizare propozitie cu spatii in plus
# ---------------------------------------------
# Pleaca de la  intrare = "   buna     ziua,    cum esti?   "
# Vrem la final:  "Buna ziua, cum esti?"
#   - elimina spatiile de la capete (.strip())
#   - elimina spatiile multiple dintre cuvinte
#     (sugestie: foloseste .split() FARA argument - elimina automat
#      spatiile multiple, apoi .join cu un singur spatiu)
#   - capitalizeaza prima litera (.capitalize())
# Afiseaza rezultatul.

# Solutie:

print("\n--- Exercitiul 15 ---")
intrare = "   buna     ziua,    cum esti?   "
intrare = intrare.strip().split()
intrare_noua = " ".join(intrare)
print(intrare_noua.capitalize())