# PROIECT DE PORTOFOLIU — Tracker aplicații de job

La fel ca la celelalte proiecte de portofoliu: pornești de la zero, ca
la un proiect real. La final, el trebuie să existe ca **repository pe
GitHub**. Ce trebuie să facă aplicația găsești mai jos; cum o
construiești, pas cu pas, e în `PASI.md`.

---

## Despre ce e vorba

Cauți de lucru și aplici la multe joburi în paralel — e ușor să pierzi
șirul: la ce ai aplicat, în ce stadiu ești. Vrei o aplicație care ține
evidența TUTUROR aplicațiilor tale, cu stare (Aplicat / Interviu /
Ofertă / Respins).

## Ce trebuie să facă aplicația

1. **Import dintr-un CSV.** `demo_data/aplicatii_demo.csv` conține
   coloanele `companie,post,data_aplicare,sursa` — aplicații deja
   făcute, poate exportate dintr-un spreadsheet personal. Importul
   adaugă DOAR aplicațiile care nu există deja — verifici după
   PERECHEA `companie` + `post` (poți aplica la mai multe posturi în
   aceeași companie, iar acelea sunt aplicații diferite, nu duplicate).

2. **Datele rămân salvate, într-un fișier JSON.** Fiecare aplicație
   are: `companie`, `post`, `data_aplicare`, `sursa` (ex: linkedin /
   site / recomandare), `stare` ("Aplicat" / "Interviu" / "Oferta" /
   "Respins"), `data_ultimului_contact`, `notite`. La import, o
   aplicație nouă pornește cu starea "Aplicat" și
   `data_ultimului_contact` egală cu `data_aplicare`. Datele trebuie
   să rămână acolo și după ce închizi și redeschizi aplicația.

3. **O pagină Streamlit cu:**
   - un tabel filtrabil după `stare` (o variantă simplă de "kanban" —
     alegi o stare dintr-un selectbox și vezi doar aplicațiile din
     acea etapă);
   - un formular de adăugare manuală a unei aplicații noi.

## Cerințe tehnice

- Doar `csv`, `json`, `os`, `datetime` (module deja predate) — fără
  `pandas`.
- Fișierul JSON de pe calculator e mereu varianta corectă a datelor:
  la fiecare rerulare a scriptului Streamlit, îl recitești, nu ții
  datele doar în memorie.
- Scrii câte o funcție separată pentru fiecare bucată de logică
  (salvare/încărcare, import din CSV) — abia la final vine partea de
  interfață Streamlit, care doar le folosește.

## Date demo

`demo_data/aplicatii_demo.csv` — 6 aplicații de start, pe care le
imporți la prima rulare ca să ai cu ce testa aplicația.

## Când e gata

- [ ] pot importa fișierul demo și văd aplicațiile în tabel
- [ ] pot adăuga manual o aplicație nouă
- [ ] pot filtra tabelul după stare
- [ ] datele rămân salvate după ce închid și redeschid aplicația
- [ ] proiectul e trimis pe Git (`git add`, `git commit`, `git push`)

---
