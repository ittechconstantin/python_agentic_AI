# EXERCITIUL 3  -  MONITORIZARE: alerta cand o operatiune e LENTA
# =============================================================
#
# CONTEXT
# ------------------
# Intr-o aplicatie reala, unele operatiuni TREBUIE sa fie rapide
# (o cautare pe site, incarcarea unei pagini). Daca devin lente,
# vrei sa fii ANUNTAT, ca sa investighezi inainte sa se planga
# utilizatorii.
#
# Vrei un decorator care:
#   - masoara cat dureaza o functie
#   - daca a durat MAI MULT decat un prag pe care il dai TU
#     (ex: 100 ms) -> scrie un WARNING in jurnal
#   - daca a fost sub prag -> scrie un mesaj normal (INFO)
#
# Important: pragul difera de la o functie la alta (o cautare are
# alt prag fata de un raport anual). De aceea decoratorul trebuie
# sa primeasca pragul ca ARGUMENT:  @alerta_daca_lent(prag_ms=100)
#
#
# RECAP RAPID DESPRE logging (folosit in lectie, sectiunea 8)
# -----------------------------------------------------------
# In loc de print(), folosim modulul `logging`. Fiecare mesaj are
# un NIVEL:
#       log.info("...")     -> mesaj normal  -> apare ca  INFO | ...
#       log.warning("...")  -> avertisment   -> apare ca  WARNING | ...
# Configurarea (data deja mai jos) trimite mesajele pe ecran.
#
#
# CE AI DE FACUT
# --------------
# Scrie un decorator CU ARGUMENT  alerta_daca_lent(prag_ms)  care:
#   1. masoara durata apelului (time.perf_counter(), in milisecunde)
#   2. apeleaza functia si retine rezultatul
#   3. daca durata > prag_ms:
#         log.warning(f"{nume} LENT: {durata} ms (peste pragul de {prag_ms} ms)")
#      altfel:
#         log.info(f"{nume} ok: {durata} ms")
#   4. INTOARCE rezultatul functiei
#   5. pastreaza identitatea functiei (@wraps)
#
# Apoi pune  @alerta_daca_lent(prag_ms=100)  pe cele doua functii
# de mai jos si ruleaza.
#
#
# CERINTE
# -------
#   - decorator CU ARGUMENT = 3 nivele de functii
#       def alerta_daca_lent(prag_ms):
#           def decorator(fn):
#               def wrapper(*a, **kw): ...
#   - foloseste log.warning / log.info (NU print)
#   - foloseste @wraps(fn)
#
#
# OUTPUT ASTEPTAT (ms-urile pot varia putin)
# ------------------------------------------
#   INFO | cauta_produse ok: 50 ms
#   ['laptop-0', 'laptop-1', 'laptop-2']
#   WARNING | genereaza_raport_anual LENT: 253 ms (peste pragul de 100 ms)
#   raport anual gata
#
#
# INDICII
# -------
#   - durata = (perf_counter dupa - perf_counter inainte) * 1000
#   - formateaza ms-urile cu {durata:.0f} (fara zecimale)
#   - pragul (prag_ms) e disponibil in interiorul wrapper-ului datorita
#     closure-ului (l-a primit functia exterioara)
# =============================================================

import time
import logging
import sys
from functools import wraps

# Configurarea jurnalului (data gata; trimite mesajele pe ecran):
logging.basicConfig(
    level=logging.INFO,
    format="{levelname} | {message}",
    style="{",
    stream=sys.stdout,
)
log = logging.getLogger("monitor")


# ---- ZONA TA DE LUCRU ---------------------------------------

def alerta_daca_lent(prag_ms):
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            start = time.perf_counter()
            rezultat = fn(*args, **kwargs)
            stop = time.perf_counter()
            durata = (stop - start) * 1000
            if durata > prag_ms:
                log.warning(f"{fn.__name__} LENT: {durata:.0f} ms (peste pragul de {prag_ms} ms)")
            else:
                log.info(f"{fn.__name__} ok: {durata:.0f} ms")
            return rezultat
        return wrapper
    return decorator

# TODO: pune  @alerta_daca_lent(prag_ms=100)  pe ambele functii
@alerta_daca_lent(prag_ms=100)
def cauta_produse(termen):
    time.sleep(0.05)                # rapid (~50 ms) -> sub prag -> INFO
    return [f"{termen}-{i}" for i in range(3)]

@alerta_daca_lent(100)
def genereaza_raport_anual():
    time.sleep(0.25)                # lent (~250 ms) -> peste prag -> WARNING
    return "raport anual gata"


# ---- COD DE TEST (nu trebuie sa-l modifici) -----------------
print(cauta_produse("laptop"))      # ar trebui sa logheze INFO (ok)
print(genereaza_raport_anual())     # ar trebui sa logheze WARNING (lent)

























