# EXERCITIUL 1  (PYDANTIC)  -  VALIDARE DE INSCRIERI
# =============================================================
#
# CONTEXT (caz real)
# ------------------
# Primesti inscrieri (dicturi) dintr-un formular / API si trebuie sa le
# validezi inainte sa le salvezi: numele destul de lung, varsta intr-un
# interval rezonabil, email cu forma corecta. Definesti o SCHEMA Pydantic
# si scrii cateva functii care o folosesc.
#
#
# CE AI DE FACUT
# --------------
# 1. Defineste modelul  Inscriere(BaseModel)  cu constrangeri (Field):
#       nume:   str  cu  min_length=2
#       varsta: int  cu  ge=0  si  le=130
#       email:  str  cu  pattern=r"^.+@.+\..+$"
#
# 2. e_valid(raw: dict) -> bool
#       True daca  raw  trece validarea, False daca arunca ValidationError.
#
# 3. erori(raw: dict) -> list[str]
#       lista mesajelor de eroare (er["msg"]) sau [] daca e valid.
#
# 4. separa(intrari: list) -> tuple
#       intoarce  (nume_valide, nr_invalide):  lista NUMELOR inscrierilor
#       valide  si  numarul celor invalide.
#
#
# CERINTE
# -------
#   - foloseste  Inscriere.model_validate(raw)  intr-un  try/except
#   - prinde  ValidationError
#   - la coercitie: "30" (string) trebuie sa treaca ca varsta valida
#
#
# OUTPUT ASTEPTAT (din codul de test de mai jos)
# ----------------------------------------------
#   valid (coercion): True
#   valid (nume scurt): False
#   valid (varsta text): False
#   nr erori (input rau): 3
#   nume valide: ['Ana']
#   nr invalide: 4
#
#
# INDICII
# -------
#   - model: class Inscriere(BaseModel): nume: str = Field(min_length=2) ...
#   - e_valid: try: Inscriere.model_validate(raw); return True
#              except ValidationError: return False
#   - erori:   except ValidationError as e: return [er["msg"] for er in e.errors()]
#   - separa:  parcurge intrarile, aduna numele valide si numara invalidele
# =============================================================

from pydantic import BaseModel, Field, ValidationError


# ---- DATE DE PORNIRE (nu le modifica) -----------------------
intrari = [
    {"nume": "Ana",    "varsta": 28,         "email": "ana@x.com"},
    {"nume": "X",      "varsta": 28,         "email": "x@y.com"},        # nume prea scurt
    {"nume": "Bogdan", "varsta": 200,        "email": "b@x.com"},        # varsta prea mare
    {"nume": "Carmen", "varsta": "treizeci", "email": "c@x.com"},        # varsta nu e numar
    {"nume": "Dan",    "varsta": 40,         "email": "dan-fara-at"},    # email invalid
]


# ---- ZONA TA DE LUCRU ---------------------------------------
# TODO: defineste modelul Inscriere(BaseModel) cu Field(...)
class Inscriere(BaseModel):
    nume:   str = Field(min_length=2)
    varsta: int = Field(ge=0, le=130)
    email:  str = Field(pattern=r"^.+@.+\..+$")

def e_valid(raw):
    # TODO: True daca raw trece validarea, altfel False
    try:
        Inscriere.model_validate(raw); return True
    except ValidationError:
        return False


def erori(raw):
    # TODO: lista mesajelor de eroare, sau [] daca e valid
    lista_erori = []
    try:
        Inscriere.model_validate(raw)
    except ValidationError as e:
        return [er["msg"] for er in e.errors()]

def separa(intrari):
    # TODO: intoarce (nume_valide, nr_invalide)
    nume_valide, nr_invalide = intrari[0]['nume'], intrari[0]['varsta']
    nr_invalide = []
    for raw in intrari:
        try:
            raw['nume']
        except ValidationError as e:
            return [er["msg"] for er in e.errors()]
        if raw['nume'] != nume_valide:
            nr_invalide.append(raw)


    return ([nume_valide], len(nr_invalide))
# ---- COD DE TEST (nu trebuie sa-l modifici) -----------------
print("valid (coercion):", e_valid({"nume": "Ana", "varsta": "30", "email": "a@b.com"}))    # True
print("valid (nume scurt):", e_valid({"nume": "X", "varsta": 30, "email": "x@y.com"}))      # False
print("valid (varsta text):", e_valid({"nume": "Ana", "varsta": "abc", "email": "a@b.com"}))  # False
print("nr erori (input rau):", len(erori({"nume": "X", "varsta": "abc", "email": "bad"})))   # 3

nume_valide, nr_invalide = separa(intrari)
print("nume valide:", nume_valide)     # ['Ana']
print("nr invalide:", nr_invalide)     # 4
