# EXERCITIUL 4  -  SERVER INSTABIL: reincearca automat (retry)
# =============================================================
#
# CONTEXT
# ------------------
# Apelezi un serviciu extern (procesare plati, trimitere SMS, API de
# vreme). Problema serviciilor de pe internet: uneori "pica" pentru o
# clipa si arunca o eroare, desi peste o secunda merg perfect.
#
# Solutia  NU e sa renunti la prima eroare, ci sa
# REINCERCI automat de cateva ori. Daca a 2-a sau a 3-a incercare
# reuseste, utilizatorul nici nu observa ca a fost o problema.
#
# Vrei un decorator care:
#   - apeleaza functia
#   - daca arunca o eroare -> mai incearca (de un numar de ori dat de TINE)
#   - daca o incercare reuseste -> intoarce rezultatul si se opreste
#   - daca s-au terminat toate incercarile -> arunca eroarea mai departe
#
# Pentru ca numarul de incercari il dai tu, decoratorul are ARGUMENT:
#       @reincearca(incercari=3)
#
#
# CE AI DE FACUT
# --------------
# Scrie un decorator CU ARGUMENT  reincearca(incercari)  care:
#   1. incearca sa apeleze functia, intr-o bucla, de maxim `incercari` ori
#   2. daca apelul reuseste -> INTOARCE rezultatul imediat (gata)
#   3. daca apelul arunca o exceptie:
#         - afiseaza:  [reincearca] incercarea <i>/<incercari> a esuat: <mesaj>
#         - daca mai sunt incercari -> mai incearca
#         - daca a fost ULTIMA incercare -> arunca eroarea mai departe (raise)
#   4. pastreaza identitatea functiei (@wraps)
#
# Apoi pune  @reincearca(incercari=3)  pe cele doua functii de mai jos.
#
#
# CERINTE
# -------
#   - decorator CU ARGUMENT = 3 nivele de functii
#       def reincearca(incercari):
#           def decorator(fn):
#               def wrapper(*a, **kw): ...
#   - foloseste try / except in interiorul buclei
#   - cand se termina incercarile, foloseste `raise` (gol) ca sa
#     re-arunci ULTIMA exceptie prinsa
#   - foloseste @wraps(fn)
#
#
# OUTPUT ASTEPTAT
# ---------------
#   [reincearca] incercarea 1/3 a esuat: serviciu indisponibil
#   [reincearca] incercarea 2/3 a esuat: serviciu indisponibil
#   plata confirmata: 250 lei
#   [reincearca] incercarea 1/3 a esuat: retea cazuta
#   [reincearca] incercarea 2/3 a esuat: retea cazuta
#   [reincearca] incercarea 3/3 a esuat: retea cazuta
#   a renuntat definitiv: retea cazuta

# =============================================================

from functools import wraps


# ---- ZONA TA DE LUCRU ---------------------------------------

def reincearca(incercari):
    # TODO: decorator CU argument (3 nivele).
    #       Bucla cu try/except: la succes return, la esec afiseaza si re-incearca,
    #       iar la ultima incercare -> raise.
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            for i in range(1, incercari + 1):
                try:
                    return fn(*args, **kwargs)
                except Exception as e:
                    print(f" [reincearca] incercarea {i}/{incercari} a esuat: {e}")
                    if i == incercari:
                        raise
            return wrapper
        return decorator


# ---- SERVICII DATE (simuleaza internetul instabil; NU le modifica) ----

# `confirma_plata` esueaza primele 2 ori, apoi merge (problema trecatoare).
stare_plata = {"apeluri": 0}
@reincearca
def confirma_plata(suma):
    stare_plata["apeluri"] += 1
    if stare_plata["apeluri"] < 3:
        raise ConnectionError("serviciu indisponibil")
    return f"plata confirmata: {suma} lei"

# `trimite_sms` e mereu picat (problema serioasa) -> va epuiza incercarile.
def trimite_sms(numar, text):
    raise ConnectionError("retea cazuta")


# TODO: pune  @reincearca(incercari=3)  pe ambele functii de mai sus.
#       (muta decoratorul deasupra lor)


# ---- COD DE TEST (nu trebuie sa-l modifici) -----------------
try:
    print(confirma_plata(250))          # reuseste la a 3-a incercare
except ConnectionError as e:
    print("a renuntat definitiv:", e)

try:
    trimite_sms("0712...", "Salut!")    # esueaza de fiecare data
except ConnectionError as e:
    print("a renuntat definitiv:", e)