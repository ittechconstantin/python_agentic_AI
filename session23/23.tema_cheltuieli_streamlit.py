# =============================================================
# TEMA - JURNAL DE CHELTUIELI  (CSV/JSON + Streamlit)
# =============================================================
# Foloseste exact aceleasi idei ca in 23.csv_json_streamlit.py
# (fisierul rezolvat la curs), dar pe alt subiect: in loc de vanzari,
# construiesti un jurnal personal de cheltuieli, cu un total defalcat
# PE CATEGORIE - asta e partea noua fata de exemplul din curs.
#
# Nu trebuie nimic ce nu ai vazut deja:
#   - st.file_uploader, st.form, st.dataframe, st.metric, st.json
#   - csv.DictReader / csv.DictWriter
#   - dictionare, bucle for, sum()
#
# Cauta liniile marcate cu "# TODO" - acolo scrii TU codul. Restul
# (importuri, foldere, titluri) e deja pus, ca sa te poti concentra pe
# logica, nu pe boilerplate. Daca te blochezi, uita-te cum a fost
# rezolvata partea echivalenta in 23.csv_json_streamlit.py - structura
# e aceeasi, doar campurile difera.
#
# CERINTE:  pip install streamlit
# Cum rulezi:  streamlit run 23.tema_cheltuieli_streamlit.py
# =============================================================

import csv
import json
import os

import streamlit as s
import streamlit as st
import pandas as pd
import numpy as np

TMP = "data_s23_tema_cheltuieli"
os.makedirs(TMP, exist_ok=True)
CALEA_CSV = os.path.join(TMP, "cheltuieli.csv")

CATEGORII = ["Mancare", "Transport", "Utilitati", "Divertisment", "Altele"]

st.title("Jurnalul meu de cheltuieli")


# #############################################################
# PARTEA 1 - INCARCA UN CSV CU CHELTUIELI SI VEZI-L CA TABEL
# #############################################################
# Identic ca structura cu Partea 1 din exemplul rezolvat: userul
# incarca un CSV (poate exporta unul din banca sau il creezi tu de
# test, cu coloanele categorie,suma,data), tu il citesti si il arati
# ca tabel.

st.header("1. Incarca un CSV cu cheltuieli")

# TODO 1.1: creeaza un st.file_uploader care accepta doar fisiere .csv
fisier_incarcat = st.file_uploader("Accepta doar fisiere csv", type=['csv'])

# TODO 1.2: daca fisier_incarcat nu e None:
#   - citeste continutul cu .read().decode("utf-8").splitlines()
#   - transforma-l in lista de dictionare cu csv.DictReader (nu uita list(...))
#   - afiseaza-l cu st.dataframe(...)
#   - afiseaza un mesaj de succes cu st.success(...), cu numarul de randuri
if fisier_incarcat is not None:
    linii_text = fisier_incarcat.read().decode("utf-8").splitlines()
    randuri = list(csv.DictReader(linii_text))
    st.dataframe(randuri)
    st.success(f"Auf fost incarcate{len(randuri)} randuri")

# #############################################################
# PARTEA 2 - FORMULAR CARE ADAUGA O CHELTUIALA NOUA
# #############################################################
# La fel ca Partea 2 din exemplul rezolvat (st.form + csv.DictWriter,
# mod "a"), dar cu campurile unei cheltuieli: categorie, suma, data.
#
# Diferenta fata de exemplul din curs: pentru categorie NU folosi
# st.text_input (userul ar putea scrie orice, cu greseli de tastare).
# Foloseste st.selectbox("Categorie", CATEGORII) - asa alege dintr-o
# lista fixa, ca sa poata fi grupate corect mai jos, la Partea 3.
# Pentru data, foloseste st.date_input("Data") - iti da direct un
# obiect de tip date, pe care il poti transforma in text cu str(...)
# cand il scrii in CSV.

st.header("2. Adauga o cheltuiala noua")

# TODO 2.1: deschide un st.form(...) si, in interiorul lui, adauga:
#   - categorie = st.selectbox("Categorie", CATEGORII)
#   - suma = st.number_input("Suma (lei)", min_value=0.0, step=1.0)
#   - data = st.date_input("Data")
#   - trimis = st.form_submit_button("Salveaza cheltuiala")
with st.form("formular_vanzare"):
    categorie = st.selectbox("Categorie", CATEGORII)
    suma = st.number_input("Suma (lei)", min_value=0.0, step=1.0)
    data = st.date_input("Data")
    trimis = st.form_submit_button("Salveaza cheltuiala")

# TODO 2.2: daca trimis e True:
#   - verifica daca fisierul CALEA_CSV exista deja (os.path.exists)
#   - deschide-l cu open(CALEA_CSV, "a", newline="", encoding="utf-8")
#   - creeaza un csv.DictWriter cu fieldnames=["categorie", "suma", "data"]
#   - scrie header-ul DOAR daca fisierul nu exista deja
#   - scrie randul nou cu writer.writerow({...})
#     (atentie: str(data), ca sa transformi obiectul date in text)
#   - afiseaza o confirmare cu st.toast(...) sau st.success(...)
if trimis:
    exista_deja = os.path.exists(CALEA_CSV)
    with open(CALEA_CSV, "a", newline="", encoding="utf-8")as f:
        writer = csv.DictWriter(f ,fieldnames=["categorie", "suma", "data"])
        if not exista_deja:
            writer.writeheader()
        writer.writerow({"categorie": categorie, "suma": suma, "data": data})
    st.toast(f"Salvat {trimis}")
    st.snow()

# #############################################################
# PARTEA 3 - TOATE CHELTUIELILE + TOTAL GENERAL + TOTAL PE CATEGORIE
# #############################################################
# Partea "noua" fata de exemplul din curs: nu vrei doar un total mare,
# ci si cat ai cheltuit pe fiecare categorie in parte. Ideea:
#   1. porneste de la un dictionar gol, ex: totale = {}
#   2. pentru fiecare cheltuiala din lista citita din CSV:
#        - ia categoria si suma (nu uita float() pe suma!)
#        - daca acea categorie nu e inca in "totale", initializeaz-o cu 0
#        - aduna suma la totale[categorie]
#   3. la final, totale e un dict de forma
#        {"Mancare": 120.0, "Transport": 45.0, ...}
#      pe care il poti afisa fie ca text (st.write(totale)), fie ca
#      grafic cu st.bar_chart(totale) - incearca ambele variante!

st.header("3. Toate cheltuielile + totaluri")

# TODO 3.1: daca CALEA_CSV exista:
#   - citeste toate randurile cu csv.DictReader (ca la Partea 3 din curs)
#   - afiseaza-le cu st.dataframe(...)c si
#     afiseaza-l cu st.metric(...)
#   - calculeaza dictionarul "totale pe categorie", asa cum e descris
#     mai sus, si afiseaza-l cu st.bar_chart(...)
# altfel:
#   - afiseaza un mesaj cu st.info("Nicio cheltuiala inca")

totale = {}


if os.path.exists(CALEA_CSV):
    with open(CALEA_CSV, "r", newline="", encoding="utf-8") as f:
        randuri = list(csv.DictReader(f))
        st.dataframe(randuri)
        totalul_general = sum(float(categorie[suma]) for row in randuri)
        st.metric("Total", f"({totalul_general:.2f} lei)")
        if categorie not in totale:
            categorie = 0
        totalul_general += totale[categorie]
        st.bar_chart(totale)
else:
    st.info(f"Nicio cheltuiala inca")



# #############################################################
# PARTEA 4 - ACELEASI DATE, CA JSON
# #############################################################
# La fel ca Partea 4 din exemplul rezolvat: recitesti CSV-ul si il
# afisezi cu st.json(...).

st.header("4. Cheltuielile in format json")

# TODO 4.1: daca CALEA_CSV exista, reciteste-l si afiseaza-l cu st.json(...)
# altfel, afiseaza st.info("Nicio cheltuiala inca")
if os.path.exists(CALEA_CSV):
    with open(CALEA_CSV, "r", newline="", encoding="utf-8") as f:
        cheltuieli = list(csv.DictReader(f))
    st.json(cheltuieli)
else:
    st.info(f"Nicio cheltuiala inca")

# #############################################################
# BONUS (optional, doar daca ai terminat restul si vrei mai mult)
# #############################################################
# st.download_button e un widget nou, nu l-am folosit la curs, dar
# documentatia oficiala Streamlit iti arata exact cum se foloseste:
# https://docs.streamlit.io/library/api-reference/widgets/st.download_button
#
# Ideea: transformi lista de cheltuieli in text JSON cu json.dumps(...),
# apoi o dai ca "data" la st.download_button, ca userul sa poata
# descarca fisierul .json pe calculatorul lui, nu doar sa-l vada in
# pagina.

# TODO BONUS: adauga un st.download_button care ofera spre descarcare
# json.dumps(vanzari, indent=2, ensure_ascii=False) ca fisier "cheltuieli.json"
st.download_button(label, data, file_name="cheltuieli.json")

# =============================================================
# RECAP - CE TREBUIE SA STIE APLICATIA TA LA FINAL
# =============================================================
# - Incarci un CSV extern si il vezi ca tabel (Partea 1)
# - Adaugi o cheltuiala noua printr-un formular, salvata pe disc (Partea 2)
# - Vezi toate cheltuielile, totalul general SI totalul pe categorie (Partea 3)
# - Vezi aceleasi date ca JSON (Partea 4)
# - (Bonus) Poti descarca datele ca fisier .json
# =============================================================
