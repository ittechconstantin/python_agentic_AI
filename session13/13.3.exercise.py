# EXCEPTII
# =============================================================

# 1. try / except TIP  -  evita impartirea la zero
# ------------------------------------------------
# CONTEXT: calculezi pretul mediu pe produs dintr-un cos.
# CERINTA: scrie  pret_mediu(total, nr_produse)  care intoarce
#          total / nr_produse, dar daca cosul e gol (nr_produse == 0)
#          intoarce 0 in loc sa crape (prinde ZeroDivisionError).

# Solutie:

print("\n--- Exercitiul 1 ---")
def pret_mediu(total, nr_produse):
    try:
        return total/nr_produse
    except ZeroDivisionError:
        return 0

print(pret_mediu(100, 10))
print(pret_mediu(100, 0))

# 2. except TIP as e  -  citeste mesajul erorii
# ---------------------------------------------
# CONTEXT: utilizatorul completeaza varsta intr-un formular.
# CERINTA: scrie  parseaza_varsta(text)  care intoarce int(text).
#          Daca textul nu e numar, prinde ValueError, printeaza mesajul
#          erorii cu `as e` si intoarce None.

# Solutie:

print("\n--- Exercitiul 2 ---")
def parseaza_varsta(text):
   try:
       return int(text)
   except ValueError as e:
       print(f"Mesajul erorii este: {e}")
       return None

print(parseaza_varsta("10"))
print(parseaza_varsta("abc"))

# 3. PATTERN "incearca, altfel default"  (+ tuplu de tipuri)
# ----------------------------------------------------------
# CONTEXT: vrei cantitatea ca numar, dar inputul poate fi orice.
# CERINTA: scrie  ca_int(text, default=1)  care intoarce int(text),
#          iar daca nu se poate (ValueError SAU TypeError) intoarce
#          valoarea default.

# Solutie:

print("\n--- Exercitiul 3 ---")
def ca_int(text, default = 1):
    try:
        return int(text)
    except (ValueError, TypeError):
        return default

print(ca_int("bgf"))
print(ca_int(45))


# 4. KeyError  -  citire sigura dintr-un raspuns JSON
# ---------------------------------------------------
# CONTEXT: un API iti da un dict, dar uneori lipsesc campuri.
# CERINTA: scrie  ia_nume(raspuns)  care intoarce raspuns["name"];
#          daca cheia lipseste, prinde KeyError si intoarce "anonim".

# Solutie:

print("\n--- Exercitiul 4 ---")
date1 = {"varsta": 23,
         "locatia": "Palticeni"}
date2 = {"nume": "Andrei",
         "locatia": "Brasov"}
date3 = {"nume": "Calin",
         "varsta": 40}



def ia_nume(raspuns):
    try:
        return raspuns["nume"]
    except KeyError:
        return "anonim"

print(ia_nume(date1))
print(ia_nume(date2))
print(ia_nume(date3))

# 5. MAI MULTE except + ORDINEA (specific -> general)
# ---------------------------------------------------
# CONTEXT: procesezi un raspuns si calculezi un raport.
# CERINTA: scrie  raport(date)  care face  100 / date["scor"]  si
#          intoarce rezultatul. Trateaza, IN ACEASTA ORDINE:
#            - KeyError          -> "lipseste 'scor'"
#            - ZeroDivisionError -> "scor zero"
#            - Exception         -> f"alta eroare: {e}"  (plasa de siguranta)

# Solutie:

date = {"b": 2}

print("\n--- Exercitiul 5 ---")
def raport(date):
    try:
        scor = date["c"]
        rezultat = 100/scor
        return rezultat
    except KeyError:
        print(f"lipseste 'scor'")
    except ZeroDivisionError:
        print(f"scor zero")
    except Exception as e:
        print(f"alta eroare: {e}")
try:
    print(raport(date))
except (KeyError,ZeroDivisionError, Exception) as e:
    print(f"{e}")

# 6. TUPLU de exceptii  -  aduna doar valorile valide
# ---------------------------------------------------
# CONTEXT: primesti o lista cu valori amestecate dintr-un formular.
# CERINTA: scrie  suma_valida(valori)  care aduna int-urile posibile.
#          Pentru fiecare valoare care da (ValueError, TypeError),
#          printeaza ca o sari si continui.

# Solutie:

print("\n--- Exercitiul 6 ---")
def suma_valida(valori):
    suma = 0
    for valoare in valori:
        try:
            suma += valoare
        except (ValueError, TypeError):
            print(f"Vom sari peste valoarea : {valoare}")
    return suma

print(suma_valida((10, 16, 29, "abc", [3,5,9], {12})))

# 7. raise  -  arunca propria exceptie
# ------------------------------------
# CONTEXT: nu accepti o varsta negativa la inregistrare.
# CERINTA: scrie  seteaza_varsta(v)  care, daca v < 0, arunca
#          ValueError cu un mesaj clar PENTRU OM; altfel intoarce v.
#          Apoi apeleaz-o intr-un try/except si printeaza mesajul.

# Solutie:

print("\n--- Exercitiul 7 ---")
def seteaza_varsta(v):
    if v < 0:
        raise ValueError("Este un numar negativ")
    else:
        return v

try:
    print(seteaza_varsta(30))
except ValueError as e:
    print(f"Mesajul erorii este: {e}")

try:
    print(seteaza_varsta(-2))
except ValueError as e:
    print(f"Mesajul erorii este: {e}")

# 8. re-raise  -  prinde, logheaza, arunca mai departe
# ----------------------------------------------------
# CONTEXT: vrei sa LOGHEZI o eroare de plata, dar tot s-o lasi sa urce
#          ca s-o trateze codul de mai sus.
# CERINTA: scrie  proceseaza_plata(suma)  care face  100 / suma; la
#          ZeroDivisionError printeaza "[log] plata esuata: ..." si
#          re-arunca aceeasi exceptie cu  raise  (fara argument).

# Solutie:

print("\n--- Exercitiul 8 ---")
def proceseaza_plata(suma):
    try:
        return 100/suma
    except ZeroDivisionError:
        print("[log] plata esuata: ...")
        raise

try:
    print(proceseaza_plata(0))
except ZeroDivisionError:
    print("Suma este nula")

# 9. TOTUL LA UN LOC  -  raport de procesare in masa
# ---------------------------------------------------
# CONTEXT: procesezi un cos brut; unele produse au pretul stricat sau lipsa.
# CERINTA: scrie  totalizeaza(items)  unde fiecare item e un dict cu cheia
#          "pret" (string). Aduna preturile valide si intoarce un dict:
#            {"total": <suma>, "ok": <nr valide>, "erori": [<mesaje>]}
#          Foloseste KeyError (lipsa "pret"), ValueError (pret ne-numar) si
#          `else` ca sa numeri doar succesele.

# Solutie:

print("\n--- Exercitiul 9 ---")

def totalizeaza(items):
    suma = 0
    nr_valide = 0
    mesaje = []
    for item in items:
        try:
            suma += int(item["pret"])
        except KeyError:
            mesaje.append(f"lipsa'pret'")
        except ValueError:
            mesaje.append(f"pret ne-numar")
        else:
            nr_valide += 1

    return {"total": suma, "ok": nr_valide, "erori": mesaje}

cos_brut = [{"pret" : 2},
            {"pret" : 32},
            {"far" : ""},
            {"pret" : "abc"},
            {"pret" : 25},
            {"pret" : 22}]

print(totalizeaza(cos_brut))