# LAMBDA, MAP, FILTER, ZIP
# =============================================================
#
#   - lambda   ->  o functie SCURTA scrisa pe o singura linie
#   - map      ->  APLICA o functie pe FIECARE element dintr-o lista
#   - filter   ->  PASTREAZA doar elementele care trec o conditie
#   - zip      ->  IMPERECHEAZA elementele din mai multe liste
#
# Cand le folosim?
#   - filtrare de date (useri activi, comenzi neonorate, log-uri ERROR)
#   - sortare dupa un criteriu personalizat (cel mai scump, cel mai recent)
#   - combinare a doua liste paralele (nume + email -> dict)
# =============================================================


# =============================================================
# 1. LAMBDA
# =============================================================
# Forma:
#   lambda argumente: expresie
#
# Ne da o functie scurta, "din zbor", folosita de obicei ca
# argument pentru alte functii (sorted, max, min, map, filter).

dublu = lambda x: x * 2
print(dublu(5))

suma = lambda x, y: x + y
print(suma(5, 6))

# =============================================================
# 2. SORTAT / MAX / MIN CU "KEY"  -  primul uz real al lambda
# =============================================================
# Multe functii built-in accepta un argument `key`: o functie
# care primeste un element si returneaza valoarea dupa care
# se face comparatia.

nume = ["ana", "maria", "Lucia", "ioana", "Cristina"]

# Sortare clasica - alfabetica:
print(sorted(nume))

# Sortare CASE-INSENSITIVE - dupa varianta lowercase:
print(sorted(nume, key= lambda x: x.lower()))

# Sortare dupa LUNGIME:
print(sorted(nume, key= lambda x: len(x)))

# Max / min cu lambda:
produse = [
    {"nume": "laptop", "pret": 4500, 'cantitate': 10},
    {"nume": "monitor", "pret": 1200, 'cantitate': 20},
    {"nume": "tableta",  "pret": 100,  'cantitate': 2}
]

# Cel mai scump produs:
print(max(produse, key= lambda y: y["cantitate"]))

# Cel mai ieftin:
print(min(produse, key= lambda q: q['pret']))


# =============================================================
# 3. MAP  -  TRANSFORMA fiecare element dintr-o lista
# =============================================================
# Forma:
#   map(functie, iterabil)
#
# Returneaza un obiect "map" (iterator). Daca vrem o lista
# clasica trebuie sa il convertim cu list(...).

# Dublam fiecare numar dintr-o lista:
numere = [1, 2, 3, 4, 5]
print(list(map(lambda x: x * 2, numere)))

# Aplicam TVA (21%) pe o lista de preturi:
preturi = [100, 200, 350, 1000]
preturi_cu_tva = list(map(lambda x: x * 1.21, preturi))
print(preturi_cu_tva)

# Convertim nume la majuscule:
nume = ["ana", "maria", "george"]
nume_majuscule = list(map(lambda name: name.upper(), nume))
print(nume_majuscule)

# Map cu o functie built-in (fara lambda):
texte = ["7", "42", "100", "3"]
integers = list(map(int, texte))
print(integers)

# =============================================================
# 4. FILTER  -  PASTREAZA elementele care trec o conditie
# =============================================================
# Forma:
#   filter(functie, iterabil)
#
# Functia trebuie sa returneze True / False.
# Daca returneaza True -> elementul ramane.
# Daca returneaza False -> elementul e exclus.

# Pastram doar numerele pare:
numere = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numere_pare = list(filter(lambda x: x % 2== 0, numere))
print(numere_pare)

# Doar produsele peste 100 lei:
preturi = [100, 200, 350, 1000]
preturi_peste_100 = list(filter(lambda x: x > 100, preturi))

# Doar nume cu mai mult de 3 litere:
words = ["ana", "maria", "george", "alex", "bogdan"]
lungime_mai_mare_3 = list(filter(lambda z: len(z) > 3, words))
print(lungime_mai_mare_3)
# Doar useri activi din lista de dict-uri:
useri = [
    {'nume': 'Ana',    'activ': True},
    {'nume': 'Mircea', 'activ': False},
    {'nume': 'George', 'activ': True},
    {'nume': 'Maria',  'activ': True},
]

activi = list(filter(lambda z: z['activ'], useri))
print(activi)

# =============================================================
# 5. ZIP  -  IMPERECHEAZA elemente din mai multe liste
# =============================================================
# Forma:
#   zip(lista1, lista2, ...)
#
# Returneaza un iterator de TUPLURI: (l1[0], l2[0]), (l1[1], l2[1]), ...
# Daca listele au lungimi diferite, se opreste la cea mai scurta.
# Folosim list(...) sau dict(...) pentru a obtine o structura clasica.

# Impereckere clasica - nume si varste:

nume = ['Ana', 'Vlad', 'George']
varsta =[30, 35, 40]


list_perechi = list(zip(nume, varsta))
print(list_perechi)

# Construim un dict din doua liste paralele:
dict_perechi = dict(zip(nume, varsta))
print(dict_perechi)

# Zip cu TREI liste:

nume = ['Ana', 'Vlad', 'George']
varsta =[30, 35, 40]
judete = ['Bucuresti', 'Cluj-Napoca', 'Iasi']

list_perechi = list(zip(nume, varsta, judete))
print(list_perechi)


# Zip cu lungimi diferite -> se opreste la cea mai scurta:

a = [1, 2, 3, 4, 5]
b = ['x', 'y', 'z']

print(list(zip(a, b)))


# =============================================================
# CONCLUZIE
# =============================================================
# Retine:
#   - lambda argumente: expresie    ->  functie scurta, pe o linie
#   - map(f, iter)                  ->  aplica f pe fiecare element
#   - filter(f, iter)               ->  pastreaza unde f -> True
#   - zip(a, b, ...)                ->  imperecheaza element cu element
#
# Toate cele 3 (map, filter, zip) returneaza ITERATOARE, deci
# de obicei le convertim cu list(...) sau dict(...) pentru a vedea
# rezultatul. Lambda este "lipiciul" care le face usor de folosit:
# scriem functia DIRECT in apel, fara sa-i dam un nume.