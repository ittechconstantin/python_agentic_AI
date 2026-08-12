# PYTHON + MySQL  -  prima conexiune  (cu PyMySQL)
# =============================================================
# Pana acum ai scris SQL de mana, in DataGrip (sesiunea 26). Acum
# trimiti ACELASI SQL, dar DIN PYTHON - ca sa poti automatiza (import
# de date, rapoarte, o aplicatie care scrie/citeste singura in baza
# de date, fara sa stai tu cu mouse-ul in DataGrip).
#
# CERINTE ca sa ruleze:
#   pip install pymysql
#   server MySQL pornit, user 'cursant', parola 'parola123', DB 'curs'
# =============================================================

import pymysql

from session28.date import password, username

DB_CONFIG ={
    "host": "localhost",
    "port": 3306,
    "user": username,     # root
    "password": password,  # parola_voastra,
    "database": "curs"
}

# 1. CONECTARE
# -------------------------------------------------------------
# pymysql.connect(...) deschide legatura cu MySQL. `conn.cursor()` iti
# da obiectul cu care trimiti SQL si citesti rezultatele.

conn = pymysql.connect(**DB_CONFIG)
print("[ok] conexiune reusita")

# 2. CREATE TABLE  -  pornim curat la fiecare rulare
# -------------------------------------------------------------
# DE CE `with conn.cursor() as c:`?
#   Un cursor e o resursa care trebuie INCHISA dupa ce termini cu ea -
#   la fel cum inchizi un fisier deschis cu open(). `with` face asta
#   AUTOMAT la finalul blocului (chiar daca apare o eroare pe drum), asa
#   ca nu mai trebuie sa scrii tu manual `c.close()` de fiecare data.
#   Fara `with`, ai risca sa uiti cate un cursor deschis - inutil, si
#   pe termen lung poate incurca alte cereri facute pe aceeasi conexiune.

with conn.cursor() as c:
    print('intra?')
    c.execute("DROP TABLE IF EXISTS s28_useri;")
    c.execute("""
        CREATE TABLE s28_useri (
         id    INT AUTO_INCREMENT PRIMARY KEY,
         nume  VARCHAR(50) not null ,
         email VARCHAR(50),
         varsta INT
        )
        """)

print("[ok] tabela creata")

# 3. INSERT  -  cu parametri (%s), NICIODATA text lipit
# -------------------------------------------------------------
# CE E SQL INJECTION?
#   Daca lipesti direct un text primit de la user in comanda SQL (cu
#   f-string sau +), acel text poate contine BUCATI DE SQL care schimba
#   COMPLET intelesul comenzii tale. Exemplu (NU rula asta):
#
nume = "x'; DROP TABLE s28_useri; --"
#     cur.execute(f"INSERT INTO s27_useri (nume) VALUES ('{nume}')")
#
#   SQL-ul trimis efectiv la server ar deveni:
#     INSERT INTO s27_useri (nume) VALUES ('x'); DROP TABLE s27_useri; --')
#   Adica DOUA comenzi in loc de una: un INSERT nevinovat, apoi un DROP
#   TABLE care sterge toata tabela. `--` transforma restul liniei in
#   comentariu, ca sa "inghita" ghilimeaua ramasa fara pereche.
#
# SOLUTIA: parametrizarea. Pui %s ca "loc gol" in SQL si trimiti
# valorile SEPARAT, ca tuplu. Driverul le trateaza mereu ca DATE, nu ca
# bucati de comanda SQL - oricat de "rautacios" ar fi textul din ele,
# nu pot schimba structura interogarii.
#
#   GRESIT:  f"... VALUES ('{nume}', ...)"   -> risc de SQL injection
#   CORECT:  "... VALUES (%s, %s, %s)"  +  (nume, email, varsta) ca tuplu
#
# ATENTIE: dupa INSERT/UPDATE/DELETE trebuie  conn.commit(), altfel
# modificarea NU se salveaza in baza de date.




with conn.cursor() as c:
    c.execute(
       "INSERT INTO s28_useri (nume, email, varsta) VALUES (%s, %s, %s)", ("Ana Popescu", "ana@popescu.ro", 30)
    )

conn.commit()


print("[ok] s-a salvat!")

# 4. executemany  -  mai multe randuri dintr-o miscare
# -------------------------------------------------------------
# DE CE executemany, si nu un `for` cu execute() de mai multe ori?
#   Ai putea sa apelezi c.execute(...) o data pentru fiecare rand,
#   intr-un for - functioneaza, dar inseamna un "du-te-vino" separat la
#   server pentru FIECARE rand. executemany() trimite acelasi SQL cu
#   TOATE randurile deodata, intr-o singura calatorie - mai rapid, si
#   codul e mai scurt. Sintaxa e identica cu execute(), doar ca al
#   doilea argument e o LISTA de tupluri, nu un singur tuplu.

useri_noi = [
    ("Horia", "h@gmail.com", 30),
    ("Maria", "m@gmail.com", 40),
    ("Ionela", "i@gmail.com", 50),
]

with conn.cursor() as c:
    # for user in useri_noi:
    #     c.execute("INSERT INTO s28_useri (nume, email, varsta) VALUES (%s, %s, %s)", (user[0], user[1], user[2]))

    c.executemany("INSERT INTO s28_useri (nume, email, varsta) VALUES (%s, %s, %s)", useri_noi)

conn.commit()

print("[ok] s-a salvat toti userii")

# 5. SELECT  -  fetchall() (toate randurile) vs fetchone() (un rand)
# -------------------------------------------------------------
# fetchall() intoarce TOATE randurile gasite, ca un tuplu de tupluri.
# Il folosesti cand te astepti la MAI MULTE randuri.

with conn.cursor() as c:
    c.execute("SELECT * FROM s28_useri;")
    toti_userii = c.fetchall()
    for user in toti_userii:
        print(user)      #(1, 'Ana Popescu', 'ana@popescu.ro', 30) un tuplu per rand


# fetchone() intoarce UN SINGUR rand (urmatorul disponibil), sau None
# daca nu mai e niciunul. Il folosesti cand stii ca rezultatul e UN
# SINGUR rand/o singura valoare - de exemplu un COUNT(*), sau o
# cautare dupa o coloana UNIQUE (aici, email).

with conn.cursor() as c:
    c.execute("SELECT * FROM s28_useri LIMIT 1;")

    utilizator_curent = c.fetchone()   # un tuplu cu primul rand intalnit, altfel NONE
    if utilizator_curent:
        ...
        # login

# 6. UPDATE
# -------------------------------------------------------------

# nume=input("Introduceti numele pentru care vreti modificata varsta: ")
# noua_varsta = int(input("Introduceti noua varsta: "))
#
# with conn.cursor() as c:
#     c.execute("UPDATE s28_useri SET varsta=%s WHERE nume=%s", (noua_varsta, nume))
#
# conn.commit()

# 7. DELETE
# -------------------------------------------------------------
with conn.cursor() as c:
    c.execute("DELETE FROM s28_useri WHERE nume = %s", ("Horia", ))

conn.commit()

# 8. INCHIDERE
# -------------------------------------------------------------
# Cand termini, inchizi conexiunea - la fel cum inchizi un fisier
# dupa ce ai citit din el.

conn.close()



# =============================================================
# DE RETINUT
# =============================================================
# - pymysql.connect(**DB_CONFIG)     -> deschide conexiunea
# - with conn.cursor() as cur:       -> cursorul trimite SQL
# - cur.execute(sql, parametri)      -> %s + tuplu, NICIODATA text lipit
# - cur.executemany(sql, lista)      -> acelasi INSERT/UPDATE, mai multe randuri odata
# - cur.fetchall() / cur.fetchone()  -> citesti rezultatul unui SELECT
# - conn.commit()                    -> OBLIGATORIU dupa INSERT/UPDATE/DELETE
# - conn.close()                     -> inchizi conexiunea la final
#
# Exersare: 28.1.exercise.py si 28.2.exercise.py
# =============================================================