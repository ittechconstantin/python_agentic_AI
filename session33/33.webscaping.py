# SESIUNEA 30 - Web Scraping (requests + BeautifulSoup)
# =============================================================
# CE INVATAM AZI (recapitulare rapida la final de sesiune):
#   1. Ce e web scraping-ul si cand il folosim (fata de un API)
#   2. Etica si regulile jocului: robots.txt, rate limiting, ToS
#   3. HTML pe scurt - ce "vede" un scraper
#   4. BeautifulSoup: parsare, select_one/select, find/find_all
#   5. Cautare dupa STRUCTURA/CONTINUT cand nu ai clase CSS cunoscute
#   6. Regex pe textul deja extras - despicarea textelor "amestecate"
#   7. Paginare - cum "mergi" prin mai multe pagini
#   8. Robustete: headers, timeout, erori, respect fata de server
#   9. Aplicatie reala: aduni date structurate intr-o lista
#
# INSTALARE:  pip install beautifulsoup4 lxml
from xml import etree

# =============================================================

import requests
from bs4 import BeautifulSoup


# #############################################################
# PARTEA 0 - CE E WEB SCRAPING-UL? (teorie, fara cod)
# #############################################################
#
# La sesiunea trecuta, un API iti dadea date DEJA structurate (JSON),
# gata de folosit. Dar nu orice site are un API. Web scraping-ul
# inseamna sa iei date direct din PAGINA WEB (HTML-ul pe care il vede
# si un om in browser) si sa le extragi TU, cu cod.
#
# Analogie: API-ul e ca un chelner care iti aduce farfuria gata
# aranjata. Scraping-ul e ca si cum ai intra in restaurant, te-ai uita
# pe fiecare masa si ai nota singur ce mananca fiecare - informatia e
# acolo, vizibila, dar TU esti cel care o citeste si o organizeaza.
#
# CAND folosim scraping (si nu API):
#   - site-ul nu ofera un API public
#   - vrei date care apar doar in pagina (ex: preturi afisate, articole)
#
# REGULA DE AUR - ETICA SI LEGALITATE:
#   - citeste robots.txt (ex: https://playtech.ro/robots.txt) - iti
#     spune ce parti ale site-ului NU vrei sa le automatizezi
#   - citeste Termenii si Conditiile site-ului (Terms of Service) -
#     unele site-uri interzic explicit scraping-ul
#   - NU lua date personale/sensibile fara motiv legitim
#   - NU bombarda serverul cu cereri (rate limiting - vezi Partea 3) -
#     poti sa-l incetinesti sau chiar sa-l pici pentru ceilalti useri
#   - foloseste datele responsabil (nu revinde/republica ce nu ai voie)
#
#
# CUM CITESTI UN robots.txt, DE FAPT
# --------------------------------------------------------------
# robots.txt e un fisier text simplu, la radacina site-ului (ex:
# https://playtech.ro/robots.txt), cu reguli grupate pe "User-agent"
# (cine sunt regulile astea) urmate de "Disallow" (ce NU are voie) si,
# uneori, "Allow" (exceptii de la un Disallow).
#
# Iata robots.txt-ul REAL, complet, de la playtech.ro (verificat direct):
#
#   User-agent: *
#   Disallow: /stiri/
#   Disallow: /tag/
#   Disallow: /wp-admin/
#   Disallow: /wp-content/plugins/
#   Disallow: /trackback/
#   Disallow: /xmlrpc.php
#   Disallow: /wp-json/
#   Allow: /wp-content/uploads/
#   Allow: /wp-admin/admin-ajax.php
#
#   Sitemap: https://playtech.ro/sitemaps/sitemap-news.xml
#   ...
#
# Cum se CITESTE asta:
#   - "User-agent: *" e grupul care se aplica ORICUI nu e mentionat
#     explicit (nu exista alte grupuri in acest fisier) - deci si
#     scriptului tau, cu User-Agent-ul lui propriu.
#   - Site-ul NU are voie sa fie accesat automatizat pe /stiri/, /tag/,
#     /wp-admin/ etc. Restul e permis implicit (tot ce NU apare la
#     Disallow e liber).
#
# ACUM, ATENTIE la o capcana REALA: fisierul de fata foloseste URL-ul
#   https://playtech.ro/stiri-it/tehnologie/
# Seamana cu "/stiri/", care e interzis - dar NU e acelasi lucru!
# "Disallow: /stiri/" blocheaza doar caile care incep EXACT cu acele
# caractere, urmate de "/": adica /stiri/altceva. Calea noastra e
# "/stiri-it/..." - dupa "stiri" urmeaza o CRATIMA, nu un "/", deci
# NU se potriveste cu regula "/stiri/" si ramane PERMISA.
#   /stiri/politica/      -> INTERZIS  (incepe exact cu "/stiri/")
#   /stiri-it/tehnologie/ -> PERMIS    (e o cale diferita, doar seamana)
# La fel, /author/... (linkurile catre autori) si /2026/titlu-articol/
# (paginile de articole) NU apar in nicio regula Disallow - sunt
# permise. Exact URL-urile pe care le folosim in exemplele de mai jos.
#
# Asta e o lectie importanta: NU citi robots.txt "in fuga", dupa cum
# "suna" o cale - verifica litera cu litera daca REALMENTE se
# potriveste cu un Disallow, mai ales cand doua cai seamana.
#
#
#
# ATENTIE: robots.txt e o CONVENTIE, nu o lege - nimic tehnic nu te
# opreste sa ignori regulile. Dar tocmai de-aia conteaza sa le respecti
# de bunavoie: e diferenta dintre un scraper responsabil si unul care
# ajunge sa fie blocat (sau reclamat) pentru ca a ignorat semnalele
# clare pe care site-ul le-a pus la dispozitie.


# #############################################################
# PARTEA 1 - HTML PE SCURT + PRIMUL SCRAPE
# #############################################################


# 1. HTML, in doua propozitii
# -------------------------------------------------------------
# HTML e un text cu "etichete" (tag-uri) care descriu structura unei
# pagini: <div>, <p>, <a>, <h1>, <span>... Fiecare tag poate avea
# ATRIBUTE (class="...", href="...", id="...") care il descriu mai
# exact. Un scraper citeste acest text si "navigheaza" prin el.
#
# Un articol de pe playtech.ro arata, simplificat, cam asa:
#   <article>
#     <h2><a href="/2026/titlu-articol/">Titlul articolului</a></h2>
#     <a href="/author/iuliakelt/">Iulia Kelt</a> 27 aug. 2026
#   </article>
#
# Observa: NU stim exact ce clase CSS foloseste playtech.ro (spre
# deosebire de un site "de exersat", care iti da clase clare gen
# ".quote"). Asta e situatia FOARTE des intalnita in scraping real -
# si exact pe asta exersam azi: cum cauti dupa STRUCTURA (ce tag e,
# ce href are) cand nu ai o clasa clara de agatat.


# 2. Aducem pagina HTML  -  la fel ca la API, dar primim HTML in loc de JSON
# -------------------------------------------------------------

URL_TEHNOLOGIE = "https://playtech.ro/stiri-it/tehnologie/"
HEADERE = {"User-Agent": "curs-python/1.0"}

r = requests.get(URL_TEHNOLOGIE, headers=HEADERE, timeout=10)
r.raise_for_status()
print(r.status_code)   # 200
print(r.text[:30])     # <!Doc....


# r.text e tot un STRING, la fel ca la API - dar acum e HTML, nu JSON.
# Nu-l putem parcurge cu .json(); avem nevoie de un PARSER de HTML.
#
# r.raise_for_status()
# -------------------------------------------------------------
# requests NU arunca automat o eroare doar pentru ca serverul a
# raspuns cu un cod "de eroare" (404 = pagina nu exista, 403 = acces
# interzis, 500 = eroare pe server etc.) - fara raise_for_status(),
# codul TAU continua sa ruleze normal, cu un r.text care poate fi o
# pagina de eroare in loc de continutul pe care il astepti, si abia
# mai tarziu, cand incerci sa parsezi "eroarea" ca si cum ar fi
# continut valid, iei o eroare ciudata si greu de inteles.
#
# r.raise_for_status() verifica status_code-ul: daca e 200 (sau alt
# cod de succes, 2xx), nu face nimic si codul continua normal. Daca
# e un cod de eroare (4xx sau 5xx), OPRESTE programul pe loc cu o
# exceptie clara (requests.exceptions.HTTPError), care iti spune
# exact ce cod ai primit - mult mai usor de depanat decat sa te
# lovesti mai tarziu de un AttributeError fara legatura aparenta.
#
# De-aia il punem imediat dupa fiecare requests.get(...) din cursul
# asta: e felul in care "esuezi rapid si clar", in loc sa lucrezi cu
# date proaste fara sa-ti dai seama.


# 3. BeautifulSoup - transforma textul HTML intr-un obiect navigabil
# -------------------------------------------------------------
# PROBLEMA: text-ul HTML brut e greu de "cautat" cu mana.
# SOLUTIA:  BeautifulSoup parseaza HTML-ul si iti da un obiect prin
#           care poti cauta tag-uri dupa nume, clasa, atribute etc.

soup = BeautifulSoup(r.text, 'lxml')
print(type(soup))       # <class 'bs4.BeautifulSoup'>
print(soup.title.text)

# #############################################################
# PARTEA 2 - CAUTARE SI EXTRAGERE DE DATE
# #############################################################


# 4. select_one / select  -  cautare cu selectori CSS (cand STII clasa)
# -------------------------------------------------------------
# Selectorii CSS sunt acelasi "limbaj" pe care il folosesti si in
# fisiere .css:
#   "div"          -> toate tag-urile <div>
#   ".clasa"       -> toate elementele cu class="clasa"
#   "div.clasa"    -> <div> care au si class="clasa"
#   "h2 a"         -> toate <a> care sunt IN INTERIORUL unui <h2>
#
#   select_one(...)  -> primul element gasit (sau None daca nu exista)
#   select(...)       -> LISTA cu toate elementele gasite
#
# Pe playtech.ro STIM ceva sigur despre structura, chiar fara sa
# stim clasele: titlul fiecarui articol e intr-un <h2>, cu un <a>
# in interior. Deci "h2 a" e un selector CSS pe care ne putem baza:

titluri = soup.select("h2 a")
print(f"Cate titluri sunt in pagina? Sunt:{len(titluri)}")
for index, titlu in enumerate(titluri, 1):
    print(f"{index}. {titlu.text.strip()}")

# 5. .text vs .get("atribut")  -  ce extragi dintr-un element
# -------------------------------------------------------------
#   element.text            -> textul VIZIBIL dintre tag-uri
#   element.get("href")     -> valoarea unui ATRIBUT (link, sursa img...)
#   element.get("class")    -> ATENTIE: class intoarce o LISTA, nu string
#                               (un element poate avea mai multe clase)

if titluri:
    primul = titluri[0]
    print("text", primul.text.strip())         # titlu articol
    print("link", primul.get("href"))          # linkul articol


# 6. find / find_all  -  varianta "clasica", utila si ea
# -------------------------------------------------------------
# Fac cam acelasi lucru ca select_one/select, dar cu sintaxa diferita:
#   find("h2")            <->  select_one("h2")
#   find_all("h2")        <->  select("h2")
#
# ATENTIE: "class" e cuvant rezervat in Python, de-aia parametrul se
# numeste class_ (cu underscore) la find/find_all, cand ai nevoie de el.

primul_h2 = soup.find("h2")
print(primul_h2)
if primul_h2 is not None:
    print("Gasit")

# 7. Cautare dupa CONTINUT, nu dupa clasa - find_all cu href=True
# -------------------------------------------------------------
# Pe langa titluri, vrem si linkurile catre AUTORI. Nu avem o clasa
# pentru ele - dar STIM ca toate arata catre "/author/...". In loc sa
# cautam o clasa, filtram TOATE linkurile de pe pagina dupa href:

linkuri_author = soup.find_all("a", href=lambda h: h and '/author/' in h)

print(f"cati autori am gasit pe pagina {len(linkuri_author)}")
for link in linkuri_author:
    print(link.text.strip())


# "href=lambda h: h and '/author/' in h" inseamna: "ia doar <a>-urile
# al caror href CONTINE '/author/'". E aceeasi idee ca la href=True
# (ia doar linkurile care AU href), dar cu o conditie mai stricta.



# 8. Regex PE TEXTUL DEJA EXTRAS - pentru date "amestecate" cu alt text
# -------------------------------------------------------------
# ATENTIE la o confuzie frecventa: regula "nu parsa HTML cu regex,
# foloseste un parser dedicat" (o gasesti si la GRESELI FRECVENTE, mai
# jos) se refera la a cauta TAG-uri direct in HTML brut - aia chiar e
# o capcana. CU TOTUL ALTCEVA e sa folosesti regex pe TEXTUL PE CARE
# L-AI SCOS DEJA cu BeautifulSoup - tehnica normala, des folosita.
#
# Exemplu, pe playtech.ro: langa numele autorului sta lipita data
# articolului ("27 aug. 2026"), fara tag separat intre ele. Pornim
# chiar de la HTML-ul brut, ca sa vezi tot drumul, pas cu pas:

html_exemplu = '''
<div>
  <a href="/author/iuliakelt/">Iulia Kelt</a>
  27 aug. 2026
</div>
'''

soup_exemplu = BeautifulSoup(html_exemplu, "lxml")
container = soup_exemplu.find("div")
text_container = container.get_text(" ", strip=True)
print(repr(text_container))   # 'Iulia Kelt 27 aug. 2026'

# Vezi: BeautifulSoup ne-a dat UN SINGUR string, in care numele
# autorului si data sunt amestecate - nu exista niciun tag separat
# pentru data, deci nu-l putem prinde cu .select(). Aici intra regex:

import re

TIPAR_DATA = re.compile(r"\d{1,2}\s+[a-zăâîșț]+\.?\s+\d{4}")
potrivire = TIPAR_DATA.search(text_container)
# print(potrivire.group(0) if potrivire is not None else None)   # "27 aug. 2026"

# \d{1,2}=ziua | \s+=spatii | [a-zăâîșț]+=luna | \.?=punct optional | \s+\d{4}=anul
# .search() cauta tiparul ORIUNDE in text; intoarce None daca nu gaseste
# nimic - de-aia verificam mereu "is not None" inainte sa citim .group(...).


# 9bis. GRUPURI DE CAPTURARE - cand vrei mai multe bucati deodata
# -------------------------------------------------------------
# Mai sus am extras UN singur lucru (data), cu .group(0) - "tot ce
# s-a potrivit". Dar la alte site-uri (ex: biziday.ro) ai nevoie sa
# desparti simultan MAI MULTE bucati din acelasi text: sursa, data SI
# ora. Din nou, pornim de la HTML, ca sa vezi exact de unde vine
# problema "amestecarii":

html_stire = (
    '<a href="/367123-2/">UEFA va depune plângere penală împotriva lui Gianni Infantino. '
    '<span>Biziday</span> &middot; 2026-08-25 @ 18:27:23</a>'
)
soup_stire = BeautifulSoup(html_stire, "lxml")
link_stire = soup_stire.find("a")
text_stire = link_stire.text
print(repr(text_stire))
# UEFA va depune plângere penală împotriva lui Gianni Infantino.  · 2026-08-25 @ 18:27:23'
#
# Observa: textul stirii ("UEFA va depune") si numele sursei ("Biziday") sunt
# LIPITE, fara spatiu - pentru ca in HTML erau doua tag-uri diferite
# (textul liber + un <span>), iar .text le-a unit fara sa adauge
# vreun separator. Exact genul de "amestec" pentru care ai nevoie de
# regex CU MAI MULTE GRUPURI deodata.
#
# Aici intra PARANTEZELE: fiecare bucata din tipar pusa intre () devine
# un "grup" separat, pe care il citesti cu .group(1), .group(2), .group(3)...

TIPAR_METADATA = re.compile(
    r"([A-ZĂÂÎȘȚ][\wăâîșțĂÂÎȘȚ]*)\s*·\s*(\d{4}-\d{2}-\d{2})\s*@\s*(\d{2}:\d{2}:\d{2})\s*$"
)
potrivire = TIPAR_METADATA.search(text_stire)
print(potrivire)

if potrivire is not None:
    sursa = potrivire.group(1)      # "Biziday"     - continutul primei ()
    data = potrivire.group(2)       # "2026-08-25"  - continutul celei de-a doua ()
    ora = potrivire.group(3)        # "18:27:23"    - continutul celei de-a treia ()
    continut = text_stire[:potrivire.start()].strip()   # tot ce e INAINTE de potrivire
    print(continut, "|", sursa, "|", data, "|", ora)

# CE INSEAMNA MAI EXACT .group(1), .group(2), .group(3):
# ---------------------------------------------------------
# Regex-ul de mai sus are TREI perechi de paranteze - deci gaseste
# TREI grupuri, numerotate de la STANGA la DREAPTA, in ordinea in
# care apar parantezele in tipar (nu in ordinea in care le citesti tu
# in cod):
#
#   ([A-ZĂÂÎȘȚ][\wăâîșțĂÂÎȘȚ]*)   <- grupul 1: un cuvant cu majuscula la
#                                     inceput (litere/cifre dupa) = "Biziday"
#   (\d{4}-\d{2}-\d{2})           <- grupul 2: o data AAAA-LL-ZZ = "2026-08-25"
#   (\d{2}:\d{2}:\d{2})           <- grupul 3: o ora HH:MM:SS    = "18:27:23"
#
# .group(1) = ce s-a potrivit STRICT in interiorul primei paranteze
# .group(2) = ce s-a potrivit STRICT in interiorul celei de-a doua
# .group(3) = ce s-a potrivit STRICT in interiorul celei de-a treia
# .group(0) (sau doar .group(), fara numar) = TOT ce s-a potrivit,
#           de la inceput la sfarsit, INCLUSIV bucatile dintre
#           paranteze ("·", "@", spatiile) - practic tot "Biziday ·
#           2026-08-25 @ 18:27:23" dintr-o bucata.
#
# Gandeste-te la paranteze ca la niste "buzunare" - regex-ul cauta
# tot tiparul deodata, dar iti pastreaza SEPARAT ce a cazut in
# fiecare buzunar, ca sa poti sa le folosesti individual dupa aceea.
#
# "$" la finalul tiparului ANCOREAZA cautarea la finalul textului -
# fara el, ai risca o potrivire gasita din greseala in mijlocul unui
# text mai lung. Il folosesti cand stii ca ce cauti e mereu ULTIMA
# bucata dintr-un text (exact cazul de mai sus: sursa+data+ora sunt
# mereu la coada textului unei stiri, niciodata la mijloc).


# #############################################################
# PARTEA 3 - PAGINARE, ROBUSTETE SI RESPECT FATA DE SERVER
# #############################################################


# 10. Paginare PRIN TIPAR DE URL - o alta metoda decat "urmareste Next"
# -------------------------------------------------------------
# La unele site-uri (ca la citatele de pe toscrape.com) urmaresti un
# buton "Next" pagina cu pagina. La playtech.ro e mai simplu: fiecare
# pagina are un URL PREVIZIBIL:
#   https://playtech.ro/stiri-it/tehnologie/          -> pagina 1
#   https://playtech.ro/stiri-it/tehnologie/page/2/   -> pagina 2
#   https://playtech.ro/stiri-it/tehnologie/page/3/   -> pagina 3
# Deci putem GENERA noi insine URL-urile, in loc sa cautam un link.

import time

BAZA = "https://playtech.ro/stiri-it/tehnologie/"
toate_stirile = []


for numar_pagina in range(1, 3 + 1):  # primele 3 pagini

    if numar_pagina == 1:
        url_pagina = BAZA
    else:
        url_pagina = f"{BAZA}page/{numar_pagina}/"

    r = requests.get(url_pagina, headers=HEADERE, timeout=10)
    r.raise_for_status()
    soup_pagina = BeautifulSoup(r.text, 'lxml')

    for h2 in soup_pagina.select("h2"):
        link = h2.select_one('a')
        if link is not None:
            toate_stirile.append(link)

    time.sleep(1)  # Politete-> ca sa nu bombardam serverul cu multe cereri

    print(f"Cate articole sunt: {len(toate_stirile)}")


# La fel ca la API (raise_for_status, timeout), scraping-ul are nevoie
# de robustete: pagina se poate schimba, serverul poate fi lent sau
# poate raspunde cu eroare - trateaza mereu cazul "nu am gasit nimic".


# =============================================================
# RECAP / GRESELI FRECVENTE
# =============================================================
# SCRAPING DE BAZA:
#   soup = BeautifulSoup(r.text, "lxml")
#   soup.select("h2 a")                -> toate elementele care se potrivesc
#   soup.find_all("a", href=lambda h: h and "/ceva/" in h)  -> filtrare dupa href
#   element.text                       -> textul vizibil
#   element.get("href")                -> valoarea unui atribut
#
# GRESELI FRECVENTE (in ordinea in care le fac cei mai multi incepatori):
#   1. Nu verifici robots.txt / ToS inainte sa faci scraping pe un
#      site real -> poate fi interzis. Cand nu esti sigur, verifica
#      manual, tu insuti, in browser - nu presupune.
#   2. select_one()/find() intorc None si apelezi .text pe ele direct ->
#      AttributeError. Verifica INTAI cu `if element is not None`.
#   3. Faci sute de cereri fara nicio pauza -> risti sa fii blocat sau
#      sa ingreunezi serverul pentru altii. Foloseste time.sleep(...).
#   4. Confunzi .text (textul vizibil) cu .get("atribut") (o valoare
#      dintr-un atribut precum href/src/title).
#   5. Uiti ca .get("class") intoarce o LISTA (un element poate avea
#      mai multe clase deodata), nu un singur string.
#   6. Parsezi HTML BRUT cu regex in loc de BeautifulSoup (adica incerci
#      sa gasesti TAG-uri si atribute direct in text, cu regex) -> HTML-ul
#      e prea neregulat pentru asta; foloseste mereu un parser dedicat
#      pentru STRUCTURA paginii. Regex-ul ramane insa o unealta buna
#      pentru a despica TEXTUL pe care BeautifulSoup l-a extras deja
#      (vezi Partea 2, sectiunea 9) - astea sunt doua lucruri diferite,
#      nu te incurca.
#   7. Nu pui headers={"User-Agent": ...} -> unele site-uri refuza
#      cereri fara un User-Agent "de om".
#   8. Presupui ca site-ul are o clasa CSS clara pentru tot -> multe
#      site-uri reale NU au (vezi Partea 2, sectiunile 7-8): cauti
#      atunci dupa structura (tag, tipar de href) si "urci" prin
#      parinti cand trebuie sa legi elemente care nu sunt vecine.
#
# In sesiunea urmatoare: mai multe despre exportul datelor (CSV/Excel)
# si, optional, Selenium pentru pagini care incarca continut cu
# JavaScript (unde BeautifulSoup, singur, nu vede nimic).
# =============================================================