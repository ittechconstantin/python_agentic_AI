# MINI-PROIECT: "Zile libere legale"  (API + requests)
# =============================================================
#
# CONTEXT (caz real)
# ------------------
# Construiesti un mic instrument care iti spune, pentru orice tara,
# cate zile libere legale sunt intr-un an, care e urmatoarea, si daca
# AZI e sau nu zi libera. Folosim Nager.Date - un API public, real,
# FARA cheie, cu date despre sarbatorile legale din peste 90 de tari.
#   https://date.nager.at
#
# De data asta o sa observi ceva important din teorie (sesiunea 29):
# unul dintre endpointuri NU intoarce deloc JSON cand raspunsul e
# "nu" - foloseste STATUS CODE-ul ca sa-ti dea raspunsul. Exact ideea
# de la "PROBLEMA: erori nevazute" din teorie, dar de data asta in
# sens pozitiv: statusul insusi E informatia.
#
#
# CE AI DE FACUT
# --------------
# Scrie 5 functii (folosind requests):
#
# 1. zile_libere(an, cod_tara)
#       -> GET /api/v3/publicholidays/<an>/<cod_tara>
#          intoarce lista de dict-uri primita direct de la API (fiecare
#          are "date", "localName", "name", ...).
#
# 2. numar_zile_libere(an, cod_tara)
#       -> NU face o cerere noua! Foloseste zile_libere(...) si
#          intoarce doar len(...) - exersezi refolosirea functiilor.
#
# 3. urmatoarea_zi_libera(cod_tara)
#       -> GET /api/v3/NextPublicHolidays/<cod_tara>
#          intoarce PRIMUL element din lista primita (cel mai apropiat
#          in timp), sau None daca lista e goala.
#
# 4. e_azi_zi_libera(cod_tara)
#       -> GET /api/v3/IsTodayPublicHoliday/<cod_tara>
#          ATENTIE: acest endpoint NU intoarce JSON! Intoarce doar un
#          STATUS CODE: 200 daca azi e zi libera, 204 daca NU e.
#          Functia intoarce True/False dupa status_code, FARA sa
#          apeleze .json() (ar da eroare, corpul e gol la 204).
#
# 5. raport_zile_libere(an, cod_tara)
#       -> combina toate functiile de mai sus intr-un text final,
#          gata de afisat (vezi formatul la OUTPUT ASTEPTAT).
#
#
# API-urile, PE SCURT
# --------------------
# Baza:  https://date.nager.at
#
#   GET /api/v3/publicholidays/{an}/{cod_tara}
#       -> listeaza TOATE zilele libere dintr-un an, pentru o tara.
#          raspuns: [{"date": "2026-01-01", "localName": "Anul Nou",
#                     "name": "New Year's Day", ...}, ...]
#
#   GET /api/v3/NextPublicHolidays/{cod_tara}
#       -> urmatoarele zile libere de AZI incolo (nu ai nevoie de an).
#          raspuns: la fel ca mai sus, dar doar cele viitoare.
#
#   GET /api/v3/IsTodayPublicHoliday/{cod_tara}
#       -> raspuns FARA CORP: doar status_code (200 = da, 204 = nu).
#
# cod_tara e codul ISO pe 2 litere: "RO" (Romania), "US", "DE", "FR"...
#
#
# CERINTE
# -------
#   - foloseste requests.get cu timeout=10 la fiecare cerere
#   - construieste URL-urile cu f-string (an si cod_tara vin ca parametri
#     de FUNCTIE aici, nu ca query string - se pun direct in path)
#   - la IsTodayPublicHoliday NU apela .json() - foloseste doar status_code
#
#
# OUTPUT ASTEPTAT (formatul e fix; datele exacte depind de ZIUA in care
# rulezi codul, pentru ca "azi" si "urmatoarea zi libera" se schimba)
# -------------------------------------------------------------------------
#   Raport pentru RO, anul 2026:
#     Total zile libere legale: 15
#     Urmatoarea zi libera: 2026-XX-XX - <nume>
#     Azi e zi libera? Nu
#
#
# INDICII
# -------
#   - listare:  requests.get(
#                 f"https://date.nager.at/api/v3/publicholidays/{an}/{cod_tara}",
#                 timeout=10,
#               )
#   - urmatoarea: requests.get(
#                 f"https://date.nager.at/api/v3/NextPublicHolidays/{cod_tara}",
#                 timeout=10,
#               )
#   - azi:      requests.get(
#                 f"https://date.nager.at/api/v3/IsTodayPublicHoliday/{cod_tara}",
#                 timeout=10,
#               )
#               apoi doar:  r.status_code == 200
# =============================================================

import requests

BAZA = "https://date.nager.at/api/v3"


# ---- ZONA TA DE LUCRU ---------------------------------------
def zile_libere(an, cod_tara):
    # TODO: GET f"{BAZA}/publicholidays/{an}/{cod_tara}" -> r.json()
    r = requests.get(f"{BAZA}/publicholidays/{an}/{cod_tara}",timeout = 10)
    r.raise_for_status()
    return r.json()

def numar_zile_libere(an, cod_tara):
    # TODO: foloseste zile_libere(an, cod_tara) -> len(...)
    #       NU face o cerere HTTP noua aici!
    return len(zile_libere(an, cod_tara))

def urmatoarea_zi_libera(cod_tara):
    # TODO: GET f"{BAZA}/NextPublicHolidays/{cod_tara}"
    #       -> primul element din lista, sau None daca lista e goala
    p = requests.get(f"{BAZA}/NextPublicHolidays/{cod_tara}",timeout=10)
    rezultat = p.json().get(f"{BAZA}/NextPublicHolidays/{cod_tara}")
    if not rezultat:
        return None
    return rezultat[0]


def e_azi_zi_libera(cod_tara):
    # TODO: GET f"{BAZA}/IsTodayPublicHoliday/{cod_tara}"
    #       -> return r.status_code == 200   (NU apela .json() aici!)
    c = requests.get( f"{BAZA}/IsTodayPublicHoliday/{cod_tara}", timeout=10)
    return c.status_code == 200

def raport_zile_libere(an, cod_tara):
    # TODO: combina toate functiile de mai sus intr-un string, in
    #       formatul de la OUTPUT ASTEPTAT.
    total_zile = numar_zile_libere(an, cod_tara)
    urmatoarea = urmatoarea_zi_libera(cod_tara)
    azi = e_azi_zi_libera(cod_tara)

    return (f"Raport pentru {cod_tara}, anul {an}\n Total zile libere legale: {total_zile}\n Urmatoarea zi libera: {urmatoarea}\n Azi e zi libera? {azi}")


# ---- COD DE TEST (nu trebuie sa-l modifici) -----------------
print(raport_zile_libere(2026, "RO"))