# =============================================================
# PAGINA  -  Adauga task
# =============================================================
# st.form (s22) trimite toate campurile O SINGURA DATA, la submit.
# O eroare 422 apare aici ca mesaj clar, camp cu camp - formatat de api().
# =============================================================

import streamlit as st
from comun import api

st.title("➕ Adauga task")

# TODO: formularul de adaugare
#   - titlu: st.text_input
#   - limbaj + dificultate: cate un st.selectbox, pe aceeasi linie (st.columns)
#   - recompensa: st.number_input
#   - buton de submit: st.form_submit_button




# TODO: cand formularul e trimis (trimis == True)
#   - trimite campurile completate mai sus catre API, ca JSON:
#       api("POST", "/task-uri", json={"titlu": titlu, "limbaj": limbaj,
#           "dificultate": dificultate, "recompensa": recompensa})
#   - daca ok: rezultat e task-ul creat, asa cum l-a intors serverul -
#     arata un mesaj de succes cu rezultat['titlu'] si rezultat['id'],
#     apoi st.balloons() (formularul se goleste singur, clear_on_submit=True)
#   - daca nu: st.error(rezultat) - mesajul vine deja formatat de api(),
#     camp cu camp
