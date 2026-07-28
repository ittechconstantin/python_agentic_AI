#LISTE IN PYTHON   []
# =============================================================
# O LISTA este o colectie ORDONATA de elemente, in care putem
# stoca mai multe valori intr-o singura variabila.
#
# Caracteristicile listei:
#   - ORDONATA      -> elementele isi pastreaza pozitia
#   - INDEXABILA    -> fiecare element are un index (de la 0)
#   - MUTABILA      -> putem ADAUGA, MODIFICA, STERGE elemente
#   - PERMITE DUPLICATE -> putem avea aceeasi valoare de mai multe ori
#   - HETEROGENA    -> poate contine tipuri diferite de date
# =============================================================


# 1. CREAREA UNEI LISTE
# -------------------------------------------------------------
# Folosim parantezele drepte  []  si separam elementele cu virgula.

lista_goala = []
numere = [1, 2, 3, 4, 5]
fructe = ["mar", "para", "banana"]
mixt = ["mar", 1, True, [1, 2, 3, 4, 5], ["a", "b", "c"]]
duplicate = [1, 2, 2, 3, 4, 4, 4, 5, 1, 6]
print(mixt)


# 2. ACCESAREA ELEMENTELOR (indexare)
# -------------------------------------------------------------
# Indecsii incep de la 0. Indecsii negativi numara de la sfarsit.
#
#   fructe:   "mar"  "para"  "banana"
#   index:      0      1        2
#   index:     -3     -2       -1

fructe = ["mar", "para", "banana"]
print(fructe[0])
print(fructe[-1])


# 3. SLICING  [start:stop:step]
# -------------------------------------------------------------
# Construieste o LISTA NOUA cu elementele selectate.
# Functioneaza la fel ca la string-uri. stop-ul NU este inclus.

numere = [10, 20, 30, 40, 50, 60, 70]
print(numere[1:4])     # [20, 30, 40]
print(numere[:3])      # [10, 20, 30]
print(numere[::2])     # [10, 30, 50, 70]

# 4. MODIFICAREA UNUI ELEMENT
# -------------------------------------------------------------
# Spre deosebire de string, lista este MUTABILA.

fructe = ["mar", "para", "banana"]
fructe[0] = 'gutui'
print(fructe)


# 5. ADAUGARE DE ELEMENTE
# -------------------------------------------------------------
# append(x)         -> adauga x la finalul listei
# extend(iterabil)  -> adauga TOATE elementele din alta lista
# insert(i, x)      -> insereaza x pe pozitia i

lista = [1, 2, 3]
print(lista)
lista.append(4)
print(lista)           # [1, 2, 3, 4]

lista.extend([5, 6, 7])
print(lista)

lista.insert(1, [5,6,7])
print(lista)

# Diferenta intre append si extend:

# append() -> adaugam cate un singur element pe rand
# extend() -> adaugam mai multe elemente in lista dintr-o data

# 6. STERGEREA ELEMENTELOR
# -------------------------------------------------------------
# remove(x)   -> sterge PRIMA aparitie a valorii x
# pop(i)      -> sterge elementul de pe indexul i SI il returneaza
# pop()       -> sterge si returneaza ULTIMUL element
# del lista[i]-> sterge elementul de pe pozitia i (cu cuvantul cheie del)
# clear()     -> goleste lista (ramane lista goala)

fructe = ["mar", "para", "banana", "para"]

print(fructe)

fructe.remove("para")
print(fructe)

element_sters = fructe.pop(2)
print(element_sters)
print(fructe)

ultimul_element_din_lista_sters = fructe.pop()
print(ultimul_element_din_lista_sters)
print(fructe)

del fructe[0]
print(fructe)

program = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(program)
program.clear()
print(program)

# 7. LUNGIMEA UNEI LISTE
# -------------------------------------------------------------
animale = ['pisica', 'caine', 'oaie']

print(len(animale))


# 8. VERIFICARE CONTINUT: in / not in
# -------------------------------------------------------------

print('pisica' in animale)    # True
print('calut' not in animale) # True

# 9. CONCATENARE SI REPETARE
# -------------------------------------------------------------
a = [1, 2, 3]
b = [4, 5, 6]
print(a + b)  # a.extend(b) [1, 2, 3, 4, 5, 6]
print(a * 3)  # [1, 2, 3, 1 ,2 ,3 , 1, 2 ,3]

# 10. SORTAREA: sort() vs sorted()
# -------------------------------------------------------------
# sort()    -> modifica lista IN LOC (nu returneaza nimic util)
# sorted()  -> returneaza o LISTA NOUA, sortata; nu modifica originalul

numere = [1, 5, 2, 4, 3]

numere.sort() # sorteaza crescator
print(numere) # [1, 2, 3, 4, 5]

numere.sort(reverse=True) # sorteaza descrescator
print(numere)  # [5, 4, 3, 2, 1]

lista_sortata = sorted(numere)
print(lista_sortata)

# 11. INVERSARE: reverse()
# -------------------------------------------------------------
# Inverseaza ORDINEA elementelor. Modifica lista in loc.

lista =[1, 4, 2, 4, 5]
lista.reverse()
print(lista)


# 12. METODE UTILE
# -------------------------------------------------------------

numere = [10, 20, 10, 10]
print(f"Numarul de 10: {numere.count(10)}")
print(f"Indexul primei aparatii elementului 20 din lista: {numere.index(20)}")

# 13. FUNCTII INTEGRATE PE LISTE DE NUMERE
# -------------------------------------------------------------
numere = [100, 200, 400, 300, 400]

print(min(numere))
print(max(numere))
print(sum(numere))
print(sum(numere) / len(numere))


# 14. COPY: copy() vs atribuire directa
# -------------------------------------------------------------
# IMPORTANT: o lista atribuita altei variabile NU se copiaza.
# Ambele variabile arata catre ACEEASI lista din memorie.

a = [1, 2, 3]
b = a            # Nu copie- b si a sunt aceeasi lista
b.append(4)
print(a)         # [1, 2, 3, 4] s-a modificat a

# Pentru o copie reala folosim .copy():

a = [1, 2, 3]
b = a.copy()
b.append(4)
print(a)          #[1, 2, 3]
print(b)          #[1, 2, 3, 4]


# 15. CONVERSIE: list() din alte secvente
# -------------------------------------------------------------
print(list("Python"))   # ['P', 'y', 't', 'h', 'o', 'n']


# =============================================================
# CONCLUZIE
# =============================================================
# Lista este structura de baza pentru a pastra mai multe valori
# intr-o singura variabila. Retine:
#   - este MUTABILA (spre deosebire de string)
#   - acces prin index (de la 0)
#   - metode esentiale: append, extend, insert, remove, pop,
#     sort, reverse, count, index
#   - functii utile pe liste de numere: len, min, max, sum
#   - .copy() pentru o copie reala (nu doar o referinta)