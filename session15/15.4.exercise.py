# EXERCITIUL 7  -  CURS VALUTAR: cache care EXPIRA (TTL)
# =============================================================
#
# CONTEXT
# ------------------
# Iei cursul valutar (EUR, USD) de la un serviciu extern. Apelul e lent,
# deci ai vrea sa-l tii in cache, ca la exercitiul 1. PROBLEMA: cursul
# se schimba in timp. Daca il tii in cache la nesfarsit, vei afisa un
# curs vechi, gresit.
#
# Solutia: un cache cu "data de expirare". Tinem rezultatul, dar DOAR
# pentru cateva secunde (TTL = "time to live", cat timp e valabil). Cand
# expira, il luam din nou, proaspat. Asa imbinam viteza (cache) cu
# corectitudinea (date care nu raman vechi la nesfarsit).
#
# Durata de valabilitate o dai TU, deci decoratorul are ARGUMENT:
#       @cache_ttl(secunde=2)
#
# IDEEA NOUA fata de cache-ul de la exercitiul 1: nu memoram doar
# rezultatul, ci PERECHEA (rezultat, momentul cand l-am calculat). La
# fiecare apel verificam daca a "expirat".
#
#
# CE AI DE FACUT
# --------------
# Scrie un decorator CU ARGUMENT  cache_ttl(secunde)  care tine un
# dictionar  args -> (rezultat, moment)  si la fiecare apel:
#   1. daca argumentele sunt in cache SI nu au expirat
#      (acum - moment < secunde):
#         - afiseaza:  [cache] HIT <nume><args>
#         - intoarce rezultatul memorat (FARA sa apeleze functia)
#   2. daca sunt in cache DAR au expirat:
#         - afiseaza:  [cache] EXPIRAT <nume><args> - reiau
#         - (continui mai jos si recalculezi)
#   3. daca NU sunt deloc in cache:
#         - afiseaza:  [cache] MISS <nume><args>
#   4. la 2 si 3: apeleaza functia, memoreaza (rezultat, momentul curent)
#      si intoarce rezultatul
#   5. pastreaza identitatea functiei (@wraps)
#
# Apoi pune  @cache_ttl(secunde=1)  pe functia `curs` de mai jos.
#
#
# CERINTE
# -------
#   - decorator CU ARGUMENT = 3 nivele de functii
#   - dictionarul de cache se creeaza in decorator (traieste in closure)
#   - in dictionar stochezi un TUPLU:  memorie[args] = (rezultat, moment)
#   - "momentul" il iei cu time.perf_counter()
#   - foloseste @wraps(fn)
#
#
# OUTPUT ASTEPTAT
# ---------------
#   [cache] MISS curs('EUR',)
#   4.97
#   [cache] HIT curs('EUR',)
#   4.97
#   [cache] MISS curs('USD',)
#   4.59
#   (... asteptam sa expire cache-ul ...)
#   [cache] EXPIRAT curs('EUR',) - reiau
#   4.97
#
#
# INDICII
# -------
#   - cheia din dictionar = `args`;  valoarea = un tuplu (rezultat, moment)
#   - despachetezi cu:  rezultat, moment = memorie[args]
#   - "a expirat?"  ->  acum - moment >= secunde
#   - `{fn.__name__}{args}`  afiseaza, ex:  curs('EUR',)
# =============================================================

import time
from functools import wraps


# ---- ZONA TA DE LUCRU ---------------------------------------

def cache_ttl(secunde):
    # TODO: decorator CU argument (3 nivele).
    #       Dictionar args -> (rezultat, moment). HIT daca proaspat,
    #       EXPIRAT daca prea vechi, MISS daca lipseste. Recalculeaza la nevoie.
    ...


# "Serviciul" de curs valutar (lent). NU-l modifica - doar il decorezi.
TABEL = {"EUR": 4.97, "USD": 4.59}

# TODO: pune  @cache_ttl(secunde=1)  pe functia de mai jos.
def curs(moneda):
    time.sleep(0.1)                 # simuleaza apelul lent la serviciu
    return TABEL[moneda]


# ---- COD DE TEST (nu trebuie sa-l modifici) -----------------
print(curs("EUR"))              # MISS - prima data, ia proaspat
print(curs("EUR"))             # HIT  - din cache, instant
print(curs("USD"))              # MISS - moneda noua

print("(... asteptam sa expire cache-ul ...)")
time.sleep(1.1)                 # lasam TTL-ul sa expire

print(curs("EUR"))              # EXPIRAT - a trecut prea mult, reia
