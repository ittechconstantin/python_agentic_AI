# Ce este o variabila?
# --------------------
# O variabila este un nume asociat unei locatii din memorie, in care se stocheaza o valoare.

# Practic, o variabila retine date pe care le putem folosi, modifica sau afisa ulterior.
# In Python, variabilele se creeaza automat in momentul in care li se atribuie o valoare.
# Tipul este determinat dinamic – nu este nevoie sa il declaram explicit.


# 1. Atribuire directa
# --------------------
# Atribuim o valoare unei variabile folosind operatorul "=".

nume = 'Horia'
varsta = 30
print(nume)
print(varsta)

# 2. Atribuire multipla (pe aceeasi linie)
# ----------------------------------------
# Putem atribui mai multe valori mai multor variabile in aceeasi instructiune.

numar1, numar2, numar3 = 1, 2, 3

print(numar2)

# 3. Atribuire in cascada
# -----------------------
# Putem atribui aceeasi valoare mai multor variabile simultan.

x = y = z = 10

print(x, y, z)


# 4. Reguli si conventii pentru denumirea variabilelor
# ----------------------------------------------------

# Denumiri corecte (legale)
total = 10           # Numele poate contine o denumire relevanta cu valoarea stocata
variabila1 = 100     # Numele variabilei poate contine cifre dar acestea sa fie mentionate la final
_variabila = 200     # Numele variabilei poate sa contina UNDERLINE la inceput.
TOTAL = 100          # Numele poate contine o denumire relevanta cu valoarea stocata, dar in majuscule
variabila_mea = 400  # SNAKE CASE - Numele variabilei poate fi despartit prin UNDERLINE
myVariableName = 500 # CAMEL CASE - Numele variabilei incepe cu litera mica iar celelate denumire incep cu litera majuscula
MyVariableName = 600 # PASCAL CASE -Numele variabilei incepe cu majuscula iar celelate cuvinte din numele variabilei vor incepe cu majuscula

print(total, TOTAL)

# Denumiri incorecte (ilegale)
# variabila mea = 100
# 5variabila = 200
# variabila-mea = 300
# if = 10


# 5. Recomandari pentru nume de variabile (stil Pythonic)
# -------------------------------------------------------

# - Foloseste nume semnificative si clare.
# - Foloseste litere mici si underscore intre cuvinte: exemplu "user_email".
# - Evita nume generice precum a, b, c sau data1, result2.
# - Nu folosi denumiri care coincid cu functii sau tipuri interne (ex: list, str, dict).
# - Urmeaza conventia PEP 8 pentru consistenta si lizibilitate.


# 6. Verificarea tipului unei variabile
# -------------------------------------
# Cu functia type() putem afla tipul unei variabile.

name = 'Horia'
age = 30
print(type(name))
print(type(age))



# 7. Schimbarea valorii unei variabile
# ------------------------------------
# O variabila poate fi suprascrisa in orice moment.

year = 2025
year = 2026
print(year)


# 8. Atribuire bazata pe expresii
# -------------------------------
# O variabila poate primi valoarea unei expresii sau a altor variabile.


suma = 10 + 20
result = 10 > 20
print(result)