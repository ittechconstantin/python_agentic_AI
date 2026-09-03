# MINI-PROIECT: "Radar Biziday"  (Web Scraping)
# =============================================================
#
# CONTEXT (caz real)
# ------------------
# Biziday.ro e un site romanesc de stiri scurte, "sintetizate" - fiecare
# stire e 1-3 propozitii, fara articol intreg de citit. E un format
# FOARTE prietenos pentru scraping: fiecare stire e, structural, UN
# SINGUR LINK, cu tot ce ne trebuie (text + sursa + data + ora) IN
# INTERIORUL textului acelui link. Nu trebuie sa navighezi prin
# parinti sau sa cauti clase CSS - totul e in text, gata de despicat
# cu regex.

#
# CE AI DE FACUT
# --------------
# Scrie 5 functii (folosind requests + BeautifulSoup + re):
#
# 1. descompune_stirea(text, href)
#       -> NU face nicio cerere HTTP! Primeste textul unui link (ex:
#          "Dolly Parton a murit la 80 de ani.Biziday · 2026-08-25 @
#          18:27:23") si href-ul lui, si intoarce un dict: {"text":
#          ..., "sursa": ..., "data": ..., "ora": ..., "url": ...}
#          Daca textul NU se potriveste tiparului asteptat (nu e o
#          stire, ci un link de navigare oarecare), intoarce None.
#
# 2. stiri_de_pe_pagina(url)
#       -> aduce pagina, ia TOATE elementele <a> de pe ea, foloseste
#          descompune_stirea(...) pentru fiecare si pastreaza doar
#          rezultatele care NU sunt None (adica doar linkurile care
#          chiar sunt stiri). Intoarce lista de dict-uri.
#
# 3. stiri_dupa_sursa(stiri, sursa)
#       -> NU face nicio cerere noua! Filtreaza lista dupa "sursa"
#          (comparatie case-insensitive).
#
# 4. sursa_cea_mai_frecventa(stiri)
#       -> numara aparitiile fiecarei "sursa" si intoarce (sursa,
#          numar) pentru cea mai frecventa. Intoarce None daca lista
#          e goala.
#
# 5. raport(n)
#       -> combina toate functiile de mai sus intr-un text final, gata
#          de afisat (vezi formatul la OUTPUT ASTEPTAT).
#
#
# STRUCTURA TEXTULUI, PE SCURT
# --------------------------------
# Textul unui link de stire arata asa (fara spatiu intre continut si
# numele sursei - sunt "lipite", pentru ca in HTML original erau doua
# elemente diferite, iar extragerea textului le-a unit):
#
#   "Continutul stirii, scris de obicei in 1-3 propozitii.Biziday · 2026-08-25 @ 18:27:23"
#
# adica: [text stire] + [Sursa] + " · " + [AAAA-LL-ZZ] + " @ " + [HH:MM:SS]
#
# Un link care NU e stire (ex: "Contact", "Politica de confidentialitate")
# nu se termina cu acest tipar - de-aia il ignoram.
#
#
# CERINTE
# -------
#   - foloseste requests.get cu timeout=10 si headers={"User-Agent": ...}
#   - foloseste BeautifulSoup(r.text, "lxml") pentru parsare
#   - foloseste modulul re pentru regex
#   - descompune_stirea, stiri_dupa_sursa si sursa_cea_mai_frecventa NU
#     fac nicio cerere HTTP
#
#
# OUTPUT ASTEPTAT (formatul e fix; stirile exacte depind de ce e ACUM
# pe biziday.ro - stirile se schimba non-stop)
# -------------------------------------------------------------------------
#   Radar Biziday (primele 5 din 20 stiri):
#     1. [2026-08-27 05:27] Sefu CIA a fost trimis la Moscova... (Biziday)
#     2. [2026-08-26 15:41] Alunecare de teren la granita... (Biziday)
#     ...
#   Sursa cea mai frecventa: Biziday (18 stiri)
#
#
# INDICII
# -------
#   - regex pentru tiparul de la finalul textului:
#         TIPAR = re.compile(
#             r"([A-ZĂÂÎȘȚ][\wăâîșțĂÂÎȘȚ]*)\s*·\s*(\d{4}-\d{2}-\d{2})\s*@\s*(\d{2}:\d{2}:\d{2})\s*$"
#         )
#         potrivire = TIPAR.search(text.strip())
#         if potrivire is None:
#             return None
#   - continutul stirii (tot ce e INAINTE de potrivire):
#         continut = text[:potrivire.start()].strip()
# =============================================================

import re

import requests
from bs4 import BeautifulSoup
from re import findall

URL = "https://www.biziday.ro/category/stiri/"
HEADERE = {"User-Agent": "curs-python-scraping/1.0 (exercitiu educativ, contact: curs@exemplu.ro)"}

TIPAR_METADATA = re.compile(
    r"([A-ZĂÂÎȘȚ][\wăâîșțĂÂÎȘȚ]*)\s*·\s*(\d{4}-\d{2}-\d{2})\s*@\s*(\d{2}:\d{2}:\d{2})\s*$"
)


# ---- ZONA TA DE LUCRU ---------------------------------------
def descompune_stirea(text, href):
    # TODO: potriveste TIPAR_METADATA la finalul textului. Daca nu se
    #       potriveste, intoarce None. Altfel, intoarce dict-ul cu
    #       text/sursa/data/ora/url.
    text = text.strip()
    potrivire = TIPAR_METADATA.search(text)
    if potrivire is None:
        return None

    sursa = potrivire.group(1)
    data = potrivire.group(2)
    ora = potrivire.group(3)
    continut = text[:potrivire.start()].strip()

    if not continut:
        return None

    return {"text": continut, "sursa": sursa, "data": data, "ora": ora, "url": href}



def stiri_de_pe_pagina(url):
    # TODO: GET la url, ia toate <a>, foloseste descompune_stirea(...)
    #       pentru fiecare si pastreaza doar rezultatele care nu sunt None.
    r = requests.get(url, headers=HEADERE, timeout=10)
    r.raise_for_status()
    stiri = BeautifulSoup(r.text, "lxml")
    titluri_stiri = stiri.select("a")
    lista_stiri = []
    for titlu in titluri_stiri:
        t = descompune_stirea(titlu.text, titlu.get("href"))
        if t:
            lista_stiri.append(t)
    return lista_stiri

# stiri = stiri_de_pe_pagina(URL)

def stiri_dupa_sursa(stiri, sursa):
    # TODO: filtreaza dupa "sursa" (case-insensitive)
    #       NU face nicio cerere HTTP aici!
    lista_noua = []
    for stire in stiri:
        if stire["sursa"].lower() == sursa.lower():
            lista_noua.append(stire)
    return lista_noua
# stiri_dupa_sursa(stiri, "Biziday")

def sursa_cea_mai_frecventa(stiri):
    # TODO: numara aparitiile fiecarei "sursa", intoarce (sursa, numar)
    #       pentru cea mai frecventa, sau None daca lista e goala.
    dictionar_surse = {}
    if not stiri:
        return None
    for stire in stiri:
        if stire["sursa"] in dictionar_surse:
            dictionar_surse[stire["sursa"]] += 1
        else:
            dictionar_surse[stire["sursa"]] = 1
    sursa_frecventa = max(dictionar_surse, key = lambda values: dictionar_surse[values])

    return sursa_frecventa, dictionar_surse[sursa_frecventa]

# print(sursa_cea_mai_frecventa(stiri))
def raport(n):
    # TODO: combina toate functiile de mai sus intr-un string, in
    #       formatul de la OUTPUT ASTEPTAT.
    ...
    stiri_pagina = stiri_de_pe_pagina(URL)
    frecventa = sursa_cea_mai_frecventa(stiri_pagina)
    text_returnat = f"Radar Biziday (primele {n} din {len(stiri_pagina)} stiri):"
    for index in range(1, n+1):
        text_stire_curenta = f"\n  {index}. [{stiri_pagina[index - 1]["data"]} {stiri_pagina[index - 1]["ora"]}] {stiri_pagina[index - 1]["text"]} ({stiri_pagina[index - 1]["sursa"]})"
        text_returnat = text_returnat + text_stire_curenta
    text_despre_frecventa = f"\nSursa cea mai frecventa: {frecventa[0]} ({frecventa[1]}de stiri)"
    text_returnat = text_returnat + text_despre_frecventa
    return text_returnat

# ---- COD DE TEST (nu trebuie sa-l modifici) -----------------
print(raport(5))

# =============================================================
# EXTINDERE OPTIONALA
# =============================================================
# 1. cauta_in_stiri(stiri, cuvant) -> stirile al caror "text" contine
#    un anumit cuvant (case-insensitive).
# 2. stiri_dintr_o_zi(stiri, data) -> filtreaza dupa "data" == data
#    data (format "AAAA-LL-ZZ").
# 3. Verifica manual (in browser) daca site-ul are si alte categorii
#    (ex: sport, extern) si adapteaza URL-ul ca sa aduci stiri dintr-o
#    alta categorie.
# =============================================================