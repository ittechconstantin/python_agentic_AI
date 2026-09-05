# EXERCITIUL 2  (PYDANTIC)  -  CATALOG DE PRODUSE DIN JSON
# =============================================================
#
# CONTEXT (caz real)
# ------------------
# Primesti produse ca STRING-uri JSON (asa vin de la un API sau dintr-un
# fisier). Le parsezi cu Pydantic - care le valideaza, le converteste
# tipurile si completeaza valorile lipsa cu DEFAULT-uri. Uneori vin UNUL
# cate unul, alteori vin toate deodata, ca o LISTA JSON. Fiecare produs
# are si o CATEGORIE, dintr-un set fix de valori posibile.
#
#
# CE AI DE FACUT
# --------------
# 1. Defineste  Categorie(str, Enum)  cu valorile:
#       ELECTRONICE = "electronice"
#       ALIMENTE    = "alimente"
#       ALTELE      = "altele"
#
# 2. Defineste modelul  Produs(BaseModel):
#       nume:      str
#       pret:      foloseste stilul  Annotated[float, Field(gt=0)]
#       stoc:      int  = 0                  (default 0 daca lipseste)
#       activ:     bool = True                (default True daca lipseste)
#       categorie: Categorie = Categorie.ALTELE   (default ALTELE daca lipseste)
#
# 3. din_json(text: str) -> Produs
#       parseaza UN produs dintr-un string JSON  (model_validate_json).
#
# 4. din_json_lista(text: str) -> list[Produs]
#       parseaza o LISTA de produse dintr-un singur string JSON (un array).
#       foloseste  TypeAdapter(list[Produs])  -  NU un loop cu din_json.
#
# 5. valoare_totala(produse: list) -> float
#       suma  pret * stoc  peste toate produsele.
#
# 6. doar_active(produse: list) -> list[str]
#       lista SORTATA a numelor produselor cu  activ == True.
#
# 7. dupa_categorie(produse: list, categorie: Categorie) -> list[str]
#       lista SORTATA a numelor produselor din categoria data.
#
# 8. ca_dict(produs: Produs) -> dict
#       transforma un produs inapoi in dict  (model_dump).
#
#
# CERINTE
# -------
#   - foloseste  Produs.model_validate_json(text)  pentru UN produs
#   - foloseste  TypeAdapter(list[Produs]).validate_json(text)  pentru LISTA
#   - pretul e strict pozitiv:  Annotated[float, Field(gt=0)]
#   - observa: campurile lipsa (stoc, activ, categorie) iau valoarea default
#
#
# OUTPUT ASTEPTAT (din codul de test de mai jos)
# ----------------------------------------------
#   laptop stoc: 3
#   mouse activ: False
#   monitor stoc (default): 0
#   monitor categorie (default): Categorie.ALTELE
#   valoare totala: 17500.0
#   active: ['Laptop', 'Monitor']
#   monitor ca dict: {'nume': 'Monitor', 'pret': 1200.0, 'stoc': 0, 'activ': True, 'categorie': <Categorie.ALTELE: 'altele'>}
#   nr produse din lista: 3
#   nume din lista: ['Casti', 'Tastatura', 'Telefon']
#   electronice din lista: ['Tastatura', 'Telefon']
#
#
# INDICII
# -------
#   - Categorie:      class Categorie(str, Enum): ELECTRONICE = "electronice"; ...
#   - pret Annotated:  pret: Annotated[float, Field(gt=0)]
#   - din_json:        return Produs.model_validate_json(text)
#   - din_json_lista:  return TypeAdapter(list[Produs]).validate_json(text)
#   - valoare_totala:  aduna  p.pret * p.stoc
#   - doar_active:     sorted(p.nume for p in produse if p.activ)
#   - dupa_categorie:  sorted(p.nume for p in produse if p.categorie == categorie)
#   - ca_dict:         return produs.model_dump()
# =============================================================

from enum import Enum
from typing import Annotated

from pydantic import BaseModel, Field, TypeAdapter


# ---- DATE DE PORNIRE (nu le modifica) -----------------------
T1 = '{"nume": "Laptop", "pret": 4500, "stoc": 3}'
T2 = '{"nume": "Mouse", "pret": 80, "stoc": 50, "activ": false}'
T3 = '{"nume": "Monitor", "pret": 1200}'

T_LISTA = '''
[
    {"nume": "Telefon",   "pret": 2500, "stoc": 5, "categorie": "electronice"},
    {"nume": "Tastatura", "pret": 150,  "stoc": 20, "categorie": "electronice"},
    {"nume": "Casti",     "pret": 300,  "stoc": 8,  "categorie": "altele"}
]
'''


# ---- ZONA TA DE LUCRU ---------------------------------------
# TODO: defineste Categorie(str, Enum)
class Categorie(str, Enum):
    ELECTRONICE = 'electronice'
    ALIMENTE = "alimente"
    ALTELE = "altele"

# TODO: defineste modelul Produs(BaseModel) cu default-uri si Annotated pentru pret
class Produs(BaseModel):
    nume: str
    pret: Annotated[float, Field(gt=0)]
    stoc: int = 0
    activ: bool = True
    categorie: Categorie = Categorie.ALTELE

def din_json(text):
    # TODO: Produs.model_validate_json(text)
    return Produs.model_validate_json(text)

def din_json_lista(text):
    # TODO: TypeAdapter(list[Produs]).validate_json(text)
    return TypeAdapter(list[Produs]).validate_json(text)


def valoare_totala(produse):
    # TODO: suma pret * stoc
    if produse:
        return sum(p.pret*p.stoc for p in produse)
    else:
        return 0

def doar_active(produse):
    # TODO: numele produselor active, sortate
    return sorted(p.nume for p in produse if p.activ)


def dupa_categorie(produse, categorie):
    # TODO: numele produselor din categoria data, sortate
    return sorted(p.nume for p in produse if p.categorie == categorie)


def ca_dict(produs):
    # TODO: produs.model_dump()
    return produs.model_dump()


# ---- COD DE TEST (nu trebuie sa-l modifici) -----------------
p1, p2, p3 = din_json(T1), din_json(T2), din_json(T3)
produse = [p1, p2, p3]

print("laptop stoc:", p1.stoc)                              # 3
print("mouse activ:", p2.activ)                             # False
print("monitor stoc (default):", p3.stoc)                   # 0
print("monitor categorie (default):", p3.categorie)         # Categorie.ALTELE
print("valoare totala:", valoare_totala(produse))           # 17500.0
print("active:", doar_active(produse))                      # ['Laptop', 'Monitor']
print("monitor ca dict:", ca_dict(p3))
# {'nume': 'Monitor', 'pret': 1200.0, 'stoc': 0, 'activ': True, 'categorie': <Categorie.ALTELE: 'altele'>}

lista = din_json_lista(T_LISTA)
print("nr produse din lista:", len(lista))                          # 3
print("nume din lista:", sorted(p.nume for p in lista))             # ['Casti', 'Tastatura', 'Telefon']
print("electronice din lista:", dupa_categorie(lista, Categorie.ELECTRONICE))
# ['Tastatura', 'Telefon']