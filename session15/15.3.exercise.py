# EXERCITIUL 6  -  JOC RPG: cooldown la vraji (decorator cu memorie)
# =============================================================
#
# CONTEXT
# ------------------
# Faci un joc. Personajul are vraji puternice (minge de foc, vindecare).
# Ca sa fie echilibrat, o vraja NU poate fi aruncata oricat de des: dupa
# ce o folosesti, intra in "cooldown" (reincarcare) cateva secunde, timp
# in care nu o poti folosi din nou.
#
# Vrei un decorator care:
#   - lasa vraja sa se execute
#   - tine minte MOMENTUL ultimei folosiri
#   - daca incerci din nou prea repede (n-au trecut destule secunde) ->
#     refuza si spune cat mai ai de asteptat
#
# Durata cooldown-ului o dai TU, deci decoratorul are ARGUMENT:
#       @cooldown(secunde=3)
#
# IDEEA NOUA fata de exercitiile dinainte: decoratorul are MEMORIE care
# se schimba in timp (ultima folosire). O tinem intr-o variabila din
# functia exterioara si o actualizam cu `nonlocal` (ca la contoarele
# din sesiunea 13).
#
#
# CE AI DE FACUT
# --------------
# Scrie un decorator CU ARGUMENT  cooldown(secunde)  care:
#   1. tine o variabila  ultima_folosire  (initial None)
#   2. la fiecare apel, citeste timpul curent cu time.perf_counter()
#   3. daca vraja a mai fost folosita SI nu au trecut `secunde` de atunci:
#         - NU rula vraja
#         - intoarce textul:
#              "<nume> in reincarcare, mai astepti <X>s"
#           unde X = cate secunde mai sunt pana se termina cooldown-ul
#   4. altfel: memoreaza momentul curent ca ultima folosire si ruleaza vraja
#   5. pastreaza identitatea functiei (@wraps)
#
# Apoi pune  @cooldown(secunde=1)  pe cele doua vraji de mai jos.
#
#
# CERINTE
# -------
#   - decorator CU ARGUMENT = 3 nivele de functii
#   - foloseste  nonlocal ultima_folosire  in wrapper ca sa o poti actualiza
#   - timpul ramas = secunde - (acum - ultima_folosire)
#   - foloseste @wraps(fn)
#
#
# OUTPUT ASTEPTAT (secundele ramase pot varia foarte putin)
# ---------------------------------------------------------
#   Minge de foc aruncata! -30 HP inamicului
#   minge_de_foc in reincarcare, mai astepti 1.0s
#   (... asteptam sa treaca cooldown-ul ...)
#   Minge de foc aruncata! -30 HP inamicului
#   Vindecare! +25 HP
#
#
# INDICII
# -------
#   - cele doua vraji au cooldown-uri SEPARATE: fiecare functie decorata
#     are propria ei  ultima_folosire  (closure diferit per decorare)
#   - prima folosire e mereu permisa (ultima_folosire e None)
#   - formateaza secundele ramase cu  {ramas:.1f}
# =============================================================

import time
from functools import wraps


# ---- ZONA TA DE LUCRU ---------------------------------------

memorie = {}
def cooldown(secunde):
    # TODO: decorator CU argument (3 nivele).
    #       Tine `ultima_folosire` (nonlocal), compara cu timpul curent,
    #       refuza daca e prea devreme, altfel actualizeaza si ruleaza.
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            acum = time.perf_counter()
            rezultat = fn(*args, **kwargs)
            ultima_folosire = time.perf_counter()
            timpul_curent = acum - ultima_folosire
            timpul_ramas = secunde - acum
            if timpul_ramas < secunde and ultima_folosire < secunde:
                return print(f"{fn}nume in reincarcare, mai astepti {timpul_ramas}s")
            else:
                memorie[args] = rezultat
                return rezultat
        return wrapper
    return decorator

# TODO: pune  @cooldown(secunde=1)  pe ambele vraji.

@cooldown(secunde=1)
def minge_de_foc():
    return "Minge de foc aruncata! -30 HP inamicului"

@cooldown(secunde=1)
def vindecare():
    return "Vindecare! +25 HP"


# ---- COD DE TEST (nu trebuie sa-l modifici) -----------------
print(minge_de_foc())           # prima folosire -> permis
print(minge_de_foc())           # imediat din nou -> in reincarcare

print("(... asteptam sa treaca cooldown-ul ...)")
time.sleep(1.1)                 # lasam cooldown-ul sa expire

print(minge_de_foc())           # a trecut destul timp -> permis iar
print(vindecare())              # alta vraja, cooldown propriu -> permis
