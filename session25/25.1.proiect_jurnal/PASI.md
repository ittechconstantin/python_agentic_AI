# GHID PAS CU PAS — Jurnal de citit / vizionat

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
le vor folosi toate funcțiile și tot ecranul de mai jos, ca să nu le
rescriem de fiecare dată separat.

Ce trebuie să faci, pas cu pas:
1. imporți modulele de care are nevoie aplicația: `csv`, `os`, `json`,
   `streamlit` și `date` din `datetime`;
2. stabilești numele folderului unde vor sta fișierele aplicației (ex.
   `demo_data`) și te asiguri că folderul chiar există pe calculator —
   dacă nu există, îl creezi;
3. stabilești drumul complet către fișierul în care vei salva
   biblioteca (folderul de mai sus + numele fișierului, ex.
   `biblioteca.json`) — îl ții într-o variabilă, ca să nu repeți acest
   drum peste tot în cod;
4. stabilești, tot ca variabile, cele două liste de valori fixe pe
   care le va folosi restul aplicației:
   - lista stărilor posibile pentru un titlu: `de citit`, `in curs`,
     `terminat`;
   - lista tipurilor posibile: `carte`, `film`.

💡 De reținut: aceste variabile (drumul către fișier, lista stărilor,
lista tipurilor) le vei folosi în aproape fiecare funcție și în
aproape fiecare ecran de mai jos — de-asta le scrii o singură dată,
chiar la începutul fișierului, nu în interiorul fiecărei funcții.

## PASUL 1 — Salvarea și încărcarea listei de titluri

**La acest pas trebuie să implementezi 2 funcții.**

Rolul lor, împreună: să facă posibil ca titlurile pe care le adaugi să
nu dispară atunci când închizi aplicația — sunt singurele două locuri
din tot codul unde vorbim cu fișierul de pe calculator.

### Funcția 1 — `incarca_titluri()`

**Rolul ei:** aduce înapoi, din fișierul salvat pe calculator, lista de
titluri pe care ai adăugat-o data trecută. Fără ea, aplicația ar porni
mereu de la zero, de parcă n-ai fi salvat niciodată nimic.

- Nu primește niciun parametru.
- Ce trebuie să faci, pas cu pas, în interior:
  1. verifici dacă fișierul cu titluri există deja pe calculator;
  2. dacă NU există (e prima dată când pornești aplicația) — nu faci
     nimic altceva, sari direct la ce trebuie să întorci;
  3. dacă există — îl deschizi și citești ce e scris în el, ca JSON.
- Ce trebuie să întoarcă:
  - o listă goală `[]`, dacă fișierul nu există;
  - lista de titluri citită din fișier, dacă există.

### Funcția 2 — `salveaza_titluri(titluri)`

**Rolul ei:** pune pe calculator orice schimbare faci în aplicație
(titlu nou, stare schimbată etc.) — altfel schimbarea s-ar pierde
imediat ce închizi pagina.

- Primește: lista completă de titluri, așa cum arată ea chiar acum (cu
  tot cu ce s-a schimbat).
- Ce trebuie să faci, pas cu pas, în interior:
  1. deschizi fișierul de pe calculator în mod scriere;
  2. scrii în el toată lista primită ca parametru, ca JSON — înlocuind
     complet ce era scris înainte acolo (nu adaugi la ce era deja
     salvat, rescrii tot fișierul).
- Ce trebuie să întoarcă: nimic — efectul ei e că fișierul de pe
  calculator s-a schimbat.

💡 De reținut: fixează ACUM câmpurile pe care le are un titlu, pentru
că le vei folosi peste tot mai departe: `titlu`, `tip`, `autor`, `an`,
`stare`, `rating`, `data_terminarii`, `notite`.

✅ Cum verifici că merge: înainte să te apuci de Streamlit, scrie un mic
test separat — apelezi `salveaza_titluri` cu o listă cu un singur titlu
inventat de tine, apoi apelezi `incarca_titluri()` și verifici că
primești înapoi exact aceleași date.

## PASUL 2 — Importul titlurilor dintr-un fișier CSV

**La acest pas trebuie să implementezi 3 funcții.**

Rolul lor, împreună: să transforme un fișier CSV (un tabel simplu, cu
virgulă între coloane) încărcat de utilizator, într-o listă de titluri
gata de adăugat în bibliotecă — fără să adaugi de două ori același
titlu.

### Funcția 1 — `normalizeaza_rand(rand_brut)`

**Rolul ei:** un rând citit dintr-un CSV vine incomplet (n-are stare,
rating, notițe) și cu toate valorile scrise ca text, chiar și anul.
Funcția asta completează ce lipsește și transformă anul din text în
număr, ca titlul rezultat să arate exact ca oricare alt titlu din
aplicație.

- Primește: un singur rând, așa cum vine dintr-un CSV — un dicționar cu
  cheile `titlu`, `tip`, `autor`, `an`, unde toate valorile sunt text.
- Ce trebuie să faci, pas cu pas, în interior:
  1. transformi valoarea de la `an` din text în număr;
  2. completezi câmpurile care nu apar deloc în CSV, cu valorile
     implicite: `stare="de citit"`, `rating=None`,
     `data_terminarii=None`, `notite=""` — pentru că un titlu proaspăt
     importat nu a fost încă citit sau vizionat de tine.
- Ce trebuie să întoarcă: un singur titlu complet (dicționar), cu toate
  cele 8 câmpuri stabilite la Pasul 1.

### Funcția 2 — `citeste_csv_incarcat(fisier)`

**Rolul ei:** ia fișierul brut pe care utilizatorul l-a încărcat în
pagina web și îl transformă într-o listă de titluri gata de folosit,
apelând `normalizeaza_rand` pentru fiecare rând din el.

- Primește: fișierul așa cum vine din pagina web (conține octeți, nu
  text simplu, pentru că așa livrează Streamlit fișierele încărcate).
- Ce trebuie să faci, pas cu pas, în interior:
  1. citești conținutul fișierului și îl transformi din octeți în text;
  2. împarți acel text pe linii;
  3. citești liniile ca pe un tabel CSV;
  4. treci fiecare rând rezultat prin `normalizeaza_rand`.
- Ce trebuie să întoarcă: lista completă de titluri, rezultate din tot
  fișierul.

### Funcția 3 — `adauga_titluri_noi(existente, importate)`

**Rolul ei:** compară titlurile deja din biblioteca ta cu cele
importate din CSV, și le adaugă doar pe cele care chiar sunt noi — ca
să nu ajungi cu același titlu de două ori în bibliotecă.

- Primește: lista de titluri deja existente în bibliotecă și lista de
  titluri importate (deja trecute prin `normalizeaza_rand`).
- Ce trebuie să faci, pas cu pas, în interior:
  1. aduci titlurile existente la litere mici, ca să poți compara fără
     să conteze majusculele ("Dune" și "dune" trebuie tratate ca fiind
     ACELAȘI titlu);
  2. păstrezi din cele importate DOAR titlurile al căror nume, adus și
     el la litere mici, nu se regăsește printre cele existente;
  3. numeri câte titluri au trecut de acest filtru.
- Ce trebuie să întoarcă: DOUĂ valori — lista rezultată (titlurile
  vechi + doar cele chiar noi) și numărul de titluri noi găsite.

💡 De reținut: dacă nu aduci ambele părți la același caz (litere mici)
înainte să le compari, o să accepți duplicate din greșeală, doar pentru
că sunt scrise diferit.

✅ Cum verifici că merge: testează aceste trei funcții separat, pe
`demo_data/carti_filme_demo.csv`, citit direct cu `open()` în loc de
încărcare din pagina web, înainte să le legi de Streamlit.

---

Cu aceste 5 funcții scrise și testate, ai toată logica aplicației gata
— fără nicio legătură încă cu pagina web. De acum înainte doar
construiești ecranul care le folosește.

---

## PASUL 3 — Ecranul de import CSV (secțiunea "1. Import date CSV" din cod)

**La acest pas NU mai scrii funcții noi** — folosești
`citeste_csv_incarcat` și `adauga_titluri_noi` de la Pasul 2, direct în
cod, ca să construiești un buton de încărcare și un mesaj.

**Rolul acestui ecran:** utilizatorul încarcă un fișier CSV, vede câte
titluri noi ar apărea, și abia dacă apasă un buton de confirmare se
salvează efectiv pe calculator.

Ce trebuie să faci, pas cu pas:
1. adaugi un loc unde utilizatorul poate încărca un fișier CSV;
2. când a fost încărcat un fișier, citești conținutul lui cu
   `citeste_csv_incarcat`;
3. calculezi, cu `adauga_titluri_noi`, cum ar arăta biblioteca DACĂ ai
   confirma importul — dar NU salvezi încă nimic, doar afișezi câte
   titluri noi ai găsi;
4. afișezi un buton cu numărul de titluri noi în text (ex. "Adaugă
   cele 3 titluri noi"), vizibil doar dacă există cel puțin un titlu
   nou de adăugat;
5. la apăsarea butonului: salvezi efectiv lista calculată la pasul 3,
   afișezi o confirmare și reîmprospătezi pagina.

💡 De reținut: de ce în doi pași (mai întâi arăți, apoi confirmi) — dacă
ai salva automat la simpla încărcare a fișierului, un CSV greșit ți-ar
strica biblioteca fără să apuci să te răzgândești.

## PASUL 4 — Catalogul cu titluri, filtrabil (secțiunea "2. Biblioteca mea" din cod)

**La acest pas NU mai scrii funcții noi.**

**Rolul acestui ecran:** utilizatorul vede toate titlurile din
bibliotecă și le poate filtra după tip și după stare, ca să găsească
rapid ce caută.

Ce trebuie să faci, pas cu pas:
1. dacă nu există încă niciun titlu în bibliotecă, afișezi un mesaj
   simplu care spune asta și te oprești aici, fără restul pașilor;
2. altfel, adaugi două liste de alegere (meniuri de tip dropdown): una
   cu tipurile posibile (carte/film), alta cu stările posibile (de
   citit / în curs / terminat);
3. din lista completă de titluri, păstrezi doar pe cele care se
   potrivesc CU AMBELE alegeri făcute de utilizator în același timp
   (tip ȘI stare, nu tip SAU stare);
4. afișezi rezultatul într-un tabel.

## PASUL 5 — Formularul de adăugare a unui titlu nou (secțiunea "3. Adaugă o carte nouă" din cod)

**La acest pas NU mai scrii funcții noi.**

**Rolul acestui ecran:** utilizatorul poate adăuga manual un titlu care
nu vine dintr-un CSV — nu tot ce ajunge în bibliotecă trebuie să fie
importat.

Ce trebuie să faci, pas cu pas:
1. adaugi un formular cu patru câmpuri, în ordinea asta: titlu, tip,
   autor, an;
2. la trimiterea formularului (doar dacă titlul introdus nu e gol):
   1. construiești un titlu nou, cu aceleași valori implicite ca la
      import (`stare="de citit"`, `rating=None`,
      `data_terminarii=None`, `notite=""`);
   2. îl adaugi la lista completă de titluri;
   3. salvezi lista completă pe calculator, apelând
      `salveaza_titluri`;
   4. afișezi o confirmare că titlul a fost adăugat.

💡 De reținut: spre deosebire de Pasul 3 (import), aici NU mai
reîmprospătezi pagina după salvare — titlul nou apare oricum în tabelul
de mai sus la următoarea interacțiune a utilizatorului cu pagina.

---

Odată terminați acești 5 pași (0-5), ai o aplicație completă: poți
importa titluri dintr-un CSV, le poți vedea filtrate după tip și stare,
și poți adăuga manual titluri noi — toate rămân salvate pe calculator,
chiar și după ce închizi și redeschizi aplicația.

## PASUL 6 — Urcă proiectul pe Git

**Rolul acestui pas:** codul tău există momentan doar pe calculatorul
tău. Ca să fie salvat "oficial" într-un istoric de versiuni (și, mai
târziu, pus pe GitHub), trebuie trimis către Git din terminal.

Ce trebuie să faci, pas cu pas, din terminal, în folderul proiectului:
1. verifici ce fișiere s-au schimbat, cu `git status` — ca să știi
   exact ce urmează să trimiți;
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

**Rolul acestui pas:** `solutie.py` nu se rulează ca un script Python
normal (cu `python solutie.py`) — e o aplicație Streamlit, și are
nevoie de propria ei comandă ca să pornească pagina web.

Ce trebuie să faci, pas cu pas, din terminal:
1. dacă nu ai Streamlit instalat încă, îl instalezi o singură dată:
   ```
   pip install streamlit
   ```
2. te asiguri că ești, din terminal, în folderul `25.1.proiect_jurnal`
   (acolo unde e fișierul `solutie.py`);
3. pornești aplicația cu:
   ```
   streamlit run solutie.py
   ```
4. Streamlit îți deschide automat o pagină în browser (de obicei la
   `http://localhost:8501`) — dacă nu se deschide singură, dă click pe
   link-ul afișat în terminal.

💡 De reținut: cât timp lași comanda pornită în terminal, aplicația
rămâne activă. Ca s-o oprești, te întorci în terminal și apeși
`Ctrl+C`.

💡 De reținut: de fiecare dată când salvezi o modificare în
`solutie.py`, Streamlit îți arată în pagina web un buton "Rerun" (sau
reîncarci singur pagina din browser) — nu trebuie să oprești și să
repornești comanda din terminal la fiecare schimbare de cod.
