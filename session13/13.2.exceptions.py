# EXCEPTII SI TRATAREA ERORILOR  (try / except)
# =============================================================


# 1. ERORI UZUALE  (ce arunca, cand)
# -------------------------------------------------------------
#   1 / 0                 -> ZeroDivisionError
#   int("abc")            -> ValueError      (valoare gresita)
#   "abc" + 5             -> TypeError        (tip gresit)
#   [1, 2, 3][10]         -> IndexError       (index inexistent)
#   {"a": 1}["b"]         -> KeyError         (cheie inexistenta)
#   open("nu_exista.txt") -> FileNotFoundError
#   print(x)  (x nedefinit) -> NameError


# 2. SINTAXA DE BAZA  -  try / except TIP
# -------------------------------------------------------------
# Pune in try DOAR liniile care chiar pot esua.
# Prinde TIPUL specific (evita  except:  gol, care prinde tot).

# a = int(input("Introduceti valoarea a=: "))
# b = int(input("Introduceti valoarea b=: "))
# try:
#     x =  a/b
# except ZeroDivisionError:
#     print("Imposibil de divizat!")


# 3. ACCES LA EXCEPTIE  -  except TIP as e
# -------------------------------------------------------------
# `as e` ne da mesajul si tipul exceptiei.
try:
    n = int("abc")
except ValueError as e:
    print(f"Mesajul erorii este: {e}")


# 4. MAI MULTE  except  +  ORDINEA (specific -> general)
# -------------------------------------------------------------
# Python sare la PRIMUL except care se potriveste; restul se ignora.
# De aceea tipurile SPECIFICE vin INAINTEA celor generale.
date = {'a': 1}
#
try:
    valoare = date['b']   # KeyError
    rezultat = 100/valoare
except KeyError:
    print("cheia 'b' nu exista in date")
except ZeroDivisionError:
    print(f"Valoarea e zero")
except Exception as e:
    print(f"Eroare generala: {e}")



# 5. else  si  finally
# -------------------------------------------------------------
# else    -> ruleaza DOAR daca NU a fost exceptie (ramura de succes)
# finally -> ruleaza INTOTDEAUNA (succes sau esec) - pentru CURATARE
#            (inchidere fisiere, conexiuni, eliberare resurse)

try:
    n = int('abc')
except ValueError:
    print("Nu este un numar")
else:
    print(f"Totul cu succes!")
finally:
    print("Am terminat")


# 6. raise  -  arunca propria exceptie
# -------------------------------------------------------------
# In functiile tale, SEMNALEAZA erorile cu raise. Apelantul le prinde.

def imparte(a, b):
    if b == 0:
        raise ZeroDivisionError("Imposibil de divizat!!!!!!")
    return a / b

try:
    print(imparte(10, 0))
except ZeroDivisionError as e:
    print(f"Mesajul erorii este: {e}")



# 7. re-raise  -  prinde, logheaza, arunca mai departe
# -------------------------------------------------------------
def proceseaza(text):
    try:
        int(text)
    except ValueError :
        raise

try:
    proceseaza("abc")
except ValueError as e:
    print(f"Mesajul erorii este: {e}")


# 8. PATTERN UZUAL  -  incearca, altfel default
# -------------------------------------------------------------

def functie_noua(text, default=0):
    try:
        return int(text)
    except(ValueError, TypeError):
        return default


print(functie_noua("42"))   # 42
print(functie_noua("abc"))  # 0
print(functie_noua("abc", 42))  #42
# =============================================================
# RECOMANDARI
# =============================================================
# - Prinde DOAR ce stii sa tratezi; restul, lasa-l sa urce.
# - Foloseste tipuri SPECIFICE (nu  except:  gol).
# - Pune in try doar liniile riscante, nu blocuri uriase.
# - Mesaje pentru OAMENI: "varsta -3 nu e permisa", nu "ERR-42".
# - Curatarea (close, release) -> in  finally  (sau "with").
#
# Sintaxa completa:
#   try:     <cod riscant>
#   except TipExceptie as e:  <reactie>
#   else:    <doar pe succes>
#   finally: <mereu - clean-up>
#
# raise X("mesaj") -> arunca o exceptie noua
# raise            -> re-arunca exceptia curenta
# =============================================================