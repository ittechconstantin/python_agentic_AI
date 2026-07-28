# EXERCITII DICTIONARE - NIVEL AVANSAT
# =============================================================
# Combinam dictionare cu liste, string-uri si slicing.
# Toate exercitiile sunt rezolvate FARA  if / for / while.
# =============================================================


# 1. Profil utilizator complet
# ----------------------------
# Construieste un dict `user` cu cheile:
#   username, email, varsta, activ
# si o cheie suplimentara `limbaje` -> lista cu limbajele cunoscute.
# Afiseaza:
#   - primul limbaj din lista
#   - cate limbaje cunoaste utilizatorul

# Solutie:

print("\n--- Exercitiul 1 ---")
user = {"username": "John",
        "email" : "john@example.com",
        "varsta" : 79,
        "status" : "activ",
        "limbaje" : ["HTML", "CSS", "Javascript"]}
print(user["limbaje"][0])
print(len(user["limbaje"]))

# 2. Dict imbricat - acces in lant
# --------------------------------
# Avem un raspuns de la un API:
#   response = {
#       "status": 200,
#       "data": {"id": 42, "name": "Ana Popescu", "roles": ["editor", "reviewer"]},
#       "message": "OK",
#   }
# Afiseaza:
#   - status-ul
#   - numele utilizatorului
#   - ultimul rol din lista de roluri

# Solutie:

print("\n--- Exercitiul 2 ---")
response = {
      "status": 200,
      "data": {"id": 42, "name": "Ana Popescu", "roles": ["editor", "reviewer"]},
      "message": "OK",
  }
print(response["status"])
print(response["data"]["name"])
print(response["data"]["roles"][-1])

# 3. Modificare in dict imbricat
# ------------------------------
# Folosind dict-ul `response` de mai sus, modifica numele utilizatorului
# in "Ana M. Popescu" si adauga rolul "admin" la finalul listei de roluri.
# Afiseaza dict-ul "data" actualizat.

# Solutie:

response["data"]["name"] = "Ana M. Popescu"
response["data"]["roles"].append("admin")
print(response["data"])

# 4. Inventar de servere
# ----------------------
# Avem dictionarul:
#   servere = {
#       "web-01": {"ip": "10.0.0.1", "cpu": 4,  "ram_gb": 8},
#       "web-02": {"ip": "10.0.0.2", "cpu": 8,  "ram_gb": 16},
#       "db-01":  {"ip": "10.0.0.3", "cpu": 16, "ram_gb": 64},
#   }
# Afiseaza:
#   - cate servere sunt in total
#   - IP-ul serverului "db-01"
#   - lista numelor de servere (cheile)

# Solutie:

print("\n--- Exercitiul 4 ---")
servere = {
     "web-01": {"ip": "10.0.0.1", "cpu": 4,  "ram_gb": 8},
     "web-02": {"ip": "10.0.0.2", "cpu": 8,  "ram_gb": 16},
     "db-01":  {"ip": "10.0.0.3", "cpu": 16, "ram_gb": 64},
}
print(len(servere.keys()))
print(servere["db-01"]["ip"])
print(list(servere.keys()))

# 5. Construim un dict din doua liste paralele
# --------------------------------------------
# Avem:
#   produse  = ["laptop", "mouse", "tastatura", "monitor"]
#   preturi  = [4500, 79, 199, 1200]
# Construieste un dict `pret_produs` care leaga fiecare produs
# de pretul lui. Foloseste:
#   dict(zip(produse, preturi))
# Afiseaza dict-ul si pretul produsului "monitor".

# Solutie:

print("\n--- Exercitiul 5 ---")
produse  = ["laptop", "mouse", "tastatura", "monitor"]
preturi  = [4500, 79, 199, 1200]
pret_produs = dict(zip(produse, preturi))
print(pret_produs)
print(pret_produs["monitor"])

# 6. Sortare dict dupa CHEIE
# --------------------------
# Avem  http_status = {500: "Server Error", 200: "OK", 404: "Not Found", 301: "Moved"}.
# Construieste un dict NOU sortat dupa cheie (crescator).
# Sugestie:
#   dict(sorted(http_status.items()))
# Afiseaza dict-ul sortat.

# Solutie:

print("\n--- Exercitiul 6 ---")
http_status = {500: "Server Error", 200: "OK", 404: "Not Found", 301: "Moved"}
dict_nou = dict(sorted(http_status.items()))
print(dict_nou)

# 7. Sortare dict dupa VALOARE
# ----------------------------
# Avem  stoc = {"mouse": 50, "laptop": 10, "tastatura": 25, "monitor": 7}.
# Construieste un dict NOU sortat dupa CANTITATE, descrescator.
# Sugestie:
#   dict(sorted(stoc.items(), key=lambda pereche: pereche[1], reverse=True))
# Afiseaza dict-ul.

# Solutie:

print("\n--- Exercitiul 7 ---")
stoc = {"mouse": 50, "laptop": 10, "tastatura": 25, "monitor": 7}
dictul = dict(sorted(stoc.items(), key=lambda pereche: pereche[1], reverse=True))
print(dictul)

# 8. Cel mai scump produs (cheie + valoare)
# -----------------------------------------
# Folosind  pret_produs = {"laptop": 4500, "mouse": 79, "tastatura": 199, "monitor": 1200}
# afiseaza:
#   - pretul cel mai mare
#   - numele produsului cu pretul cel mai mare
# Sugestie pentru numele produsului - foloseste max cu key:
#   max(pret_produs, key=lambda nume: pret_produs[nume])

# Solutie:

print("\n--- Exercitiul 8 ---")
pret_produs = {"laptop": 4500, "mouse": 79, "tastatura": 199, "monitor": 1200}
print(max(pret_produs.values()))
print(max(pret_produs.keys(), key = lambda nume: pret_produs[nume]))

# 9. Adaugare conditionala fara if
# ---------------------------------
# Avem  config = {"host": "localhost", "port": 8080}.
# Vrem sa adaugam cheia "debug" cu valoarea True DOAR daca lipseste.
# Sugestie: foloseste .setdefault().
# Apoi incearca sa "fortezi" debug = False cu .setdefault() si arata
# ca valoarea NU se schimba daca cheia exista deja.

# Solutie:

print("\n--- Exercitiul 9 ---")
config = {"host": "localhost", "port": 8080}
config.setdefault("debug", True)
config.setdefault("debug", False)
print(config)

# 10. Numarare aparitii intr-o lista (frequency map)
# --------------------------------------------------
# Vrem sa stim de cate ori apare fiecare nivel de log intr-o lista.
# Avem  loguri = ["INFO", "ERROR", "INFO", "WARN", "ERROR", "INFO"].
# Construieste dictul:
#   {"INFO": 3, "ERROR": 2, "WARN": 1}
# Sugestie - fara loop, folosim .count() pe lista, pentru fiecare cheie unica:
#   chei_unice = list(set(loguri))
#   contoare = dict(map(lambda nivel: (nivel, loguri.count(nivel)), chei_unice))

# Solutie:

print("\n--- Exercitiul 10 ---")
loguri = ["INFO", "ERROR", "INFO", "WARN", "ERROR", "INFO"]
chei_unice = list(set(loguri))
contoare = dict(map(lambda nivel: (nivel, loguri.count(nivel)), chei_unice))
dict_contoare = dict(sorted(contoare.items(), key=lambda pereche: pereche[1], reverse=True))
print(dict_contoare)

# 11. Inversare cheie / valoare
# -----------------------------
# Avem  http_status = {200: "OK", 404: "Not Found", 500: "Server Error"}.
# Construieste un dict in care valorile devin chei si invers:
#   {"OK": 200, "Not Found": 404, "Server Error": 500}
# Sugestie:
#   dict(map(lambda p: (p[1], p[0]), http_status.items()))

# Solutie:

print("\n--- Exercitiul 11 ---")
http_status = {200: "OK", 404: "Not Found", 500: "Server Error"}
noul_status = dict(map(lambda p:(p[1], p[0]), http_status.items()))
print(noul_status)

# 12. Filtrare dict dupa valoare (fara if)
# ----------------------------------------
# Avem  stoc = {"mouse": 50, "laptop": 10, "tastatura": 25, "monitor": 7, "casti": 0}.
# Vrem un dict NOU doar cu produsele care au cantitate > 10.
# Sugestie - folosim filter cu lambda pe perechile dict-ului:
#   dict(filter(lambda p: p[1] > 10, stoc.items()))

# Solutie:

print("\n--- Exercitiul 12 ---")
stoc = {"mouse": 50, "laptop": 10, "tastatura": 25, "monitor": 7, "casti": 0}
noul_stoc = dict(filter(lambda p: p[1] > 10,stoc.items()))
print(noul_stoc)

# 13. Raport text dintr-un dict
# -----------------------------
# Avem  user = {"username": "horia", "email": "h@x.com", "rol": "admin", "limbaje": ["Python", "Go", "SQL"]}.
# Construieste un raport multi-linie de forma:
#
#   ===== Profil utilizator =====
#   Username: horia
#   Email:    h@x.com
#   Rol:      ADMIN
#   Limbaje:  Python, Go, SQL
#   =============================
#
# Sugestie: foloseste f-string-uri si " , ".join() pentru limbaje.

# Solutie:

print("\n--- Exercitiul 13 ---")
user = {"username": "horia", "email": "h@x.com", "rol": "admin", "limbaje": ["Python", "Go", "SQL"]}
print(user["limbaje"])
print(f"===== Profil utilizator =====")
print(f"Username: {user['username']}")
print(f"Email: {user['email']}")
print(f"Rol: {user['rol'].upper()}")
print(f"Limbaje:", " , ".join(user['limbaje']))

# 14. Fuziune cu suprascriere - operatorul |
# ------------------------------------------
# Avem doua dictionare de configurare:
#   default_config = {"host": "localhost", "port": 8080, "debug": False, "timeout": 30}
#   user_config    = {"port": 9090, "debug": True}
# Construieste dictul final aplicand intai default-urile,
# apoi suprascriind cu config-ul utilizatorului. (b castiga in conflict)
# Foloseste operatorul  |  si afiseaza dict-ul.

# Solutie:

print("\n--- Exercitiul 14 ---")
default_config = {"host": "localhost", "port": 8080, "debug": False, "timeout": 30}
user_config    = {"port": 9090, "debug": True}
config = default_config.setdefault("port", "debug")
print(config)
final_config = default_config | user_config
print(final_config)

# 15. Mini agenda - cautare email dupa username
# ---------------------------------------------
# Avem  agenda = {
#       "horia":  "horia@example.com",
#       "ana":    "ana@example.com",
#       "george": "george@example.com",
#   }
# Vrem sa afisam emailul utilizatorului "ana".
# Daca utilizatorul nu exista (ex: "vlad"), afisam mesajul "necunoscut".
# Foloseste .get() cu default - obtii varianta sigura, fara if.

# Solutie:

print("\n--- Exercitiul 15 ---")
agenda = {
      "horia":  "horia@example.com",
      "ana":    "ana@example.com",
      "george": "george@example.com",
  }
print(agenda.get("ana"))
print(agenda.get("vlad", "necunoscut"))

# 16. Adaugare mai multe chei dintr-o lista (fromkeys + update)
# -------------------------------------------------------------
# Vrem sa adaugam la un dict existent un grup de feature-flags
# care toate pleaca de la valoarea False.
# Plecam de la:  flags = {"dark_mode": True}
# Avem lista feature-urilor noi:
#   noi = ["beta_ui", "search_v2", "ai_assistant"]
# Construieste un dict cu cheile din `noi`, toate cu valoarea False,
# si imbina-l in `flags` cu .update(). Afiseaza dict-ul final.

# Solutie:

print("\n--- Exercitiul 16 ---")
flags = {"dark_mode": True}
noi = ["beta_ui", "search_v2", "ai_assistant"]
feature_flags = dict.fromkeys(noi, False)
flags.update(feature_flags)
print(flags)

