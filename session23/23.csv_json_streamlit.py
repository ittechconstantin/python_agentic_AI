# =============================================================
# CSV/JSON + STREAMLIT  -  o interfata vizuala peste fisierele de pe disc
# =============================================================
# Ai invatat Streamlit in sesiunea 22 si CSV/JSON mai sus, in
# 23.csv_json.py (open/with, csv.reader/writer, csv.DictReader/
# DictWriter, json.loads/dumps). Aici le combini: in loc sa citesti si
# sa scrii fisiere doar din terminal, construiesti o interfata vizuala
# peste ele - exact ce faci intr-o aplicatie reala.
#
# Nu introducem nimic nou fata de csv/json/Streamlit - doar le folosim
# IMPREUNA, pe un caz concret (vanzari).
#
# CERINTE:  pip install streamlit
# Cum rulezi:  streamlit run 23.csv_json_streamlit.py
# =============================================================

import csv
import json
import os

import streamlit as st

# IMPORTANT despre Streamlit: la FIECARE interactiune a userului (upload,
# apasare buton, scriere in input), Streamlit ruleaza din nou TOT fisierul,
# de sus pana jos, ca un script nou. De aceea liniile de mai jos (crearea
# folderului, calea catre CSV) se executa la fiecare rerun - nu doar o
# singura data, la pornire.

TMP = "data_s23_streamlit"  # numele folderului unde tinem fisierele salvate; e doar un string, folderul inca nu exista pe disc
os.makedirs(TMP, exist_ok=True)  # creeaza folderul TMP daca nu exista deja; exist_ok=True inseamna "nu da eroare daca exista deja"
CALEA_CSV = os.path.join(TMP, "vanzari_streamlit.csv")  # combina folderul + numele fisierului intr-o cale valida (ex: "data_s23_streamlit/vanzari_streamlit.csv")

st.title("Vanzari - CSV/JSON cu interfata streamlit")

# #############################################################
# PARTEA 1 - INCARCI UN CSV SI IL VEZI CA TABEL
# #############################################################
# st.file_uploader iti da fisierul incarcat de user ca un obiect "in
# memorie" - il citesti cu .read(), il decodezi la text, apoi il
# parsezi EXACT ca pe orice CSV, cu csv.DictReader.

st.header("1. Incarca un CSV si vezi ca un tabel")

# fisier_incarcat NU e o cale pe disc, ci un obiect special de tip
# "UploadedFile" care se comporta ca un fisier deschis, tinut in memorie
# de browser/Streamlit. Cat timp userul nu a ales inca niciun fisier,
# fisier_incarcat este None.
fisier_incarcat = st.file_uploader("Alege un fisier csv", type=['csv'])  # type=['csv'] limiteaza selectia doar la fisiere .csv

if fisier_incarcat is not None:  # intram aici doar dupa ce userul a incarcat un fisier
    # .read() citeste tot continutul fisierului ca octeti (bytes), nu ca text.
    # .decode("utf-8") transforma octetii in text (str), folosind encoding-ul
    # utf-8 - acelasi encoding cu care scriem noi mai jos, la salvare.
    # .splitlines() sparge textul mare in lista de linii (una pe rand),
    # exact ce asteapta csv.DictReader ca input.
    linii_text = fisier_incarcat.read().decode("utf-8").splitlines()
    print(linii_text)  # doar pentru debug, se vede in terminalul unde ai rulat "streamlit run", NU in pagina web
    randuri = list(csv.DictReader(linii_text))  # DictReader foloseste automat prima linie ca nume de coloane si construieste un dict per rand
    st.dataframe(randuri)  # streamlit stie sa afiseze o lista de dict-uri direct ca tabel interactiv (poti sorta, scrolla etc.)
    st.success(f"Au fost incarcare {len(randuri)} randuri")  # cutie verde de confirmare, cu numarul de randuri citite din fisier


# #############################################################
# PARTEA 2 - FORMULAR CARE ADAUGA UN RAND NOU PE DISC
# #############################################################
# st.form grupeaza mai multe inputuri si le trimite O SINGURA DATA, la
# apasarea butonului - nu la fiecare tasta. Salvarea foloseste modul
# "a" (append), ca sa nu stergem ce era deja scris.

st.header("2. Adauga o vanzare noua")

# "form_vanzare" e doar un id intern, unic, ca streamlit sa stie ce
# formular e acesta (poti avea mai multe formulare pe aceeasi pagina).
# In interiorul lui "with", inputurile NU declanseaza un rerun la fiecare
# tasta apasata - valorile raman "in asteptare" pana userul apasa butonul
# de submit. Asta e diferenta fata de st.text_input folosit singur, in
# afara unui form, care reruleaza scriptul la fiecare caracter tastat.
with st.form("form_vanzare"):
    produs = st.text_input("Introduceti numele produsului: ")
    cantitate = st.number_input("Cantitate", min_value=1, step=1)  # min_value=1 -> nu accepta cantitate 0 sau negativa
    pret = st.number_input("Pret unitar(lei)", min_value=0.0, step=0.5)  # step=0.5 -> sagetile de +/- din UI cresc/scad din 0.5 in 0.5
    trimis = st.form_submit_button("Salveaza vanzarea")  # trimis e True DOAR in rularea (rerun-ul) in care s-a apasat acest buton; la orice alt rerun e False

# trimis and produs: verificam si ca s-a apasat butonul, si ca userul chiar
# a scris ceva in campul "produs" (un string gol e considerat False in Python).
if trimis and produs:
    exista_deja = os.path.exists(CALEA_CSV)  # True daca fisierul CSV exista deja pe disc, False daca inca nu a fost creat
    # newline="" e recomandarea oficiala din documentatia modulului csv,
    # pe Windows: fara el, csv.writer poate introduce randuri goale suplimentare.
    # mod "a" (append) = scriem la finalul fisierului, fara sa stergem ce era deja acolo.
    with open(CALEA_CSV, "a", newline="", encoding="utf-8") as f:
        # DictWriter stie sa scrie un dict ca un rand de CSV, atata timp cat
        # cheile dictului corespund cu fieldnames declarate aici.
        writer = csv.DictWriter(f, fieldnames=["produs", "cantitate", "pret"])
        if not exista_deja:
            writer.writeheader()  # scriem randul de antet (produs,cantitate,pret) DOAR daca fisierul e nou-nout, altfel am duplica antetul de fiecare data

        writer.writerow({'produs': produs, 'cantitate': cantitate, 'pret': pret})  # scriem efectiv randul nou, ca text CSV, pe disc
    st.toast(f"Salvat: {produs}")  # notificare mica, discreta, in coltul paginii
    st.balloons()  # efect vizual (baloane) - doar cosmetic, arata ca operatia a reusit


# #############################################################
# PARTEA 3 - TOATE VANZARILE SALVATE PANA ACUM + TOTAL
# #############################################################
# De fiecare data cand Streamlit reruleaza scriptul (la orice
# interactiune), recitim fisierul de pe disc - asa vezi mereu starea
# CURENTA, inclusiv randul adaugat mai sus.

st.header("3. Toate vanzarile salvate pana acum")

if os.path.exists(CALEA_CSV):  # daca fisierul inca nu exista (nicio vanzare salvata), sarim direct la else
    with open(CALEA_CSV, "r", encoding="utf-8") as f:
        vanzari = list(csv.DictReader(f))  # citim din nou TOT fisierul de pe disc, inclusiv randul adaugat mai sus la Partea 2
        # list(...) e important: csv.DictReader e un iterator care se "consuma"
        # o singura data. Daca l-am folosi de mai multe ori fara list(),
        # a doua oara ar aparea gol, pentru ca fisierul a fost deja citit
        # pana la capat.

    st.dataframe(vanzari)  # tabelul cu toate vanzarile de pana acum, mereu la zi (pentru ca recitim fisierul la fiecare rerun)
    # Valorile citite din CSV sunt intotdeauna string-uri (chiar daca "arata"
    # ca numere), de aceea trebuie convertite explicit cu float() inainte
    # de inmultire - altfel Python ar incerca sa inmulteasca text cu text.
    total = sum(float(produs['cantitate']) * float(produs['pret']) for produs in vanzari)
    st.metric("Total incasari: ", f"{total:.2f} lei")  # afisare tip "KPI" (cifra mare, cu eticheta); :.2f rotunjeste la 2 zecimale
else:
    st.info("Nicio vanzare")  # cutie albastra informativa, afisata cand nu exista inca niciun rand salvat


# #############################################################
# PARTEA 4 - ACELEASI DATE, CA JSON  (pentru un API)
# #############################################################
# Acelasi flux CSV -> JSON din lectie (23.csv_json.py, sectiunea 17),
# dar afisat vizual cu st.json in loc de print.


st.header("Date in format json")

if os.path.exists(CALEA_CSV):
    with open(CALEA_CSV, "r", encoding="utf-8") as f:
        vanzari = list(csv.DictReader(f))  # exact aceeasi citire ca la Partea 3 (recitim CSV-ul, il transformam in lista de dict-uri)

    # st.json(vanzari) face automat, "pe sub capota", ce faceai manual in
    # 23.csv_json.py cu json.dumps(vanzari, indent=2) + print(...): ia o
    # structura Python (lista de dict-uri) si o afiseaza ca JSON. Diferenta
    # e ca aici rezultatul e interactiv - poti sa strangi/extinzi obiectele
    # din pagina, in loc sa citesti text simplu in terminal.
    st.json(vanzari)

else:
    st.info("Nicio vanzare")  # aceeasi verificare ca la Partea 3, repetata aici pentru ca aceasta sectiune reciteste fisierul independent


# =============================================================
# RECAP
# =============================================================
# - st.file_uploader + csv.DictReader  -> incarci si parsezi un CSV
#   incarcat de user (nu unul de pe disc, stiut dinainte).
# - st.form + st.form_submit_button    -> trimiti mai multe campuri
#   deodata, apoi scrii pe disc cu csv.DictWriter (mod "a" = append).
# - Recitesti fisierul la FIECARE rerulare -> interfata arata mereu
#   starea curenta, fara sa tii tu manual o lista in memorie.
# - st.json(...) -> acelasi rezultat ca json.dumps + print, dar
#   afisat vizual, pliabil, usor de citit.
# =============================================================
