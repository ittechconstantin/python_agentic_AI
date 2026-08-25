# MINI-PROIECT: "Buletinul de dimineata"  (API + requests)
# =============================================================
#
# CONTEXT (caz real)
# ------------------
# Construiesti, PAS CU PAS, un mic bot care iti afiseaza un "buletin de
# dimineata": vremea din orasul tau si un curs valutar, luate LIVE de pe
# internet - nu date fixe, ca la jsonplaceholder. De data asta, cand
# rulezi codul, rezultatul chiar reflecta ce se intampla ACUM afara.
#
# Folosim doua API-uri REALE, publice, FARA cheie:
#   - Open-Meteo (geocoding + vreme)   https://open-meteo.com
#   - Frankfurter (curs valutar, date de la Banca Centrala Europeana)
#     https://frankfurter.dev
#
# Fiecare functie e un "pas" din proiect. Ultima functie le combina pe
# toate intr-un mesaj final, frumos formatat - genul de lucru pe care
# il poti arata cu mandrie, nu doar un numar afisat in consola.
#
#
# CE AI DE FACUT
# --------------
# Scrie 5 functii (folosind requests), in ordine:
#
# 1. gaseste_oras(nume_oras)
#       -> GET la geocoding API, intoarce un tuplu (latitudine, longitudine,
#          nume_gasit) pentru primul rezultat. Daca orasul nu e gasit
#          (lista "results" lipseste sau e goala), intoarce None.
#
# 2. vremea_curenta(lat, lon)
#       -> GET la forecast API cu current_weather=true, intoarce dict-ul
#          de sub cheia "current_weather" (are "temperature", "windspeed",
#          "weathercode").
#
# 3. descrie_vreme(cod)
#       -> NU e cerere HTTP! E o functie locala care traduce un
#          "weathercode" (numar) intr-o descriere text, folosind dict-ul
#          CODURI_VREME de mai jos. Daca nu gaseste codul, intoarce
#          "vreme necunoscuta".
#
# 4. curs_valutar(sursa, tinta)
#       -> GET la Frankfurter, intoarce rata de schimb (un float) dintre
#          moneda sursa si moneda tinta.
#
# 5. buletin(oras, suma, moneda_sursa, moneda_tinta)
#       -> COMBINA toate functiile de mai sus intr-un text final,
#          gata de afisat (vezi formatul exact mai jos, la OUTPUT).
#
#
# API-urile, PE SCURT (vezi si INDICII pentru URL-uri complete)
# ---------------------------------------------------------------
# GEOCODING (nume oras -> coordonate):
#   GET https://geocoding-api.open-meteo.com/v1/search
#   params: {"name": nume_oras, "count": 1, "language": "ro"}
#   raspuns: {"results": [{"latitude": .., "longitude": .., "name": ..}, ...]}
#   ATENTIE: daca orasul nu exista, cheia "results" LIPSESTE din raspuns -
#            foloseste .get("results") ca sa nu iei KeyError.
#
# VREME (coordonate -> vreme curenta):
#   GET https://api.open-meteo.com/v1/forecast
#   params: {"latitude": lat, "longitude": lon, "current_weather": True}
#   raspuns: {"current_weather": {"temperature": .., "windspeed": ..,
#                                  "weathercode": .., "time": ..}}
#
# CURS VALUTAR (sursa -> tinta):
#   GET https://api.frankfurter.dev/v1/latest
#   params: {"base": sursa, "symbols": tinta}
#   raspuns: {"amount": 1.0, "base": "EUR", "date": "...",
#             "rates": {"RON": 4.97}}
#
#
# CERINTE
# -------
#   - foloseste requests.get cu timeout=10 la FIECARE cerere
#   - parametrii de query prin params={...} (NU lipiti de mana in URL)
#   - gaseste_oras() trebuie sa se apere de orase inexistente (.get)
#   - descrie_vreme() NU face nicio cerere HTTP - e logica locala
#
#
# OUTPUT ASTEPTAT (format, nu valori exacte - vremea si cursul sunt LIVE!)
# -------------------------------------------------------------------------
#   Buletin pentru Bucuresti:
#     Vremea acum: 21.3Â°C, cer senin, vant 8.4 km/h
#     100 EUR = 497.32 RON
#
# (numerele tale vor fi diferite, pentru ca sunt date reale, in timp real)
#
#
# INDICII
# -------
#   - geocoding:  requests.get(
#                   "https://geocoding-api.open-meteo.com/v1/search",
#                   params={"name": nume_oras, "count": 1, "language": "ro"},
#                   timeout=10,
#                 )
#   - vreme:      requests.get(
#                   "https://api.open-meteo.com/v1/forecast",
#                   params={"latitude": lat, "longitude": lon,
#                           "current_weather": True},
#                   timeout=10,
#                 )
#   - valutar:    requests.get(
#                   "https://api.frankfurter.dev/v1/latest",
#                   params={"base": sursa, "symbols": tinta},
#                   timeout=10,
#                 )
#   - orase inexistente: r.json().get("results")  -> None daca lipseste
# =============================================================
import code
from itertools import count

import requests

GEOCODING_URL = "https://geocoding-api.open-meteo.com/v1/search"
VREME_URL = "https://api.open-meteo.com/v1/forecast"
VALUTAR_URL = "https://api.frankfurter.dev/v1/latest"

# Traducere partiala a codurilor meteo standard (WMO) in text - nu trebuie
# sa le stii pe toate, doar sa exersezi cautarea intr-un dict.
CODURI_VREME = {
    0: "cer senin",
    1: "predominant senin",
    2: "partial noros",
    3: "innorat",
    45: "ceata",
    51: "burnita usoara",
    61: "ploaie usoara",
    63: "ploaie moderata",
    65: "ploaie puternica",
    71: "ninsoare usoara",
    80: "averse",
    95: "furtuna",
}


# ---- ZONA TA DE LUCRU ---------------------------------------
def gaseste_oras(nume_oras):
    # TODO: GET la GEOCODING_URL cu params={"name": nume_oras, "count": 1,
    #       "language": "ro"}. Foloseste r.json().get("results") ca sa nu
    #       crapi daca orasul nu exista. Intoarce (lat, lon, nume) sau None.
    r = requests.get(GEOCODING_URL, params={"name": nume_oras, "count": 1, "language": "ro"})

    rezultate = r.json()['results']
    if not rezultate:
        return None
    primul = rezultate[0]
    return primul['latitude'], primul['longitude'], primul['name']

orasalul_cautat = gaseste_oras("Timisoara")
print(orasalul_cautat)

def vremea_curenta(lat, lon):
    # TODO: GET la VREME_URL cu params={"latitude": lat, "longitude": lon,
    #       "current_weather": True}. Intoarce r.json()["current_weather"].

    r = requests.get(VREME_URL, params={"latitude": lat, "longitude": lon, "current_weather": True} )
    print(r.json())
    result = r.json()['current_weather']
    return result

print(vremea_curenta(orasalul_cautat[0], orasalul_cautat[1]))

def descrie_vreme(cod):
    # TODO: cauta 'cod' in CODURI_VREME, cu valoare implicita
    #       "vreme necunoscuta" daca nu exista (foloseste .get).

   return CODURI_VREME.get(cod, "vreme necunoscuta")

def curs_valutar(sursa, tinta):
    # TODO: GET la VALUTAR_URL cu params={"base": sursa, "symbols": tinta}.
    #       Intoarce r.json()["rates"][tinta]  (un float).
    p = requests.get(VALUTAR_URL, params={"base": sursa, "symbols": tinta})
    rezultat = p.json()["rates"][tinta]
    return float(rezultat)

def buletin(oras, suma, moneda_sursa, moneda_tinta):
    # TODO: combina toate functiile de mai sus intr-un string, in
    #       formatul aratat la OUTPUT ASTEPTAT. Daca orasul nu e gasit,
    #       intoarce  f"Orasul '{oras}' nu a fost gasit."
    date_oras = gaseste_oras(oras)
    lat, lon, nume = date_oras
    vremea = vremea_curenta(lat, lon)
    descriere = descrie_vreme(vremea["weathercode"])
    rata = curs_valutar(moneda_sursa, moneda_tinta)
    print(vremea, descriere, rata)

    # if not date_oras:
    #     return f"Orasul '{oras}' nu a fost gasit."
    # return (f"Vremea pentru{oras}\n Vremea acum: {vremea_curenta()}")

# ---- COD DE TEST (nu trebuie sa-l modifici) -----------------
print(buletin("Bucuresti", 100, "EUR", "RON"))
# print()
# print(buletin("OrasCareNuExista123", 100, "EUR", "RON"))