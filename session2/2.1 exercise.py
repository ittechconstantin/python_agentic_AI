# EXERCITII STRING
# =============================================================
# Foloseste DOAR ce am invatat: variabile, tipuri,
# print(), operatori si tot ce e in 2.string.py.
# =============================================================


# 1. Nume complet
# ---------------
# Ai variabilele:
#   prenume = "Horia"
#   nume    = "Scurtu"
# Creeaza o variabila `nume_complet` care le concateneaza cu
# un spatiu intre ele si afiseaz-o.

# Solutie:

print("\n--- Exercitiul 1 ---")
prenume = "Horia"
nume    = "Scurtu"
nume_complet = nume + " " + prenume
print(nume_complet)

# 2. Repetare mesaj
# -----------------
# Folosind operatorul *, afiseaza de 5 ori textul "Bun venit! ".

# Solutie:

print("\n--- Exercitiul 2 ---")
linie = "Bun venit! " * 5
print(linie)

# 3. Lungimea unui mesaj
# ----------------------
# Calculeaza si afiseaza numarul de caractere din:
#   "Astazi invatam string-uri in Python!"

# Solutie:

print("\n--- Exercitiul 3 ---")
mesaj = "Astazi invatam string-uri in Python!"
print(len(mesaj))

# 4. Litere mari si mici
# ----------------------
# Avem  text = "Python Este Un Limbaj De Programare".
# Afiseaza:
#   - varianta cu TOATE LITERELE MARI
#   - varianta cu toate literele mici
#   - varianta cu prima litera majuscula, restul mici

# Solutie:

print("\n--- Exercitiul 4 ---")
text = "Python Este Un Limbaj De Programare"
print(text.upper())
print(text.lower())
print(text.capitalize())

# 5. Eliminare spatii
# -------------------
# Curata textul:  "    informatii despre factura   "
# de spatiile de la inceput si sfarsit si afiseaza-l.

# Solutie:

print("\n--- Exercitiul 5 ---")
textul =  "    informatii despre factura   "
print(textul.strip())

# 6. Impartire in cuvinte
# -----------------------
# Foloseste .split() pe textul:
#   "Imi place sa invat Python pentru ca este simplu"
# Afiseaza lista rezultata si lungimea ei.

# Solutie:

print("\n--- Exercitiul 6 ---")
textul_dat = "Imi place sa invat Python pentru ca este simplu"
print(textul_dat.split())

# 7. Unire cuvinte intr-un text
# -----------------------------
# Avem o lista:
#   limbaje = ["Python", "Java", "GO", "PHP", "Rust"]
# Foloseste .join() ca sa obtii un singur string in care
# limbajele sunt separate prin ", ". Afiseaza rezultatul.

# Solutie:

print("\n--- Exercitiul 7 ---")
limbaje = ["Python", "Java", "GO", "PHP", "Rust"]
solutia = ", ".join(limbaje)
print(solutia)

# 8. Inlocuire cuvant
# -------------------
# Pleaca de la textul:  "Imi place Java foarte mult"
# Inlocuieste "Java" cu "Python" si afiseaza rezultatul.

# Solutie:

print("\n--- Exercitiul 8 ---")
textul = "Imi place Java foarte mult"
noul_text = textul.replace("Java", "Python")
print(noul_text)

# 9. Slicing - primele si ultimele caractere
# ------------------------------------------
# Avem  cuvant = "Programare".
# Afiseaza:
#   - primele 4 caractere
#   - ultimele 4 caractere
#   - de la al 3-lea caracter pana la sfarsit

# Solutie:

print("\n--- Exercitiul 9 ---")
cuvant = "Programare"
print(cuvant[:4])
print(cuvant[-4:])
print(cuvant[2:])

# 10. Verificare continut cu  in
# ------------------------------
# Avem  email = "popescu.maria@gmail.com".
# Afiseaza True / False pentru:
#   - contine "@"
#   - se termina in ".com"   (foloseste .endswith)
#   - contine "yahoo"

# Solutie:

print("\n--- Exercitiul 10 ---")
email = "popescu.maria@gmail.com"
print("@" in email)
print(email.endswith(".com"))
print("yahoo" in email)

# 11. Formatare cu f-string
# -------------------------
# Avem:  nr_comanda = 123456,  client = "Maria",  total = 249.5
# Construieste si afiseaza un mesaj de forma:
#   "Comanda #123456 a clientului Maria are valoarea 249.50 lei"
# (foloseste {total:.2f} pentru cele 2 zecimale)

# Solutie:

print("\n--- Exercitiul 11 ---")
nr_comanda = 123456
client = "Maria"
total = 249.5
print(f"Comanda #{nr_comanda} a clientului {client} are valoarea de {total:.2f} lei")

# 12. Numarare aparitii
# ---------------------
# Avem  text = "banana".
# Calculeaza si afiseaza de cate ori apare litera "a".

# Solutie:

print("\n--- Exercitiul 12 ---")
text = "banana"
print(text.count("a"))