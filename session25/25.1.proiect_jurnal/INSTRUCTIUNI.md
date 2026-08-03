# PROIECT DE PORTOFOLIU — Jurnal de citit / vizionat

Acesta e un proiect de portofoliu: pornești de la zero, ca la un
proiect real. La final, el trebuie să existe ca **repository pe
GitHub**. Ce trebuie să facă aplicația găsești mai jos; cum o
construiești, pas cu pas, e în `PASI.md`.

---

## Despre ce e vorba

O aplicație personală în care ții evidența cărților și filmelor: ce ai
citit/văzut deja, ce vrei să citești/vezi — genul de aplicație pe care
mulți o construiesc pentru ei înșiși (o mini variantă personală de
Goodreads/Letterboxd).

## Ce trebuie să facă aplicația

1. **Import dintr-un CSV.** Primești o listă de titluri
   (`demo_data/carti_filme_demo.csv`, cu coloanele `titlu,tip,autor,an`)
   pe care le poți adăuga în biblioteca ta. Importul adaugă DOAR
   titlurile care nu există deja (verifici după `titlu`) — nu
   suprascrie ce ai deja în bibliotecă.

2. **Datele rămân salvate, într-un fișier JSON.** Fiecare titlu are:
   `titlu`, `tip` ("carte" sau "film"), `autor`, `an`, `stare` ("de
   citit" / "in curs" / "terminat"), `rating`, `data_terminarii` și
   `notite`. Datele trebuie să rămână acolo și după ce închizi și
   redeschizi aplicația.

3. **O pagină Streamlit cu:**
   - un tabel cu toate titlurile, filtrabil după `tip` și după `stare`;
   - un formular prin care adaugi manual un titlu nou (nu tot ce
     ajunge în bibliotecă trebuie să vină din CSV).

## Cerințe tehnice

- Folosești **doar** `csv`, `json`, `os` (module deja predate) — fără
  `pandas`.
- Fișierul JSON de pe calculator e mereu varianta corectă a datelor:
  la fiecare rerulare a scriptului Streamlit, îl recitești, nu ții
  datele doar în memorie.
- Scrii câte o funcție separată pentru fiecare bucată de logică
  (salvare/încărcare, import din CSV) — abia la final vine partea de
  interfață Streamlit, care doar le folosește.

## Date demo

`demo_data/carti_filme_demo.csv` — o listă de start cu 8 titluri
(cărți și filme amestecate), pe care le imporți la prima rulare, ca să
ai cu ce testa aplicația.

## Când e gata

- [ ] pot importa fișierul demo și văd titlurile în tabel
- [ ] pot adăuga manual un titlu nou
- [ ] pot filtra titlurile după tip și după stare
- [ ] datele rămân salvate după ce închid și redeschid aplicația
- [ ] proiectul e trimis pe Git (`git add`, `git commit`, `git push`)

---
