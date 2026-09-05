# PYDANTIC (partea 2)  -  validatori, modele compuse, alias-uri,
#                          serializatori, Union, Generic, config
# =============================================================
# In fisierul anterior am invatat baza (schema + Field + tipuri speciale +
# coercitie). Acum adaugam lucrurile pe care le folosesti in aplicatii
# reale, mai mari:
#   - reguli PROPRII de validare/normalizare (nu doar cele din Field)
#   - modele care CONTIN alte modele (nested)
#   - date/ore, alias-uri (camelCase vs snake_case)
#   - control pe EXPORT (serializatori proprii)
#   - un camp care poate fi UNUL din mai multe forme de model (Union)
#   - o "forma" de model refolosita cu orice tip (Generic)
#
# Ideea principala, ca PROBLEMA -> SOLUTIE:
#   PROBLEMA: Field(...) stie doar reguli simple (lungime, interval, regex).
#             Dar tu vrei: "fa username lowercase si fara spatii", "calculeaza
#             pretul final din alte campuri", "valideaza si adresa dinauntru",
#             "un webhook poate trimite fie o plata reusita, fie una esuata",
#             "config-ul aplicatiei sa vina din variabile de mediu".
#   SOLUTIA:  validatori proprii (@field_validator, @model_validator),
#             modele imbricate, serializatori proprii, Union cu
#             discriminator, Generic[T], si BaseSettings.
#
# CERINTE:  pip install pydantic pydantic-settings
#
# Ce trebuie sa stii deja (recap):
#   - Pydantic basics: BaseModel, Field, tipuri speciale, model_validate,
#     ValidationError, Annotated (fisierul anterior)
#   - decoratori (s14/15), datetime
# =============================================================

import os
from datetime import datetime, date
from typing import Optional, List, Literal, Union, Generic, TypeVar, TypedDict

from pydantic import (
    BaseModel, Field, ValidationError,
    field_validator, model_validator, ConfigDict,
    field_serializer, model_serializer,
    TypeAdapter, dataclasses as pyd_dataclasses, SecretStr, EmailStr,
)


# #############################################################
# PARTEA 1 - VALIDATORI PROPRII
# #############################################################


# 1. PROBLEMA -> SOLUTIA: @field_validator (reguli pe UN camp)
# -------------------------------------------------------------
# Field(...) nu poate face "lowercase + fara spatii + are cifra". Pentru
# reguli proprii scrii o metoda decorata cu  @field_validator("camp"):
#   - primeste valoarea, o poate NORMALIZA (strip, lower) si o intoarce
#   - daca e invalida, arunca  ValueError(...)  cu un mesaj clar
# Implicit ruleaza in mode="after" - adica DUPA ce Pydantic a incercat
# deja coercitia standard (ex: "30" -> 30 la un int).

class Cont(BaseModel):
    username : str
    parola   : SecretStr
    email    : EmailStr

    @field_validator("username")
    @classmethod
    def norm_username(cls, v):
        v = v.strip().lower()  #   an a
        if len(v) < 3:
            raise ValueError("Username-ul are mai putin de 3 caractere")

        if " " in v:
            raise ValueError("Username-ul nu poate avea spatii")

        return v   # intoarcem valoarea

try:
    c = Cont(username='a', parola="pass", email= "ana")
    print(c.username)
except ValidationError as e:
    print(e)


# 2. mode="before": transformi valoarea INAINTE de coercitia standard
# -------------------------------------------------------------
# field_validator normal (mode="after") primeste valoarea DUPA ce Pydantic
# a incercat deja sa o converteasca la tip. Uneori vrei sa intervii MAI
# DEVREME - de exemplu, datele vin ca "1.234,56" (format RO) si trebuie
# curatate INAINTE ca Pydantic sa incerce sa faca float() din ele.

class Factura(BaseModel):
    suma : float

    @field_validator("suma", mode="before")
    @classmethod
    def normalizare_suma(cls, v):
        if isinstance(v, str):
            v = v.replace(".", "").replace(",", '.')
            return v

f = Factura(suma = "1.234,56")
print(f.suma, type(f.suma))


# 3. @model_validator: reguli care ating MAI MULTE campuri
# -------------------------------------------------------------
# field_validator vede un singur camp. Cand regula depinde de mai multe
# campuri (sau vrei sa CALCULEZI un camp), folosesti  @model_validator.
# mode="after" ruleaza dupa ce toate campurile au fost validate; primesti
# obiectul intreg (self).


class Comanda(BaseModel):
    pret_brut: float = Field(gt=0)
    discount: float = Field(ge=0, le=100)
    pret_final: Optional[float] = None   # il vom calcula noi

    @model_validator(mode="after")
    def calcul(self):
        if self.pret_final is None:
            self.pret_final = self.pret_brut * (100 - self.discount)/ 100
        return self


c = Comanda(pret_brut=100, discount=15)
print(c.pret_final)
# #############################################################
# PARTEA 2 - MODELE COMPUSE + TIMP
# #############################################################



# 4. LISTE DE MODELE
# -------------------------------------------------------------
# Un camp poate fi o lista de modele - fiecare element e validat.

class Adresa(BaseModel):
    strada: str
    oras: str


class Firma(BaseModel):
    nume   : str
    birouri: List[Adresa]

fi = Firma(nume="Firma mea SRL", birouri=[
    {'strada': 'Mihai Eminescu nr.5', "oras": "Cluj"},
    {'strada': 'Mihai Cosbug nr.5', "oras": "Bucuresti"}
])

print(f"nr birouri", len(fi.birouri), "primul birou este", fi.birouri[0].oras)

# #############################################################
# PARTEA 3 - INTRARE / IESIRE (alias-uri, export, serializatori)
# #############################################################



# 5. EXPORT CONFIGURABIL (model_dump cu optiuni)
# -------------------------------------------------------------
# model_dump accepta:  exclude={...}, exclude_none=True, by_alias=True

class UserV2(BaseModel):
    nume:str=Field(by_alias = "fullname")
    email:str
    parola: Optional[str] = None
    rol : str = "user"


api = {'fullname': "Horia", "email": "hscurtu@gmail.com"}

u4 = UserV2(nume=api['fullname'], email =api['email'])
print(u4.model_dump())
print(u4.model_dump(by_alias=True))

# 6. @model_serializer: controlezi TOT exportul modelului
# -------------------------------------------------------------
# Cand vrei o forma de export complet diferita de campurile interne
# (de ex. un rezumat, nu toate campurile brute).

# {'produs': 'Laptop', 'pret_afisat': '4500.0 lei', 'status': 'in stoc'}

class Produs(BaseModel):
    nume :str
    pret: float
    stoc : int

    @model_serializer
    def rezumat(self):
        status = "in stoc" if self.stoc > 0 else "epuizat"
        return {"produs": self.nume, "pret_afisat": f"{self.pret} lei", "status": status}


pr = Produs(nume="Laptop", pret=4500.0, stoc =10)
print(pr.model_dump())







# =============================================================
# RECAP / IDEI CHEIE
# =============================================================
# VALIDATORI PROPRII:
#   @field_validator("camp")            -> normalizezi/verifici UN camp;
#                                          return valoarea procesata;
#                                          raise ValueError daca e gresit
#   @field_validator("camp", mode="before") -> transformi valoarea
#                                          INAINTE de coercitia standard
#   @model_validator(mode="after")      -> reguli intre MAI MULTE campuri,
#                                          sau calculezi un camp
#
# MODELE COMPUSE:
#   - un camp poate fi alt MODEL (nested) -> validat recursiv
#   - sau o LISTA de modele  (List[Model])
#   - datetime/date parseaza string-uri ISO automat
#
# INTRARE/IESIRE:
#   - Field(alias="camelCase") + ConfigDict(populate_by_name=True)
#   - model_dump(exclude=..., exclude_none=True, by_alias=True)
#   - @field_serializer("camp")  -> format custom la export, un singur camp
#   - @model_serializer          -> format custom la export, tot modelul
# =============================================================