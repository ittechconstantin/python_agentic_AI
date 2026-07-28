# DICTIONARE IN PYTHON   {}
# =============================================================
# Un DICTIONAR (dict) este o colectie de perechi  CHEIE: VALOARE.
# Practic, este o "agenda": pentru fiecare CHEIE (ex: un username)
# avem o VALOARE asociata (ex: adresa de email).
#
# Caracteristicile dictionarului:
#   - PERECHI cheie:valoare   ->  acces rapid dupa cheie
#   - CHEILE sunt UNICE       ->  o cheie nu se poate repeta
#   - CHEILE sunt IMUTABILE   ->  string, int, float, bool, tuplu
#   - VALORILE sunt orice     ->  numere, string, lista, alt dict, etc.
#   - MUTABIL                 ->  putem adauga / modifica / sterge
#   - ORDONAT (din Python 3.7)->  pastreaza ordinea de inserare
#
# Cand folosim un dict in viata reala (IT) ?
#   - configurare aplicatie       (host, port, debug, timeout)
#   - profil utilizator           (username, email, rol)
#   - raspuns de la un API        (status, data, message)
#   - coduri de eroare            (404 -> "Not Found")
#   - inventar / stoc de produse  (nume_produs -> cantitate)
# =============================================================


# 1. CREAREA UNUI DICTIONAR
# -------------------------------------------------------------
# Folosim acolade { }  si separam perechile cu virgula.
# Fiecare pereche are forma:    cheie: valoare

dict_gol = {}
print(dict_gol)

user = {
    'username': 'horia',
    'email': 'horia.scurtu@itschool.ro',
    'varsta': 30,
    'activ': True
}
print(user)

# Putem crea un dict si cu functia dict() din perechi:

user = dict(username = 'horia', email = 'horia.scurtu@itschool.ro')
print(user)


# 2. ACCESAREA VALORILOR PRIN CHEIE
# -------------------------------------------------------------
# Punem cheia intre paranteze drepte:   dict[cheie]
# Daca cheia NU exista -> eroare KeyError.

user = {
    'username': 'horia',
    'email': 'horia.scurtu@itschool.ro',
    'varsta': 30,
    'activ': True
}
print(user['username'])


# 3. ACCESARE SIGURA CU .get()
# -------------------------------------------------------------
# .get(cheie)             -> valoarea cheii sau None daca lipseste
# .get(cheie, default)    -> valoarea cheii sau "default" daca lipseste
#
# Avantaj: NU produce eroare daca cheia nu exista.

print(user.get('username'))   # horia
print(user.get('age'))        # None
print(user.get('age', "Nu exista varsta"))  # Nu exista cheia

# 4. MODIFICAREA UNEI VALORI
# -------------------------------------------------------------
# Atribuim o valoare noua unei chei deja existente.

user['username'] = 'Horia'  # noua valoarea pentru cheia "username" va fi 'Horia'
print(user)

# 5. ADAUGAREA UNEI CHEI NOI
# -------------------------------------------------------------
# Daca atribuim o valoare unei chei care NU exista, ea este ADAUGATA.

user['rol'] = 'super_admin'
print(user)


# 6. STERGEREA UNEI CHEI
# -------------------------------------------------------------
#   pop(cheie)            -> sterge cheia SI returneaza valoarea ei
#   pop(cheie, default)   -> daca lipseste, returneaza default (fara eroare)
#   popitem()             -> sterge ULTIMA pereche adaugata si o returneaza
#   del dict[cheie]       -> sterge cheia (cu cuvantul cheie del)
#   clear()               -> goleste dict-ul

server = {'host': 'localhost', 'port': 8080, 'debug': True}
print(server)
server.pop('debug')
print(server)

valoare_stearsa  = server.pop('debug', 'Nu exista')
print(valoare_stearsa)

ultima_pereche = server.popitem()
print(ultima_pereche)
print(server)

del server['host']
print(server)

server.clear()
print(server)

# 7. LUNGIMEA DICTIONARULUI
# -------------------------------------------------------------
# len() returneaza numarul de PERECHI (chei).

user = {
    'username': 'horia',
    'email': 'horia.scurtu@itschool.ro',
    'varsta': 30,
    'activ': True
}

print(f"Numarul de elemente din dictionar este: {len(user)}")

# 8. VERIFICAREA EXISTENTEI UNEI CHEI:  in / not in
# -------------------------------------------------------------
# IMPORTANT: "in" verifica DOAR cheile, NU si valorile.

permisiuni = {'read': True, 'scris': False, 'delete': True}

print('read' in permisiuni)          # True
print('delete' not in permisiuni)    # False



# 9. METODELE .keys(), .values(), .items()
# -------------------------------------------------------------
#   .keys()    -> obiect cu toate CHEILE
#   .values()  -> obiect cu toate VALORILE
#   .items()   -> obiect cu toate PERECHILE  (cheie, valoare)
#
# Putem converti la list() daca vrem o lista clasica.

permisiuni = {'read': True, 'scris': False, 'delete': True}
print(permisiuni.keys())
print(permisiuni.values())
print(permisiuni.items())

# 10. ACTUALIZARE / FUZIONARE: .update()
# -------------------------------------------------------------
# .update(alt_dict)  -> adauga / suprascrie chei dintr-un alt dict.
# Cheile existente se actualizeaza, cele noi se adauga.

config = {'host': 'localhost', 'port': 8080, 'debug': True}
config.update({'port': 9000, 'timeout': 30})
config.update({'os': 'Linux', 'db': 'PostgreSQL'})
print(config)


# 11. OPERATORUL  |   (Python 3.9+)  -  fuzionare cu dict NOU
# -------------------------------------------------------------
# a | b  -> dict NOU cu toate cheile din a si b (in caz de conflict
#          castiga b - cel din dreapta).


a = {'host': 'localhost', 'port': 8080, 'debug': True}
b = {'port': 9000, 'timeout': 30}
c = a | b
print(c)


# 12. COPIEREA UNUI DICTIONAR
# -------------------------------------------------------------
# La fel ca la liste: atribuirea NU copiaza, ambele variabile
# arata catre acelasi dict din memorie.

a = {'x': 1, 'y': 2}
b = a               # NU copiaza, a si b sunt acelasi dict
b['z'] = 3
print(a)            # {'x': 1, 'y': 2, 'z': 3}
print(b)            # {'x': 1, 'y': 2, 'z': 3}


# Pentru o copiere reala
a = {'x': 1, 'y': 2}
b = a.copy()
b['z'] = 3
print(a)               #{'x': 1, 'y': 2}
print(b)               #{'x': 1, 'y': 2, 'z': 3}

# 13. .setdefault()  -  citeste sau seteaza la o valoare implicita
# -------------------------------------------------------------
# Daca cheia EXISTA -> returneaza valoarea ei.
# Daca cheia NU exista -> o ADAUGA cu valoarea data si o returneaza.


profile = {'username': 'horia'}
email = profile.setdefault('email', 'adresa_default@gmail.com')
print(email)


# 14. FROMKEYS  -  dict cu chei dintr-o lista, toate cu aceeasi valoare
# -------------------------------------------------------------
# Util pentru a initializa contoare sau flag-uri pentru o lista de chei.

servicii = ['nginx', 'postgresql', 'redis']
status = dict.fromkeys(servicii, 'down') # in variabila status definesc un dict cu cheiele din lista servicii iar ca valoare va fi 'down' pentru toate
print(status)

# 15. DICTIONARE IMBRICATE  (nested dict)
# -------------------------------------------------------------
# Valoarea unei chei poate fi LA RANDUL EI un dict (sau o lista).
# Asa modelam structuri reale: useri cu adresa, raspuns API etc.

user = {
    'username': 'horia',
    'email': 'horia@gmail.com',
    'adresa': {
        'oras': 'Bucuresti',
        'strada': 'Strada Mihai Eminescu',
        'cod_postal': '010011'
    },
    'limbaje': ['Python', 'Go', 'SQL']
}

# Vreau sa accesez orasul
print(user['adresa']['oras'])    # Bucuresti
print(user['limbaje'][0])        # Python


# 16. EXEMPLU PRACTIC: RASPUNS DE LA UN API
# -------------------------------------------------------------
# Aproape orice raspuns JSON dintr-un API este un dictionar.

response = {
    'status': 200,
    'data': {
        'id': 1,
        'name': 'George Popescu',
        'roles': ['admin', 'editor']
    }
}

# 200
print(response['status'])
# editor
print(response['data']['roles'][1])


# 17. CONVERSII UTILE
# -------------------------------------------------------------
# Putem construi un dict dintr-o LISTA DE TUPLURI (cheie, valoare):

perechi = [("host", "localhost"), ("port", 8080), ("debug", True)]
config = dict(perechi)
print(config)


# 18. AFISARE FRUMOASA CU f-string
# -------------------------------------------------------------
# Cand vrem sa generam mesaje pe baza unui dict, folosim f-string-uri.

print(f"Username: {user['username']}")

# Combinam dict cu liste si string-uri pentru rapoarte rapide:

stoc = {'mouse': 50, 'laptop': 10, 'tastatura': 25, 'monitor': 7, 'casti': 0}

print(f"Numarul de produse in magazin:{len(stoc)}")
print(f"Total bucati: {sum(stoc.values())}")
print(f"Cea mai mare cantitate: {max(stoc.values())}")
print(f"Cea mai min cantitate: {min(stoc.values())}")

# =============================================================
# CONCLUZIE
# =============================================================
# Dictionarul este structura de baza pentru a asocia o CHEIE
# cu o VALOARE. Retine:
#   - { "cheie": valoare, ... }
#   - acces rapid prin    dict[cheie]    sau    dict.get(cheie)
#   - cheile sunt UNICE si IMUTABILE (string, numar, tuplu)
#   - metode esentiale: .get, .keys, .values, .items, .update,
#     .pop, .popitem, .clear, .copy, .setdefault, .fromkeys
#   - "in" verifica CHEILE, nu valorile
#   - dictionarele se imbrica natural si modeleaza foarte bine
#     date din IT: configuratii, useri, raspunsuri API, JSON.
# =============================================================