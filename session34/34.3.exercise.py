# EXERCITIUL 3  (PYDANTIC)  -  COMENZI VALIDE + RAPORT
# =============================================================
#
# CONTEXT (caz real)
# ------------------
# Primesti comenzi brute (dicturi) de la un formular de checkout. Unele
# sunt gresite (cantitate 0, pret negativ, produs gol, email invalid,
# cantitate trimisa ca text cand magazinul cere strict un numar). Le
# VALIDEZI cu Pydantic, pastrezi doar comenzile bune si scoti un raport pe
# ele. Fiecare comanda are si emailul clientului, optional un link catre
# produs si optional un token de plata (care nu trebuie sa apara niciodata
# in clar intr-un print/log).
#
#
# CE AI DE FACUT
# --------------
# 1. Defineste modelul  Comanda(BaseModel)  cu constrangeri:
#       produs:        str    cu  min_length=1        (nu gol)
#       cantitate:     int    STRICT si  gt=0          (nu accepta "2" ca text)
#       pret:          float  cu  gt=0                 (strict pozitiv)
#       email_client:  EmailStr                        (email validat real)
#       link_produs:   Optional[HttpUrl] = None        (poate lipsi)
#       token_plata:   Optional[SecretStr] = None      (poate lipsi; ascuns la print)
#
#    Pentru "cantitate strict si gt=0" foloseste stilul modern:
#       Annotated[int, Field(gt=0, strict=True)]
#
# 2. parseaza_valide(brute: list) -> list[Comanda]
#       intoarce DOAR comenzile care trec validarea (sari peste cele rele).
#
# 3. total_incasat(comenzi: list) -> float
#       suma  cantitate * pret  peste comenzile date.
#
# 4. cea_mai_scumpa(comenzi: list) -> str
#       numele produsului cu cea mai mare valoare de linie (cantitate*pret).
#
# 5. nr_respinse(brute: list) -> int
#       cate comenzi brute NU trec validarea.
#
# 6. cu_link(comenzi: list) -> list[str]
#       lista SORTATA a numelor produselor care AU  link_produs  setat.
#
# 7. token_al(comenzi: list, produs: str) -> str | None
#       valoarea REALA (nu ascunsa) a tokenului de plata pentru comanda cu
#       numele  produs  dat; None daca nu exista comanda sau nu are token.
#
#
# CERINTE
# -------
#   - foloseste  Comanda.model_validate(raw)  intr-un  try/except ValidationError
#   - la  cea_mai_scumpa  foloseste  max(..., key=...)
#   - la  token_al  foloseste  .get_secret_value()  pe campul SecretStr
#
#
# OUTPUT ASTEPTAT (din codul de test de mai jos)
# ----------------------------------------------
#   nr valide: 3
#   total incasat: 10900.0
#   cea mai scumpa: laptop
#   nr respinse: 4
#   cu link: ['monitor']
#   token casti: tok_secret_123
#   token laptop: None
#
#
# INDICII
# -------
#   - cantitate:       Annotated[int, Field(gt=0, strict=True)]
#   - parseaza_valide: incearca sa validezi fiecare; la ValidationError, o sari
#   - total_incasat:   sum(c.cantitate * c.pret for c in comenzi)
#   - cea_mai_scumpa:  max(comenzi, key=lambda c: c.cantitate * c.pret).produs
#   - nr_respinse:     len(brute) - len(parseaza_valide(brute))
#   - cu_link:         sorted(c.produs for c in comenzi if c.link_produs is not None)
#   - token_al:        gaseste comanda cu acel produs; daca are token,
#                       return c.token_plata.get_secret_value(); altfel None
# =============================================================

from typing import Optional, Annotated

from pydantic import BaseModel, Field, ValidationError, EmailStr, HttpUrl, SecretStr


# ---- DATE DE PORNIRE (nu le modifica) -----------------------
brute = [
    {"produs": "laptop",  "cantitate": 2, "pret": 4500, "email_client": "ana@x.com"},
    {"produs": "mouse",   "cantitate": 0, "pret": 80,   "email_client": "b@x.com"},        # cantitate 0 -> invalid
    {"produs": "monitor", "cantitate": 1, "pret": 1200, "email_client": "c@x.com",
     "link_produs": "https://shop.example.com/monitor"},
    {"produs": "",        "cantitate": 3, "pret": 50,   "email_client": "d@x.com"},        # produs gol -> invalid
    {"produs": "casti",   "cantitate": 2, "pret": 350,  "email_client": "e@x.com",
     "token_plata": "tok_secret_123"},
    {"produs": "tastatura", "cantitate": "2", "pret": 200, "email_client": "f@x.com"},     # cantitate ca text -> invalid (strict)
    {"produs": "webcam",  "cantitate": 1, "pret": 300,  "email_client": "nu-e-email"},     # email invalid -> invalid
]


# ---- ZONA TA DE LUCRU ---------------------------------------
# TODO: defineste modelul Comanda(BaseModel) cu Field(...) si tipuri speciale
class Comanda(BaseModel):
    produs:  str = Field(min_length=1)
    cantitate: Annotated[int, Field(gt=0, strict=True)]
    pret: float= Field(gt=0)
    email_client: EmailStr
    link_produs: Optional[HttpUrl] = None
    token_plata: Optional[SecretStr] = None

def parseaza_valide(brute):
    # TODO: intoarce lista comenzilor valide (sari peste cele care pica)
    brute = []
    valide = []

    for c in brute:
        try:
            Comanda.model_validate(brute)
            valide.append(c)
        except ValidationError as e:
            pass

def total_incasat(comenzi):
    # TODO: suma cantitate * pret
    return sum(c.cantitate * c.pret for c in comenzi)


def cea_mai_scumpa(comenzi):
    # TODO: produsul cu valoarea de linie maxima
    return max(comenzi, key=lambda c: c.cantitate * c.pret).produs

def nr_respinse(brute):
    # TODO: cate NU trec validarea

    return len(brute) - len(parseaza_valide(brute))

def cu_link(comenzi):
    # TODO: numele produselor cu link_produs setat, sortate
    sortate = (c.produs for c in comenzi if c.link_produs is not None)
    print(sorted(sortate))

def token_al(comenzi, produs):
    # TODO: valoarea reala a tokenului pentru acel produs, sau None
     return   (c.token_plata.get_secret_value() for c in comenzi if c.produs == produs)



# ---- COD DE TEST (nu trebuie sa-l modifici) -----------------
valide = parseaza_valide(brute)
print("nr valide:", len(valide))                    # 3
print("total incasat:", total_incasat(valide))      # 10900.0
print("cea mai scumpa:", cea_mai_scumpa(valide))    # laptop
print("nr respinse:", nr_respinse(brute))           # 4
print("cu link:", cu_link(valide))                  # ['monitor']
print("token casti:", token_al(valide, "casti"))    # tok_secret_123
print("token laptop:", token_al(valide, "laptop"))  # None