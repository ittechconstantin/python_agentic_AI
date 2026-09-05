# EXERCITIUL 1  (PYDANTIC AVANSAT)  -  CONT + COMANDA
# =============================================================
#
# CONTEXT (caz real)
# ------------------
# Validezi date de inregistrare cu reguli PROPRII: normalizezi username-ul
# si emailul (field_validator) si calculezi automat totalul unei comenzi
# din alte campuri (model_validator). Exact ce ai in orice back-end serios.
#
#
# CE AI DE FACUT
# --------------
# 1. Modelul  Utilizator(BaseModel)  cu doua  @field_validator:
#       username: str  -> .strip().lower();  ValueError daca len < 3 sau
#                         daca are spatiu.
#       email:    str  -> .strip().lower();  ValueError daca NU are exact un
#                         "@" si cel putin un ".".
#
# 2. Modelul  Comanda(BaseModel)  cu un  @model_validator(mode="after"):
#       cantitate:   int   (Field gt=0)
#       pret_unitar: float (Field gt=0)
#       total:       Optional[float] = None  -> daca e None, il calculezi
#                    ca  cantitate * pret_unitar.
#
# 3. curata_username(u: str) -> str
#       construieste un Utilizator cu emailul "x@y.com" si intoarce
#       username-ul NORMALIZAT (deci  "  Ana  " -> "ana").
#
# 4. e_valid(username: str, email: str) -> bool
#       True daca  Utilizator(username=..., email=...)  trece, altfel False.
#
# 5. total(cantitate: int, pret_unitar: float) -> float
#       construieste o Comanda si intoarce  total-ul calculat.
#
#
# CERINTE
# -------
#   - foloseste  @field_validator("camp")  si  @model_validator(mode="after")
#   - in validatori: normalizezi, apoi  raise ValueError(...)  daca e gresit
#   - prinde  ValidationError  in  e_valid
#
#
# OUTPUT ASTEPTAT (din codul de test de mai jos)
# ----------------------------------------------
#   username curatat: ana_popescu
#   valid (spatiu in user): False
#   valid (email fara @): False
#   valid ok: True
#   total comanda: 30.0
#
#
# INDICII
# -------
#   - field_validator:  @field_validator("username")  +  @classmethod
#                       def _f(cls, v): v = v.strip().lower(); ...; return v
#   - model_validator:  @model_validator(mode="after")
#                       def _f(self): if self.total is None: self.total = ...
#   - e_valid: try: Utilizator(...); return True  except ValidationError: False
# =============================================================

from typing import Optional
from pydantic import BaseModel, Field, ValidationError, field_validator, model_validator


# ---- ZONA TA DE LUCRU ---------------------------------------
# TODO: modelul Utilizator (cu 2 field_validator)
class Utilizator(BaseModel):
    username: str
    email : str

    @field_validator("username")
    @classmethod
    def norm_username(cls, v):
        v = v.strip().lower()
        if len(v) < 3:
            raise ValueError("username <3 caractere")
        if " " in v:
            raise ValueError("username cu spatiu")
        return v

    @field_validator("email")
    @classmethod
    def norm_email(cls, v):
        v = v.strip().lower()
        if v.count('@') != 1 or '.' not in v:
            raise ValueError("Contine prea multe @ ")
        return v


# TODO: modelul Comanda (cu model_validator care calculeaza total)
class Comanda(BaseModel):
    cantitate: int = Field(gt=0)
    pret_unitar: float=Field(gt=0)
    total : Optional[float] = None # daca e None, il calculam din cantitate* pret_unitar

    @model_validator(mode="after")
    def calcul_pret_final(self):
        if self.total is None:
            self.total = self.cantitate * self.pret_unitar
        return self

Comanda(cantitate=1, pret_unitar=10)
c1 = Comanda(cantitate=1, pret_unitar=10, total = 10)

def curata_username(u):
    # TODO: Utilizator(username=u, email="x@y.com").username
    return Utilizator(username=u, email="x@y.com").username


def e_valid(username, email):
    # TODO: True daca trece validarea, altfel False
    try:
        Utilizator(username=username, email=email)
        return True
    except ValidationError:
        return False


def total(cantitate, pret_unitar):
    # TODO: Comanda(cantitate=..., pret_unitar=...).total
    return  Comanda(cantitate=cantitate, pret_unitar=pret_unitar).total


# ---- COD DE TEST (nu trebuie sa-l modifici) -----------------
print("username curatat:", curata_username("  Ana_Popescu  "))     #ana_popescu
print("valid (spatiu in user):", e_valid("a b", "x@y.com"))        # False
print("valid (email fara @):", e_valid("bogdan", "invalid"))       # False
print("valid ok:", e_valid("carmen", "C@X.com"))                   # True
print("total comanda:", total(3, 10.0))                            # 30.0
