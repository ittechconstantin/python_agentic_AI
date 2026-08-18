# EXERCITIUL 2  (PYTHON + MySQL)  -  BIBLIOTECA PERSONALA
# =============================================================
#
# CONTEXT (caz real)
# ------------------
# Tii evidenta cartilor tale si a cui le-ai imprumutat, in DOUA
# tabele MySQL legate printr-un FOREIGN KEY (ca la useri/comenzi
# din sesiunea 26):
#
#   ex29_carti        - cartile pe care le detii
#   ex29_imprumuturi  - cine si cand a imprumutat o carte
#
# Fiecare imprumut are un `carte_id` care ARATA spre `id`-ul din
# ex29_carti - exact "trimiterea" despre care s-a discutat la FK.
# Aici, in plus fata de exercitiile anterioare, o functie va trebui
# sa faca un JOIN intre cele doua tabele, ca sa afle NUMELE cartii,
# nu doar id-ul ei.
#
# Codul de PREGATIRE (conexiune + creare tabele + date DEMO) e deja
# scris mai jos - tu completezi doar functiile din ZONA TA DE LUCRU.
#
#
# CE AI DE FACUT
# --------------
# Scrie 4 functii:
#
# 1. nr_carti_disponibile(conn)
#       -> cate carti au disponibila = TRUE, in total.
#
# 2. carti_dupa_autor(conn, autor_fragment)
#       -> TITLURILE cartilor al caror autor CONTINE `autor_fragment`
#          (foloseste LIKE), ordonate alfabetic dupa titlu.
#
# 3. imprumuta_carte(conn, titlu, imprumutat_de, data_imprumut)
#       -> cauta cartea dupa titlu (potrivire EXACTA).
#          - daca NU exista o carte cu acel titlu -> return False
#            (nu modifici nimic)
#          - daca exista, dar disponibila = FALSE (e deja
#            imprumutata) -> return False (nu modifici nimic)
#          - daca exista si e disponibila -> adauga un rand nou in
#            ex29_imprumuturi (carte_id, imprumutat_de, data_imprumut),
#            SETEAZA disponibila = FALSE pe cartea respectiva,
#            face commit, si returneaza True.
#          data_imprumut e text 'AAAA-LL-ZZ', ex: '2026-06-01'.
#
# 4. istoric_imprumuturi(conn, titlu)
#       -> foloseste JOIN intre ex29_carti si ex29_imprumuturi ca sa
#          gasesti NUMELE persoanelor (`imprumutat_de`) care au
#          imprumutat cartea cu titlul dat, ordonate CRESCATOR dupa
#          data_imprumut (cea mai veche cerere prima).
#
#
# CERINTE
# -------
#   - foloseste  cur.execute(SQL, (param,))  cu  %s  (parametrizare!)
#   - la INSERT/UPDATE nu uita  conn.commit()
#   - pentru un singur rezultat (ex: id-ul unei carti):  cur.fetchone()
#     - ATENTIE: daca nu exista niciun rand, fetchone() intoarce None -
#       verifica asta INAINTE sa incerci sa citesti fetchone()[0]
#   - la punctul 2, tiparul LIKE se construieste in Python:
#       f"%{autor_fragment}%"
#     si se trimite CA PARAMETRU (nu lipit direct in SQL)
#   - la punctul 3, ai nevoie de DOUA comenzi separate: mai intai un
#     SELECT ca sa afli id-ul si disponibilitatea cartii, apoi (doar
#     daca se poate imprumuta) un INSERT si un UPDATE
#   - la punctul 4, JOIN se scrie ca in 26.teorie.sql:
#       FROM ex29_imprumuturi i JOIN ex29_carti c ON c.id = i.carte_id
#
#
# OUTPUT ASTEPTAT (din codul de test de mai jos)
# ----------------------------------------------
#   disponibile (initial): 4
#   dupa autor 'Orwell': ['1984']
#   imprumuta '1984' catre Ana: True
#   disponibile (dupa imprumut): 3
#   imprumuta 'Dune' catre Georgeta (deja imprumutata): False
#   imprumuta 'Carte Inexistenta' catre Vlad: False
#   istoric '1984': ['Ana']
#   istoric 'Dune': ['Mihai']
# =============================================================

import pymysql

from session28.date import password, username

DB_CONFIG = {
    "host": "localhost",
    "port": 3306,
    "user": username,
    "password": password,
    "database": "curs",
}


# ---- PREGATIRE (dat - nu modifica) --------------------------
def get_conn():
    return pymysql.connect(**DB_CONFIG)


def pregateste(conn):
    with conn.cursor() as cur:
        # ATENTIE la ordine: intai copilul (imprumuturi), apoi
        # parintele (carti) - FK-ul nu permite sa stergi parintele
        # cat timp mai exista randuri copil care il refera.
        cur.execute("DROP TABLE IF EXISTS ex29_imprumuturi")
        cur.execute("DROP TABLE IF EXISTS ex29_carti")

        cur.execute("""
            CREATE TABLE ex29_carti (
                id           INT AUTO_INCREMENT PRIMARY KEY,
                titlu        VARCHAR(150) NOT NULL,
                autor        VARCHAR(100) NOT NULL,
                an_aparitie  INT,
                disponibila  BOOLEAN NOT NULL DEFAULT TRUE
            )
        """)
        cur.execute("""
            CREATE TABLE ex29_imprumuturi (
                id             INT AUTO_INCREMENT PRIMARY KEY,
                carte_id       INT NOT NULL,
                imprumutat_de  VARCHAR(100) NOT NULL,
                data_imprumut  DATE NOT NULL,
                FOREIGN KEY (carte_id) REFERENCES ex29_carti(id)
            )
        """)

        cur.executemany(
            """INSERT INTO ex29_carti
               (titlu, autor, an_aparitie, disponibila)
               VALUES (%s, %s, %s, %s)""",
            [
                ("1984",            "George Orwell",      1949, True),
                ("Fahrenheit 451",  "Ray Bradbury",        1953, True),
                ("Sapiens",         "Yuval Noah Harari",   2011, True),
                ("Dune",            "Frank Herbert",       1965, False),  # deja imprumutata
                ("Clean Code",      "Robert C. Martin",    2008, True),
            ],
        )

        # "Dune" e deja imprumutata de Mihai, de dinainte
        cur.execute("""
            INSERT INTO ex29_imprumuturi (carte_id, imprumutat_de, data_imprumut)
            SELECT id, 'Mihai', '2026-05-01' FROM ex29_carti WHERE titlu = 'Dune'
        """)
    conn.commit()


# ---- ZONA TA DE LUCRU ---------------------------------------
def nr_carti_disponibile(conn):
    # TODO: COUNT(*) din ex29_carti WHERE disponibila = TRUE
    with conn.cursor() as c:
        c.execute("""
        SELECT COUNT(*) FROM ex29_carti WHERE disponibila = TRUE
        """)
        return c.fetchone()[0]


def carti_dupa_autor(conn, autor_fragment):
    # TODO: titlurile cartilor al caror autor CONTINE autor_fragment,
    # ordonate alfabetic dupa titlu
    with conn.cursor() as c:
        c.execute("""
        SELECT titlu FROM ex29_carti
        WHERE autor LIKE %s
        ORDER BY titlu DESC;
        """,  (f"%{autor_fragment}%",))
        # tupluri = c.fetchall()
        # lista_de_titluri = []
        # for tuplu in tupluri:
        #     lista_de_titluri.append(tuplu[0])
        # return lista_de_titluri
        return [tuplu[0] for tuplu in c.fetchall()]


def imprumuta_carte(conn, titlu, imprumutat_de, data_imprumut):
    # TODO:
    #  1) cauta (id, disponibila) pentru cartea cu acest titlu
    #  2) daca nu exista SAU nu e disponibila -> return False
    #  3) altfel: INSERT in ex29_imprumuturi, UPDATE disponibila=FALSE,
    #     commit, return True
    with conn.cursor() as c:
        c.execute("""
        SELECT id, disponibila FROM ex29_carti
        WHERE titlu = %s
        """, titlu)
        carte = c.fetchone()
        if not carte:
            return False
        else:
            if carte[1] is False:
                return False
            else:
                c.execute("""
                INSERT INTO ex29_imprumuturi (carte_id, imprumutat_de, data_imprumut)
                VALUES (%s, %s, %s)""", (carte[0], imprumutat_de, data_imprumut))
                c.execute("""
                UPDATE ex29_carti SET disponibila = False WHERE id = %s""", (carte[0],))
                conn.commit()
                return True

def istoric_imprumuturi(conn, titlu):
    # TODO: JOIN ex29_imprumuturi cu ex29_carti, numele persoanelor
    # care au imprumutat cartea cu acest titlu, ordonate crescator
    # dupa data_imprumut
    with conn.cursor() as c:
        c.execute("""
        SELECT ex29_imprumuturi.imprumutat_de
        FROM ex29_imprumuturi
        JOIN ex29_carti ON ex29_imprumuturi.carte_id = ex29_carti.id
        WHERE ex29_carti.titlu LIKE %s
        ORDER BY ex29_imprumuturi.data_imprumut;
        """, titlu)
        return [tuplu[0] for tuplu in c.fetchall()]


# ---- COD DE TEST (nu trebuie sa-l modifici) -----------------
conn = get_conn()
pregateste(conn)

print("disponibile (initial):", nr_carti_disponibile(conn))          # 4
print("dupa autor 'Orwell':", carti_dupa_autor(conn, "Orwell"))      # ['1984']

print("imprumuta '1984' catre Ana:", imprumuta_carte(conn, "1984", "Ana", "2026-06-01"))
# True
print("disponibile (dupa imprumut):", nr_carti_disponibile(conn))    # 3

print("imprumuta 'Dune' catre Georgeta (deja imprumutata):",
      imprumuta_carte(conn, "Dune", "Georgeta", "2026-06-02"))
# False

print("imprumuta 'Carte Inexistenta' catre Vlad:",
      imprumuta_carte(conn, "Carte Inexistenta", "Vlad", "2026-06-02"))
# False

print("istoric '1984':", istoric_imprumuturi(conn, "1984"))          # ['Ana']
print("istoric 'Dune':", istoric_imprumuturi(conn, "Dune"))          # ['Mihai']

with conn.cursor() as cur:
    cur.execute("DROP TABLE IF EXISTS ex29_imprumuturi")
    cur.execute("DROP TABLE IF EXISTS ex29_carti")
conn.commit()
conn.close()