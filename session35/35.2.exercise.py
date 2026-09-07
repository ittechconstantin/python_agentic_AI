# EXERCITIUL 2  (PYDANTIC AVANSAT)  -  PAYLOAD DE LA UN API EXTERN
# =============================================================
#
# CONTEXT (caz real)
# ------------------
# Un serviciu extern (ex: un CRM, un webhook de plati) iti trimite date in
# camelCase: "firstName", "lastName", "location", "registeredAt". In
# Python vrei snake_case si validare, iar cateodata trebuie sa trimiti
# datele INAPOI in acelasi format camelCase - dar formatat FRUMOS, nu ca
# ISO brut. In plus, unele campuri numerice vin "murdare" (ex: varsta
# trimisa ca "35 ani", nu ca numar curat) si trebuie curatate INAINTE ca
# Pydantic sa incerce conversia.
#
#
# CE AI DE FACUT
# --------------
# 1. Modelul  Locatie(BaseModel):  oras: str,  tara: str.
#
# 2. Modelul  Client(BaseModel)  care accepta numele in camelCase prin alias:
#       model_config = ConfigDict(populate_by_name=True)
#       prenume:     str      cu  alias="firstName"
#       nume:        str      cu  alias="lastName"
#       varsta:      int      cu  alias="age"  si  ge=0
#       locatie:     Locatie  cu  alias="location"        (model imbricat!)
#       inregistrat: date     cu  alias="registeredAt"
#
#    Adauga un  @field_validator("varsta", mode="before")  care, DACA
#    valoarea e string, pastreaza doar cifrele din ea (ex: "35 ani" -> "35")
#    inainte ca Pydantic sa incerce sa o converteasca la int.
#
#    Adauga un  @field_serializer("inregistrat")  care formateaza data la
#    EXPORT ca "10 mai 2026" (ziua, luna scurta in romana, anul) - fara sa
#    schimbe cum e stocat campul intern (ramane un obiect  date  normal).
#
# 3. din_api(payload: dict) -> Client
#       valideaza payload-ul camelCase intr-un Client (model_validate).
#
# 4. nume_complet(client) -> str
#       prenume + " " + nume.
#
# 5. inapoi_api(client) -> dict
#       exporta clientul INAPOI in camelCase  (model_dump cu by_alias=True).
#       "registeredAt" va aparea deja formatat frumos, datorita serializerului.
#
#
# CERINTE
# -------
#   - foloseste  Field(alias="...")  si  ConfigDict(populate_by_name=True)
#   - modelul Client contine un model Locatie (nested), validat automat
#   - "varsta" foloseste  mode="before"  ca sa curete textul INAINTE de coercitie
#   - "inregistrat" foloseste  @field_serializer  pentru formatul de export
#
#
# OUTPUT ASTEPTAT (din codul de test de mai jos)
# ----------------------------------------------
#   prenume: Ana
#   oras: Cluj
#   nume complet: Ana Pop
#   inapoi api: {'firstName': 'Ana', 'lastName': 'Pop', 'age': 28, 'location': {'oras': 'Cluj', 'tara': 'RO'}, 'registeredAt': '10 mai 2026'}
#   varsta curatata (text): 35
#
#
# INDICII
# -------
#   - alias:          prenume: str = Field(alias="firstName")
#   - nested:          locatie: Locatie = Field(alias="location")
#   - mode="before":   @field_validator("varsta", mode="before")
#                       def _f(cls, v):
#                           if isinstance(v, str):
#                               v = "".join(ch for ch in v if ch.isdigit())
#                           return v
#   - field_serializer: @field_serializer("inregistrat")
#                       def _f(self, v: date) -> str: ... return f"{v.day} {luna} {v.year}"
#   - din_api:         return Client.model_validate(payload)
#   - inapoi_api:      return client.model_dump(by_alias=True)
# =============================================================

from datetime import date

from pydantic import BaseModel, Field, ConfigDict, field_validator, field_serializer


# ---- DATE DE PORNIRE (nu le modifica) -----------------------
PAYLOAD = {
    "firstName": "Ana",
    "lastName":  "Pop",
    "age":       28,
    "location":  {"oras": "Cluj", "tara": "RO"},
    "registeredAt": "2026-05-10",
}

PAYLOAD_TEXT_AGE = {
    "firstName": "Bogdan",
    "lastName":  "Ionescu",
    "age":       "35 ani",
    "location":  {"oras": "Iasi", "tara": "RO"},
    "registeredAt": "2026-01-15",
}


# ---- ZONA TA DE LUCRU ---------------------------------------
# TODO: modelul Locatie(BaseModel)
class Locatie(BaseModel):
    oras: str
    tara: str

# TODO: modelul Client(BaseModel) cu alias-uri, Locatie imbricat,
#       field_validator(mode="before") pe varsta, field_serializer pe inregistrat
class Client(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    prenume:     str = Field(alias="firstName")
    nume:        str = Field(alias="lastName")
    varsta:      int = Field(alias="age", ge = 0)
    locatie: Locatie = Field(alias="location")
    inregistrat: date = Field(alias="registeredAt")

    @field_validator("varsta", mode = "before")
    @classmethod
    def curata_varsta(cls, v):
        if isinstance(v, str):
            v = "".join(ch for ch in v if ch.isdigit())
        return v


    @field_serializer("inregistrat")
    @classmethod
    def serializeaza_data(cls, v: date) -> str:
        luna = {
            1 : "jan",
            2 : "feb",
            3 : "mar",
            4 : "apr",
            5 : "mai",
            6 : "iun",
            7 : "iul",
            8 : "aug",
            9 : "sep",
            10 : "oct",
            11 : "nov",
            12 : "dec",
        }
        return f"{v.day} {luna[v.month]} {v.year}"

def din_api(payload):
    # TODO: Client.model_validate(payload)
    return Client.model_validate(payload)


def nume_complet(client):
    # TODO: prenume + " " + nume
    return f"{client.prenume + " " + client.nume}"


def inapoi_api(client):
    # TODO: client.model_dump(by_alias=True)
    return client.model_dump(by_alias=True)


# ---- COD DE TEST (nu trebuie sa-l modifici) -----------------
c = din_api(PAYLOAD)
print("prenume:", c.prenume)               # Ana
print("oras:", c.locatie.oras)             # Cluj
print("nume complet:", nume_complet(c))    # Ana Pop
print("inapoi api:", inapoi_api(c))
# {'firstName': 'Ana', 'lastName': 'Pop', 'age': 28, 'location': {'oras': 'Cluj', 'tara': 'RO'}, 'registeredAt': '10 mai 2026'}

c2 = din_api(PAYLOAD_TEXT_AGE)
print("varsta curatata (text):", c2.varsta)   # 35