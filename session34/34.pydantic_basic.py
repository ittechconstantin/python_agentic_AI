# PYDANTIC  -  validare si parsare de date
# =============================================================
# Cand datele vin din AFARA aplicatiei tale - body de la un API, un
# formular, o linie de CSV - NU poti avea incredere in ele. Pot avea
# tipuri gresite, campuri lipsa, valori aberante.
#
# Ideea principala, ca PROBLEMA -> SOLUTIE:
#   PROBLEMA: verifici de mana fiecare camp (e int? nu lipseste? e email?).
#             E plictisitor, se uita cazuri, iar erorile apar tarziu, aiurea
#             (un AttributeError la 100 de linii distanta).
#   SOLUTIA:  scrii o SCHEMA (o clasa cu type hints) si Pydantic:
#             valideaza tipurile, le CONVERTESTE la ce trebuie si arunca o
#             eroare clara imediat.
#
# CERINTE:  pip install pydantic email-validator
#
# Ce trebuie sa stii deja (recap):
#   - clase si type hints  (nume: str)
#   - dicturi si JSON (sesiunea 24), API-uri cu requests (sesiunea 29)
# =============================================================


# #############################################################
# PARTEA 1 - BAZELE: SCHEMA, CONVERSIE, ERORI
# #############################################################


# 1. PROBLEMA -> SOLUTIA: primul model (BaseModel)
# -------------------------------------------------------------
# O schema Pydantic e o clasa care mosteneste BaseModel. Fiecare camp are
# un TIP (type hint). Cand construiesti obiectul, Pydantic verifica totul.
from pydantic import BaseModel, ValidationError, Field

class User(BaseModel):
    nume:   str
    varsta: int
    email : str

u = User(nume="Mircea", varsta=21, email= "hscurtu@gmail.com" )
print(u)       # nume='Mircea' varsta=21 email='hscurtu@gmail.com'
print(type(u)) # <class '__main__.User'>
print(u.varsta) # 21
print(type(u.varsta)) # <class 'int'>



# 2. COERCITIE: converteste tipuri compatibile ("30" -> 30)
# -------------------------------------------------------------
# Foarte util cand datele vin ca text (din CSV, din URL): Pydantic
# incearca sa converteasca la tipul cerut.

u = User(nume = "Mircea", varsta="31", email = 'hscurtu@gmail.com')
print(u.varsta, type(u.varsta)) # 31 <class 'int'>


# 3. ValidationError: eroare CLARA cand ceva nu se poate converti
# -------------------------------------------------------------
# Daca "treizeci" nu poate deveni int, Pydantic NU ghiceste - arunca
# ValidationError, cu detalii despre CE camp si DE CE.

try:
    u = User(nume = "Mircea", varsta="treizeci", email = 'hscurtu@gmail.com')
    print(u.varsta, type(u.varsta))
except ValidationError as e:
    print('=====')
    print(e)

# 4. Construire din DICT si din JSON  (cazul real)
# -------------------------------------------------------------
# Rareori scrii campurile de mana. De obicei ai un dict (din JSON) sau
# chiar un string JSON (din API). Doua metode:

u = User.model_validate({"nume": "George", "varsta": 40, "email": "george@gmail.com"})
print("nume", u.nume)


text = '{"nume": "George", "varsta": 40, "email": "george@gmail.com"}'
u1 = User.model_validate_json(text)
print("nume", u1.nume)



# 5. EXPORT inapoi: model_dump / model_dump_json
# -------------------------------------------------------------
# Dupa ce ai un obiect validat, il poti transforma inapoi in dict sau JSON
# (ca sa il salvezi, sa il trimiti mai departe etc.).
print("====5=====")
print(u.model_dump())
print(type(u.model_dump()))       # dict
print(u.model_dump_json())        # JSON STRING
print(type(u.model_dump_json()))

model_dump = u.model_dump()
model_dump_json = u.model_dump_json()

# print(model_dump['nume'])
# print(model_dump_json['nume'])

# model_dump -> dict -> Cand lucrezi cu date in Python(le procesezi, le parsezi, folosesti in alte functii)
# model_dump_json -> JSON String -> Cand vrei sa trimiti datele catre alt cineva (API, fisier)

# 6. CAMPURI OPTIONALE si valori DEFAULT
# -------------------------------------------------------------
# Un camp cu valoare dupa  =  are un default (poate lipsi la construire).
# Optional[str] = None  inseamna "poate fi text sau poate lipsi (None)".
from typing import Optional


class Produs(BaseModel):
    nume:     str
    pret:     float
    stoc:     int = 0               # default 0
    descriere:Optional[str] = None  # poate lipsi


p = Produs(nume="Laptop", pret=9.99)
print(p.stoc, p.descriere)  # 0 None


# #############################################################
# PARTEA 2 - CONSTRANGERI cu Field (reguli mai fine)
# #############################################################


# 7. PROBLEMA: tipul e corect, dar valoarea e absurda
# -------------------------------------------------------------
# "varsta: int" accepta si -5, si 300. Vrem REGULI: lungimi, intervale,
# format. SOLUTIA: Field(...) langa camp.
#   numere:    ge (>=), gt (>), le (<=), lt (<)
#   string:    min_length, max_length, pattern (regex)


class Inscrieri(BaseModel):
    nume:     str  = Field(min_length=2, max_length=50)
    varsta:   int  = Field(ge=18, le=130)
    email:    str
    pret:     float= Field(gt=0) # strict pozitiv

ok = Inscrieri(nume="Ana", varsta=18, email="ana@gmail.com", pret=9)
print("valid", ok.nume)

# varsta peste limita,
try:
    cursant = Inscrieri(nume="Ioana", varsta=140, email="ana@gmail.com", pret=9)
except ValidationError as e:
    print(e)


# 8. RAPORT de erori: e.errors() (loc / msg / type)
# -------------------------------------------------------------
# .errors() iti da o LISTA de dicturi, cate unul per problema. Perfect ca
# sa arati utilizatorului exact ce campuri sunt gresite (nu un stack trace).

try:
    cursant = Inscrieri(nume="I", varsta=140, email="ana@gmail.com", pret=0)
except ValidationError as e:
    print("Total probleme: " , len(e.errors()))
    for er in e.errors():
        print(f"   camp {er['loc'][0]}: regula {er['type']} cu mesajul {er['msg']}")


# 9. Field(pattern=...) e un regex - exista tipuri GATA VALIDATE
# -------------------------------------------------------------
# Pentru lucruri comune (email, URL, parola secreta) Pydantic are TIPURI GATA
# FACUTE, mult mai corecte decat un regex scris de mana.
#   EmailStr   -> validare REALA de email (foloseste email-validator)
#   HttpUrl    -> validare de URL
#   SecretStr  -> valoarea NU apare la print()/log (o ascunde automat)
from pydantic import EmailStr, HttpUrl, SecretStr

class ContSigur(BaseModel):
    email:    EmailStr
    homepage: HttpUrl
    parola:   SecretStr


cs = ContSigur(email = "ana@example.com", homepage="https://example.com", parola="Secret123")
print(cs.email)    #ana@example.com
print(cs.homepage) #https://example.com/
print(cs.parola)   # **********
print(cs.parola.get_secret_value()) # Secret123


try:
    ContSigur(email = "nu-e-email", homepage="nu-e-url", parola="x")
except ValidationError as e:
    print(e)


# 10. Enum: campul poate avea DOAR valori dintr-un set fix
# -------------------------------------------------------------
# PROBLEMA: rol: str accepta orice text ("admin", "adminn", "ADMIN"...).
# SOLUTIA: un Enum limiteaza valorile posibile; Pydantic il valideaza automat.
from enum import Enum


class Rol(str, Enum):
    ADMIN = 'admin'
    EDITOR = 'editor'
    VIZIATOR = 'viziator'


class Utilizator(BaseModel):
    nume : str
    rol : Rol = Rol.VIZIATOR


u = Utilizator(nume="Horia", rol="admin")
print(u.rol, type(u.rol)) # Rol.ADMIN <enum 'Rol'>
print(u.rol == Rol.ADMIN) # True

try:
    Utilizator(nume="Horia", rol="superadmin")
except ValidationError as e:
    print(f"rol invalid: {e.errors()[0]['type']}")


# 11. STIL MODERN: Annotated[tip, Field(...)] - reguli REFOLOSIBILE
# -------------------------------------------------------------
# PROBLEMA: "camp: int = Field(ge=0, le=130)" functioneaza, dar daca ai
# 5 campuri de "varsta" in 5 modele diferite, repeti regula peste tot.
# SOLUTIA: cu Annotated definesti tipul + regula O SINGURA DATA si il
# refolosesti ca pe un tip normal, in orice model.
from typing import Annotated

Varsta = Annotated[int, Field(ge=0, le=130)]
Numescurt = Annotated[str, Field(min_length=2, max_length=20)]



class PersoanaV2(BaseModel):
    varsta: Varsta
    nume: Numescurt


class AnagajatV2(BaseModel):
    varsta: Varsta
    nume: Numescurt


# 12. STRICT MODE: opreste coercitia automata (tipul trebuie sa fie EXACT)
# -------------------------------------------------------------
# PROBLEMA: uneori coercitia ("30" -> 30) NU e ce vrei - intr-un API strict,
# varsta="30" (string) ar trebui RESPINSA, nu acceptata.
# SOLUTIA: Field(strict=True) pe un camp, sau ConfigDict(strict=True) pe
# toata clasa.
from pydantic import ConfigDict

class ComandaStricta(BaseModel):
    cantitate: int = Field(strict=True)

ComandaStricta(cantitate=6)

# 13. TypeAdapter: validezi FARA sa definesti un BaseModel
# -------------------------------------------------------------
# PROBLEMA: uneori nu ai nevoie de o clasa intreaga - vrei doar sa validezi
# "asta e o lista de email-uri?", o singura data, undeva intr-o functie.
# SOLUTIA: TypeAdapter(tip) - functioneaza ca un BaseModel, dar pentru
# orice tip Python (list, dict, tuple, tipuri Pydantic etc.).
from pydantic import TypeAdapter

ListaDeEmailuri = TypeAdapter(list[EmailStr])

emailuri = ListaDeEmailuri.validate_python(['ana@x.com', 'ioana@x.com'])
print(emailuri)

try:
    ListaDeEmailuri.validate_python(['ana', 'ioana@x.com', 'b', 'c@x.com'])
except ValidationError as e:
    for er in e.errors():
        print(f'eroare la adresa de email ')

# #############################################################
# PARTEA 3 - APLICATII REALE
# #############################################################


# 14. VALIDEAZA raspunsul unui API (nu te increde orbeste)
# -------------------------------------------------------------
# Cand consumi un API, defineste o schema pentru ce ASTEPTI. Daca API-ul
# lipseste un camp, afli IMEDIAT, nu peste 100 de linii.
import requests

class UserApi(BaseModel):
    id: int
    name: str
    username: str
    email : EmailStr

r = requests.get("https://jsonplaceholder.typicode.com/users/1", timeout=10)
u = UserApi.model_validate(r.json())

print(u.name, u.username)

# 15. PROCESARE BULK: valid/invalid cu raport (nu te opresti la prima eroare)
# -------------------------------------------------------------
# Cand procesezi multe inregistrari (ex: un CSV), NU vrei sa se opreasca
# tot la prima gresita. Le iei una cate una: cele bune intr-o lista, cele
# rele in alta, cu motivul.

class Persoana(BaseModel):
    nume:   str = Field(min_length=2)
    varsta: int = Field(ge=0, le=130)
    email:  str

intrari = [
    {"nume": "Ana",   "varsta": 28,    "email": "ana@x.com"},
    {"nume": "X",     "varsta": "abc", "email": "x@y.z"},      # varsta gresita
    {"nume": "Horia", "varsta": 30,    "email": "horia@x.com"},
    {"nume": "",      "varsta": 25,    "email": "y@y.z"},      # nume prea scurt
]

valide, invalide = [], []
for raw in intrari:
    try:
        valide.append(Persoana.model_validate(raw))
    except ValidationError as e:
        invalide.append((raw["nume"], len(e.errors())))

print(f"valide: {len(valide)} -> {[v.nume for v in valide]}")   # ['Ana', 'Horia']
print(f"invalide: {len(invalide)} -> {invalide}")


# =============================================================
# RECAP / GRESELI FRECVENTE
# =============================================================
# Pydantic = SCHEMA + VALIDARE + PARSE pentru o clasa Python.
#
# Pasi tipici:
#   1) class Schema(BaseModel):  camp: tip = Field(reguli)
#   2) construire:  Schema(**date)  /  Schema.model_validate(dict)
#                   /  Schema.model_validate_json(text)
#   3) export:      m.model_dump()  /  m.model_dump_json()
#   4) eroare:      try: ... except ValidationError as e: e.errors()
#
# CONSTRANGERI (Field):
#   numere:  ge / gt / le / lt
#   string:  min_length / max_length / pattern (regex)
#   default: camp: tip = valoare   sau   Field(default_factory=list)
#
# TIPURI GATA VALIDATE (mai bune decat un regex scris de mana):
#   EmailStr / HttpUrl / SecretStr / Enum
#
# STIL MODERN:
#   Annotated[tip, Field(...)]  -> regula ATASATA tipului, refolosibila
#   Field(strict=True) / ConfigDict(strict=True)  -> opreste coercitia
#   TypeAdapter(tip).validate_python(...)  -> validezi fara sa faci un BaseModel
#
# GRESELI FRECVENTE:
#   - crezi ca "int" verifica si valoarea - NU; pentru reguli ai nevoie de Field.
#   - nu prinzi ValidationError -> aplicatia crapa cu stack trace la user.
#   - valideaza la FRONTIERA (imediat ce primesti datele), o singura data.
#   - la procesare in masa, colecteaza erorile, nu te opri la prima.
#   - un regex de email scris de mana e aproape mereu mai slab decat EmailStr.
#
# In fisierul urmator (partea 2): validatori personalizati
# (field_validator / model_validator), modele imbricate, alias-uri,
# serializatori proprii, Union/Generic, si configurare din .env.
# =============================================================