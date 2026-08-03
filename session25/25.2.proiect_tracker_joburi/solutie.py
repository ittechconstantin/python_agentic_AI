import csv
import os
import json
import streamlit as st
from datetime import date

# ======================================================================
# Acesta e un schelet de pornire, nu o solutie. Cateva lucruri
# sunt deja implementate (ca sa vezi un exemplu de stil de cod), iar restul
# sunt marcate cu TODO, in ordinea exacta din PASI.md. Nu sari peste ordine -
# fiecare TODO se bazeaza pe cele de dinaintea lui.
# ======================================================================

# ==============PASUL 0 — CONFIGURARE=========================
TMP = "demo_data"                                 # folderul cu fisierele aplicatiei
os.makedirs(TMP, exist_ok=True)                   # il cream daca nu exista deja

calea_db = os.path.join(TMP, "aplicatii.json")    # aici salvam toate aplicatiile - fisierul
                                                    # exista deja cu cateva aplicatii puse acolo
                                                    # dinainte (vezi demo_data/aplicatii.json),
                                                    # ca sa ai cu ce testa aplicatia din prima
                                                    # rulare, fara sa faci mai intai un import CSV

STARI = ["Aplicat", "Interviu", "Oferta", "Respins"]   # starile posibile pentru o aplicatie


# ==============PASUL 1 — Salvarea si incarcarea aplicatiilor=========================

def incarca_aplicatii():
    """Citeste lista de aplicatii salvata pe calculator. Implementata ca exemplu."""
    if os.path.exists(calea_db):                     # verifica daca fisierul exista
        with open(calea_db, encoding="utf-8") as f:  # il deschide
            return json.load(f)                      # il citeste ca JSON
    else:
        return []                                    # prima rulare - nu exista inca nimic salvat


def salveaza_aplicatii(aplicatii):
    """
    TODO (PASI.md, Pasul 1, Functia 2):
    - primeste lista completa de aplicatii, asa cum arata ea acum
    - scrie toata lista in fisierul de pe calculator (calea_db), ca JSON,
      inlocuind complet ce era scris inainte acolo (nu adauga, rescrie tot)
    - nu intoarce nimic
    """
    pass


# ==============PASUL 2 — Import din CSV, fara duplicate=========================

# De ce avem nevoie de functia asta? Un rand citit dintr-un CSV vine
# incomplet, are doar companie/post/data_aplicare/sursa, dar aplicatia
# ta are nevoie si de stare, data_ultimului_contact si notite, ca sa
# arate la fel ca oricare alta aplicatie din tracker. Fara ea, aplicatiile
# importate ar avea alte campuri decat cele adaugate manual, si restul
# codului (filtrare, afisare in tabel) s-ar strica sau ar da eroare.
# Exemplu, ca sa vezi exact ce intra si ce trebuie sa iasa din functie:
#
#   INTRA (rand_brut, asa cum vine dintr-un CSV):
#   {"companie": "TechNova", "post": "Python Developer",
#    "data_aplicare": "2026-07-25", "sursa": "linkedin"}
#
#   IESE (ce trebuie sa intoarca normalizeaza_rand):
#   {"companie": "TechNova", "post": "Python Developer",
#    "data_aplicare": "2026-07-25", "sursa": "linkedin",
#    "stare": "Aplicat", "data_ultimului_contact": "2026-07-25", "notite": ""}
#
def normalizeaza_rand(rand_brut):
    """
    TODO (PASI.md, Pasul 2, Functia 1):
    - primeste un rand brut dintr-un CSV: companie, post, data_aplicare, sursa
      (toate valorile sunt text)
    - pastreaza companie/post/data_aplicare/sursa asa cum vin
    - completeaza stare="Aplicat"
    - completeaza data_ultimului_contact cu ACEEASI valoare ca data_aplicare
      (la import, "ultimul contact" e chiar momentul aplicarii)
    - completeaza notite=""
    - intoarce un singur dict, cu toate cele 7 campuri
    """
    pass


# De ce avem nevoie de functia asta? Dupa ce utilizatorul incarca un
# fisier CSV in pagina web, cineva trebuie sa il transforme intr-o lista
# de aplicatii pe care le putem folosi in cod. Functia asta face exact
# asta: primeste fisierul incarcat si intoarce direct lista gata de
# folosit, ca sa nu repetam acesti pasi de fiecare data cand citim un CSV.
# Exemplu, ca sa vezi exact ce intra si ce trebuie sa iasa din functie:
#
#   INTRA (fisier), continutul CSV incarcat, ca text simplu ar arata asa:
#   companie,post,data_aplicare,sursa
#   TechNova,Python Developer,2026-07-25,linkedin
#   DataForge,Backend Engineer,2026-07-20,site
#
#   IESE (lista de aplicatii, dupa ce fiecare rand a trecut prin
#   normalizeaza_rand):
#   [
#     {"companie": "TechNova", "post": "Python Developer", "data_aplicare": "2026-07-25",
#      "sursa": "linkedin", "stare": "Aplicat", "data_ultimului_contact": "2026-07-25", "notite": ""},
#     {"companie": "DataForge", "post": "Backend Engineer", "data_aplicare": "2026-07-20",
#      "sursa": "site", "stare": "Aplicat", "data_ultimului_contact": "2026-07-20", "notite": ""},
#   ]
#
def citeste_csv_incarcat(fisier):
    """Transforma fisierul CSV incarcat de utilizator intr-o lista de aplicatii. Implementata ca exemplu."""
    # fisierul vine ca text codificat (nu il putem citi direct), il
    # decodam mai intai, apoi il impartim pe linii
    linii_text = fisier.read().decode("utf-8").splitlines()
    return [normalizeaza_rand(r) for r in csv.DictReader(linii_text)]


def adauga_aplicatii_noi(existente, importate):
    """
    TODO (PASI.md, Pasul 2, Functia 3):
    - primeste lista de aplicatii deja existente si lista celor importate
    - ATENTIE: cheia de unicitate e PERECHEA (companie, post), nu doar
      compania - poti aplica la mai multe posturi in aceeasi companie, iar
      acelea sunt aplicatii DIFERITE, nu duplicate
    - construieste o multime de perechi (companie, post) aduse la litere
      mici, din aplicatiile existente
    - pastreaza din cele importate DOAR aplicatiile a caror pereche
      (companie, post), adusa tot la litere mici, nu se regaseste in acea
      multime
    - intoarce DOUA valori: lista rezultata (existente + doar cele chiar
      noi) si numarul de aplicatii noi
    """
    pass


# ==============STREAMLIT=========================
# De aici incolo e partea pe care o vede utilizatorul in pagina web. Folosim
# doar functiile de mai sus, nu mai scriem logica noua aici.

st.set_page_config(page_title="Tracker aplicatii de job")
st.title("Tracker-ul meu de aplicatii de job")

aplicatii = incarca_aplicatii()   # lista curenta, valabila pentru toata rularea asta a scriptului

# ------------- 1. Import date CSV (PASI.md, Pasul 3) -------------
st.header("1. Import date CSV")
fisier_incarcat = st.file_uploader("Lista de aplicatii de adaugat", type="csv")

if fisier_incarcat is not None:
    importate = citeste_csv_incarcat(fisier_incarcat)
    # TODO (PASI.md, Pasul 3):
    # 1. calculezi o PREVIZUALIZARE cu adauga_aplicatii_noi(aplicatii, importate)
    #    -> primesti (lista_rezultata, cate_noi); NU salvezi inca nimic
    # 2. afisezi cu st.caption cate aplicatii noi s-au gasit
    # 3. afisezi un buton (vizibil doar daca cate_noi > 0) cu textul
    #    "Adauga cele {cate_noi} aplicatii noi"
    # 4. la apasarea butonului: salveaza_aplicatii(lista_rezultata),
    #    st.success(...), st.rerun()
    pass


# ------------- 2. Tabelul filtrabil dupa stare (PASI.md, Pasul 4) -------------
st.header("2. Aplicatiile mele")
# TODO (PASI.md, Pasul 4):
# 1. daca `aplicatii` e goala, afisezi un st.info care spune userului sa
#    importe fisierul demo sau sa adauge o aplicatie manual, si te opresti
#    aici (fara restul de mai jos)
# 2. altfel, adaugi un st.selectbox cu optiunile ["Toate"] + STARI
# 3. daca s-a ales "Toate", afisezi toata lista; altfel pastrezi doar
#    aplicatiile care au exact acea stare
# 4. afisezi rezultatul cu st.dataframe, plus un st.caption cu numarul
#    afisat din total


# ------------- 3. Adauga aplicatie noua (PASI.md, Pasul 5) -------------
st.header("3. Adauga o aplicatie noua")
# TODO (PASI.md, Pasul 5):
# 1. un st.form cu patru campuri: companie, post, data aplicarii
#    (valoare implicita azi, cu st.date_input), sursa
# 2. la trimiterea formularului (doar daca si compania, si postul sunt
#    completate):
#    - construiesti aplicatia noua, cu stare="Aplicat" si
#      data_ultimului_contact = data aplicarii aleasa in formular
#    - o adaugi la lista completa cu .append(...)
#    - apelezi salveaza_aplicatii, afisezi o confirmare, st.rerun()
pass
