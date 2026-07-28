# FISIERE, CSV si JSON  -  citire / scriere pe disc
# =============================================================
# Pana acum, datele noastre traiau doar in memorie: cand programul se
# inchidea, dispareau. Acum invatam sa le SALVAM pe disc si sa le
# CITIM inapoi, in doua formate pe care le intalnesti tot timpul in IT:
#
#   CSV  - "Comma-Separated Values" - un tabel ca text simplu; il
#          deschizi cu Excel, il exporti din baze de date, il descarci
#          din rapoarte.
#   JSON - "JavaScript Object Notation" - date structurate/imbricate;
#          standardul pentru API-uri si fisiere de configurare.
#
# Python are pentru ele doua module BUILT-IN:  csv  si  json  (nu
# instalezi nimic). Dar mai intai trebuie sa stim sa lucram cu fisiere.
# =============================================================

import csv
import json
import os

# Ca exemplele sa fie auto-suficiente, cream FOLDERE locale langa
# script. Fisierele raman pe disc, deci le poti deschide cu un editor
# sa vezi ce am scris. Fiecare PARTE a lectiei scrie in FOLDERUL EI -
# usor de gasit ce a generat ce, in loc sa amestecam totul intr-un
# singur folder.
#   os.makedirs(cale, exist_ok=True)  = creeaza folderul; exist_ok=True
#                                       inseamna "nu da eroare daca exista"
#   os.path.join(a, b)                = lipeste caile corect pe orice sistem
TMP_FISIERE = "data_s23_fisiere"    # Partea 1 - open/with/moduri
TMP_CSV = "data_s23_csv"            # Partea 2 - csv.reader/writer
TMP_JSON = "data_s23_json"          # Partea 3 - json.loads/dumps

for folder in (TMP_FISIERE, TMP_CSV, TMP_JSON):
    os.makedirs(folder, exist_ok=True)


# =============================================================
# PARTEA 1 - FISIERE: open, moduri, with
# =============================================================


# 1. open()  -  deschide un fisier; MODURI
# -------------------------------------------------------------
# Sintaxa:  f = open(cale, mod, encoding="utf-8")
# Moduri:
#   "r"  READ    - citire (default). Fisierul TREBUIE sa existe.
#   "w"  WRITE   - scriere. Daca fisierul exista, il GOLESTE si scrie
#                  de la zero (atentie: pierzi ce era acolo!).
#   "a"  APPEND  - scriere la sfarsit, pastrand ce era deja.
# encoding="utf-8" = seteaza corect caracterele (foloseste-l mereu).


# 2. PROBLEMA: open() + close() manual e fragil
# -------------------------------------------------------------
# Dupa ce deschizi un fisier, trebuie sa-l INCHIZI cu f.close() ca sa
# se salveze pe disc si sa eliberezi resursele.


cale_txt = os.path.join(TMP_FISIERE, 'salut.txt')


# f = open(cale_txt, 'w', encoding="UTF-8")
# f.write("Hello\n")          # \n pentru a trece pe linia urmatoare
# f.write("How are you?")
# f.close()                   # OBLIGATORIU f.close()


# Dar daca intre open() si close() apare o eroare, close() NU se mai
# executa: fisierul ramane deschis, datele pot lipsi de pe disc.


# 3. SOLUTIA:  with open(...) as f  -  inchide singur fisierul
# -------------------------------------------------------------
# Blocul de sub  with  e "protejat": la iesire (chiar si la eroare)
# Python apeleaza SINGUR f.close(). De aici incolo folosim doar  with.

with open(cale_txt, 'w', encoding="utf-8") as f:
    f.write("Imi place python\n")
    f.write("Imi place programarea")
# la aceasta linie fisierul e deja inchis automat


# 4. CITIRE  -  tot fisierul, sau linie cu linie
# -------------------------------------------------------------

with open(cale_txt, 'r', encoding="utf-8") as f:
    for linie in f:
        print(linie.rstrip())  # scoate \n dupa fiecare linie

# Linie cu linie (cel mai des; nu tine tot fisierul in memorie):


# 5. APPEND  -  adauga la final, fara sa stergi
# -------------------------------------------------------------
with open(cale_txt, 'a', encoding='utf-8') as f:
    f.write("\nScriere corecta, Horatiuu!!")

print("======")
with open(cale_txt, 'r', encoding='utf-8') as f:
    # print(f.read())   # afiseaza tot continutul
    # print(f.readline()) # primul rand
    # print(f.readline()) # al doilea  rand
    print(f.readlines())

def suma(a, b):
    with open(cale_txt, 'a', encoding='utf-8') as f:
        f.write(f"\n{a} + {b} = {a + b}")

    return a+b

suma(3, 4)

# =============================================================
# PARTEA 2 - CSV
# =============================================================


# 6. CE ESTE CSV  +  de ce nu "de mana"
# -------------------------------------------------------------
# Un CSV are linii de text; fiecare linie e un RAND, iar coloanele sunt
# separate prin virgula. Prima linie e adesea HEADER-ul (numele
# coloanelor):
#   nume,varsta,rol
#   Ana,28,admin
#
# PROBLEMA daca "parsezi" de mana cu split(","): se strica atunci cand
# un camp CONTINE o virgula (ex: "Popescu, Ana") sau ghilimele. Modulul
# csv se ocupa singur de aceste cazuri. Deci il folosim pe el.


# 7. SCRIERE cu csv.writer  (randuri ca liste)
# -------------------------------------------------------------
cale_csv = os.path.join(TMP_CSV, 'useri.csv')
with open(cale_csv, 'w', newline="", encoding="UTF-8") as f:
    writer = csv.writer(f)
    writer.writerow(['nume', 'varsta', 'rol'])
    writer.writerow(["Florin", 56, 'sysadmin'])
    writer.writerow(["George", 19, 'junior'])


# 8. CITIRE cu csv.reader  -  ATENTIE: totul e STRING
# -------------------------------------------------------------

with open(cale_csv, 'r', encoding="utf-8") as f:
    for rand in csv.reader(f):
        print(rand)

# Observam ca varsta stocheaza ca informatie string, nu int/float. Conversia o vei face tu

# 9. SARI PESTE HEADER  +  converteste tipurile
# -------------------------------------------------------------
with open(cale_csv, 'r', encoding="utf-8") as f:
    reader = csv.reader(f)
    next(reader)            # consuma(sari peste) linia de header
    for nume, varsta, rol in reader:
        print(f"{nume} cu varsta {varsta} are rolul {rol}")

# 10. csv.DictReader / DictWriter  -  cod mai citibil (dict-uri)
# -------------------------------------------------------------
# DictReader foloseste header-ul ca sa-ti dea dict-uri: u["nume"] in
# loc de u[0]. Mult mai clar.

with open(cale_csv, encoding="utf-8") as f:
    for u in csv.DictReader(f):
        print(u)

# DictWriter scrie dict-uri, dandu-i numele coloanelor:
useri = [
    {'nume': 'Ana',   'varsta': 20, 'rol': 'junior'},
    {'nume': 'Ioana', 'varsta': 30, 'rol': 'senior'},
]

with open('data_s23_csv/useriHORIA.csv', 'w', newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["nume", "varsta", "rol"])
    writer.writeheader()
    writer.writerows(useri)


# =============================================================
# PARTEA 3 - JSON
# =============================================================


# 11. CE ESTE JSON  +  maparea tipurilor
# -------------------------------------------------------------
# JSON e text pentru date STRUCTURATE (imbricate). Corespondenta cu
# tipurile Python:
#   object  <-> dict      string <-> str        true/false <-> True/False
#   array   <-> list      number <-> int/float  null       <-> None


# 12. STRING  <->  PYTHON:  json.loads  /  json.dumps
# -------------------------------------------------------------
# loads  = "load string" (text->obiect Python)

text = '{"nume": "Ana", "varsta": 28, "roluri": ["sysadmin", "junior"]}'
print(type(text))
date = json.loads(text)
print(type(date))
print(date['nume'])

# dumps = "dump string" (obiect Python -> text)
obiect = {"nume": "Ana", "varsta": 28, "active": True, "telefon": None}
print(json.dumps(obiect))


# 13. STRUCTURI IMBRICATE  (raspuns de API)
# -------------------------------------------------------------
# Puterea JSON: dict-uri in dict-uri, liste de dict-uri etc.

api_response = {
    "status": "ok",
    "data": {
            "id": 1,
            "nume": "Ana",
            "tags": ['python', 'sql']
         }

}

text = json.dumps(api_response)
inapoi = json.loads(text)
print(type(text))
print(api_response['data']['tags'])



# =============================================================
# RECAP / GRESELI FRECVENTE
# =============================================================
# FISIERE:
#   - foloseste mereu  with open(...) as f:  (se inchide singur)
#   - moduri:  "r" citire, "w" scrie de la zero, "a" adauga la final
#   - encoding="utf-8" mereu
#
# CSV:
#   - la SCRIERE:  newline=""  + encoding="utf-8"
#   - valorile citite sunt mereu STRING; convertesti tu la int/float
#   - DictReader / DictWriter = cod mai citibil (foloseste header-ul)
#   - nu parsa CSV cu split(",") - modulul csv trateaza corect virgulele
#
# JSON:
#   - loads / dumps  -> string in memorie
#   - load  / dump   -> fisier (fara "s")
#   - indent=2 pentru fisiere lizibile; ensure_ascii=False pentru diacritice
#   - default=  pentru tipuri pe care JSON nu le stie (set, obiecte proprii)
#
# Greseli frecvente:
#   - sa uiti sa convertesti string-urile din CSV la numere (adunari gresite).
#   - sa deschizi CSV pentru scriere fara  newline=""  (randuri goale pe Windows).
#   - sa confunzi dump/dumps (fisier vs string).
#   - sa deschizi cu "w" cand voiai "a" -> stergi tot fisierul.
#
# =============================================================
# CONCLUZIE
# =============================================================
# with open(cale, "w", encoding="utf-8") as f: ...   # fisiere text
# csv.reader / writer         -> liste            (randuri)
# csv.DictReader / DictWriter -> dict-uri          (cu header)
# json.loads / dumps          -> string in memorie
# json.load  / dump           -> fisier
#
# Toate sunt module BUILT-IN. Fisierele scrise sunt in 3 foldere,
# separate pe partea care le-a generat: data_s23_fisiere/, data_s23_csv/,
# data_s23_json/.
# =============================================================