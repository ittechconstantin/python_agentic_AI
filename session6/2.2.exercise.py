# RECAPITULARE - EXERCITII MIXTE
# =============================================================


# 1. Generare username din nume complet
# -------------------------------------
# Avem  nume_complet = "Ana Maria Popescu".
# Construieste un username de forma:  "ana.popescu"
# Pasi:
#   1) .lower()
#   2) .split()
#   3) primul cuvant + "." + ULTIMUL cuvant
# Pentru bonus:  afiseaza si o varianta cu initiala primului cuvant si
# numele complet:  "a.popescu"

# Solutie:

nume_complet = "Ana Maria Popescu"
nume_complet = nume_complet.lower().split()
prenume, *nume = nume_complet
nume_final = nume_complet[0] + "." + nume_complet[-1]
print(nume_final)
nume_bonus = prenume[0] + "." + nume_complet[-1]
print(nume_bonus)

# 2. Permisiuni si roluri (frozenset + dict)
# ------------------------------------------
# Definim mapping de roluri:
#   roluri = {
#       frozenset({"read"}):                     "user",
#       frozenset({"read", "comment"}):          "viewer",
#       frozenset({"read", "write"}):            "editor",
#       frozenset({"read", "write", "delete"}):  "admin",
#   }
# Pentru fiecare set de permisiuni de mai jos, afiseaza rolul:
#   p1 = {"read"}
#   p2 = {"comment", "read"}
#   p3 = {"write", "read", "delete"}
# (Atentie - cautam dupa frozenset(p)!)

# Solutie:

roluri = {
      frozenset({"read"}):                     "user",
      frozenset({"read", "comment"}):          "viewer",
      frozenset({"read", "write"}):            "editor",
      frozenset({"read", "write", "delete"}):  "admin",
  }

p1 = roluri.get(frozenset({"read"}))
print(p1)
p2 = roluri.get(frozenset({"comment", "read"}))
print(p2)
p3 = roluri.get(frozenset({"write", "read", "delete"}))
print(p3)


# print(roluri[frozenset({"user"})])

# 3. Diff intre 2 versiuni de fisiere (set ops)
# ---------------------------------------------
# Avem fisierele dintr-o aplicatie in doua momente:
#   v1 = ["main.py", "utils.py", "config.py", "test.py"]
#   v2 = ["main.py", "utils.py", "config.py", "api.py", "models.py"]
# Afiseaza:
#   - fisiere ADAUGATE in v2 (nu erau in v1)
#   - fisiere STERSE in v2 (erau in v1, nu mai sunt)
#   - fisiere COMUNE
#   - un mesaj de tipul:  "v2: +2 / -1 / =3"

# Solutie:

v1 = ["main.py", "utils.py", "config.py", "test.py"]
v2 = ["main.py", "utils.py", "config.py", "api.py", "models.py"]

v1, v2 = set(v1), set(v2)
print(v2.difference(v1))
print(v2.symmetric_difference(v1))
print(v1.intersection(v2))
