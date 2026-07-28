# EXERCITII  if / elif / else
# =============================================================

# (NU folosim for / while - nu le-am invatat inca.)
# =============================================================


# 1. Validare email cu mesaje clare
# ---------------------------------
# Avem  email = "ana@@example".
# Verifica IN ORDINE si afiseaza primul mesaj care se potriveste:
#   - "lipseste @"            daca nu contine @
#   - "prea multi @"          daca contine mai mult de un @
#   - "lipseste ."            daca nu contine .
#   - "prea scurt"            daca are mai putin de 5 caractere
#   - "valid"                 altfel

# Solutie:

print("\n--- Exercitiul 1 ---")
email = "ana@@example"
if "@" not in email:
    print("lipseste @")
elif email.count("@") > 1:
    print("prea multi @@")
elif "." not in email:
    print("lipseste .")
elif len(email) < 5:
    print("prea scurt")
else:
    print("valid")

# 2. Mesaj pentru cod HTTP cu fallback
# ------------------------------------
# Avem un dict de coduri:
#   coduri = {200: "OK", 301: "Moved", 404: "Not Found", 500: "Server Error"}
# Si un cod primit:  cod = 418
# Daca codul este in dict -> afiseaza  "<cod>: <mesaj>"
# Altfel -> afiseaza "Cod necunoscut: <cod>"

# Solutie:

print("\n--- Exercitiul 2 ---")
coduri = {200: "OK", 301: "Moved", 404: "Not Found", 500: "Server Error"}
cod = 418
if cod in coduri:
    print(f"{cod}: {coduri[cod]}")
else:
    print(f"Cod necunoscut: {cod}")

# 3. BMI cu interpretare
# ----------------------
# Avem  greutate = 78  si  inaltime = 1.78.
# Calculeaza  bmi = greutate / (inaltime ** 2)
# Apoi clasifica:
#   - bmi < 18.5         -> "subponderal"
#   - bmi < 25           -> "normal"
#   - bmi < 30           -> "supraponderal"
#   - altfel             -> "obez"
# Afiseaza:  "BMI = X.XX -> categorie"

# Solutie:

print("\n--- Exercitiul 3 ---")
greutate = 78
inaltime = 1.78
bmi = greutate / (inaltime ** 2)
print(bmi)
if bmi < 18.5:
    print("subponderal")
elif bmi < 25:
    print("normal")
elif bmi < 30:
    print("supraponderal")
else:
    print("obez")


# 4. Login (multi-criteriu)
# -------------------------
# Avem un "registru" de useri:
#   useri = {
#       "ana":   {"parola": "abc12345", "blocat": False},
#       "horia": {"parola": "qwerty12", "blocat": True},
#   }
# Si un input:  username = "ana", parola_intrare = "abc12345"
# Verifica:
#   - daca username NU exista -> "user inexistent"
#   - daca user este blocat   -> "cont blocat"
#   - daca parola nu se potriveste -> "parola gresita"
#   - altfel -> "login reusit pentru <username>"

# Solutie:

print("\n--- Exercitiul 4 ---")
useri = {
      "ana":   {"parola": "abc12345", "blocat": False},
      "horia": {"parola": "qwerty12", "blocat": True},
  }
username = "ana"
parola_intrare = "abc12345"
if username not in useri:
    print("user inexistent")
if useri[username]["blocat"]:
    print("cont blocat")
if parola_intrare != useri[username]["parola"]:
    print("parola gresita")
else:
    print(f"login reusit pentru {username}")



# 5. Disponibilitate username
# ---------------------------
# Avem o lista de username-uri deja folosite:
#   existente = {"ana", "horia", "george", "vlad", "maria"}
# Si un username dorit:  dorit = "Horia "
# Pasi:
#   - curata-l: .strip().lower()
#   - daca este SUB 3 caractere -> "prea scurt"
#   - daca contine SPATIU -> "spatii nepermise"
#   - daca este in `existente` -> "deja folosit"
#   - altfel -> "disponibil"

# Solutie:

print("\n--- Exercitiul 5 ---")
existente = {"ana", "horia", "george", "vlad", "maria"}
dorit = "Horia "
username_dorit = dorit.strip().lower()
if len(username_dorit) < 3:
    print("prea scurt")
elif " " in username_dorit:
    print("spatii nepermise")
elif username_dorit in existente:
    print("deja folosit")
else:
    print("disponibil")

# 6. Recomandare film (varsta + gen)
# ----------------------------------
# Avem  varsta = 14  si  gen = "horror".
# Reguli:
#   - "kids"     -> oricine
#   - "general"  -> minim 6
#   - "horror"   -> minim 16
#   - "documentar" -> oricine
#   - alt gen    -> "gen necunoscut"
# Decide si afiseaza "permis" / "interzis" / "gen necunoscut".

# Solutie:

print("\n--- Exercitiul 6 ---")
varsta = 14
gen = "horror"
if gen == "kids":
    print("permis")
elif gen == "general" and varsta >= 6:
    print("permis")
elif gen == "horror" and varsta >=16:
    print("permis")
elif gen == "documentar":
    print("permis")
else:
    print("interzis")

# 7. Calcul taxa progresiv (transe de venit)
# ------------------------------------------
# Avem  venit = 7500.
# Transe (lunare):
#   - <= 2000       -> 0% taxa
#   - <= 5000       -> 10% pe ce depaseste 2000
#   - <= 10000      -> 10% pe (5000-2000) + 20% pe ce depaseste 5000
#   - peste 10000   -> 10% pe (5000-2000) + 20% pe (10000-5000) + 30% pe ce depaseste 10000
# Calculeaza si afiseaza taxa cu 2 zecimale.

# Solutie:

print("\n--- Exercitiul 7 ---")
venit = 7500
taxa = 0
taxa_sub_5000 = (venit - 2000) * 0.10
taxa_sub_10000 = ((5000 - 2000) * 0.10) + ((venit - 5000) * 0.20)
taxa_peste_10000 = taxa = ((5000 - 2000) * 0.10) + ((venit - 5000) * 0.20) + ((venit - 10000) * 0.30)
if venit <= 2000:
    print(f"{taxa:.2f}")
elif venit <= 5000:
    print(f"{(taxa_sub_5000):.2f}")
elif venit <= 10000:
    print(f"{(taxa_sub_10000):.2f}")
elif venit >= 10000:
    print(f"{(taxa_peste_10000):.2f}")

# 8. Detectare tip fisier dupa extensie
# -------------------------------------
# Avem  fisier = "raport.PDF".
# Curata-l (lower) si decide:
#   - .pdf, .docx, .txt        -> "document"
#   - .png, .jpg, .jpeg, .gif   -> "imagine"
#   - .mp4, .mov, .avi          -> "video"
#   - .zip, .tar, .gz           -> "arhiva"
#   - altceva                    -> "necunoscut"
# Sugestie: foloseste .endswith() in if/elif.

# Solutie:

print("\n--- Exercitiul 8 ---")
fisier = "raport.PDF"
fisier_curatat = fisier.lower()
if fisier_curatat.endswith(".pdf" or ".docx" or ".txt"):
    print("document")
elif fisier_curatat.endswith(".png" or ".jpg" or ".jpeg" or ".gif"):
    print("image")
elif fisier_curatat.endswith(".mp4" or ".mov" or ".avi"):
    print("video")
elif fisier_curatat.endswith(".zip" or ".tar" or ".gz"):
    print("arhiva")
else:
    print("necunoscut")

# 9. Status server complet (dict imbricat + if)
# ----------------------------------------------
# Avem  server = {
#     "nume": "web-01",
#     "cpu":  82,           # procent
#     "ram":  77,           # procent
#     "disk": 91,           # procent
#     "online": True,
# }
# Reguli:
#   - daca offline -> "DOWN"
#   - daca disk >= 90 sau cpu >= 90 sau ram >= 90 -> "CRITIC"
#   - daca disk >= 75 sau cpu >= 75 sau ram >= 75 -> "WARN"
#   - altfel -> "OK"
# Afiseaza un mesaj "<nume>: <stare>"

# Solutie:

print("\n--- Exercitiul 9 ---")
server = {
    "nume": "web-01",
    "cpu":  82,           # procent
    "ram":  77,           # procent
    "disk": 91,           # procent
    "online": True,
}
if server["online"] is False:
    print("DOWN")
elif server["disk"] >= 90 or server["cpu"] >= 90 or server["ram"] >= 90:
    print("CRITIC")
elif server["disk"] >= 75 or server["cpu"] >= 75 or server["ram"] >= 75:
    print("WARN")
else:
    print("OK")

# 10. Cupon de reducere - validare
# --------------------------------
# Avem un set de cupoane valide si datele de intrare:
#   cupoane = {"PRIMA10", "BLACKFRIDAY", "SUMMER25"}
#   cupon_user = "blackfriday"
#   total_cos = 250
# Reguli:
#   - cuponul trebuie comparat case-INsensitive cu cele din set
#     (sugestie:  cupon_user.upper() in cupoane)
#   - cosul trebuie sa fie >= 100 lei pentru a accepta cupon
# Daca toate sunt OK -> aplica 15% reducere si afiseaza pretul final.
# Altfel -> afiseaza motivul ("cupon invalid" sau "cos prea mic").

# Solutie:

print("\n--- Exercitiul 10 ---")
cupoane = {"PRIMA10",
           "BLACKFRIDAY", "SUMMER25"}
cupon_user = "blackfriday"
total_cos = 250
if cupon_user.upper() in cupoane and total_cos >= 100:
    print(total_cos * 0.85)
else:
    print("cupon invalid" or "cos prea mic")

# 11. Statistici cos in functie de prag
# -------------------------------------
# Avem un cos:
#   cos = {"laptop": 4500, "mouse": 79, "tastatura": 199, "monitor": 1200}
# Calculeaza:
#   - total = sum(cos.values())
# Decide nivelul:
#   - total < 100   -> "free shipping NU se aplica"
#   - total < 500   -> "free shipping standard"
#   - altfel        -> "free shipping express"
# Afiseaza un raport.

# Solutie:

print("\n--- Exercitiul 11 ---")
cos = {"laptop": 4500, "mouse": 79, "tastatura": 199, "monitor": 1200}
total = sum(cos.values())
# print(total)
if total < 100:
    print("free shipping NU se aplica")
elif total < 500:
    "free shipping standard"
else:
    print("free shipping express")

# 12. Permisiuni minime pentru o actiune
# --------------------------------------
# Avem permisiunile unui user:
#   permisiuni = {"read", "write"}
# Si o lista de actiuni dorite, fiecare cu permisiunile necesare:
#   - actiune: "edit_articol"   -> are nevoie de  {"read", "write"}
#   - actiune: "publish"        -> are nevoie de  {"read", "write", "publish"}
#   - actiune: "stergere_user"  -> are nevoie de  {"read", "delete"}
# Pentru actiunea  ceruta = "publish",  decide:
#   - "permis" daca permisiunile contin tot ce trebuie (issubset)
#   - "lipseste: {set_ce_lipseste}"  altfel
# Sugestie:
#   nevoie = {"read", "write", "publish"}
#   if nevoie.issubset(permisiuni): ...
#   altfel: lipsesc = nevoie - permisiuni

# Solutie:

print("\n--- Exercitiul 12 ---")
permisiuni = {"read", "write"}
nevoie = {"read", "write", "publish"}
actiunea_ceruta = "publish"
set_ce_lipseste = nevoie - permisiuni
if nevoie.issubset(permisiuni):
    print("permis")
else:
    print(f"lipseste: {set_ce_lipseste}")

