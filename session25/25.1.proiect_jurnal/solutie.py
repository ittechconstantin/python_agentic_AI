import csv
import os
import json
import streamlit as st
from datetime import date

# Cele doua fisiere de date, din folderul demo_data/:
#
# - biblioteca.json  -> aici locuieste, de fapt, biblioteca ta. E fisierul
#                        pe care il citeste incarca_titluri() si il scrie
#                        salveaza_titluri(). Se modifica automat de catre
#                        aplicatie, de fiecare data cand adaugi/schimbi ceva
#                        - nu il editezi tu manual.
#
# - carti_filme_demo.csv -> o lista gata facuta de titluri (8 carti/filme),
#                        pusa acolo doar ca sa ai cu ce testa aplicatia de
#                        la inceput. Se foloseste O SINGURA DATA, cand il
#                        incarci prin butonul de import din pagina - dupa
#                        aceea, titlurile din el ajung in biblioteca.json,
#                        iar fisierul CSV ramane neschimbat pe calculator.
# ======================================================================

# ==============CONFIGURARE=========================
# Scopul aplicatiei: un jurnal personal de carti/filme (tip mini Goodreads).
# Fiecare titlu are o "stare" (de citit / in curs / terminat), un rating si
# notite, iar toate datele sunt salvate pe calculator intr-un fisier JSON, ca sa
# ramana acolo si dupa ce inchidem si redeschidem aplicatia.

TMP = "demo_data"                        # numele folderului unde tinem fisierele aplicatiei
os.makedirs(TMP, exist_ok=True)          # cream folderul demo_data daca nu exista deja

calea_db = os.path.join(TMP, "biblioteca.json")   # aici traieste "baza de date" a aplicatiei

STARI = ["de citit", "in curs", "terminat"]  # toate starile posibile pentru un titlu
TIPURI = ['carte', "film"]                    # cele doua tipuri de titluri acceptate

# ==============PASUL 1=============================
# Aici tinem lista de carti/filme si dupa ce inchidem aplicatia. Nu vrem
# sa disparem tot ce am adaugat de fiecare data cand oprim programul. De
# aceea scriem lista intr-un fisier de pe calculator (biblioteca.json) de
# fiecare data cand se schimba ceva, si o citim din acel fisier de fiecare
# data cand pornim aplicatia din nou.

# De ce avem nevoie de functia asta? Cand pornim aplicatia, nu vrem sa
# incepem mereu cu o lista goala, vrem sa vedem exact titlurile pe care
# le-am salvat data trecuta. Functia asta se ocupa de partea de "citire":
# se uita pe calculator daca exista deja un fisier cu titluri salvate si,
# daca da, il aduce inapoi ca lista, gata de folosit in aplicatie.
def incarca_titluri():
    if os.path.exists(calea_db):                    # verifica daca fisierul exista
        with open(calea_db, encoding='utf-8') as f: # il deschide
            return json.load(f)                     # json.load(f) citeste informatiile din f, il interpreteaza ca un JSON
    else:
        return []                                   # daca fisierul nu exista, nu afisam nimic



# De ce avem nevoie de functia asta? e partea de "scriere". De fiecare
# data cand se schimba ceva in lista (adaugam un titlu, ii schimbam
# starea, ii dam un rating), trebuie sa punem si pe calculator schimbarea
# aceea, nu doar sa o tinem in memorie cat timp e deschisa pagina. Fara ea,
# tot ce am adauga s-ar pierde imediat ce inchidem aplicatia.
def salveaza_titluri(titluri):
    # scrie intreaga lista pe calculator, suprascriind complet fisierul vechi -
    # nu adaugam la finalul lui, il inlocuim in intregime cu ce avem acum
    # in memorie (de-asta orice functie care modifica un titlu trebuie sa
    # apeleze salveaza_titluri cu LISTA COMPLETA, nu doar cu titlul schimbat)
    with open(calea_db, mode='w', encoding="utf-8") as f:
        json.dump(titluri,f, indent=2)


# ==============PASUL 2=============================
# Aici luam un fisier CSV pe care il incarca utilizatorul, si il transformam intr-o
# lista de titluri gata de pus in biblioteca, avand grija sa nu adaugam
# de doua ori acelasi titlu.

# Exemplu, ca sa vezi exact ce intra si ce iese din functie:
#
#   INTRA (rand_brut, asa cum vine dintr-un CSV):
#   {"titlu": "Dune", "tip": "carte", "autor": "Frank Herbert", "an": "1965"}
#
#   IESE (ce intoarce normalizeaza_rand):
#   {"titlu": "Dune", "tip": "carte", "autor": "Frank Herbert", "an": 1965,
#    "stare": "de citit", "rating": None, "data_terminarii": None, "notite": ""}
#
def normalizeaza_rand(rand_brut):
    # un rand citit dintr-un CSV vine cu TOATE valorile ca text (chiar si
    # anul) si nu are deloc coloanele stare/rating/data_terminarii/notite -
    # aici completam exact acele campuri, cu valorile implicite pentru un
    # titlu proaspat importat: nu a fost inca citit/vizionat de noi
    return {
        'titlu': str(rand_brut['titlu'].strip()),
        'tip': str(rand_brut['tip']).strip(),
        'autor': str(rand_brut['autor']).strip(),
        'an': int(rand_brut['an']),
        'stare': "de citit",
        'rating': None,
        'data_terminarii': None,
        'notite': ""
    }

# Exemplu, ca sa vezi exact ce intra si ce iese din functie:
#
#   INTRA (fisier), continutul CSV incarcat, ca text simplu ar arata asa:
#   titlu,tip,autor,an
#   Dune,carte,Frank Herbert,1965
#   Oppenheimer,film,Christopher Nolan,2023
#
#   IESE (lista de titluri, dupa ce fiecare rand a trecut prin normalizeaza_rand):
#   [
#     {"titlu": "Dune", "tip": "carte", "autor": "Frank Herbert", "an": 1965,
#      "stare": "de citit", "rating": None, "data_terminarii": None, "notite": ""},
#     {"titlu": "Oppenheimer", "tip": "film", "autor": "Christopher Nolan", "an": 2023,
#      "stare": "de citit", "rating": None, "data_terminarii": None, "notite": ""},
#   ]
#
def citeste_csv_incarcat(fisier):
    # fisier.read() citeste tot continutul din fisier
    #.decode("utf-8") transforma acel bytes(fisier) intr-un sir de caractere
    # imparte textul in linii
    linii_text = fisier.read().decode("utf-8").splitlines()
    return [normalizeaza_rand(r) for r in csv.DictReader(linii_text)]


def adauga_titluri_noi(existente, importate):
    """ Adaugam DOAR titlurile noi care nu exista deja"""

    # mutam totul la litere mici ca sa comparam fara sa conteze majusculele -
    # "Dune" si "dune" trebuie tratate ca fiind acelasi titlu, altfel am
    # accepta duplicate din greseala doar din cauza scrierii diferite
    titluri_existente = {rand['titlu'].lower() for rand in existente}
    de_adaugat = [rand for rand in importate if rand['titlu'].lower() not in titluri_existente]
    # intoarcem lista completa rezultata (existente + doar cele chiar noi) SI
    # numarul de titluri noi, ca sa il putem afisa userului in Streamlit
    # (ex. "3 titluri noi gasite"), fara sa mai numaram inca o data acolo
    return existente+de_adaugat, len(de_adaugat)


# ==============STREAMLIT=============================
# De aici incolo e partea pe care o vede utilizatorul in pagina web: butoane,
# tabele, formulare. Folosim doar functiile scrise mai sus, nu mai adaugam
# logica noua aici. Un lucru important de stiut despre Streamlit: de fiecare
# data cand utilizatorul apasa pe ceva (un buton, un formular), tot codul de
# mai jos se executa din nou, de la inceput pana la sfarsit - de aceea citim
# lista de titluri din fisier chiar la inceput, ca sa avem mereu varianta
# cea mai recenta.

st.set_page_config(page_title="Jurnal carti/filme")
st.title("Jurnalul meu cu carti/filme")

titluri = incarca_titluri()   # "poza" curenta a bibliotecii, valabila pentru toata rularea asta a scriptului

# ------------- 1. Import date CSV -------------
# Intentia: userul incarca un CSV, VEDE cate titluri noi ar aparea (fara sa
# se salveze nimic inca), si abia daca apasa butonul de confirmare se scrie
# efectiv pe calculator. Asa evitam sa suprascriem biblioteca din greseala doar
# pentru ca userul a incarcat fisierul gresit.
st.header("1. Import date CSV")
fisier_incarcat = st.file_uploader("Lista de titluri de adaugat", type="csv")

if fisier_incarcat is not None:
    importate = citeste_csv_incarcat(fisier_incarcat)
    # aici avem doar o PREVIZUALIZARE: titluri_previzualitate e cum ar arata
    # biblioteca DACA am confirma importul - nu am salvat inca nimic
    titluri_previzualitate, cate_noi = adauga_titluri_noi(titluri, importate)
    st.caption(f"{cate_noi} titluri noi gasite")

    # butonul apare doar daca chiar exista ceva de adaugat; la click salvam
    # efectiv pe calculator lista din previzualizare si reincarcam pagina
    # (st.rerun()) ca tabelul de mai jos sa reflecte imediat noile titluri
    if cate_noi > 0 and st.button(f"Adauga cele {cate_noi} titluri noi"):
        salveaza_titluri(titluri_previzualitate)
        st.success(f"{cate_noi} titluri noi au fost adaugate!")
        st.rerun()


# ==============2. CATALOG CU CARTILE/FILME=============================
# Intentia: userul alege un tip si o stare din cele doua selectbox-uri, iar
# tabelul de mai jos arata DOAR titlurile care se potrivesc cu ambele
# filtre in acelasi timp (tip SI stare, nu tip SAU stare).
st.header("2. Biblioteca mea")
if not titluri:
    st.info("Nu exista niciun titlu adaugat.")
else:
    col_tip, col_stare = st.columns(2)

    with col_tip:
        tip_ales = st.selectbox("Filtreaza dupa tip", TIPURI )
    with col_stare:
        stare_aleasa = st.selectbox("Filtreaza dupa stare", STARI)

    # pastram din lista completa doar titlurile care indeplinesc AMBELE
    # conditii deodata (filtrele se combina, nu se aplica separat)
    titluri_filtrare = [t for t in titluri if t['tip'] == tip_ales and t['stare'] == stare_aleasa]

    st.dataframe(titluri_filtrare)


# ==============3.Adauga o carte noua=============================
# Intentia: un formular simplu prin care userul adauga MANUAL un titlu care
# nu vine din CSV. Orice titlu nou adaugat aici porneste cu aceleasi valori
# implicite ca la import (stare "de citit", fara rating/data/notite), pentru
# ca inca nu a fost citit/vizionat.
with st.form("form_adaugare"):
    titlu_nou = st.text_input("Introduceti un titlu")
    tip_nou = st.selectbox("Tip", TIPURI)
    autor_nou = st.text_input("Introduceti un autor")
    an_adaugat = st.number_input("Introduceti anul cartii", min_value=2000, step=1, value=2026)
    adauga = st.form_submit_button("Adauga in biblioteca")

    if adauga and titlu_nou:
        titluri.append({
            "titlu": titlu_nou,
            "tip": tip_nou,
            "autor": autor_nou,
            "an": an_adaugat,
            "stare": "de citit",
            "rating": None,
            "data_terminarii": None,
            "notite": ""
        })

        salveaza_titluri(titluri)
        st.toast("Felicitari ai adaugat o carte noua!")
