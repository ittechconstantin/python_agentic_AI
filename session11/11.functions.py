# FUNCTII IN PYTHON  (def)
# =============================================================
# O FUNCTIE este o "bucata de cod cu nume". O scrii O DATA,
# si o poti folosi DE OAREORI in tot programul, doar prin
# numele ei.
#
# De ce avem nevoie de functii?
#   - DRY (Don't Repeat Yourself) - nu rescriem aceeasi logica
#   - Citire usoara - codul devine "vorbit": calculeaza_taxa(),
#     valideaza_email(), trimite_notificare()
#   - Testare si depanare mai usoara
#   - Refolosire intre proiecte
#
# Functii pe care le-am folosit deja, fara sa le numim asa:
#   - print(), len(), sum(), max(), min(), sorted(), int(), str()
#   - .append(), .upper(), .split() (sunt METODE = functii pe obiecte)
# Acum invatam sa ne SCRIEM PROPRIILE noastre functii.
# =============================================================


# 1. SINTAXA DE BAZA
# -------------------------------------------------------------
# Forma:
#   def nume_functie(parametri):
#       <bloc indentat - corpul functiei>
#       return <valoare>          # OPTIONAL
#
# - cuvantul cheie  def  porneste DEFINIREA
# - nume_functie:    folosim litere mici si _ (snake_case)
# - parametri:       valori "intrate" pe care le primeste
# - return:          valoarea pe care o "returneaza" (trimite inapoi)

def saluta():
    print('Salut!')

# Pana aici am DEFINIT functia. Ea NU s-a executat inca.
# O APELAM (chemam) folosind numele si ( ):

saluta()             # afiseaza Salut!
saluta()             # putem chema functia de cate ori avem nevoie


# 2. FUNCTIE CU UN PARAMETRU
# -------------------------------------------------------------
# Parametrii sunt "variabile speciale" care primesc valori
# de la cel ce APELEAZA functia.

def saluta_pe(nume):
    print(f"Salut, {nume}!")


saluta_pe('Ana')        # Salut, Ana!
saluta_pe('George')     # Salut, George!


# Argumentul "Ana" se pune in parametrul `nume` cand se ruleaza functia.


# 3. FUNCTIE CU MAI MULTI PARAMETRI
# -------------------------------------------------------------
# Parametrii se separa prin virgula.

def profil(nume, varsta, rol):
    print(f"Nume: {nume}, Varsta: {varsta}, Rol: {rol}")

# Varianta 1
profil('Ana', 28, 'admin')
profil('George', 30, 'user')
profil('Vlad', 28, 'admin')

# Varianta 2
# name = input("Introduceti numele: ")
# age = int(input("Introduceti varsta: "))
# role = input("Introduceti rolul:")
# profil(name, age, role)

# Varianta 3
# Solicitam date dintr-o tabela cu angajati si pentru fiecare angajat apelam functia profil dandu-i valori pentru nume, varsta si rol


# Varianta 4
# Sa afisez profilul pentru 3 angajati introdusi de la tastatura
# nr_angajati = int(input("Cate angajati vreti sa introduceti? "))
#
# for i in range(nr_angajati):
#     name = input("Introduceti numele: ")
#     age = int(input("Introduceti varsta: "))
#     role = input("Introduceti rolul:")
#     profil(name, age, role)


# 4. RETURN  -  cum trimitem o valoare INAPOI
# -------------------------------------------------------------
# `print()` afiseaza, `return` ofera o VALOARE pe care o putem
# folosi mai departe (in alte calcule, atribuiri etc.).

def aduna(a, b):
    return a + b


rezultat = aduna(3, 5)
print(rezultat)

# 5. DIFERENTA  print  vs  return
# -------------------------------------------------------------
# print():    afiseaza pe ecran si NU intoarce nimic util
# return:     nu afiseaza, dar ne da inapoi o VALOARE



# 6. RETURN  fara valoare  -  echivalent cu  return None
# -------------------------------------------------------------
# Daca o functie nu are return explicit, returneaza implicit None.


def text():
    print("Imi place python")

x = text()
print(x)


# 7. RETURN  oprește executia functiei
# -------------------------------------------------------------
# Linia care urmeaza dupa un return executat NU se mai executa.


def este_par(n):
    if n % 2 == 0:
        return True     # iesim imediat din functie
    return False        # se executa doar daca conditia de mai sus este false

print(este_par(10))
print(este_par(11))

# 8. PARAMETRI CU VALORI IMPLICITE  (default)
# -------------------------------------------------------------
# Putem da o valoare DEFAULT pentru un parametru. Daca apelantul
# nu trimite nimic, se foloseste valoarea implicita.


def saluta(nume, mesaj='Salut!'):
    print(f"{mesaj}, {nume}!")

saluta('Ana')     # Salut, Ana!
saluta('George', 'Buna ziua') # Buna ziua, George!



# REGULA: parametrii cu default trebuie pusi DUPA cei fara default.
# def f(a, b=10, c):  # GRESIT
# def f(a, c, b=10):  # CORECT


# 9. ARGUMENTE POZITIONALE  vs  KEYWORD
# -------------------------------------------------------------
# La APEL, putem trimite argumentele:
#   - POZITIONAL    -  in ordinea parametrilor:  saluta("Ana", "Hi")
#   - KEYWORD       -  cu numele parametrului:    saluta(nume="Ana", mesaj="Hi")
# Stilul keyword este mai citibil cand sunt multi parametri.
saluta('George', 'Buna ziua')
saluta(mesaj="Salut", nume="Ana")


# 10. RETURN MULTIPLE VALUES  (de fapt, un tuplu)
# -------------------------------------------------------------
# `return a, b` returneaza UN TUPLU (a, b). Apelantul poate
# despacheta tuplul cu unpacking.

def min_max(a, b):
    return min(a, b), max(a, b)

m, M = min_max(3, 10)
print(m)
print(M)

# 11. FUNCTII CARE CHEAMA ALTE FUNCTII
# -------------------------------------------------------------
# Asa construim programe complexe: din "caramizi" mici si simple.

def aria_dreptunghi(lungime, latime):
    return lungime * latime

def perimetru_dreptunghi(lungime, latime):
    return 2 * (lungime + latime)

def descriere_dreptunghi(lungime, latime):
    a = aria_dreptunghi(lungime, latime)
    p = perimetru_dreptunghi(lungime, latime)
    return f"Dreptunghi cu lungime {lungime} si latime {latime} are aria {a} si perimetrul {p}"

print(descriere_dreptunghi(10, 20))

# 12. DOCSTRING  -  documentare in functie
# -------------------------------------------------------------
# Un string in TRIPLE GHILIMELE pus IMEDIAT dupa def este
# "documentatia" functiei. Apare la help() si in IDE.

def aduna(a, b):
    """Returneaza suma a si b."""
    return a + b


print(aduna.__doc__)         # afiseaza documentatia functiei
help(aduna)                  # arata semnatura functiei + docstring


# 13. TYPE HINTS  -  scurta mentiune  (optional, dar util)
# -------------------------------------------------------------
# Putem ADNOTA tipurile parametrilor si al return-ului.
# Python NU le verifica - sunt doar pentru CITITOR si IDE.

def aduna(a: int, b: int) -> int:
    """Returneaza suma a si b."""
    return a + b

# 14. FUNCTIE = OBIECT  (poate fi pusa in variabila / lista / dict)
# -------------------------------------------------------------
# In Python, functiile sunt OBIECTE. Le poti pasa ca argument,
# pune in lista / dict, returna din alta functie.

def adunare(a, b): return a + b
def scadere(a, b): return a - b
def inmultire(a, b): return a * b

# Punem functiile intr-un dict si "alegem" prin cheie:
operatii = {
    "+": adunare,
    "-": scadere,
    "*": inmultire
}
print(operatii["+"](3, 5))

# (atentie: NU "operatii[semn]" + (6, 7) - ci "operatii[semn](6, 7)")


# 16. VARIABILELE DIN INTERIORUL FUNCTIEI - O SCURTA NOTA
# -------------------------------------------------------------
# Variabilele create INTR-O functie traiesc DOAR in functie.
# Nu poti accesa din afara.
#
# Vom intelege exact cum functioneaza in sesiunea urmatoare,
# cand discutam despre SCOPE. Pana atunci, retine intuitia:
#   "ce intra ca parametru, ce iese ca return - asa comunici".

def calculeaza():
    rezultat_intern = 100
    return rezultat_intern * 2

valoare = calculeaza()
print(valoare)    # 200
# print(rezultat_intern)     # NameError- nu exista in afara functiei



# =============================================================
# CONCLUZIE
# =============================================================
# Functii:
#     def nume(parametri):
#         ...
#         return valoare
#
# Reguli de baza:
#   - PARAMETRII sunt valorile primite la apel
#   - RETURN trimite o valoare inapoi (poate fi tuplu = mai multe valori)
#   - daca nu pui return, functia returneaza None
#   - poti da valori IMPLICITE  (def f(x, n=10):)
#   - poti chema cu argumente POZITIONALE sau KEYWORD
#   - LAMBDA = functie mica, dintr-o linie, fara nume
#   - DOCSTRING-ul (""") este documentatia functiei
#
# Functiile sunt cea mai importanta unealta de organizare a
# codului. De aici incolo, vom incepe sa scriem TOT codul
# in functii bine numite.
# =============================================================