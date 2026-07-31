# EXERCITIUL 1  (Streamlit)  -  CONFIGURATOR DE PIZZA
# =============================================================
#
# CONTEXT (caz real)
# ------------------
# "Construieste-ti singur pizza": alegi marimea, toppingurile, tipul de
# blat si daca vrei livrare - iar pretul final se recalculeaza LIVE, la
# fiecare schimbare (asa functioneaza orice configurator de produs online).
# Exersezi o combinatie larga de widgets din galeria vazuta in lectie:
# selectbox, multiselect, segmented_control, toggle, number_input, metric.
#
# `PRET_BAZA`, `PRET_TOPPING`, `PRET_BLAT_GROS`, `PRET_LIVRARE` sunt date.
#
#
# CE AI DE FACUT  (scrie in ZONA TA DE LUCRU)
# -------------------------------------------
# 1. st.title("Configurator de pizza")
# 2. selectbox "Marime":  key="marime", optiuni  list(PRET_BAZA)
# 3. multiselect "Toppinguri":  key="toppinguri",
#       optiuni  ["cascaval extra", "ciuperci", "masline", "sunca", "ananas", "ardei"]
# 4. segmented_control "Blat":  key="blat",
#       optiuni  ["subtire", "normal", "gros cu cascaval"],  default="normal"
# 5. toggle "Livrare la domiciliu (+8 RON)":  key="livrare"
# 6. number_input "Cantitate":  key="cantitate", min_value=1, value=1
# 7. calculeaza:
#       pret_pizza = PRET_BAZA[marime] + len(toppinguri) * PRET_TOPPING
#                    + (PRET_BLAT_GROS daca blat == "gros cu cascaval", altfel 0)
#       total = pret_pizza * cantitate
#               + (PRET_LIVRARE daca livrare e activat, altfel 0)
# 8. afiseaza cu  st.metric("Total de plata", f"{total} RON")
#
#
# CUM VERIFICI
# ------------
#   streamlit run 22.1.exercise.py
#   (schimbi optiunile si vezi pretul recalculandu-se instant)
#
#
# COMPORTAMENT ASTEPTAT (exemplu)
# -------------------------------
#   marime="Medie" (28), toppinguri=["cascaval extra","ciuperci"] (2x4=8),
#   blat="normal" (+0), cantitate=2, livrare=ON (+8)
#   -> pret_pizza = 28+8+0 = 36  ->  total = 36*2 + 8 = 80 RON
#
#
# INDICII
# -------
#   - marime = st.selectbox("Marime", list(PRET_BAZA), key="marime")
#   - toppinguri = st.multiselect("Toppinguri", [...], key="toppinguri")
#   - blat = st.segmented_control("Blat", [...], key="blat", default="normal")
#   - livrare = st.toggle("Livrare la domiciliu (+8 RON)", key="livrare")
#   - cantitate = st.number_input("Cantitate", min_value=1, value=1, key="cantitate")
#   - pret_pizza = PRET_BAZA[marime] + len(toppinguri) * PRET_TOPPING
#     if blat == "gros cu cascaval": pret_pizza += PRET_BLAT_GROS
#   - total = pret_pizza * cantitate
#     if livrare: total += PRET_LIVRARE
#   - st.metric("Total de plata", f"{total} RON")
# =============================================================

import streamlit as st
from streamlit import spinner
from numpy.random.mtrand import normal

PRET_BAZA = {"Mica": 20, "Medie": 28, "Mare": 36}
PRET_TOPPING = 4
PRET_BLAT_GROS = 6
PRET_LIVRARE = 8


# ---- ZONA TA DE LUCRU ---------------------------------------
# TODO: scrie aici interfata (title + selectbox + multiselect +
#       segmented_control + toggle + number_input + calcul + metric)


st.title("Configurator de pizza")
marime = st.selectbox("Marime", options=list(PRET_BAZA), key="marime")
toppinguri = st.multiselect("Toppinguri", ["cascaval extra", "ciuperci", "masline", "sunca", "ananas", "ardei"], key="toppinguri")
blat = st.segmented_control("Blat", ["subtire", "normal", "gros cu cascaval"], default="normal")
livrare = st.toggle("Livrare la domiciliu (+8 RON)", key="livrare")
cantitate = st.number_input("Cantitate", min_value=1, value=1, key="cantitate")

pret_pizza = PRET_BAZA[marime] + len(toppinguri) * PRET_TOPPING
if blat == "gros cu cascaval": pret_pizza += PRET_BLAT_GROS
total = pret_pizza * cantitate
if livrare: total += PRET_LIVRARE
st.metric("Total de plata", f"{total} RON")
