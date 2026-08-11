# GHID PAS CU PAS — Tracker aplicații de job

Acest fișier NU e o soluție — e ordinea în care construiești aplicația,
bucată cu bucată. Ideea de bază: nu scrii tot dintr-o dată. Mai întâi
faci funcțiile care lucrează cu datele (fără nicio legătură cu pagina
web), le testezi separat, și abia după ce funcționează sigur, adaugi
peste ele partea vizuală din Streamlit (butoane, tabele, formulare).

La fiecare pas îți spun: câte funcții ai de scris, ce rol are fiecare
(la ce ajută în aplicație), ce primește, ce trebuie să faci pas cu pas
în interiorul ei și ce trebuie să întoarcă la final. Nu îți dau codul
din interior — îl scrii tu. Nu sări peste ordine, fiecare pas are
nevoie de ce ai construit la pasul anterior.

---

## PASUL 0 — Configurarea de la începutul fișierului

**La acest pas nu scrii nicio funcție** — doar câteva linii, o singură
dată, la începutul fișierului. Rolul lor: pregătesc "uneltele" pe care
le vor folosi toate funcțiile și tot ecranul de mai jos.

Ce trebuie să faci, pas cu pas:
1. imporți modulele de care are nevoie aplicația: `csv`, `os`, `json`,
   `streamlit` și `date` din `datetime`;
2. stabilești numele folderului unde vor sta fișierele aplicației (ex.
   `demo_data`) și te asiguri că folderul chiar există pe calculator —
   dacă nu există, îl creezi;
3. stabilești drumul complet către fișierul în care vei salva toate
   aplicațiile (folderul de mai sus + un nume, ex. `aplicatii.json`) —
   îl ții într-o variabilă, ca să nu repeți acest drum peste tot în cod;
4. stabilești, tot ca variabilă, lista stărilor posibile pentru o
   aplicație: `Aplicat`, `Interviu`, `Oferta`, `Respins`.

💡 De reținut: aceste variabile le vei folosi în aproape fiecare
funcție și în aproape fiecare ecran de mai jos — de-asta le scrii o
singură dată, la începutul fișierului.

import csv
import os
import json
import streamlit as st
import date from datetime

TMP = "demo_data"
os.makedirs(TMP, exist_ok=True)

calea_db = os.path.join(TMP, "aplicatii.json")

STARI = ["Aplicat", "Interviu", "Oferta", "Respins"]

## PASUL 1 — Salvarea și încărcarea listei de aplicații

**La acest pas trebuie să implementezi 2 funcții.**

Rolul lor, împreună: să facă posibil ca aplicațiile pe care le adaugi
să nu dispară atunci când închizi pagina — sunt singurele două locuri
din tot codul unde vorbim cu fișierul de pe calculator.

### Funcția 1 — `incarca_aplicatii()`

def incarca_aplicatii():
    if os.path.exists(calea_db):
        with open(calea_db, encoding = 'utf-8') as f:
            return json.load(f)
    else:
        return []

**Rolul ei:** aduce înapoi, din fișierul salvat pe calculator, lista de
aplicații pe care ai adăugat-o data trecută. Fără ea, aplicația ar
porni mereu de la zero.

- Nu primește niciun parametru.
- Ce trebuie să faci, pas cu pas, în interior:
  1. verifici dacă fișierul cu aplicații există deja pe calculator;
  2. dacă NU există (e prima dată când pornești aplicația) — nu faci
     nimic altceva, sari direct la ce trebuie să întorci;
  3. dacă există — îl deschizi și citești ce e scris în el, ca JSON.
- Ce trebuie să întoarcă:
  - o listă goală `[]`, dacă fișierul nu există;
  - lista de aplicații citită din fișier, dacă există.

### Funcția 2 — `salveaza_aplicatii(aplicatii)`

def salveaza_aplicatii(aplicatii):
    with open(calea_db, mode='w', encoding='utf-8') as f:
        json.dump(aplicatii,f, indent=2)

**Rolul ei:** pune pe calculator orice schimbare faci (aplicație nouă,
stare schimbată) — altfel schimbarea s-ar pierde imediat ce închizi
pagina.

- Primește: lista completă de aplicații, așa cum arată ea chiar acum.
- Ce trebuie să faci, pas cu pas, în interior:
  1. deschizi fișierul de pe calculator în mod scriere;
  2. scrii în el toată lista primită ca parametru, ca JSON — înlocuind
     complet ce era scris înainte acolo.
- Ce trebuie să întoarcă: nimic — efectul ei e că fișierul de pe
  calculator s-a schimbat.

💡 De reținut: fixează ACUM câmpurile pe care le are o aplicație,
pentru că le vei folosi peste tot mai departe: `companie`, `post`,
`data_aplicare`, `sursa`, `stare`, `data_ultimului_contact`, `notite`.

✅ Cum verifici că merge: apelezi `salveaza_aplicatii` cu o listă cu o
singură aplicație inventată de tine, apoi `incarca_aplicatii()`, și
verifici că primești înapoi exact aceleași date.

## PASUL 2 — Importul aplicațiilor dintr-un fișier CSV

**La acest pas trebuie să implementezi 3 funcții.**

Rolul lor, împreună: să transforme un fișier CSV (un tabel simplu, cu
virgulă între coloane) încărcat de utilizator, într-o listă de
aplicații gata de adăugat — fără să adaugi de două ori aceeași
aplicație.

### Funcția 1 — `normalizeaza_rand(rand_brut)`

def normalizeaza_rand(rand_brut):
    return {'companie': str(rand_brut['companie'].strip()),
            'post': str(rand_brut['post'].strip(),
            'data_aplicare': str(rand_brut['data_aplicare'].strip(),
            'sursa': str(rand_brut['sursa'].strip(),
            'stare': "Aplicat",
            'data_ultimului_contact': "data_aplicare",
            'notite':""
    }

**Rolul ei:** un rând citit dintr-un CSV vine incomplet (n-are stare,
n-are dată de ultim contact) — funcția asta completează ce lipsește.

- Primește: un singur rând, așa cum vine dintr-un CSV — un dicționar cu
  cheile `companie`, `post`, `data_aplicare`, `sursa`, toate ca text.
- Ce trebuie să faci, pas cu pas, în interior:
  1. păstrezi `companie`, `post`, `data_aplicare` și `sursa` așa cum
     vin din CSV;
  2. completezi `stare` cu valoarea implicită `"Aplicat"` — orice
     aplicație proaspăt importată e, evident, doar "aplicată";
  3. completezi `data_ultimului_contact` cu ACEEAȘI valoare ca
     `data_aplicare` — la momentul importului n-ai vorbit încă cu
     nimeni, deci "ultimul contact" e chiar momentul aplicării;
  4. completezi `notite` cu text gol `""`.
- Ce trebuie să întoarcă: un singur dicționar — aplicația completă, cu
  toate cele 7 câmpuri stabilite la Pasul 1.

### Funcția 2 — `citeste_csv_incarcat(fisier)`

def citeste_csv_incarcat(fisier):
    linii_text = fisier.read().decode("utf-8").splitlines()
    return [normalizeaza rand(r) for r in csv. DictReader(linii_text)]

**Rolul ei:** ia fișierul brut pe care utilizatorul l-a încărcat în
pagina web și îl transformă într-o listă de aplicații gata de folosit,
apelând `normalizeaza_rand` pentru fiecare rând.

- Primește: fișierul așa cum vine din pagina web (conține octeți, nu
  text simplu).
- Ce trebuie să faci, pas cu pas, în interior:
  1. citești conținutul fișierului și îl transformi din octeți în text;
  2. împarți acel text pe linii;
  3. citești liniile ca pe un tabel CSV;
  4. treci fiecare rând rezultat prin `normalizeaza_rand`.
- Ce trebuie să întoarcă: lista completă de aplicații, rezultate din
  tot fișierul.

### Funcția 3 — `adauga_aplicatii_noi(existente, importate)`

def adauga_aplicatii_noi(existente, importate):
    aplicatii_existente = {rand['companie', 'post'].lower() for rand in existente}
    de_adaugat = [rand for rand in importate if rand ['companie', 'post'].lower() not in aplicatii_existente]
    return aplicatii_existente+de_adaugat, len(de_adaugat))

**Rolul ei:** compară aplicațiile deja salvate cu cele importate din
CSV, și le adaugă doar pe cele care chiar sunt noi.

- Primește: lista de aplicații deja existente și lista de aplicații
  importate (deja trecute prin `normalizeaza_rand`).
- Ce trebuie să faci, pas cu pas, în interior:
  1. construiești o listă de PERECHI `(companie, post)`, aduse la
     litere mici, din aplicațiile existente — NU doar numele companiei;
  2. păstrezi din cele importate DOAR aplicațiile a căror pereche
     `(companie, post)`, adusă și ea la litere mici, nu se regăsește
     printre cele existente;
  3. numeri câte aplicații au trecut de acest filtru.
- Ce trebuie să întoarcă: DOUĂ valori — lista rezultată (cele vechi +
  doar cele chiar noi) și numărul de aplicații noi găsite.

💡 De reținut: aici cheia de unicitate NU e doar `companie`, ci
PERECHEA `(companie, post)` — poți aplica la mai multe posturi în
aceeași companie, iar acelea sunt aplicații DIFERITE, nu duplicate. Dacă
compari doar după companie, o să respingi din greșeală aplicații
valide.

✅ Cum verifici că merge: testează aceste trei funcții separat, pe
`demo_data/aplicatii_demo.csv`, citit direct cu `open()`, înainte să le
legi de Streamlit.

---

Cu aceste 5 funcții scrise și testate, ai toată logica aplicației gata.
De acum înainte doar construiești ecranul care le folosește.

---

## PASUL 3 — Ecranul de import CSV

st.set_page_config(page_title="Tracker aplicatii job")
st.title("Jurnalul meu de aplicatii")
aplicatii = incarca_aplicatii()
st.header("1. Import date CSV")
fisier_incarcat - st.file_uploader("Lista de aplicatii de adaugat, type="csv")
if fisier_incarcat is not None:
    importate = citeste_csv_incarcat(fisier_incarcat)
    aplicatii_previzualitate, cate_noi = adauga_aplicatii_noi(aplicatii, importate)
    st.caption(f"{cate_noi}aplicatii noi gasite")

if cate_noi > 0 and st.button("Adauga cele{cate_noi} aplicatii noi"):
    salveaza_aplicatii(aplicatii_previzualizate)
    st.succes(f"{cate_noi} aplicatii noi au fost adaugate!")
    st.rerun()

**La acest pas NU mai scrii funcții noi** — folosești
`citeste_csv_incarcat` și `adauga_aplicatii_noi` de la Pasul 2.

**Rolul acestui ecran:** utilizatorul încarcă un fișier CSV, vede câte
aplicații noi ar apărea, și abia dacă apasă un buton de confirmare se
salvează efectiv pe calculator.

Ce trebuie să faci, pas cu pas:
1. adaugi un loc unde utilizatorul poate încărca un fișier CSV;
2. când a fost încărcat un fișier, citești conținutul lui cu
   `citeste_csv_incarcat`;
3. calculezi, cu `adauga_aplicatii_noi`, cum ar arăta lista DACĂ ai
   confirma importul — dar NU salvezi încă nimic, doar afișezi câte
   aplicații noi ai găsi;
4. afișezi un buton cu numărul de aplicații noi în text (ex. "Adaugă
   cele 3 aplicații noi"), vizibil doar dacă există cel puțin una nouă;
5. la apăsarea butonului: salvezi efectiv lista calculată la pasul 3,
   afișezi o confirmare și reîmprospătezi pagina.

💡 De reținut: de ce în doi pași (mai întâi arăți, apoi confirmi) — dacă
ai salva automat la simpla încărcare a fișierului, un CSV greșit ți-ar
strica lista fără să apuci să te răzgândești.

## PASUL 4 — Tabelul filtrabil după stare

st.header("2. Trackerul meu")
if not aplicatii:
    st.info("Nu exista nicio aplicatie adaugata.")
else:
    col_toate = st.columns(1)
    
    with col_stari:
        stari_ales = st.selectbox("Filtreaza dupa stari", [Toate] + STARI)

    aplicatii_filtrare = [a for a in aplicatii if a['stari'] == a_ales]
    st.dataframe(titluri_filtrare)

**La acest pas NU mai scrii funcții noi.**

**Rolul acestui ecran:** utilizatorul vede toate aplicațiile, sau doar
pe cele dintr-o anumită etapă (o variantă simplă de "kanban" — alegi o
stare și vezi doar aplicațiile din acea etapă).

Ce trebuie să faci, pas cu pas:
1. dacă nu există încă nicio aplicație, afișezi un mesaj simplu care
   spune asta și te oprești aici;
2. altfel, adaugi o listă de alegere (dropdown) cu opțiunile
   `["Toate"] + STARI`;
3. dacă utilizatorul a ales "Toate", afișezi toată lista; altfel,
   păstrezi doar aplicațiile care au exact acea stare;
4. afișezi rezultatul într-un tabel.

## PASUL 5 — Adăugare aplicație nouă

with st.form("form_adaugare):
    companie_nou = st.text_input
    'companie': companie_nou,
    'post': post_nou,
    'stare': "Aplicat",
    'data_ultimului_contact': "data_aplicare",
    'notite':""

**La acest pas NU mai scrii funcții noi.**

**Rolul acestui ecran:** utilizatorul poate adăuga manual o aplicație
care nu vine dintr-un CSV.

Ce trebuie să faci, pas cu pas:
1. adaugi un formular cu patru câmpuri: companie, post, data aplicării
   (valoare implicită azi), sursă (ex. linkedin, site, recomandare);
2. la trimiterea formularului (doar dacă și compania, și postul sunt
   completate):
   1. construiești o aplicație nouă, cu `stare="Aplicat"` și
      `data_ultimului_contact` egală cu data aplicării alese în
      formular — la fel ca la import;
   2. o adaugi la lista completă de aplicații;
   3. salvezi lista completă pe calculator, apelând
      `salveaza_aplicatii`;
   4. afișezi o confirmare.

---

Odată terminați acești 5 pași (0-5), ai o aplicație completă: poți
importa aplicații dintr-un CSV, le poți vedea filtrate după stare, și
poți adăuga una nouă manual — toate rămân salvate pe calculator.

## PASUL 6 — Urcă proiectul pe Git

**Rolul acestui pas:** codul tău există momentan doar pe calculatorul
tău. Ca să fie salvat "oficial" într-un istoric de versiuni (și, mai
târziu, pus pe GitHub), trebuie trimis către Git din terminal.

Ce trebuie să faci, pas cu pas, din terminal, în folderul proiectului:
1. verifici ce fișiere s-au schimbat, cu `git status`;
2. adaugi toate fișierele schimbate în "lista de trimis", cu:
   ```
   git add .
   ```
3. le salvezi în istoric, cu un mesaj scurt care spune ce ai făcut:
   ```
   git commit -m "mesajul tau aici"
   ```
4. trimiți commit-ul către repository-ul de pe GitHub, cu:
   ```
   git push
   ```

💡 De reținut: pașii 2-3-4 se repetă de fiecare dată când vrei să
salvezi progresul — cel mai bine faci câte un commit după fiecare pas
terminat (0, 1, 2...), nu abia la final, cu tot codul odată.

## PASUL 7 — Cum rulezi aplicația

**Rolul acestui pas:** un fișier Streamlit nu se rulează ca un script
Python normal (cu `python numele_fisierului.py`) — are nevoie de
propria lui comandă ca să pornească pagina web.

Ce trebuie să faci, pas cu pas, din terminal:
1. dacă nu ai Streamlit instalat încă, îl instalezi o singură dată:
   ```
   pip install streamlit
   ```
2. te asiguri că ești, din terminal, în folderul
   `25.2.proiect_tracker_joburi` (acolo unde ai scris fișierul tău);
3. pornești aplicația cu:
   ```
   streamlit run numele_fisierului_tau.py
   ```
4. Streamlit îți deschide automat o pagină în browser (de obicei la
   `http://localhost:8501`) — dacă nu se deschide singură, dă click pe
   link-ul afișat în terminal.

💡 De reținut: cât timp lași comanda pornită în terminal, aplicația
rămâne activă. Ca s-o oprești, te întorci în terminal și apeși
`Ctrl+C`.

---