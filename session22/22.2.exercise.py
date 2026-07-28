# EXERCITIUL 2  (Streamlit)  -  PLAYLIST MUZICAL (session_state)
# =============================================================
#
# CONTEXT (caz real)
# ------------------
# Construiesti un playlist: adaugi melodii una cate una, si ele RAMAN pe
# ecran, cu durata totala calculata live. Aici e cheia Streamlit: scriptul
# se re-ruleaza la fiecare click, deci playlist-ul trebuie tinut in
# st.session_state (altfel s-ar goli la fiecare adaugare).
#
#
# CE AI DE FACUT  (scrie in ZONA TA DE LUCRU)
# -------------------------------------------
# 1. st.title("Playlist-ul tau")
# 2. initializeaza  st.session_state.playlist  cu o lista GOALA, daca nu exista.
# 3. text_input pentru titlu:  key="titlu"
# 4. text_input pentru artist:  key="artist"
# 5. pills pentru gen:  key="gen",
#       optiuni  ["pop", "rock", "hip-hop", "electronic", "clasica"],
#       default="pop"
# 6. slider pentru durata (minute):  key="durata", min_value=1, max_value=10, value=3
# 7. buton "Adauga in playlist" (key="adauga"): daca titlul nu e gol, adauga
#       {"titlu": ..., "artist": ..., "gen": ..., "durata": ...}
#    in  st.session_state.playlist.
# 8. buton "Goleste playlist" (key="goleste"): reseteaza playlist-ul la [].
# 9. afiseaza  st.write(f"{n} melodii, {total} minute")  (n = cate melodii,
#    total = suma duratelor), apoi fiecare melodie cu
#    st.write(f"- {titlu} - {artist} ({gen}, {durata} min)").
#
#
# CUM VERIFICI
# ------------
#   streamlit run 22.2.exercise.py
#   (adaugi melodii; lista si durata totala cresc si NU se pierd la click)
#
#
# COMPORTAMENT ASTEPTAT (exemplu)
# -------------------------------
#   adaugi "Nu ma las" - "Grupul X" (rock, 4 min), apoi "Vara" - "Grupul Y"
#   (pop, 3 min)
#   -> session_state.playlist are 2 elemente
#   -> pe ecran:  "2 melodii, 7 minute"
#      "- Nu ma las - Grupul X (rock, 4 min)"
#      "- Vara - Grupul Y (pop, 3 min)"
#
#
# INDICII
# -------
#   - if "playlist" not in st.session_state: st.session_state.playlist = []
#   - titlu = st.text_input("Titlu", key="titlu")
#   - artist = st.text_input("Artist", key="artist")
#   - gen = st.pills("Gen", [...], key="gen", default="pop")
#   - durata = st.slider("Durata (minute)", 1, 10, 3, key="durata")
#   - if st.button("Adauga in playlist", key="adauga") and titlu:
#         st.session_state.playlist.append({"titlu": titlu, "artist": artist,
#                                            "gen": gen, "durata": durata})
#   - if st.button("Goleste playlist", key="goleste"): st.session_state.playlist = []
#   - total = sum(m["durata"] for m in st.session_state.playlist)
#   - st.write(f"{len(st.session_state.playlist)} melodii, {total} minute")
#   - for m in st.session_state.playlist:
#         st.write(f"- {m['titlu']} - {m['artist']} ({m['gen']}, {m['durata']} min)")
# =============================================================

import streamlit as st


# ---- ZONA TA DE LUCRU ---------------------------------------
# TODO: scrie aici interfata (title + session_state + text_input x2 +
#       pills + slider + 2 butoane + afisare lista)

st.title("Playlist-ul tau")
st.text_input("Titlu", key="titlu")
if "playlist" not in st.session_state: st.session_state.playlist = []
st.text_input("Artist", key="artist")
st.pills("Gen", ["pop", "rock", "hip-hop", "electronic", "clasica"], key="gen", default="pop")
st.slider("Durata (minute)", 1, 10, 3, key="durata")
if st.button("Adauga in playlist", key="adauga") and "titlu":st.session_state.playlist.append({"titlu": titlu, "artist": artist,"gen": gen, "durata": durata})
if st.button("Goleste playlist", key="goleste"): st.session_state.playlist = []
total = sum(m["durata"] for m in st.session_state.playlist)
st.write(f"{len(st.session_state.playlist)} melodii, {total} minute")
for m in st.session_state.playlist:
        st.write(f"- {m['titlu']} - {m['artist']} ({m['gen']}, {m['durata']} min)")
