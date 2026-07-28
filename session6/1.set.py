# SET-URI IN PYTHON   {}
# =============================================================
# Un SET este o colectie de elemente UNICE, NEORDONATA.
# Inspirata din matematica (multimi): {1, 2, 3}.
#
# Caracteristicile set-ului:
#   - ELEMENTE UNICE     -> duplicatele sunt IGNORATE automat
#   - NEORDONAT          -> NU avem index, NU exista set[0]
#   - MUTABIL            -> putem .add() si .remove()
#   - ELEMENTELE IMUTABILE -> doar string, numere, bool, tupluri
#                            (NU putem pune liste sau dicturi intr-un set)
#   - operatii rapide de UNIUNE, INTERSECTIE, DIFERENTA
#
# Cand folosim un set in IT?
#   - eliminare DUPLICATE dintr-o lista (emails, IP-uri, useri)
#   - verificare rapida de APARTENENTA  (este X in lista permisa?)
#   - skill-uri / tag-uri / permisiuni
#   - useri online / offline / nou aparuti
#   - useri activi azi vs ieri (cine a venit, cine a plecat)
# =============================================================


# 1. CREAREA UNUI SET
# -------------------------------------------------------------
# -------------------------------------------------------------
# Folosim acolade  { }  cu elementele separate prin virgula.
# ATENTIE:  {}  inseamna  DICT GOL, NU set gol !
# Pentru set gol folosim functia  set().

set_gol = set()      # un set gol
nu_este_set = {}     # ATENTIE! ESTE UN DICT GOL !

print(set_gol)

emailuri = {'a@x.com', 'b@x.com', 'c@x.com'}
print(emailuri)
mixt = {"server", 80, True, (1, 2), 1}   # Cand aveti True si 1 in set unul din elemente va fi eliminat la fel si pentru False
print(len(mixt))
print(mixt)


# 2. DUPLICATELE SUNT IGNORATE AUTOMAT
# -------------------------------------------------------------
# Aceasta este "super-puterea" set-ului.

ips = {'192.168.1.1', '192.168.1.1', '192.168.1.2'}
print(len(ips))
print(ips)

# 3. CONVERSIE LISTA -> SET   (deduplicare)
# -------------------------------------------------------------
# Cea mai simpla metoda de a elimina duplicatele dintr-o lista.

useri_logati = ['ana', 'vlad', 'ana', 'vlad', 'maria']
unici = set(useri_logati)   # {'ana', 'vlad', 'maria'}
lista_unici = list(unici)   # ['ana', 'vlad', 'maria']
print(lista_unici)


# Daca vrem o LISTA fara duplicate (eventual sortata):
lista_unica_sortata = sorted(set(useri_logati))
print(lista_unica_sortata)


# 4. SET-UL ESTE NEORDONAT  -  NU exista index !
# -------------------------------------------------------------
# Spre deosebire de lista / tuplu / string, NU putem face set[0].

# s = {'a', 'b', 'c'}
# print(s[0])    # TypeError


# 5. ADAUGAREA: .add()  si  .update()
# -------------------------------------------------------------
# .add(x)            -> adauga UN element. Daca exista deja, nu se intampla nimic.
# .update(iterabil)  -> adauga MAI MULTE elemente dintr-o lista / set / tuplu

permisuni = {'read'}
print(permisuni)
print(type(permisuni))

permisuni.add('write')
permisuni.add('read')
print(permisuni)

permisiuni_noi=['delete', 'execute', 'read']
permisuni.update(permisiuni_noi)
print(permisuni)



# 6. STERGEREA: .remove(), .discard(), .pop(), .clear()
# -------------------------------------------------------------
# .remove(x)   -> sterge x. EROARE daca nu exista.
# .discard(x) -> sterge x daca exista. NU da eroare daca nu exista.
# .pop()       -> sterge un element ALEATOR si il returneaza.
# .clear()     -> goleste set-ul.

permisuni = {'read', 'write', 'delete', 'execute', 'stop'}

permisuni.remove('write')
permisuni.discard('read')
element_sters_aleatoriu = permisuni.pop()
print(permisuni)
print(element_sters_aleatoriu)
permisuni.clear()
print(permisuni)

# 7. LUNGIME si APARTENENTA:  len, in, not in
# -------------------------------------------------------------
# Verificarea  in  pe set este FOARTE rapida (mult mai rapida ca pe lista).

emailuri_blocate = {'spam@x.com', "no-reply@x.com", "bot@x.com"}
print(len(emailuri_blocate))
print('spam@x.com' in emailuri_blocate)     # True
print('spa@x.com' not in emailuri_blocate)  # True
print('bot@x.com' not in emailuri_blocate)  # False



# 8. OPERATII DE MULTIME (cele mai utile facilitati ale set-ului)
# -------------------------------------------------------------
# Avem doi useri si skill-urile lor:

ana = {'Python', 'SQL', 'Docker', 'Linux'}
george = {'Python', 'Go', 'SQL', 'Kubernetes'}


# UNIUNE  -  toate skill-urile reunite
# Operator:  |        Metoda:  .union(iterabil)

print(ana | george)
print(ana.union(george))

# INTERSECTIE  -  skill-uri pe care le AU AMBII
# Operator:  &        Metoda:  .intersection(iterabil)

print(ana & george)
print(ana.intersection(george))

# DIFERENTA  -  skill-uri pe care le are ANA, dar nu si GEORGE
# Operator:  -        Metoda:  .difference(iterabil)
print('DIFERENTA')
print(ana - george)
print(ana.difference(george))


print('DIFERENTA SIMETRICA')
# DIFERENTA SIMETRICA  -  skill-uri "exclusive" (doar la unul, nu la amandoi)
# Operator:  ^        Metoda:  .symmetric_difference(iterabil)

print(ana ^ george)
print(ana.symmetric_difference(george))


# Intersectie set si lista

a = {1, 2}
b = [3, 4]

# print(a | b)
print(a.union(b))

# 9. CONVERSII
# -------------------------------------------------------------
# Putem trece intre  set / list / tuple / string  in ambele sensuri.


print(set([1, 2, 3, 3, 4]))    # {1, 2, 3, 4}
print(set((1, 2, 3, 3, 4)))    # {1, 2, 3, 4}
print(set('abcABC'))           # {'a', 'b', 'c', 'A', 'B', 'C'} - separa fiecare caracter din string si va prelua litere UNICE


# 10. FROZENSET  -  varianta IMUTABILA a set-ului
# -------------------------------------------------------------
# La fel ca setul, dar NU poate fi modificat (.add, .remove nu exista).
# Avantaj:  poate fi folosit ca CHEIE in dict sau element in alt set.

f = frozenset(['write', 'read', 'delete'])
print(f)
# f.add('execute')
# f.remove('read')
# print(f)
# =============================================================
# CONCLUZIE
# =============================================================
# Set-ul:  { "a", "b", "c" }
#   - colectie de elemente UNICE, NEORDONATA
#   - set gol se face cu  set()  -  NU cu  {}
#   - NU are index   (nu se poate set[0])
#   - .add, .remove, .discard, .pop, .clear, .update
#   - operatii de multime:  |  &  -  ^   (uniune, intersectie,
#     diferenta, diferenta simetrica)
#   - util la: deduplicare, comparari intre colectii, apartenenta rapida
#   - frozenset = set imutabil, poate fi cheie in dict