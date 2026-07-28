# EXERCITII DICTIONARE
# =============================================================
# Foloseste DOAR ce am invatat pana acum: variabile, tipuri,
# print(), operatori, string-uri, liste si tot ce e in 4.dict.py.
# (NU folosim if / for / while - inca nu le-am invatat.)
# =============================================================


# 1. Crearea unui dictionar
# -------------------------
# Creeaza un dict numit `user` cu urmatoarele perechi:
#   username -> "horia"
#   email    -> "horia@example.com"
#   varsta   -> 30
# Afiseaza dictionarul.

# Solutie:

print("\n--- Exercitiul 1 ---")
user = {
    "username": "horia",
    "email": "horia@example.com",
    "varsta": 30
}
print(user)

# 2. Accesarea valorilor
# ----------------------
# Folosind dict-ul de mai sus, afiseaza:
#   - username-ul
#   - email-ul
#   - varsta utilizatorului

# Solutie:

print("\n--- Exercitiul 2 ---")
print(user["username"])
print(user["email"])
print(user["varsta"])

# 3. Acces sigur cu .get()
# ------------------------
# Avem  config = {"host": "localhost", "port": 8080}.
# Foloseste .get() pentru a afisa:
#   - valoarea cheii "host"
#   - valoarea cheii "debug" (NU exista, ar trebui sa fie None)
#   - valoarea cheii "debug" cu default-ul False

# Solutie:

print("\n--- Exercitiul 3 ---")
config = {"host": "localhost", "port": 8080}
print(config.get("host"))
print(config.get("debug"))
print(config.get("debug", False))

# 4. Modificarea unei valori
# --------------------------
# Avem  user = {"username": "horia", "rol": "user"}.
# Modifica rolul la "admin" si afiseaza dictionarul.

# Solutie:

print("\n--- Exercitiul 4 ---")
user = {"username": "horia", "rol": "user"}
user["rol"] = "admin"
print(user)

# 5. Adaugarea unei chei noi
# --------------------------
# Avem  server = {"host": "localhost"}.
# Adauga doua chei noi:
#   port    -> 8080
#   debug   -> True
# Afiseaza dictionarul final.

# Solutie:

print("\n--- Exercitiul 5 ---")
server = {"host": "localhost"}
server["port"] = 8080
server["debug"] = True
print(server)

# 6. Stergere cu pop()
# --------------------
# Avem  config = {"host": "localhost", "port": 8080, "debug": True}.
# Sterge cheia "debug" cu .pop() si afiseaza:
#   - valoarea returnata
#   - dictionarul ramas

# Solutie:

print("\n--- Exercitiul 6 ---")
config = {"host": "localhost", "port": 8080, "debug": True}
print(config.pop("debug"))
print(config)

# 7. Stergere cu del
# ------------------
# Avem  user = {"username": "horia", "email": "x@y.z", "telefon": "0712"}.
# Sterge cheia "telefon" folosind  del  si afiseaza dictionarul.

# Solutie:

print("\n--- Exercitiul 7 ---")
user = {"username": "horia", "email": "x@y.z", "telefon": "0712"}
del user["telefon"]
print(user)

# 8. Lungimea dictionarului
# -------------------------
# Avem  stoc = {"laptop": 10, "mouse": 50, "tastatura": 25, "monitor": 7}.
# Afiseaza cate produse diferite sunt in stoc.

# Solutie:

print("\n--- Exercitiul 8 ---")
stoc = {"laptop": 10, "mouse": 50, "tastatura": 25, "monitor": 7}
print(len(stoc.keys()))

# 9. Verificare existenta cheie:  in / not in
# -------------------------------------------
# Avem  permisiuni = {"read": True, "write": False}.
# Afiseaza True / False pentru:
#   - "read" exista in dict
#   - "delete" exista in dict
#   - "delete" NU exista in dict

# Solutie:

print("\n--- Exercitiul 9 ---")
permisiuni = {"read": True, "write": False}
print("read" in permisiuni)
print("delete" in permisiuni)
print("delete" not in permisiuni)

# 10. .keys() si .values()
# ------------------------
# Avem  user = {"username": "horia", "email": "h@x.com", "rol": "admin"}.
# Afiseaza:
#   - lista cheilor
#   - lista valorilor

# Solutie:

print("\n--- Exercitiul 10 ---")
user = {"username": "horia", "email": "h@x.com", "rol": "admin"}
print(user.keys())
print(user.values())

# 11. .items()
# ------------
# Folosind acelasi dict de la ex. 10, afiseaza lista perechilor (cheie, valoare).

# Solutie:

print("\n--- Exercitiul 11 ---")
print(user.items())

# 12. Update / fuzionare
# ----------------------
# Avem  config = {"host": "localhost", "port": 8080}.
# Foloseste .update() pentru a:
#   - schimba portul in 9090
#   - adauga cheia "debug" cu valoarea True
# Afiseaza dictionarul final.

# Solutie:

print("\n--- Exercitiul 12 ---")
config = {"host": "localhost", "port": 8080}
config.update({"port": 9090})
config.update({"debug": True})
print(config)

# 13. Coduri HTTP
# ---------------
# Construieste un dict numit `http_status` cu urmatoarele perechi:
#   200 -> "OK"
#   404 -> "Not Found"
#   500 -> "Internal Server Error"
# Apoi afiseaza:
#   - mesajul corespunzator codului 404
#   - mesajul pentru codul 500, scris cu litere mari (.upper())

# Solutie:

print("\n--- Exercitiul 13 ---")
http_status = {200 : "OK",
               404 : "Not Found",
               500 : "Internal Server Error",}
print(http_status[404])
print(f"{http_status[500].upper()}")

# 14. Statistici pe valori
# ------------------------
# Avem  stoc = {"laptop": 10, "mouse": 50, "tastatura": 25, "monitor": 7}.
# Afiseaza:
#   - numarul total de bucati (sum)
#   - cantitatea cea mai mare (max)
#   - cantitatea cea mai mica (min)
# Sugestie: aplica functiile pe stoc.values().

# Solutie:

print("\n--- Exercitiul 14 ---")
stoc = {"laptop": 10, "mouse": 50, "tastatura": 25, "monitor": 7}
print(sum(stoc.values()))
print(max(stoc.values()))
print(min(stoc.values()))

# 15. Dict cu valori implicite folosind fromkeys
# ----------------------------------------------
# Avem o lista de servicii:
#   servicii = ["nginx", "postgres", "redis"]
# Construieste un dict in care fiecare serviciu pleaca cu starea "down".
# Afiseaza dictionarul.

# Solutie:

print("\n--- Exercitiul 15 ---")
servicii = ["nginx", "postgres", "redis"]
status = dict.fromkeys(servicii, "down")
print(status)

# 16. Afisare frumoasa cu f-string
# --------------------------------
# Avem  user = {"username": "horia", "email": "h@x.com", "rol": "admin"}.
# Construieste si afiseaza un mesaj de forma:
#   "User: horia | Email: h@x.com | Rol: ADMIN"
# (rolul cu litere mari)

# Solutie:

print("\n--- Exercitiul 16 ---")
user = {"username": "horia", "email": "h@x.com", "rol": "admin"}
print(f"User: {user['username']} | Email: {user['email']} | Rol: {user['rol'].upper()}")