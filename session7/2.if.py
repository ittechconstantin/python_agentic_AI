# INSTRUCTIUNEA  if  IN PYTHON
# =============================================================
# Pana acum codul nostru a fost LINIAR: rulam fiecare linie,
# in ordine, mereu.
# `if` ne permite sa LUAM DECIZII: sa rulam un bloc de cod
# DOAR cand o conditie este adevarata. Asa apare logica reala
# in programe: validari, alegeri, fluxuri diferite.
#
# Cand folosim `if`?
#   - validari de input (email valid? parola destul de lunga?)
#   - drepturi de acces (e admin? are voie?)
#   - status code-uri HTTP (200 -> ok, 404 -> nu exista, 500 -> eroare)
#   - reactii la erori (daca lipseste cheia, foloseste un default)
#   - praguri (daca pretul > 100 lei -> aplica reducere)
# =============================================================


# 1. SINTAXA DE BAZA
# -------------------------------------------------------------
# Forma:
#   if conditie:
#       <bloc - se executa daca conditia este True>
#
# Reguli importante:
#   - dupa  if  vine o EXPRESIE care da True / False
#   - dupa expresie pune  :   (doua puncte)
#   - blocul de sub if este INDENTAT cu 4 spatii (sau 1 tab)
#   - cand iesim din indentare, am iesit din if

varsta = 19

if varsta >= 18:
    print("Esti major")  # se executa -> 19 >= 18 este True

print("Sfarsit program") # se executa intodeauna(neindentat)

# 2. INDENTAREA - DE CE CONTEAZA
# -------------------------------------------------------------
# Python NU foloseste { } pentru a marca un bloc de cod.
# Foloseste INDENTAREA. Daca scrii "in afara" indentarii,
# linia ta NU mai face parte din if.

scor = 90
if scor >= 80:
    print("Aprobat")
    print("Bine!")

print("Sfarsit program")


# 3. if / else
# -------------------------------------------------------------
# Forma:
#   if conditie:
#       ... (cand True)
#   else:
#       ... (cand False)
# Exact UNA din cele doua ramuri se executa.

nota = 4
if nota >= 8:
    print("Aprobat")
else:
    print("Picat")

# 4. if / elif / else  (lant de decizii)
# -------------------------------------------------------------
# elif = "altfel daca". Putem inlantui cate vrem.
# Python OPRESTE cautarea la PRIMA conditie adevarata.

cod_http = 404

if cod_http == 200:
    print("ok- cerere reusita")
elif cod_http == 404:
    print("not found- pagina nu a fost gasita")
elif cod_http == 500:
    print("eroare server")
else:
    print("cod invalid")


# 6. CONDITII INLANTUITE vs CONDITII IMBRICATE
# -------------------------------------------------------------
# Cand avem nevoie sa verificam MAI MULTE conditii deodata:
# preferam  and / or  in loc de if-uri imbricate.
# E mai citibil si mai scurt.

# Stil incorect (imbricat fara motiv):
varsta = 20
are_permis = True

if varsta >= 18:
    if are_permis:
        print("Este major si are permis")

# Stil mai bun

if varsta >= 18 and are_permis :
    print("Este major si are permis")


# 7. EXPRESII "ADEVARATE" SI "FALSE" - TRUTHINESS
# -------------------------------------------------------------
# In Python, in interiorul unui  if  putem pune ORICE expresie.
# Python o converteste automat la True / False urmand reguli simple:
#
#   FALSE -> 0, 0.0, "", [], (), {}, set(), None
#   TRUE  -> orice altceva (numere ne-zero, string-uri ne-goale,
#                           liste cu cel putin un element, etc.)


if "":                       # string gol -> False
    print('nu se afiseaza')

if 'python':                 # string ne-gol -> True
    print("afisat")

if []:                       # lista gol -> False
    print("nu se afiseaza")

if 0:                        # numar 0 -> False
    print("nu se afiseaza")

if 1:                        # numar 1 -> True
    print("afisat")


# 8. EXPRESIA TERNARA  -  if pe o singura linie
# -------------------------------------------------------------
# Forma:
#   <valoare_daca_True>  if  <conditie>  else  <valoare_daca_False>
# Foarte utila cand vrem sa atribuim o valoare in functie de o conditie.
scor = 75

# TERNARA
status = "promovat" if scor >= 80 else "nepromovat"
print(status)

# Varianta clasica
status = "nepromovat"
if scor >= 80:
    status = "promovat"
print(status)


# 9. if cu in / not in - validari simple
# -------------------------------------------------------------
permisiuni = ["read", "write", "execute"]

if "read" in permisiuni:
    print("Ai permisiunea de stergere")

if "delete" not in permisiuni:
    print("Nu ai permisiunea de stergere")

# 10. ATENTIE LA  =  vs  ==
# -------------------------------------------------------------
#   =   este ATRIBUIRE   (pune o valoare intr-o variabila)
#   ==  este COMPARARE   (verifica egalitatea)
# In  if  folosim INTOTDEAUNA  ==.

x = 5
if x == 5:
    print("x este 5")

# 11. if cu None  -  folosim  is / is not
# -------------------------------------------------------------
# Convetia Python pentru None, True, False:  folosim  is / is not.

valoare = None

if valoare is None:
    print("valoare este None")
else:
    print("valoare NU este None")

# =============================================================
# CONCLUZIE
# =============================================================
# `if` ne permite sa luam decizii in cod.
#
# Sintaxa esentiala:
#     if  conditie:
#         ...
#     elif conditie:
#         ...
#     else:
#         ...
#
# - Indentarea defineste blocul (4 spatii).
# - Conditia este o expresie care da True / False (sau e
#   convertita automat - "truthiness").
# - Folosim  ==  pentru comparare,  is / is not  cu None.
# - Combinam conditii cu  and / or / not.
# - Expresia ternara:    A  if  cond  else  B
# - if + dict + in / not in + .get() = combinatie super utila
#   pentru validari si default-uri.
# =============================================================