# SESIUNEA 32 - API-uri + consumare cu requests
# =============================================================
# CE INVATAM AZI (recapitulare rapida la final de sesiune):
#   1. Ce e un API si de ce avem nevoie de el
#   2. Cum arata un schimb HTTP (cerere / raspuns, status codes)
#   3. GET - citim date (cu parametri si headers)
#   4. .json() - din text in obiect Python
#   5. POST / PUT / DELETE - scriem / modificam / stergem date
#   6. Robustete: timeout, status_code, raise_for_status, exceptii
#   7. Aplicatii reale: rapoarte si agregari peste date luate din API
#
# CE TREBUIE SA STII DEJA (prerechizite):
#   - dicturi si liste (accesare, iterare, .get())
#   - functii, try/except
#   - JSON (sesiunea 24): un dict/lista serializat ca text
#
# INSTALARE:  pip install requests
#
# API-uri PUBLICE, FARA CHEIE, folosite in exemple:
#   - https://jsonplaceholder.typicode.com  (fake REST API, date fixe,
#     ideal pentru exersat pentru ca NU modifica nimic cu adevarat)
#   - https://httpbin.org                    (echo - iti intoarce exact
#     ce ai trimis, util ca sa vezi ce "vede" serverul)
# =============================================================
from pprint import pprint

import requests


# #############################################################
# PARTEA 0 - CE E UN API? (teorie, fara cod)
# #############################################################
#
# API = Application Programming Interface = un "meniu" prin care doua
# programe vorbesc intre ele, fara sa stie fiecare cum e construit celalalt
# pe dinauntru.
#
# PROBLEMA pe care o rezolva:
#   Vrei date pe care NU le ai local - cursul valutar de azi, vremea,
#   userii unei aplicatii, postarile de pe un site. Datele astea sunt
#   pe un SERVER, in alta parte, si se pot schimba oricand.
#
# SOLUTIA:
#   Ceri serverului prin HTTP (protocolul pe care il foloseste si
#   browser-ul tau cand deschizi un site). Trimiti o CERERE (request),
#   primesti inapoi un RASPUNS (response), de obicei in format JSON.
#   In Python, facem asta cu libraria  requests.
#
# Cele mai comune API-uri de pe web sunt cele de tip REST:
#   - folosesc HTTP ca protocol de transport
#   - fiecare "lucru" (user, post, comentariu) are o adresa (URL) proprie
#   - actiunea pe care o faci (citesti / creezi / stergi) e data de
#     VERBUL HTTP folosit (GET / POST / PUT / DELETE) - vezi Partea 2


# #############################################################
# PARTEA 1 - CITIRE (GET): aduci date de pe web
# #############################################################


# 1. CUM ARATA un schimb HTTP
# -------------------------------------------------------------
#   CLIENT  --- cerere  (URL, metoda, headers, body)  --->  SERVER
#   CLIENT  <-- raspuns (status code, headers, body)  <---  SERVER
#
# O CERERE (request) are:
#   - URL          -> adresa resursei (ex: .../posts/1)
#   - METODA       -> ce vrei sa faci (GET, POST, PUT, DELETE...)
#   - HEADERS      -> metadate (cine esti, ce format accepti)
#   - BODY         -> date trimise (doar la POST/PUT, de regula)
#
# Un RASPUNS (response) are:
#   - STATUS CODE  -> un numar care spune daca a mers sau nu
#   - HEADERS      -> metadate despre raspuns
#   - BODY         -> continutul propriu-zis (de obicei JSON)
#
# STATUS CODES - trebuie sa le recunosti din prima cifra:
#   2xx  succes                (200 OK, 201 Created, 204 No Content)
#   3xx  redirectionare        (301, 302 - resursa s-a mutat)
#   4xx  greseala CLIENTULUI   (400 cerere gresita, 401 neautentificat,
#                                403 interzis, 404 nu exista)
#   5xx  greseala SERVERULUI   (500 eroare interna, 503 indisponibil)
#
# Retine: un 4xx sau 5xx NU inseamna ca programul tau Python a crapat -
# inseamna ca SERVERUL a raspuns cu o veste proasta. Vezi Partea 9.


# 2. PRIMUL GET  -  requests.get(...)
# -------------------------------------------------------------
# Ceri o resursa si primesti un obiect "response" (r) cu tot ce a
# raspuns serverul: status code, headere, si continut (text).

r = requests.get("https://jsonplaceholder.typicode.com/posts/1", timeout=10)
# print("status", r.status_code)
# print(r.text)

# r.text este intotdeauna un STRING (text brut). Chiar daca "arata" ca
# un dict, Python nu stie inca sa lucreze cu el ca si cum ar fi unul.


# 3. .json()  -  din text JSON in obiect Python
# -------------------------------------------------------------
# PROBLEMA: raspunsul e doar TEXT; nu poti face r.text["title"] - ar da
#           eroare, pentru ca string-urile nu se indexeaza cu chei.
# SOLUTIA:  .json() parseaza acel text si il transforma direct intr-un
#           dict/lista Python, cu care poti lucra normal.

post = r.json()       # DICT
print(post['body'])   # valoarea cheii body din dictionar

# ATENTIE: .json() esueaza (arunca eroare) daca raspunsul NU e JSON
# valid - de exemplu daca serverul a intors o pagina HTML de eroare.
# De aceea verificam mereu statusul INAINTE sa apelam .json() (Partea 9).


# 4. GET cu PARAMETRI  (query string  ?cheie=valoare)
# -------------------------------------------------------------
# Multe API-uri accepta filtre trimise in URL, dupa semnul "?", sub
# forma cheie=valoare, separate prin "&" (ex: ?postId=1&_limit=5).
#
# NU lipi parametrii de mana in string! Da-i prin params={...} -
# requests ii formateaza si ii "encodeaza" corect (spatii, caractere
# speciale etc.) automat.


def afiseazeaza_postarea(url, id):
    r = requests.get(url, params={'postId': id}, timeout=10)
    all_emails = [item['email']  for item in  r.json()]

    return all_emails

print(afiseazeaza_postarea('https://jsonplaceholder.typicode.com/comments', 2))


# 5. HEADERS  -  metadate ale cererii
# -------------------------------------------------------------
# Headerele sunt informatii ATASATE cererii, nu date propriu-zise:
# cine esti (User-Agent), ce format accepti (Accept), daca esti
# autentificat (Authorization) etc.
#
# httpbin.org/headers e un "ecou": iti intoarce exact headerele pe
# care le-a primit de la tine - util ca sa verifici ce ai trimis.

r = requests.get('https://httpbin.org/headers', headers={"User-Agent": "curs-python"}, timeout=10)
primite = r.json()['headers']
print(primite['User-Agent'])


# #############################################################
# PARTEA 2 - SCRIERE (POST/PUT/DELETE) + ROBUSTETE
# #############################################################


# 6. Verbele HTTP si maparea CRUD
# -------------------------------------------------------------
# CRUD = Create, Read, Update, Delete - cele 4 operatii de baza pe care
# le faci de obicei asupra unor date. Fiecare are un verb HTTP corespunzator:
#
#   GET    -> Read    (citesti, NU modifici nimic pe server)
#   POST   -> Create  (creezi o resursa noua)
#   PUT    -> Update  (inlocuiesti complet o resursa existenta)
#   DELETE -> Delete  (stergi o resursa)
#
# (exista si PATCH, pentru actualizare PARTIALA - nu il folosim aici,
# dar e bine sa stii ca exista.)


# 7. POST  -  trimiti un body JSON  (json=...)
# -------------------------------------------------------------
# Parametrul json= face doua lucruri automat pentru tine:
#   1. serializeaza dict-ul Python in text JSON
#   2. seteaza singur headerul Content-Type: application/json
# La creare cu succes, serverul raspunde de regula cu status 201.

nou = {
    "userId": 1,
    "title": "Cea mai buna zi ever",
    "body": "Marti este o zi superba pentru a invata Python"
  }

r = requests.post("https://jsonplaceholder.typicode.com/posts/", json=nou, timeout=10)
print("POST STATUS", r.status_code)   # 201
print("id_atribuit", r.json()['id'])  # 101
print("ultima postare", r.json())


# IMPORTANT: jsonplaceholder e un API "de joaca" - simuleaza raspunsul,
# dar NU salveaza nimic cu adevarat pe server. Perfect pentru exersat
# fara sa strici date reale.


# 8. PUT  si  DELETE
# -------------------------------------------------------------
# PUT inlocuieste TOATA resursa - de aceea trimitem toate campurile,
# nu doar cel pe care vrem sa-l schimbam.

r = requests.put("https://jsonplaceholder.typicode.com/posts/2", json={
    "userId": 1,
    "id": 2,
    "title": "Cea mai buna zi ever",
    "body": "Marti este o zi superba pentru a invata Python"
  }, timeout=10)

print("PUT", r.status_code)  # 200

r1 = requests.delete("https://jsonplaceholder.typicode.com/posts/1", json=nou, timeout=10)
print("DELETE", r.status_code) # 200


# 10. EXCEPTIILE principale din requests
# -------------------------------------------------------------
# Toate mostenesc din requests.exceptions.RequestException, deci poti
# prinde si generic cu  except requests.exceptions.RequestException,
# daca nu conteaza tipul exact.
#
#   Timeout          - serverul nu a raspuns la timp (vezi timeout=...)
#   ConnectionError  - nu ne-am putut conecta deloc (domeniu gresit,
#                       fara internet, server oprit)
#   HTTPError        - status 4xx/5xx (doar dupa ce apelezi
#                       raise_for_status())
print("=============10======================")
try:
    response = requests.get('https://horiascurtu.eu/', timeout=3)
except requests.exceptions.ConnectionError:
    print("Nu ne-am putut conecta deloc, domeniul nu exista")





# =============================================================
# RECAP / GRESELI FRECVENTE
# =============================================================
# CITIRE:
#   r = requests.get(url, params={...}, headers={...}, timeout=10)
#   r.status_code                 -> numarul (200, 404, ...)
#   r.json()                      -> raspunsul JSON ca dict/lista Python
#
# SCRIERE:
#   requests.post(url, json={...}, timeout=10)   # 201 la creare
#   requests.put(url, json={...}, timeout=10)    # inlocuieste tot
#   requests.delete(url, timeout=10)             # sterge
#
# GRESELI FRECVENTE (in ordinea in care le fac cei mai multi incepatori):
#   1. Lipseste timeout -> programul se poate bloca la infinit.
#      Pune-l MEREU: timeout=10.
#   2. Nu verifici statusul -> un 404/500 trece neobservat, iar codul
#      pare ca merge cand de fapt nu a primit date bune. Foloseste
#      status_code sau raise_for_status().
#   3. Apelezi .json() inainte sa verifici statusul -> daca serverul a
#      raspuns cu HTML de eroare, .json() arunca el insusi o exceptie
#      (nu foarte clara). Verifica INTAI statusul.
#   4. Lipesti parametrii de mana in URL (ex: url + "?postId=" + str(id))
#      -> foloseste params={...}, requests face encoding-ul corect.
#   5. Trimiti body-ul ca string (data=str(dict)) -> foloseste json={...},
#      care serializeaza corect si seteaza headerul potrivit.
#   6. Nu prinzi nicio exceptie -> orice problema de retea iti opreste
#      brutal programul. Prinde macar Timeout, ConnectionError, HTTPError.
#
# In sesiunea urmatoare: PYDANTIC - validezi automat datele primite
# de la un API, in loc sa verifici manual fiecare camp cu if-uri.
# =============================================================