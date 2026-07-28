# RECAPITULARE
# =============================================================
# Fiecare exercitiu COMBINA cel putin 2 structuri / concepte
# din ce am invatat: variabile, operatori, string-uri, liste,
# dictionare, tupluri, set-uri.
#
# Reguli:
#   - NU folosim if / for / while - inca nu le-am invatat.
#   - Folosim functii ajutatoare cunoscute:
#     sorted, sum, len, min, max, set, list, tuple, dict,
# =============================================================
from itertools import count
from shlex import split

# 1. Profil scurt afisat (dict + f-string + .upper)
# -------------------------------------------------
# Avem  user = {"nume": "ana popescu", "rol": "admin", "varsta": 28}.
# Afiseaza un mesaj de forma:
#   "ANA POPESCU (28 ani) - rol: ADMIN"

# Solutie:

user = {"nume": "ana popescu", "rol": "admin", "varsta": 28}
print(f"{user['nume'].upper()}, ({user['varsta']} ani) - rol: {user['rol'].upper()} ")

# 2. Lista cumparaturi - total cos (lista + sum + f-string)
# ---------------------------------------------------------
# Avem doua liste paralele:
#   produse = ["paine", "lapte", "ciocolata", "cafea"]
#   preturi = [4.5, 7.99, 12.5, 23.0]
# Afiseaza:
#   - cate produse sunt
#   - totalul cu 2 zecimale
#   - mesajul: "Cos: 4 produse, total 47.99 lei"

# Solutie:

produse = ["paine", "lapte", "ciocolata", "cafea"]
preturi = [4.5, 7.99, 12.5, 23.0]
print(len(produse))
total_produse = sum(preturi)
print(f"{total_produse:.2f}")
print(f"Cos: {len(produse)} produse, total {total_produse:.2f} lei")

# 3. Cuvinte distincte dintr-un text (string -> list -> set)
# ----------------------------------------------------------
# Avem  text = "python este cool python e simplu cool".
# Afiseaza:
#   - lista de cuvinte (split)
#   - cate cuvinte sunt in total
#   - setul de cuvinte distincte
#   - cate cuvinte distincte sunt

# Solutie:

textul_dat = "python este cool python e simplu cool"
lista_cuvinte = split(textul_dat)
print(lista_cuvinte)
print(len(lista_cuvinte))
setul_distinct = set(lista_cuvinte)
print(setul_distinct)
print(len(setul_distinct))

# 4. Note la examen (list + min/max/sum + f-string)
# -------------------------------------------------
# Avem  note = [9, 7, 8, 10, 6, 5, 9, 8, 7, 10].
# Afiseaza un mic raport cu:
#   - numarul de note
#   - nota minima si maxima
#   - media (cu 2 zecimale)
#   - cate note de 10 au fost (.count())

# Solutie:

note = [9, 7, 8, 10, 6, 5, 9, 8, 7, 10]
print(len(note))
print(min(note))
print(max(note))
media_note = sum(note) / len(note)
print(f"{media_note:.2f}")
note_de_10 = note.count(10)
print(note_de_10)

# 5. Unpacking dintr-o linie de log (string + split + tuple unpacking)
# -------------------------------------------------------------------
# Avem  linie = "2026-05-09 ERROR auth user not found".
# Despacheteaza in 3 variabile:
#   data, nivel, *mesaj = linie.split()
# Afiseaza:
#   - data
#   - nivelul
#   - mesajul reasamblat (cu " " intre cuvinte)

# Solutie:

linie = "2026-05-09 ERROR auth user not found"
data, nivel, *mesaj = linie.split()
print(data)
print(nivel)
mesaj_reasamblat = " ".join(mesaj)
print(mesaj_reasamblat)


# 6. Inventar simplu (dict + sum + max + f-string)
# ------------------------------------------------
# Avem  stoc = {"laptop": 10, "mouse": 50, "tastatura": 25, "monitor": 7}.
# Afiseaza:
#   - numar de produse diferite
#   - total bucati pe stoc
#   - cantitatea cea mai mare

# Solutie:

stoc = {"laptop": 10, "mouse": 50, "tastatura": 25, "monitor": 7}
print(len(stoc.keys()))
print(sum(stoc.values()))
print(max(stoc.values()))

# 7. Rezultate sportive (lista de tupluri + unpacking + f-string)
# ---------------------------------------------------------------
# Avem  meciuri = [("Steaua", "Dinamo", 2, 1), ("Rapid", "CFR", 1, 1)].
# Despacheteaza primul meci si afiseaza:
#   "Steaua 2 - 1 Dinamo"
# Afiseaza si cate meciuri sunt in lista.

# Solutie:

meciuri = [("Steaua", "Dinamo", 2, 1),
           ("Rapid", "CFR", 1, 1)]
echipa1, echipa2, gol1, gol2 = meciuri[0]
print(f"{echipa1} {gol1} - {gol2} {echipa2}")
print(len(meciuri))

# 8. Skill-uri comune intre 2 useri (set + intersectie)
# ------------------------------------------------------
# Avem:
#   ana   = {"Python", "SQL", "Docker", "Linux"}
#   horia = {"Python", "Go", "SQL", "Kubernetes"}
# Afiseaza:
#   - skill-urile comune
#   - skill-urile pe care le are doar Ana
#   - cate skill-uri are fiecare

# Solutie:

ana   = {"Python", "SQL", "Docker", "Linux"}
horia = {"Python", "Go", "SQL", "Kubernetes"}
print(ana.intersection(horia))
print(ana.difference(horia))
print(len(ana), len(horia))

# 9. Status servicii (fromkeys + update)
# ---------------------------------------
# Pleaca de la o lista de servicii:
#   servicii = ["nginx", "postgres", "redis", "rabbitmq"]
# Construieste un dict cu valoarea "down" pentru toate.
# Apoi marcheaza ca "up" serviciile  "nginx" si "postgres".
# Afiseaza dict-ul.

# Solutie:

servicii = ["nginx", "postgres", "redis", "rabbitmq"]
dictionar = dict.fromkeys(servicii, "down")
print(dictionar)
dictionar.update({"nginx" : "up"})
dictionar.update({"postgres" : "up"})
print(dictionar)

# 10. Conversie agenda (lista de tupluri <-> dict)
# ------------------------------------------------
# Avem  perechi = [("ana", "0712"), ("horia", "0723"), ("george", "0734")].
# Construieste un dict `agenda`. Afiseaza:
#   - numarul Anei
#   - lista numelor (cheile)
# Apoi reverse: din dict obtine inapoi lista de tupluri (.items())

# Solutie:

perechi = [("ana", "0712"),
           ("horia", "0723"),
           ("george", "0734")]
noua_agenda = dict(perechi)
print(noua_agenda["ana"])
print(sorted(noua_agenda.keys()))
noua_lista = sorted(list(noua_agenda.items()))
print(noua_lista)

# 11. Useri logati azi (lista cu duplicate + set + sorted)
# --------------------------------------------------------
# Avem  log = ["ana", "horia", "ana", "george", "ana", "vlad", "horia"].
# Afiseaza:
#   - cate logari TOTAL
#   - useri DISTINCTI (set, sortati alfabetic)
#   - cati useri DISTINCTI

# Solutie:

log = ["ana", "horia", "ana", "george", "ana", "vlad", "horia"]
print(len(log))
print(sorted(set(log)))
log = frozenset(log)
print(log)

# 12. Reteta (dict cu lista ca valoare + len + ", ".join)
# -------------------------------------------------------
# Avem  reteta = {
#   "nume": "Tort de ciocolata",
#   "ingrediente": ["faina", "zahar", "cacao", "oua", "lapte", "unt"],
#   "timp_minute": 90,
# }
# Afiseaza un mesaj de forma:
#   "Tort de ciocolata - 6 ingrediente - 90 minute"
#   "Ingrediente: faina, zahar, cacao, oua, lapte, unt"

# Solutie:

reteta = {
  "nume": "Tort de ciocolata",
  "ingrediente": ["faina", "zahar", "cacao", "oua", "lapte", "unt"],
  "timp_minute": 90,
}

print(f"{reteta['nume']} - {len(reteta['ingrediente'])} ingrediente - {reteta['timp_minute']} minute")
print(f"Ingrediente: {reteta['ingrediente'][0]} {reteta['ingrediente'][1]} {reteta['ingrediente'][2]} {reteta['ingrediente'][3]} {reteta['ingrediente'][-2]} {reteta['ingrediente'][-1]}")


# 13. Validare email simplu (string + in + booleeni)
# --------------------------------------------------
# Avem  email = "ana@example.com".
# Afiseaza True / False pentru:
#   - contine "@"
#   - contine "."
#   - este corect (contine si "@" SI ".")
# (Folosim AND si OR - sunt operatori, nu if!)

# Solutie:

email = "ana@example.com"
print("@" in email)
print("." in email)
print("@" in email and "." in email)

# 14. Numar de cuvinte unice pe articol (dict cu set ca valoare)
# --------------------------------------------------------------
# Avem  articole = {
#   "art1": "python python web web web html",
#   "art2": "java spring spring kotlin",
# }
# Construieste un nou dict `unique_count` care leaga titlul de
# numarul de cuvinte distincte din articol.
# Sugestie:
#   {
#       "art1": len(set(articole["art1"].split())),
#       "art2": len(set(articole["art2"].split())),
#   }

# Solutie:

articole = {
  "art1": "python python web web web html",
  "art2": "java spring spring kotlin",
}

unique_count =  {
      "art1": len(set(articole["art1"].split())),
      "art2": len(set(articole["art2"].split())),
}
print(unique_count)