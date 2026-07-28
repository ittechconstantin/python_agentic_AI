# TUPLURI IN PYTHON   ()
# =============================================================
# Un TUPLU (tuple) este o colectie ORDONATA de valori, foarte
# asemanatoare cu o lista, cu o diferenta esentiala:
# tuplul este IMUTABIL - odata creat, NU mai poate fi modificat.
#
# Caracteristicile tuplului:
#   - ORDONAT       -> elementele isi pastreaza pozitia
#   - INDEXABIL     -> acces prin index, ca la liste / string-uri
#   - IMUTABIL      -> nu se mai poate adauga / modifica / sterge
#   - PERMITE DUPLICATE
#   - HETEROGEN     -> poate avea tipuri diferite
#   - HASHABIL      -> il putem folosi ca CHEIE intr-un dict
#                      (atata timp cat elementele lui sunt tot imutabile)
#
# Cand folosim un tuplu in IT?
#   - coordonate           (x, y)
#   - culori RGB           (255, 100, 0)
#   - server               (host, port)
#   - versiune semantica   (major, minor, patch)
#   - inregistrari fixe    (nume, email, varsta)
#   - chei compuse in dict (tara, oras) -> populatie
# =============================================================


# 1. CREAREA UNUI TUPLU
# -------------------------------------------------------------
# Folosim PARANTEZE ROTUNDE  ( )  si separam elementele cu virgula.

tuplu_gol = ()
coord = (10, 20)
mixt = ("server", 8080, True)

# Atentie la TUPLUL CU UN SINGUR ELEMENT - virgula este OBLIGATORIE:
nu_e_tuplu = (5)    # int
e_tuplu = (5,)      # tuplu ! ATENTIE, PUNE VIRGULA


# Putem omite parantezele - virgula e cea care face tuplul.
# Asta se numeste "tuple packing":

versiune = 4, 3, 2
print(versiune, type(versiune))

# 2. ACCESARE PRIN INDEX (la fel ca la liste si string-uri)
# -------------------------------------------------------------
#   server:  "10.0.0.1"   8080   "online"
#   index:       0          1        2
#   index:      -3         -2       -1

server = ("10.0.0.1", 8080, "online")
print(server[0])


# 3. SLICING  [start:stop:step] ->
# -------------------------------------------------------------
# Functioneaza identic cu lista / string. Stop-ul NU este inclus.

print(server[1:2])
print(server[::-1])

# 4. IMUTABILITATEA - NU se poate modifica
# -------------------------------------------------------------
# Aceasta este DIFERENTA majora fata de lista.
coord = (10, 20)
# coord[0] = 20   # TYPERROR: 'tuple' object does not support item assignment


# Atentie: daca un tuplu CONTINE o lista, lista DIN INTERIOR poate
# fi modificata - dar tuplul in sine ramane "acelasi tuplu".

mixt = ("user", [1, 2, 3], True, ('a', 'b', 'c'))
print(mixt)
mixt[1].append(4)
print(mixt)


# 5. CONCATENARE  +   si REPETARE  *
# -------------------------------------------------------------
# Nu modifica tuplul original - construiesc UN TUPLU NOU.

a = (1, 2, 3)
b = (4, 5, 6)
c = a + b
print(c)
d = a * 3
print(d)

# 6. LUNGIME, SUMA, MIN, MAX
# -------------------------------------------------------------
numere = (1, 2, 3, 4, 5)
print(len(numere))
print(sum(numere))
print(min(numere))
print(max(numere))


# 7. METODE DISPONIBILE: count() si index()
# -------------------------------------------------------------
# Tuplul are DOAR 2 metode (fiind imutabil, nu are append/pop/etc.):
#   count(x)  -> de cate ori apare x
#   index(x)  -> indexul PRIMEI aparitii a lui x
t = (1, 2, 3, 2, 4, 5, 2, 6)
print(t.count(2))
print(t.index(2))


# 8. VERIFICAREA APARTENENTEI:  in / not in
# -------------------------------------------------------------
permisiuni = ('read', 'write', 'execute')
print('read' in permisiuni)        # True
print('delete' in permisiuni)      # False


# 9. UNPACKING  -  scoatem valorile in variabile
# -------------------------------------------------------------
# Aceasta este una dintre cele mai utile facilitati din Python.

coord = (10, 20)
x, y  = coord
print(x, y)  # 10 20

server = ("10.0.0.1", 8080, "online")
host, port, status = server


# Numarul de variabile TREBUIE sa fie egal cu numarul de elemente.


# 10. SWAP DE VARIABILE  -  truc clasic Python
# -------------------------------------------------------------
# Putem schimba intre ele valorile a doua variabile pe un rand:
a = 5
b = 10
a, b = b, a
print(a, b)    # 10 5

# 11. UNPACKING CU  * (rest)
# -------------------------------------------------------------
# Daca avem mai multe elemente decat variabile, putem prinde "restul"
# intr-o lista cu prefixul *.

prima, *restul = (1, 2, 3, 4, 5)
print(prima)  # 1
print(restul) # [2, 3, 4, 5]

prima, *mijloc, ultima = (1, 2, 3, 4, 5)
print(prima)    # 1
print(mijloc)   # [2, 3, 4]
print(ultima)   # 5

# 12. CONVERSII
# -------------------------------------------------------------
# Putem converti intre lista si tuplu in ambele sensuri.

lista = [1, 2, 3]
t = tuple(lista)
print(t)

t = (10, 20, 30)
lista = list(t)
print(lista)


# 13. TUPLUL CA ELEMENT INTR-O LISTA  (lista de inregistrari)
# -------------------------------------------------------------
# Folosit foarte des pentru a stoca "randuri" - inregistrari fixe.

useri = [
    ('George', 'george@gmail.com', 'admin'),
    ('Maria', 'maria@gmail.com', 'editor'),
    ('Ionela', 'ionela@gmail.com', 'user'),
]

print(useri[1][0])
print(useri[1][2])
# Unpacking direct din inregistrare:
nume, email , rol = useri[0]
print(nume, email, rol)

# 14. TUPLUL CA CHEIE IN DICTIONAR
# -------------------------------------------------------------
# Tuplul este HASHABIL (daca elementele lui sunt imutabile),
# deci poate fi cheie. Lista NU poate fi cheie.

# Cheie compusa: (tara, oras) -> populatie

populatii = {
    ("RO", "Cluj"):        325000,
    ("RO", "Bucuresti"):  1716000,
    ("DE", "Berlin"):     3700000,
    ("DE", "Munchen"):    1488000,
}

print(populatii[("RO", "Cluj")])

# Coordonate ca cheie - util in jocuri / harti / grid-uri:


# 15. SORTARE SI ALTE TRUCURI CU TUPLURI
# -------------------------------------------------------------
# Cand sortam o lista de tupluri, Python sorteaza intai dupa primul
# element, apoi dupa al doilea (lexicografic).

versiuni = [(1, 2, 0), (1, 0, 9), (2, 0, 0), (1, 2, 5)]
versiuni_sortate = sorted(versiuni)
print(versiuni_sortate)

# Putem sorta dupa un anumit element folosind  key=lambda:
preturi  = [('laptop', 4500), ('mouse', 79), ('monitor', 1200), ('tastatura', 199)]
preturi_sortate = sorted(preturi, key=lambda x: x[1])
print(preturi_sortate)


# 16. DE CE FOLOSIM TUPLU IN LOC DE LISTA?
# -------------------------------------------------------------
# 1) IMUTABILITATEA -> garantia ca datele nu se schimba "din greseala".
# 2) Poate fi CHEIE intr-un dict / element intr-un set.
# 3) Mai rapid decat lista la creare si parcurgere.
# 4) Comunica intentia: "asta e o inregistrare fixa" - nu o colectie
#    care va creste / scadea.
#
# Regula simpla:
#   - colectie CARE SE MODIFICA  -> lista
#   - inregistrare FIXA          -> tuplu


# =============================================================
# CONCLUZIE
# =============================================================
# Tuplul:  ( 1, 2, 3 )
#   - acces prin index, slicing, in / not in   (ca la lista)
#   - len, sum, min, max
#   - metode disponibile: doar  count()  si  index()
#   - IMUTABIL - nu putem schimba elementele
#   - se poate UNPACKING:    a, b, c = (1, 2, 3)
#   - se poate folosi ca CHEIE in dict / element in set
#   - "tuplu cu un singur element"  trebuie virgula:  (5,)
# =============================================================