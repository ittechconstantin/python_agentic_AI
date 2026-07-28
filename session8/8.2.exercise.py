# EXERCITII  for
# =============================================================
# Mini-scenarii care combina for cu if/elif/else, dictionare,
# liste, set-uri, tupluri si string-uri.
# (NU folosim while - urmeaza in sesiunea urmatoare.)
# =============================================================
from operator import contains, index

# 1. Frequency counter pe log
# ---------------------------
# Avem  loguri = ["INFO", "ERROR", "INFO", "WARN", "INFO", "ERROR", "DEBUG"].
# Construieste un dict cu numarul de aparitii pentru fiecare nivel.
# Sugestie:  freq[n] = freq.get(n, 0) + 1
# Afiseaza:
#   - dict-ul cu frecvente
#   - nivelul cel mai frecvent (folosind max + key=lambda)

# Solutie:

print("\n--- Exercitiul 1 ---")
loguri = ["INFO", "ERROR", "INFO", "WARN", "INFO", "ERROR", "DEBUG"]
freq = {}
print(freq)
for log in loguri:
    if loguri.count(log) > 0:
        freq[log] = freq.get(log, 0) + 1
print(freq)
print(max(freq, key=lambda n: freq[n]))

# 2. Group-by - produse pe categorii
# ----------------------------------
# Avem o lista de tupluri (produs, categorie):
#   produse = [
#       ("laptop",     "electronice"),
#       ("mar",         "fructe"),
#       ("mouse",       "electronice"),
#       ("para",        "fructe"),
#       ("tastatura",   "electronice"),
#       ("banana",      "fructe"),
#   ]
# Construieste un dict {categorie: [lista produselor]}.

# Solutie:

print("\n--- Exercitiul 2 ---")
produse = [
      ("laptop",     "electronice"),
      ("mar",         "fructe"),
      ("mouse",       "electronice"),
      ("para",        "fructe"),
      ("tastatura",   "electronice"),
      ("banana",      "fructe"),
  ]

for produs,categorie in produse:
    print({categorie:[produs]})
    continue

# 3. Validare emailuri pe lista
# -----------------------------
# Avem  emailuri = ["ana@x.com", "fara_at.com", "horia@@x.com",
#                   "george@y.com", "vlad@z"].
# Imparte-le in 2 liste:  valide  si  invalide.
# Reguli simple: are exact UN @ si contine ".".

# Solutie:

print("\n--- Exercitiul 3 ---")
emailuri = ["ana@x.com", "fara_at.com", "horia@@x.com",
                  "george@y.com", "vlad@z"]
valide = []
invalide = []
for email in emailuri:
    if email.count("@") == 1 and "." in email:
        valide.append(email)
    else:
        invalide.append(email)
print(f"{valide}: ")
print(f"{invalide}: ")


# 4. Total cos cu reduceri pe categorie
# -------------------------------------
# Avem un cos in care fiecare produs are pret si categorie:
#   cos = [
#       ("laptop",     4500, "electronice"),
#       ("mar",          5,  "fructe"),
#       ("monitor",   1200,  "electronice"),
#       ("para",         3,  "fructe"),
#       ("ciocolata",   12,  "dulciuri"),
#   ]
# Reduceri:
#   - "electronice"  -> 10%
#   - "fructe"       -> 0%
#   - "dulciuri"     -> 5%
#   - alta categorie -> 0%
# Calculeaza si afiseaza totalul final cu reducerile aplicate (2 zecimale).

# Solutie:

print("\n--- Exercitiul 4 ---")
cos = [
      ("laptop",     4500, "electronice"),
      ("mar",          5,  "fructe"),
      ("monitor",   1200,  "electronice"),
      ("para",         3,  "fructe"),
      ("ciocolata",   12,  "dulciuri"),
  ]

for produs, pret, tip in cos:
    if "electronice" in cos:
        print(f"{pret["electronice"]*0.90:.2f}")
    elif "fructe" in cos:
        print(f"{pret["fructe"]*1.00:.2f}")
    elif "dulciuri" in cos:
         print(f"{pret["dulciuri"]*0.95:.2f}")
    else:
        print(pret)

# 5. Cautare cu break + for/else
# ------------------------------
# Avem o lista cu username-uri:
#   useri = ["ana", "horia", "george", "vlad", "maria"]
# Si cautam "vlad". Foloseste for/else:
#   - daca il gasesti -> printeaza "gasit la indexul X" si break
#   - daca termini bucla fara break -> printeaza "nu exista"

# Solutie:

print("\n--- Exercitiul 5 ---")
useri = ["ana", "horia", "george", "vlad", "maria"]
user_dorit = "vlad"
for user in useri:
        if user_dorit in useri:
            print(f"gasit la indexul: {useri.index(user_dorit)}")
            break
        else:
            print("nu exista")

# 6. Numara vocale si consoane
# ----------------------------
# Avem  text = "Programare in Python".
# Numara cate vocale ("aeiouAEIOU") si cate consoane (litere care
# NU sunt vocale si NU sunt spatii).
# Foloseste for + if/elif.

# Solutie:

print("\n--- Exercitiul 6 ---")
text = "Programare in Python"
nr_vocale = 0
nr_consoane = 0
for cuvant in text.strip().split():
    for caracter in cuvant:
        if caracter in ("a","e","i","o","u","A","E","I","O","U"):
            nr_vocale += 1
        else:
            nr_consoane += 1
print(nr_vocale)
print(nr_consoane)


# 7. Inversare manuala a unui string
# ----------------------------------
# Avem  text = "Python".
# Construieste un string NOU cu literele in ordine inversa,
# FARA slicing [::-1].
# Foloseste for + concatenare (atentie: string-ul e imutabil,
# se construieste prin reasignare).

# Solutie:

print("\n--- Exercitiul 7 ---")
text = "Python"
string_nou = ""
for caracter in text:
    print(caracter)
    print(string_nou)
    string_nou = caracter + string_nou
    print(string_nou)
print(string_nou)


# 8. FizzBuzz - varianta clasica
# -------------------------------
# Pentru fiecare numar de la 1 la 20:
#   - daca este divizibil cu 3 SI cu 5  -> afiseaza "FizzBuzz"
#   - daca este divizibil DOAR cu 3      -> afiseaza "Fizz"
#   - daca este divizibil DOAR cu 5      -> afiseaza "Buzz"
#   - altfel                              -> afiseaza numarul

# Solutie:

print("\n--- Exercitiul 8 ---")
for i in range(1,21):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

# 9. Acces in dict imbricat (dict de dict)
# -----------------------------------------
# Avem  servere = {
#       "web-01": {"cpu": 82, "ram": 70, "online": True},
#       "web-02": {"cpu": 35, "ram": 60, "online": True},
#       "db-01":  {"cpu": 90, "ram": 95, "online": False},
#       "cache-01": {"cpu": 22, "ram": 30, "online": True},
#   }
# Genereaza un raport pentru toate serverele:
#   - daca offline           -> "DOWN"
#   - cpu >= 90 sau ram >= 90 -> "CRITIC"
#   - cpu >= 70 sau ram >= 70 -> "WARN"
#   - altfel                  -> "OK"
# Afiseaza ca:  "<nume>: <stare>"

# Solutie:

print("\n--- Exercitiul 9 ---")
servere = {
      "web-01": {"cpu": 82, "ram": 70, "online": True},
      "web-02": {"cpu": 35, "ram": 60, "online": True},
      "db-01":  {"cpu": 90, "ram": 95, "online": False},
      "cache-01": {"cpu": 22, "ram": 30, "online": True},
  }
for server in servere:
    if servere[server]["online"] is False:
        print(f"{server}: DOWN")
    elif servere[server]["cpu"] >= 90 or servere[server]["ram"] >= 90:
        print(f"{server}: CRITIC")
    elif servere[server]["cpu"] >= 70 or servere[server]["ram"] >= 70:
        print(f"{server}: WARN")
    else:
        print("OK")

# 10. Detectare permisiuni lipsa per user
# ---------------------------------------
# Avem  necesare = {"read", "write", "delete"}.
# Avem useri si permisiunile lor:
#   useri = {
#       "ana":    {"read", "write", "delete"},
#       "horia":  {"read", "write"},
#       "george": {"read"},
#       "vlad":   {"read", "delete"},
#   }
# Pentru fiecare user afiseaza:
#   - "<user>: OK" daca are toate permisiunile
#   - "<user>: lipseste {set_lipsuri}" altfel
# Foloseste set difference.

# Solutie:

print("\n--- Exercitiul 10 ---")
necesare = {"read", "write", "delete"}
useri = {
      "ana":    {"read", "write", "delete"},
      "horia":  {"read", "write"},
      "george": {"read"},
      "vlad":   {"read", "delete"},
  }

for user in useri:
    set_lipsuri = necesare - useri[user]
    if necesare.issubset(useri[user]):
        print(f"{user}: OK")
    elif necesare.difference(useri[user]):
        print(f"lipseste {set_lipsuri}")
