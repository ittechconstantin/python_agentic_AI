# EXERCITIUL 2  -  APLICATIE BANCARA: validare + autorizare
# =============================================================
#
# CONTEXT
# ------------------
# Construiesti partea de operatiuni dintr-o aplicatie bancara.
# Ai cateva operatiuni: depunere, retragere, inchidere de cont.
#
# Doua reguli apar IN MAI MULTE locuri, deci nu vrei sa le copiezi:
#   - REGULA DE BANI: o suma de operat trebuie sa fie pozitiva
#     (nu poti depune/retrage 0 sau o suma negativa)
#   - REGULA DE ACCES: doar anumiti utilizatori au voie sa faca
#     anumite operatiuni (ex: doar un "admin" poate inchide un cont)
#
# Solutia: doi decoratori-"paznici" pe care ii pui peste operatiuni.
# Astfel, operatiunea propriu-zisa ramane curata, iar verificarile
# stau separat si se REFOLOSESC.
#
#
# CE AI DE FACUT
# --------------
# 1. Scrie un decorator  suma_valida(fn)  care:
#       - se asteapta ca functia decorata sa primeasca (cont, suma, ...)
#       - daca  suma <= 0  ->  raise ValueError cu mesajul:
#            "suma trebuie sa fie pozitiva, am primit <suma>"
#       - altfel apeleaza functia normal si intoarce rezultatul
#
# 2. Scrie un decorator CU ARGUMENT  necesita_rol(rol_cerut)  care:
#       - se uita la  utilizator_curent["rol"]
#       - daca rolul curent NU e cel cerut  ->  raise PermissionError:
#            "nevoie de rol '<rol_cerut>', tu esti '<rol_curent>'"
#       - altfel apeleaza functia normal
#    ATENTIE: decorator CU ARGUMENT inseamna 3 nivele de functii:
#       def necesita_rol(rol_cerut):   <- primeste configurarea
#           def decorator(fn):          <- primeste functia
#               def wrapper(*a, **kw):  <- ruleaza la fiecare apel
#
# 3. Aplica decoratorii pe operatiuni:
#       - depune(cont, suma)        -> doar suma_valida
#       - retrage(cont, suma)       -> necesita_rol("client") SI suma_valida
#                                      (le STIVUIESTI: amandoi trebuie sa treaca)
#       - inchide_cont(cont)        -> doar necesita_rol("admin")
#
#
# CERINTE
# -------
#   - foloseste @wraps(fn) in fiecare wrapper
#   - la retrage, pune  @necesita_rol("client")  DEASUPRA lui  @suma_valida
#     (intai verificam accesul, apoi suma)
#   - operatiunile modifica dictionarul `conturi` (soldurile)
#
#
# OUTPUT ASTEPTAT
# ---------------
#   sold dupa depunere: 1200.0
#   sold dupa retragere: 1100.0
#   respins (suma): suma trebuie sa fie pozitiva, am primit -5
#   respins (rol): nevoie de rol 'admin', tu esti 'client'
#   cont RO02 inchis, sold returnat 500.0
#
#
# INDICII
# -------
#   - "utilizatorul logat" e simulat de dictionarul global utilizator_curent
#   - ca sa testezi accesul de admin, schimbi utilizator_curent["rol"]
#   - cand un decorator face `raise`, functia decorata NICI nu mai ruleaza
# =============================================================

from functools import wraps

# "Sesiunea" utilizatorului logat (simulata) si conturile din banca:
utilizator_curent = {"nume": "Ana", "rol": "client"}
conturi = {"RO01": 1000.0, "RO02": 500.0}


# ---- ZONA TA DE LUCRU ---------------------------------------

def suma_valida(fn):
    @wraps(fn)
    def wrapper(suma, *args, **kwargs):
        if suma(conturi) <= 0:
            raise ValueError(f"suma trebuie sa fie pozitiva, am primit {suma}")
        else:
            return fn(suma, *args, **kwargs)
    return wrapper

def necesita_rol(rol_cerut):
    def decorator(fn):
        @wraps(fn)
        def wrapper(suma, *args, **kwargs):
            if utilizator_curent["rol"] == rol_cerut:
                return fn(suma, *args, **kwargs)
            else:
                raise PermissionError(f"nevoie de rol '{rol_cerut}', tu esti '{utilizator_curent["rol"]}'")
        return wrapper
    return decorator

# TODO: decoreaza corect fiecare operatiune


@suma_valida
def depune(cont, suma):
    conturi[cont] += suma
    return conturi[cont]

@necesita_rol("client")
@suma_valida
def retrage(cont, suma):
    conturi[cont] -= suma
    return conturi[cont]

@necesita_rol("admin")
def inchide_cont(cont):
    sold = conturi.pop(cont)
    return f"cont {cont} inchis, sold returnat {sold}"


# ---- COD DE TEST (nu trebuie sa-l modifici) -----------------

print("sold dupa depunere:", depune("RO01", 200))     # 1200.0
print("sold dupa retragere:", retrage("RO01", 100))   # 1100.0 (Ana e client, ok)

try:
    retrage("RO01", -5)                               # suma invalida
except ValueError as e:
    print("respins (suma):", e)

try:
    inchide_cont("RO02")                              # Ana NU e admin
except PermissionError as e:
    print("respins (rol):", e)

utilizator_curent["rol"] = "admin"                    # ne logam ca admin
print(inchide_cont("RO02"))                           # acum merge
