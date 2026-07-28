# RECAPITULARE - "CHEATSHEET" PYTHON
# =============================================================
# Acest fisier este un REZUMAT vizual al tot ce am invatat
# in sesiunile 1-5. Nu introducem nimic nou: doar punem
# lucrurile in oglinda, ca sa fie usor de comparat si
# sa stim cand sa folosim fiecare structura.
# =============================================================


# 1. VARIABILE, TIPURI, PRINT
# -------------------------------------------------------------
nume = "Horia"          # str
varsta = 30             # int
inaltime = 1.78         # float
admin = True            # bool

print(nume, varsta, inaltime, admin)
print(type(nume), type(varsta), type(inaltime), type(admin))


# 2. F-STRING - cea mai citibila formatare
# -------------------------------------------------------------
pret = 19.987
print(f"{nume} are {varsta} ani")
print(f"Total: {pret:.2f} lei")            # 2 zecimale
print(f"Numar: {1234567:,}")                 # separator de mii


# 3. OPERATORI - reamintire rapida
# -------------------------------------------------------------
# Aritmetici:        +  -  *  /  //  %  **
# Comparare:         ==  !=  <  >  <=  >=
# Logici:            and  or  not
# Atribuire compusa: +=  -=  *=  /=  //=  %=  **=
# Apartenenta:       in  not in
# Identitate:        is  is not       (folosit cu None / True / False)

print(10 // 3, 10 % 3, 2 ** 8)               # 3 1 256
print(7 == 7 and 5 < 10)                     # True
print("@" in "ana@example.com")              # True


# 4. COLLECTII - TABLOUL COMPARATIV
# =============================================================
#
#  Tip      Sintaxa     Mutabil?  Ordonat?  Indexabil?  Duplicate?  Cheie in dict?
#  ----------------------------------------------------------------------
#  str      "abc"       NU        DA         DA          DA          DA
#  list     [1,2,3]     DA        DA         DA          DA          NU
#  tuple    (1,2,3)     NU        DA         DA          DA          DA  (daca elementele sunt imutabile)
#  set      {1,2,3}     DA        NU         NU          NU          NU
#  frozenset            NU        NU         NU          NU          DA
#  dict     {"a":1}     DA        DA*        DA(prin cheie) NU(chei)  -
#
#  * dict pastreaza ordinea de inserare (Python 3.7+)
# =============================================================


# 5. CREARE - cum arata fiecare colectie
# -------------------------------------------------------------
s_text   = "Hello"
lst      = [1, 2, 3]
tpl      = (1, 2, 3)
st       = {1, 2, 3}
dct      = {"host": "localhost", "port": 8080}

# COLECTII GOALE - atentie la set !
gol_lst  = []
gol_tpl  = ()
gol_set  = set()      # NU  {}   -  asta e dict gol !
gol_dct  = {}

# Tuplul cu un singur element - virgula obligatorie:
un_tpl   = (5,)


# 6. LUNGIME - len() merge la TOATE
# -------------------------------------------------------------
print(len(s_text), len(lst), len(tpl), len(st), len(dct))


# 7. APARTENENTA - "in" merge la TOATE
# -------------------------------------------------------------
# Atentie:
#   - la string  -> cauta SUBSTRING
#   - la list/tuple -> cauta ELEMENT
#   - la set     -> cauta ELEMENT (foarte rapid)
#   - la dict    -> cauta CHEIE (NU valoare)

print("ell" in s_text)          # True
print(2 in lst)                  # True
print(3 in tpl)                  # True
print(1 in st)                   # True
print("host" in dct)             # True   - cauta cheia
print("localhost" in dct)        # False  - "in" la dict NU vede valorile


# 8. INDEXARE / SLICING - merg pe str, list, tuple
# -------------------------------------------------------------
# NU merg pe set si nu merg DIRECT pe dict (dict-ul are chei).

print(s_text[0], s_text[-1], s_text[1:4])
print(lst[0],    lst[-1],    lst[1:])
print(tpl[0],    tpl[-1],    tpl[::-1])

# Pentru dict accesam prin CHEIE:
print(dct["host"])
print(dct.get("debug", False))   # acces sigur, fara KeyError


# 9. CELE MAI IMPORTANTE METODE PE STRING
# -------------------------------------------------------------
# Toate returneaza un STRING NOU (string-ul e imutabil!).
text = "  Salut Python  "
print(text.strip())                 # "Salut Python"
print(text.lower(), text.upper())
print(text.replace("Python", "Lume"))
print(text.split())                 # ["Salut", "Python"]
print("-".join(["a", "b", "c"]))    # "a-b-c"
print("Python".startswith("Py"))    # True
print("file.pdf".endswith(".pdf"))  # True
print("ab,cd,ef".count(","))        # 2
print("Python".find("th"))          # 2
print("Py3".isalnum(), "12".isdigit(), "ab".isalpha())


# 10. CELE MAI IMPORTANTE METODE PE LISTA
# -------------------------------------------------------------
nums = [3, 1, 4, 1, 5]

nums.append(9)            # [3, 1, 4, 1, 5, 9]
nums.extend([2, 6])       # [3, 1, 4, 1, 5, 9, 2, 6]
nums.insert(0, 0)         # [0, 3, 1, 4, 1, 5, 9, 2, 6]
nums.remove(1)            # sterge prima 1
ult = nums.pop()          # extrage ultimul
nums.sort()               # in loc
nums.reverse()            # in loc
print(nums)
print(nums.count(1), nums.index(3))
print(min(nums), max(nums), sum(nums), sum(nums) / len(nums))

# sort() vs sorted():
a = [3, 1, 2]
b = sorted(a)             # b nou; a neschimbat
a.sort()                  # a se modifica
print(a, b)


# 11. CELE MAI IMPORTANTE METODE PE TUPLU
# -------------------------------------------------------------
# Tuplul are DOAR 2 metode (e imutabil): count, index.
t = (10, 20, 30, 20, 40)
print(t.count(20))        # 2
print(t.index(30))         # 2

# Putere: UNPACKING
host, port = ("localhost", 8080)
prima, *restul = (1, 2, 3, 4, 5)
print(host, port)
print(prima, restul)

# SWAP cu tuplu:
x, y = 5, 10
x, y = y, x
print(x, y)


# 12. CELE MAI IMPORTANTE METODE PE SET
# -------------------------------------------------------------
a = {1, 2, 3}
b = {3, 4, 5}

a.add(4)                  # {1, 2, 3, 4}
a.discard(99)             # nu da eroare daca lipseste
a.update([5, 6])

# Operatii de multime - cele mai utile:
print(a | b)              # uniune
print(a & b)              # intersectie
print(a - b)              # diferenta
print(a ^ b)              # diferenta simetrica


# Folosim CONST: deduplicarea unei liste
unice = list(set([1, 1, 2, 3, 3]))
print(unice)


# 13. CELE MAI IMPORTANTE METODE PE DICT
# -------------------------------------------------------------
config = {"host": "localhost", "port": 8080}

print(config["host"])
print(config.get("debug", False))     # acces sigur

config["debug"] = True                 # adauga / suprascrie
config.update({"port": 9090, "ssl": True})   # in masa
val = config.pop("ssl")                # sterge si returneaza
config.setdefault("timeout", 30)       # daca lipseste -> seteaza
print(config)

# Inspectie:
print(list(config.keys()))
print(list(config.values()))
print(list(config.items()))

# Fuzionare cu  |  (Python 3.9+):
defaults = {"host": "localhost", "port": 8080}
override = {"port": 9090}
final = defaults | override
print(final)             # {'host': 'localhost', 'port': 9090}

# Init pe baza unei liste de chei:
status = dict.fromkeys(["nginx", "redis"], "down")
print(status)


# 14. CONVERSII INTRE COLECTII
# -------------------------------------------------------------
# Toate aceste functii pot construi un tip dintr-un alt iterabil:
#   list(...) tuple(...) set(...) dict(...) str(...) frozenset(...)

print(list("abc"))                          # ['a', 'b', 'c']
print(tuple([1, 2, 3]))                     # (1, 2, 3)
print(set([1, 2, 2, 3]))                    # {1, 2, 3}
print(list((10, 20, 30)))                   # [10, 20, 30]

# Lista de tupluri (cheie, valoare) -> dict
perechi = [("host", "localhost"), ("port", 8080)]
print(dict(perechi))



# 15. CAND ALEGEM CE STRUCTURA?
# -------------------------------------------------------------
# Decizia in 4 intrebari:
#
# 1) Datele se VOR SCHIMBA dupa creare?
#       NU       -> tuple sau frozenset (semnaleaza intentia)
#       DA       -> list / set / dict
#
# 2) Vreau sa OPRESC duplicatele?
#       DA       -> set / dict (chei unice)
#       NU       -> list / tuple
#
# 3) Vreau sa accesez dupa un NUME / CHEIE?
#       DA       -> dict
#       NU       -> list / tuple / set
#
# 4) Ordinea conteaza?
#       DA       -> list / tuple / dict (pastreaza ordinea inserarii)
#       NU       -> set / frozenset (mai rapid pentru "in")


# =============================================================
# CONCLUZIE
# =============================================================
# - str   -> text imutabil (split, join, replace, strip, f-string)
# - list  -> colectie ordonata, mutabila, "merge la orice"
# - tuple -> inregistrare fixa (record); poate fi cheie de dict
# - set   -> elemente unice; uniune/intersectie/diferenta rapide
# - dict  -> cheie -> valoare; coloana vertebrala a JSON-ului si
#            a configuratiilor
# Cunoscand bine aceste 5 tipuri si operatorii (+ in, +, *, ==),
# putem deja modela aproape orice problema reala in Python.
# =============================================================