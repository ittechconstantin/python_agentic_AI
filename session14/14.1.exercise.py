# EXERCITIUL 1  -  MAGAZIN ONLINE: cronometru + cache
# =============================================================
#
# CONTEXT
# ------------------
# Lucrezi la un magazin online. Pretul unui produs se ia dintr-o
# baza de date / dintr-un serviciu extern, iar interogarea este
# LENTA (sa zicem ~0.2 secunde per produs).
#
# Problema: pe o pagina, acelasi produs poate fi cerut de mai multe
# ori (in lista, in cosul de cumparaturi, in recomandari). Daca
# interogam baza de date de fiecare data, pagina se incarca greu.
#
# Vrei doua lucruri, FARA sa modifici functia care ia pretul:
#   1) sa MASORI cat dureaza fiecare apel (ca sa vezi cat de lent e)
#   2) sa nu mai interoghezi de doua ori pentru acelasi produs
#      (sa retii rezultatul = CACHE)
#
# Solutia: doi decoratori pe care ii pui peste functia de pret.
#
#
# CE AI DE FACUT
# --------------
# 1. Scrie un decorator  cronometreaza(fn)  care:
#       - masoara cat dureaza apelul (foloseste time.perf_counter())
#       - afiseaza:  [timp] <nume_functie><argumente> a durat <X> ms
#       - INTOARCE rezultatul functiei (nu-l pierde!)
#       - pastreaza identitatea functiei (foloseste @wraps)
#
# 2. Scrie un decorator  cache(fn)  care:
#       - tine un dictionar in care memoreaza rezultatele
#       - daca argumentele au mai fost folosite -> afiseaza
#            [cache] HIT  ...
#         si intoarce rezultatul memorat (FARA sa apeleze fn)
#       - daca nu -> afiseaza
#            [cache] MISS ... - interoghez
#         apeleaza fn, memoreaza rezultatul si il intoarce
#
# 3. Pune AMBII decoratori pe functia  pret_produs(id_produs).
#    Ordinea conteaza! Vrem ca, la un cache HIT, cronometrul sa arate
#    ~0 ms (adica timpul masurat sa INCLUDA verificarea din cache).
#    Asadar  @cronometreaza  trebuie sa fie DEASUPRA lui  @cache.
#
#
# CERINTE
# -------
#   - foloseste *args / **kwargs unde e nevoie
#   - foloseste @wraps(fn) in fiecare decorator
#   - NU modifica corpul functiei pret_produs (doar o decorezi)
#
#
# OUTPUT ASTEPTAT (aproximativ; ms-urile difera de la PC la PC)
# -------------------------------------------------------------
#   [cache] MISS pret_produs(1,) - interoghez
#   [timp] pret_produs(1,) a durat 202 ms
#   19.99
#   [cache] HIT  pret_produs(1,)
#   [timp] pret_produs(1,) a durat 0 ms
#   19.99
#   [cache] MISS pret_produs(2,) - interoghez
#   [timp] pret_produs(2,) a durat 205 ms
#   49.5
#   pret_produs
#
#
# INDICII
# -------
#   - durata in secunde * 1000 = milisecunde; formateaza cu {durata:.0f}
#   - dictionarul din cache trebuie creat IN decorator, nu in wrapper,
#     ca sa "traiasca" intre apeluri (closure)
#   - cheia din dictionar pot fi chiar argumentele: `args`
# =============================================================


import sys
import logging
from functools import wraps
import time
logging.basicConfig(level=logging.INFO, format="{levelname} | {message}", style="{", stream=sys.stdout)
log = logging.getLogger("magazin")

# ---- ZONA TA DE LUCRU ---------------------------------------

# def cronometreaza(fn):
    # TODO: scrie decoratorul (masoara timpul, afiseaza, intoarce rezultatul)

def cronometreaza(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        rezultat = fn(*args, **kwargs)
        stop = time.perf_counter()
        durata = stop - start
        log.info(f"{fn.__name__} a durat {durata:.0f} ms")
        return rezultat
    return wrapper

# @cronometreaza



# def cache(fn):
#     TODO: scrie decoratorul (HIT / MISS, memoreaza in dictionar)
def cache(fn):
    memorie = {}
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if args in memorie:
            log.info(f"HIT: {fn.__name__} args={args} kwargs={kwargs}")
            return memorie[args]
        else:
            log.info(f"MISS: {fn.__name__} args={args} kwargs={kwargs} - interoghez")
            rezultat = fn(*args, **kwargs)
            memorie[args] = rezultat
            return rezultat
    return wrapper

# Catalogul de preturi (simuleaza baza de date)
CATALOG = {1: 19.99, 2: 49.50, 3: 5.00}


# TODO: pune cei doi decoratori AICI, in ordinea corecta
@cronometreaza
@cache
def pret_produs(id_produs):
    time.sleep(0.2)                 # simuleaza interogarea lenta - NU modifica
    return CATALOG.get(id_produs, 0.0)


# ---- COD DE TEST (nu trebuie sa-l modifici) -----------------
print(pret_produs(1))           # MISS - prima data, lent
print(pret_produs(1))           # HIT  - instant, din cache
print(pret_produs(2))           # MISS - produs nou
print(pret_produs.__name__)     # trebuie sa afiseze 'pret_produs' (datorita @wraps)
