# GENERATORI IN PYTHON  (yield)
# =============================================================
# Un GENERATOR este o functie care, in loc sa construiasca si sa
# intoarca TOATE valorile deodata (intr-o lista), le produce UNA
# CATE UNA, la cerere, pe masura ce ai nevoie de ele.
#
# Cuvantul cheie e `yield` ("ofera"). O functie care contine `yield`
# devine automat o "functie generator".
#
# DE CE sunt utili?
#   - MEMORIE: nu tin toate valorile in RAM, ci doar una la un moment
#     dat. Poti procesa milioane de randuri / fisiere uriase / fluxuri
#     fara sa ramai fara memorie.
#   - LAZY ("lenes"): calculeaza doar cat ii ceri. Daca te opresti mai
#     devreme, restul nici nu se mai calculeaza.
#   - se inlantuie frumos (pipeline): sursa -> filtru -> transformare,
#     totul curgand cate un element pe rand.
#
# De ce ai nevoie ca sa intelegi generatorii (recap):
#   - bucle for si range
#   - liste si list comprehension  [x for x in ...]
#   - functii cu return
# =============================================================


# #############################################################
# PARTEA 1 - BAZELE, PAS CU PAS
# #############################################################


# 1. PROBLEMA: o lista mare ocupa multa memorie
# -------------------------------------------------------------
# La fel ca la decoratori: intai vedem PROBLEMA, apoi solutia.
#
# Vrem patratele numerelor de la 0 la n. Varianta clasica le pune
# pe TOATE intr-o lista si o intoarce.

import sys


def patrate_lista(n):
    rezultat = []
    for i in range(n):
        rezultat.append(i * i)
    return rezultat        # intoarcem o list acompleta deoadata

lista = patrate_lista(1_000_000)
print(lista[:5])       # [0, 1, 4, 9, 16]
print(f"Lista ocupa {sys.getsizeof(lista) // 1024} KB")

# Problema: chiar daca ne trebuie doar primele 5 valori, am construit
# si tinut in memorie TOATE un milion. Risipa de timp si de RAM.

# 2. SOLUTIA: yield - prima functie generator
# -------------------------------------------------------------
# Inlocuim `append` + `return lista` cu `yield`. Functia nu mai
# construieste o lista: ofera cate o valoare pe rand, prin `yield`.


def patrate_gen(n):
    for i in range(n):
        yield i * i   # ofera i * i si se opreste aici pana i se cere urmatorul rezultat


# ATENTIE: apeland functia generator, corpul NU ruleaza inca!
# Primesti un "obiect generator" - o promisiune ca va produce valori.

g = patrate_gen(1_000_000)
print(g)
print(f"Generatorul ocupa {sys.getsizeof(g)} Bytes")


# 3. CUM CONSUMI un generator: for si next()
# -------------------------------------------------------------
# Cel mai des: cu un for, exact ca pe o lista.
for valoare in patrate_gen(5):
    print(valoare)

# Pe dedesubt, for-ul cheama `next()` pentru fiecare element.
# Poti face si manual:

g = patrate_gen(5)
print(next(g))  # 0
print(next(g))  # 1
print(next(g))  # 4
print(next(g))  # 16

# Cand nu mai sunt valori, next() arunca StopIteration:
try:
    print(next(g))
except StopIteration:
    print('gata, generatorul s-a terminat')

# 4. LAZY: produce o valoare doar cand i-o ceri
# -------------------------------------------------------------
# Generatorul ruleaza corpul "in reprize": pana la urmatorul yield,
# apoi se opreste si asteapta. Se vede clar daca punem print-uri.

def numere_cu_mesaj():
    print("1-> se calculeaza 1")
    yield 1
    print("2-> se calculeaza 2")
    yield 2
    print("3-> se calculeaza 3")
    yield 3

g = numere_cu_mesaj()
print("am creat generatorul, dar inca nu s-a calculat nimic")
print("cer prima valoare...")
print(next(g))
print("cel a doua valoare...")
print(next(g))
print(next(g))
# Daca ne oprim aici, "-> calculez 3" NU se mai executa niciodata.


# 5. Generatorul se EPUIZEAZA (o singura trecere)
# -------------------------------------------------------------
# Spre deosebire de o lista, un generator se poate parcurge O SINGURA
# DATA. Dupa ce l-ai consumat, e gol.

g = patrate_gen(3)
print(list(g))   # l-am consumat tot
print(list(g))   # e gol
# Daca ai nevoie de valori de mai multe ori, fie refaci generatorul,
# fie le pui intr-o lista: list(patrate_gen(3)).


# 6. GENERATOR EXPRESSION: (x for x in ...) vs [x for x in ...]
# -------------------------------------------------------------
# Stii deja list comprehension cu paranteze patrate [].
# Daca folosesti paranteze ROTUNDE (), obtii un generator: nu se
# construieste nicio lista, valorile se produc la cerere.

list_comp = [x * x  for x in range(5)]   # construiecte o lista ACUM
gen_exp   = (x * x  for x in range(5))   # generator expr
print(list_comp)          # [0, 1, 4, 9, 16]
print(gen_exp)            # generator object
print(list(gen_exp))      # [0, 1, 4, 9, 16] consumat o data


# Cel mai util: cand dai generatorul direct unei functii ca sum/max,
# fara lista intermediara - economisesti memorie.
print(sum(x * x for x in range(1_000_000)))
# range(1_000_000) -> produce valorile pe rand
# (x * x for x in range(1_000_000)  -> generator expr.
# sum(x * x for x in range(1_000_000)) cere urmatoare valoare de la generator
# o adauga la rezultat si apoi va cere urmatoarea valorea

# generatorul, valoarea curenta lui x si rezultatul acumulat de sum


print(sum([x * x for x in range(1_000_000)]))

# se calculeaza toate cele 1.000.000 de patrate
# se construieste o lista imensa cu toate elemente in memorie
# sum() parcurge lista si face adunare

# ==> MEMORIA CONSUMATA ESTE MULT MAI MARE


# #############################################################
# PARTEA 2 - DE CE CONTEAZA (cazuri reale)
# #############################################################

# 7. MEMORIE: procesarea unui fisier mare, linie cu linie
# -------------------------------------------------------------
# Cazul clasic: ai un fisier de log / un CSV de zeci de GB. Nu il poti
# incarca tot in memorie. Solutia: il citesti LAZY, o linie pe rand.
#
# In Python, un fisier deschis e DEJA un generator de linii:
#       with open("vanzari.csv") as f:
#           for linie in f:        # o linie pe rand, NU tot fisierul deodata
#               proceseaza(linie)
#
# Aici simulam "liniile unui fisier" cu un generator, ca exemplul sa
# ruleze fara sa avem nevoie de un fisier real pe disc.

def linii_log():
    yield "INFO utilizator logat"
    yield "ERROR plata esuata"
    yield "INFO produs in cosul de cumparaturi"
    yield "INFO produs in cosul de cumparaturi"
    yield "ERROR stoc insuficient"
    yield "INFO delogare"

# Numaram erorile FARA sa tinem toate liniile in memorie:
nr_erori = sum(1 for linie in linii_log() if linie.startswith("ERROR"))
print(nr_erori)


# 8. PIPELINE: inlantuim generatori (sursa -> filtru -> transformare)
# -------------------------------------------------------------
# Caz real: un flux de comenzi. Vrem suma comenzilor PLATITE.
# Construim un "lant": fiecare etapa primeste elemente de la cea de
# dinainte si le da mai departe, cate unul, fara liste intermediare.


def comenzi():
    yield {"id": 1, "platita": True,  "suma": 350}
    yield {"id": 2, "platita": False, "suma": 450}
    yield {"id": 3, "platita": True,  "suma": 150}
    yield {"id": 4, "platita": True,  "suma": 50}
    yield {"id": 5, "platita": False, "suma": 50}
    yield {"id": 6, "platita": True,  "suma": 950}


platite = (c for c in comenzi() if c['platita'])  # etapa 1 : filtreaza
sume = (c['suma'] for c in platite)               # etapa 2 : extragem suma
total = sum(sume)                                 # etapa 3: aduna
print(f"TOTAL comenzi platite: {total}")


# 9. FLUX INFINIT / la cerere
# -------------------------------------------------------------
# Un generator poate produce valori la INFINIT (cu while True).
# Asta ar fi imposibil cu o lista - n-ai putea-o construi niciodata.
# Tu controlezi cate iei, cu `break`.

def numere_de_la(start):
    n = start
    while True:      # bucla infinita dar e ok , e lazy
        yield n
        n += 1

# Luam doar primele 5, apoi ne oprim:

g = numere_de_la(100)
for x in g:
    if x >= 105:
        break
    print(x, end="  ")
print()


# 10. AGREGARE IN FLUX: total/medie fara a tine tot in memorie
# -------------------------------------------------------------
# Caz real: ai un milion de tranzactii. Vrei totalul si media, dar
# NU vrei sa tii toate sumele in memorie deodata.

def tranzactii(n):
    for i in range(n):
        yield (i % 100) + 1      # simulez o suma intre 1 si 100


total = 0
nr = 0

for suma in tranzactii(1_000_000):
    total += suma
    nr += 1

print(f"{nr} tranzactii, total: {total}, media: {total/nr:.2f}")

# Niciodata n-am avut un milion de valori in memorie deodata.


# #############################################################
# PARTEA 3 - UNELTE DIN STANDARD LIBRARY
# #############################################################


# 11. itertools  -  unelte gata facute pentru generatori/iteratori
# -------------------------------------------------------------
# Modulul `itertools` ofera "caramizi" foarte folosite cu generatori.

from itertools import islice, count, chain

# count(start) = generator infinit: start, start+1, start+2, ...
# islice(gen, n) = ia primele n elemente dintr-un generator (ca o "felie")
primele_5 = list(islice(count(10), 5))   #[10, 11, 12, 13, 14]
print(primele_5)
# islice e modul curat de a "taia" un flux infinit, fara break manual:
print(list(islice(numere_de_la(4), 3)))

# chain(a, b) = lipeste mai multi iteratori unul dupa altul (tot lazy)

print(list(chain([1, 2], [3, 4], [5, 6])))  #[1, 2, 3, 4, 5, 6]
# 12. yield from  -  delega catre alt generator
# -------------------------------------------------------------
# Cand vrei sa "retransmiti" toate valorile altui generator/iterabil,
# in loc de  `for x in sub: yield x`  scrii direct  `yield from sub`.
def grupa_a():
    yield "a1"
    yield "a2"

def grupa_b():
    yield "b1"
    yield "b2"

def toate_grupele():
    yield from grupa_a()      # da toate valorile din grupa a
    yield from grupa_b()      # apoi toate din grupa b

print(list(toate_grupele()))   #['a1', 'a2', 'b1', 'b2']



# =============================================================
# RECAP / GRESELI FRECVENTE
# =============================================================
# - `yield` transforma functia in generator: produce valori pe rand.
# - Apeland functia generator NU ruleaza corpul; primesti un obiect
#   generator. Corpul ruleaza pe masura ce ceri valori (for / next).
# - Un generator se consuma O SINGURA DATA. Pentru reutilizare:
#   pune-l intr-o lista (list(gen)) sau refa-l.
# - (x for x in ...) = generator;  [x for x in ...] = lista.
# - Avantaje: memorie mica (un element odata) + lazy (calcul la cerere).
# - Poti avea fluxuri INFINITE (while True + yield); controlezi cu
#   break sau itertools.islice.
# - Da generatorul direct lui sum/max/min/any/all/"".join(...) ca sa
#   eviti liste intermediare.
# - yield from = retransmite toate valorile altui generator.
#
# CAND folosesti generatori (in loc de liste):
#   - date multe / fisiere mari / fluxuri (procesare in flux)
#   - cand nu ai nevoie de toate valorile deodata
#   - cand vrei pipeline-uri (sursa -> filtru -> transformare)
# CAND NU:
#   - cand chiar ai nevoie de toata colectia (indexare, len, reparcurgere)
# =============================================================