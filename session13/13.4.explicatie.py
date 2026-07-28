# RUNDA 4 - try / except / else / finally / raise
# Pentru fiecare intrebare: codul real + explicatie detaliata
# ============================================================


# ------------------------------------------------------------
# 1) Categorie: else-pe-succes   |   Corect: B -> "ok"
# ------------------------------------------------------------
try:
    n = int("42")
except ValueError:
    print("err")
else:
    print("ok")

# EXPLICATIE:
# - int("42") este valid, deci conversia REUSESTE si nu se arunca
#   nicio exceptie.
# - Pentru ca blocul `try` s-a terminat FARA eroare, ramura
#   `except` este sarita complet.
# - Ramura `else` ruleaza DOAR pe succes (adica numai cand `try`
#   nu a aruncat nimic). Cum aici a fost succes, intra pe `else`.
# REZULTAT AFISAT: ok


# ------------------------------------------------------------
# 2) Categorie: finally-mereu   |   Corect: B -> "finally" apoi "try"
# ------------------------------------------------------------
def f2():
    try:
        return "try"
    finally:
        print("finally")

print(f2())

# EXPLICATIE:
# - In `try` avem `return "try"`. In mod normal te-ai astepta ca
#   functia sa iasa imediat, dar...
# - `finally` ruleaza MEREU, indiferent ce se intampla in `try`,
#   inclusiv atunci cand `try` are un `return`.
# - Mai mult: `finally` ruleaza INAINTE ca valoarea sa fie efectiv
#   returnata catre apelant. Deci ordinea reala este:
#     1. Python pregateste valoarea de return ("try")
#     2. ruleaza `finally` -> se printeaza "finally"
#     3. abia apoi f2() intoarce "try"
#     4. print(f2()) afiseaza "try"
# REZULTAT AFISAT (in ordine): finally, apoi try


# ------------------------------------------------------------
# 3) Categorie: finally-return   |   Corect: B -> "2"
# ------------------------------------------------------------
# def f3():
#     try:
#         return 1
#     finally:
#         return 2
#
# print(f3())

# EXPLICATIE:
# - Capcana clasica de interviu.
# - `try` zice `return 1`, dar inainte sa apuce sa intoarca valoarea,
#   ruleaza `finally`.
# - In `finally` avem `return 2`. Un `return` din `finally`
#   SUPRASCRIE orice return pregatit in `try`.
# - finally ruleaza ultimul si "castiga", deci valoarea 1 este pierduta.
# - Din acest motiv se recomanda sa NU pui `return` in `finally`,
#   pentru ca ascunde/anuleaza rezultate si chiar exceptii.
# REZULTAT AFISAT: 2


# ------------------------------------------------------------
# 4) Categorie: raise-propriu   |   Corect: B -> "varsta negativa"
# ------------------------------------------------------------
def varsta(v):
    if v < 0:
        raise ValueError("varsta negativa")
    return v

try:
    varsta(-1)
except ValueError as e:
    print(e)

# EXPLICATIE:
# - varsta(-1): v este negativ, deci se executa
#   `raise ValueError("varsta negativa")`, care arunca o exceptie
#   de tip ValueError cu mesajul dat de noi.
# - `except ValueError as e` prinde acea exceptie si o leaga
#   de variabila `e`.
# - print(e) afiseaza MESAJUL exceptiei (textul dat la `raise`),
#   nu numele clasei "ValueError" si nici numarul -1.
# REZULTAT AFISAT: varsta negativa


# ------------------------------------------------------------
# 5) Categorie: re-raise   |   Corect: B -> "log" apoi "sus"
# ------------------------------------------------------------
def f5():
    try:
        return int("x")
    except ValueError:
        print("log")
        raise

try:
    f5()
except ValueError:
    print("sus")

# EXPLICATIE:
# - int("x") nu e un numar valid, deci arunca ValueError.
# - `except ValueError` din interiorul lui f5() o prinde si
#   printeaza "log".
# - `raise` SINGUR (fara argument) RE-ARUNCA exact aceeasi exceptie
#   mai departe, in sus, catre cine a apelat f5().
# - Codul exterior are si el `try/except ValueError`, prinde
#   exceptia re-aruncata si printeaza "sus".
# - Acesta este un pattern util: logheaza/trateaza ceva local,
#   apoi lasi exceptia sa urce ca sa fie tratata la nivelul de sus.
# REZULTAT AFISAT (in ordine): log, apoi sus


# ------------------------------------------------------------
# 6) Categorie: pattern-default   |   Corect: B -> "0"
# ------------------------------------------------------------
def ca_int(t, d=0):
    try:
        return int(t)
    except ValueError:
        return d

print(ca_int("abc"))

# EXPLICATIE:
# - Pattern uzual: "incearca conversia, altfel intoarce o valoare
#   implicita (default)".
# - int("abc") nu poate fi convertit, deci arunca ValueError.
# - `except ValueError` prinde eroarea si in loc sa lase programul
#   sa crape, intoarce valoarea default `d`, care aici e 0
#   (nu am dat al doilea argument, deci se foloseste d=0).
# REZULTAT AFISAT: 0