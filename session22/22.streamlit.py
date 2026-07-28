# STREAMLIT  -  interfete web din Python
# =============================================================
# Pana acum "interfata" aplicatiilor tale a fost terminalul sau /docs.
# Streamlit iti lasa sa faci o INTERFATA WEB reala scriind DOAR Python -
# fara HTML, CSS sau JavaScript.
#
# Ideea principala, ca PROBLEMA -> SOLUTIE:
#   PROBLEMA: o interfata web "clasica" cere HTML + CSS + JavaScript - mult
#             de invatat doar ca sa arati niste butoane si campuri.
#   SOLUTIA:  Streamlit - scrii  st.title(...), st.button(...), st.text_input(...)
#             in Python, iar el deseneaza pagina si o tine "vie" in browser.
#
# MODELUL DE RERULARE (cel mai important de inteles!):
#   La FIECARE interactiune (tastezi, apesi un buton), Streamlit ruleaza
#   INTREG scriptul de sus in jos, din nou. De aceea variabilele obisnuite
#   "uita" - pentru starea care trebuie sa RAMANA, folosim  st.session_state.
#
# Sesiunea de azi e o TURA LARGA prin ce ofera Streamlit - un fel de
# "catalog" pe care sa-l rasfoiesti si la care sa te intorci oricand ai
# nevoie de un widget anume. Nu retine totul pe de rost - retine CA EXISTA
# si UNDE sa cauti.
#
# CERINTE:  pip install streamlit
# Cum rulezi:  streamlit run 22.streamlit.py   (se deschide in browser)
#
# Ce trebuie sa stii deja: functii, dicturi, liste.
# =============================================================

import streamlit as st
from streamlit import spinner

st.title("Streamlit - demo")

# #############################################################
# PARTEA 1 - BAZE: text, primul widget, modelul de rerulare
# #############################################################

st.header("1. Text si primul widget")

# Afisare: st.write scrie aproape orice (text, numere, dicturi, liste).
st.write("Salut! Aceasta pagina e scris dintr-un fisier python")

# Primul widget: text_input. Ce tastezi devine valoarea variabilei.
# key="nume" e o eticheta interna (utila si la testare).

nume = st.text_input("Cum te cheama?")


# ATENTIE la rerulare: linia de mai jos se re-executa la FIECARE tasta.

if nume:
    st.write(f"Salut, {nume}")
else:
    st.write("Adauga un nume mai sus")

age = st.number_input("Care este varsta ta?")
comentariu = st.text_area("Descriere")

# #############################################################
# PARTEA 2 - WIDGET-URI DE INPUT (galerie)
# #############################################################
# Toate widget-urile de mai jos functioneaza LA FEL: le dai o eticheta,
# poate niste optiuni, un  key=  unic - si ele iti intorc valoarea curenta,
# gata de folosit direct intr-o variabila.

st.header("2. Widgeturi de input ")

st.subheader("2.1 Text si numere")
poveste = st.text_area("Scrie cateva randuri despre tine", key="poveste", height=80)
varsta = st.number_input("Varsta", min_value=0, max_value=120, value=25,  key="varsta")

# pills/segmented_control = alternative moderne la radio - arata ca niste
# "chip-uri"/butoane, utile cand ai putine optiuni si vrei ceva vizual.

st.subheader("2.2 Alegerea unei optiuni")
c1, c2 = st.columns(2)
pret = c1.slider("Buget(Ron)", min_value=0, max_value=200, value=125, step=50, key="pret")
marime = c2.select_slider("Marime haine", options=["XS", "S", "M", "L"], value ="S", key="marime")

st.subheader("2.3 Alegerea dintr-o lista")
c3, c4, = st.columns(2)
nivel = c3.radio("Nivel", ["Incepator", "Mediu", "Senior"], key="nivel", horizontal=True)
prioritate = c4.segmented_control("Prioritate", ['mica', 'mediu', 'mare'], key="prioritate")

st.subheader("2.4 Comutatoare")
c5, c6 = st.columns(2)
SMS = st.checkbox("SMS")
EMAIL = c5.checkbox("EMAIL")
mod_avansat = c6.toggle("Tema preferata", value = "#4f46e5", key="culoare")

st.subheader("2.5 Date, time, color_picker, file uploader")
c7, c8, c9 = st.columns(3)
data_nastere = c7.date_input("Data nasterii", key ="data")
time = c8.time_input("Ora curenta", key="ora")
color = c9.color_picker("Culoarea preferata", value = "#ffffff", key='color')

rezervare = st.datetime_input("Selecteaza data si ora:", key="rezervare")

fisier = st.file_uploader("Incarca CV-ul tau", type=['txt'], key="fisier")

if fisier is not None:
    continut = fisier.read().decode("utf-8")
    st.write(f"Fisierul cu numele {fisier.name} contine textul: {continut} si are {len(continut)} caractere")


# #############################################################
# PARTEA 3 - LAYOUT: cum organizezi pagina
# #############################################################

st.header("3. Layout")

# --- COLOANE: elemente unul langa altul, deja le-ai folosit mai sus ---
c1, c2 =  st.columns(2)
c1.metric("Suma varsta + pret", varsta+pret)
c2.metric("Litere din comentariu", len(poveste))

# --- SIDEBAR: bara din stanga, buna pentru filtre/setari globale ---
st.sidebar.header("Setari")
tema_compacta = st.sidebar.checkbox("Mod compact", key="compact")

# --- TABS: continut organizat pe "file" ---

tab1, tab2 = st.tabs(["Tabel", "Detalii"])
with tab1:
    st.dataframe({'oras': ['Bucuresti', 'Timisoara', 'Cluj'], 'populatie': [100, 500, 300]})

with tab2:
    with st.expander("Vezi mai mult"):
        st.write("Te-am paaacalit!")

# --- POPOVER: un mic "balon" care apare langa un buton, fara sa navighezi ---

with st.popover("Ce este un popover"):
    st.write("Popoverul este un continut mic, care apare langa un buton")


# #############################################################
# PARTEA 4 - AFISARE DATE SI GRAFICE
# #############################################################


# st.metric (l-ai vazut deja) - un "card" cu o cifra, optional cu delta.
st.metric("Temperatura", value = "21C", delta = "-2C")

# st.dataframe / st.table - tabele. st.json / st.code - date brute/cod.
st.json({"nume": nume or "necunoscut", "varsta": varsta})
st.code("print('Hello guyzzzzz')")
st.code("if x > 3: \n print('ceva')")

# Grafice - le dai date (dict/listă/DataFrame) si Streamlit deseneaza axele:
import random
date_grafic = {
    'zi': list(range(1, 8)),
    'vanzari': [random.randint(10, 100) for valoare in range(7)]
}

st.line_chart(date_grafic, x='zi', y='vanzari')
st.bar_chart(date_grafic, x='zi', y='vanzari')



# #############################################################
# PARTEA 5 - SESSION_STATE (starea care RAMANE)
# #############################################################

st.header("5. Session State")

# PROBLEMA: un contor cu o variabila normala s-ar reseta la 0 la FIECARE
# rerulare (adica la fiecare click). Nu ar creste niciodata.
#
# SOLUTIA: st.session_state - un "dictionar" care SUPRAVIETUIESTE rerularilor.
# Il initializezi o data (daca nu exista deja), apoi il modifici.

if "contor" not in st.session_state:
    st.session_state.contor = 0

col_a, col_b = st.columns(2)
if col_a.button("Incrementeaza", key="plus"):
    st.session_state.contor += 1      # ramane valoarea la rerulari
if col_b.button("Reset", key="reset"):
    st.session_state.contor = 0

st.metric("Contor", st.session_state.contor)


# --- FORM: aduni mai multe inputuri si le trimiti O DATA (nu la fiecare tasta) ---
st.subheader("FORM")

with st.form("f"):
    first_name = st.text_input("First name", key="first name")
    email = st.text_input("Email", key="email")
    trimis = st.form_submit_button("Trimite")

if trimis:
    st.write("S-a salvat!")


# #############################################################
# PARTEA 6 - FEEDBACK SI PROGRES
# #############################################################
# Cand aplicatia ta face ceva (salveaza, incarca, calculeaza), utilizatorul
# trebuie sa vada CE se intampla - Streamlit are unelte gata facute pentru
# fiecare situatie.

st.subheader("6. Feedback si progress")
# --- mesaje colorate, dupa tipul rezultatului ---
st.success("Felicitari! Ai invatat Streamlit")
st.warning("Mai incearca!")
st.error("Pericol")
st.info("Info")

# --- toast: un mesaj mic, temporar, in coltul paginii (nu ocupa loc fix) ---
if st.button("Arata un toast", key = 'toast'):
    st.toast("Gata!", icon="👍")

# --- progress + spinner: cand ceva DUREAZA ---
if st.button("Simuleaza un flux mai lung", key="simuleaza"):
    bara = st.progress(0, text="Se proceseaza")
    import time
    for procent in range(0, 101,20):
        time.sleep(0.4)
        bara.progress(procent, text=f"Se proceseaza....{procent}")
    with st.spinner("Aproape gata..."):
        time.sleep(0.8)

    st.success("Terminat")


# --- status: un bloc care isi schimba starea (running -> complete/error) ---
with st.status("Verificare date...", expanded=True) as status:
    st.write("Pasul1: citeste datele")
    st.write("Pasul2: validare")
    status.update(label = "Verificare completa!", state="complete")

# --- celebrare: st.balloons() / st.snow() - de folosit RAR, la momente cheie ---
if st.button("Afiseaza baloane", key = 'baloane'):
    st.balloons()

if st.button("Afiseaza zapada", key = 'snow'):
    st.snow()

# =============================================================
# RECAP / IDEI CHEIE
# =============================================================
# - Streamlit = interfata web din Python pur. Rulezi cu:  streamlit run fisier.py
# - MODELUL DE RERULARE: scriptul ruleaza de sus in jos la FIECARE interactiune.
#   -> variabilele obisnuite se reseteaza; pentru stare care RAMANE, session_state.
#
# GALERIA DE WIDGET-URI VAZUTE AZI (revino aici cand ai nevoie de unul):
#   Input simplu:    text_input, text_area, number_input
#   Plaja de valori: slider, select_slider
#   Din lista:       selectbox, multiselect
#   Alegere rapida:  radio, pills, segmented_control
#   Comutatoare:     checkbox, toggle
#   Altele:          date_input, time_input, color_picker, file_uploader
#   Layout:          columns, sidebar, tabs, expander, container, popover
#   Afisare/date:    write, markdown, metric, dataframe, table, json, code
#   Grafice:         line_chart, area_chart, bar_chart (vezi si s38)
#   Feedback:        success/error/warning/info, toast, progress, spinner,
#                    status, balloons, snow
#   Chat:            chat_message, chat_input
#   Stare:           session_state, form + form_submit_button
#
# Mult mai tarziu in curs, dupa intreg arcul FastAPI (sesiunile 33-37), te
# intorci la Streamlit in sesiunea 38 ca sa construiesti o INTERFATA reala
# pentru API-ul Buget Personal: login (JWT), formular de tranzactii, sold,
# grafice pe categorii - UI care vorbeste cu backend-ul tau, folosind exact
# widget-urile de mai sus (metric, bar_chart, form-uri, navigare pe pagini).
# =============================================================