# STRING-URI IN PYTHON
# =============================================================
# Un STRING este o secventa (un sir) de caractere. Este tipul
# de date pe care il folosim pentru a reprezenta TEXT:
# litere, cifre vazute ca text, simboluri, spatii, emoji etc.
# Tipul lui in Python se numeste  str.
# =============================================================


# 1. CREAREA UNUI STRING
# -------------------------------------------------------------
# Putem folosi:
#   - ghilimele simple   '...'
#   - ghilimele duble    "..."
#   - ghilimele triple   '''...'''  sau  """..."""  (multi-linie)

string_simplu = 'Hello'
string_duble = "Hello world!"


# Triple ghilimele -> pastreaza randurile noi exact cum scriem
string_triplu = '''
  Hello world!
  1. Afiseaza text
  2. Afiseaza numere
  3. Afiseaza liste
  '''

string_triplu = """
  Hello world!
  1. Afiseaza text
  2. Afiseaza numere
  3. Afiseaza liste
  """
print(string_triplu)

# Cand alegem ' sau " ?
# Daca textul contine ghilimele duble, folosim simple si invers:

citat = "El a spus:'Python este un limbaj de programare'"
print(citat)



# 2. CARACTERE SPECIALE (escape)
# -------------------------------------------------------------
# Caracterul "\" introduce o secventa speciala:
#   \n  -> rand nou
#   \t  -> tab
#   \\  -> backslash (un singur \)
#   \'  -> apostrof intr-un string cu ghilimele simple
#   \"  -> ghilimele duble intr-un string cu ghilimele duble

print("Hello\nworld!")
print("Coloana1\tColoana2\tColoana3")
print("Cale Windows C:\\Windows\\System32")
print('Text cu \"ghilimele duble\"')



# 3. STRING-URILE SUNT IMUTABILE
# -------------------------------------------------------------
# Odata creat, un string NU mai poate fi modificat la o pozitie.
# Putem doar sa cream un STRING NOU pe baza celui vechi.

nume = 'Java'
# nume[0] = 'P'  # TypeError: nu se poate


# 4. CONCATENARE, REPETARE SI LUNGIME
# -------------------------------------------------------------
# +   uneste doua string-uri
# *   repeta un string de N ori
# len() returneaza numarul de caractere

a = 'Hello'
b = ' world!'
c = a + b # concatenare, alipire
print(c)

linie = '-' * 20
print(linie)

mesaj = "Astazi invatam python"
print(len(mesaj))

# Atentie: NU putem concatena string + numar fara conversie:
varsta = str(30)
print("Am " + varsta + " ani")


# 5. INDEXARE
# -------------------------------------------------------------
# Fiecare caracter are un INDEX. Indexarea incepe de la 0.
# Indecsi NEGATIVI numara de la sfarsit (-1 = ultimul caracter).
#
#  text:    P  y  t  h  o  n
#  index:   0  1  2  3  4  5
#  index:  -6 -5 -4 -3 -2 -1

text = 'Python'
print(text[0])    #P
print(text[5])    #n
print(text[-1])   #n (ultimul)
print(text[-2])   #o (penultimul)



# 6. SLICING  [start:stop:step]
# -------------------------------------------------------------
# Extrage o BUCATA dintr-un string.
#   - start  = de unde incepem (inclusiv)   - default 0
#   - stop   = unde ne oprim (EXCLUSIV)     - default lungimea
#   - step   = pasul                        - default 1
#
# Regula importanta: stop-ul NU este inclus.

s = "Programare"
print(s[0:4])  #Prog
print(s[:4])   #Prog
print(s[4:])   #ramare
print(s[:])    #Programare
print(s[::2])  #Pormr  (din 2 in 2)
print(s[1:5:3])#rr

# 7. VERIFICAREA CONTINUTULUI: in / not in
# -------------------------------------------------------------
email = 'ana@gmail.com'
print('@' in email)
print('yahoo' not in email)


# 8. METODE PENTRU LITERE MARI / MICI
# -------------------------------------------------------------
text = "Python ESTE cool!"
print(text.lower())      # scris cu minuscule
print(text.upper())      # scris cu majuscule
print(text.title())      # prima litera din fiecare cuvant
print(text.capitalize()) # primt litera scris cu majuscula

# 9. CURATARE SPATII (whitespace)
# -------------------------------------------------------------
mesaj = "   Salutare!  "
print(mesaj.strip())    # sterge la inceput si final spatiile
print(mesaj.lstrip())   # sterge doar la inceput
print(mesaj.rstrip())   # sterge doar la sfarsit


# 10. SPLIT si JOIN
# -------------------------------------------------------------
# split()  -> dintr-un STRING obtinem o LISTA de bucati
# join()   -> dintr-o LISTA obtinem un STRING

mesaj = "Imi place sa invat Python"
cuvinte = mesaj.split()   # separatorul default este spatiu
print(cuvinte)

masini = ["BMW", "Audi", "Mercedes"]
text = ", ".join(masini)
print(text)

# 11. INLOCUIRE: replace()
# -------------------------------------------------------------
text = "Python este un limbaj de programare"
print(text.replace('i', 'y'))


# 12. CAUTARE: find() si count()
# -------------------------------------------------------------
# find()  -> indexul primei aparitii (sau -1 daca nu gaseste)
# count() -> de cate ori apare un substring


text = "Invata Python. Python este simplu"
print(text.find('Python')) # 7
print(text.count('Python'))# 2

# 13. METODE DE VERIFICARE (returneaza True / False)
# -------------------------------------------------------------
text = '1234'.isdigit()  # True -> sunt doar cifre
text = 'Python'.isalpha()# True -> sunt doar litere


# 14. STARTSWITH / ENDSWITH
# -------------------------------------------------------------

fisier = 'raport_2026.pdf'
print(fisier.endswith('.pdf'))   # True
print(fisier.startswith('raport')) # True


# 15. FORMATAREA STRING-URILOR
# -------------------------------------------------------------
# Avem 3 modalitati moderne:
#   a) concatenare cu virgula in print() - pentru cazuri simple
#   b) metoda .format()
#   c) f-string  (RECOMANDAT - cel mai citibil)

nume = 'George'
an = 1990

# (a) print cu virgula
print(nume, 's-a nascut in anul', an)

# (b) .format()

print("{} s-a nascut in anul {}".format(nume, an))

# (c) f-string


print(f"{nume} s-a nascut in anul {an}.")
# In f-string putem pune si EXPRESII intre acolade:

# =============================================================
# CONCLUZIE
# =============================================================
# String-urile sunt unul dintre cele mai des folosite tipuri de date.
# Retine: sunt IMUTABILE, indexate de la 0, si au o multime de
# metode utile (.lower, .upper, .strip, .split, .join, .replace,
# .find, .count, .startswith, .endswith).
# Folosim f-string pentru orice mesaj construit dinamic.
# =============================================================