# EXERCITIUL 2  (PYTHON + MySQL)  -  EVIDENTA ABONAMENTELOR LUNARE
# =============================================================
#
# CONTEXT (caz real)
# ------------------
# Tii evidenta abonamentelor tale lunare (Netflix, sala, Spotify...),
# cu datele intr-o tabela MySQL `ex27_abonamente`. Trebuie sa scrii
# FUNCTII care gasesc abonamentele scumpe, adauga abonamente noi,
# modifica pretul (creste abonamentul) si sterg abonamente anulate -
# fiecare functie primeste conexiunea `conn` si ruleaza SQL parametrizat.
#
# Codul de PREGATIRE (conexiune + creare tabela + date DEMO) e deja
# scris mai jos - tu completezi doar functiile din ZONA TA DE LUCRU.
# La finalul fisierului ai si o sectiune JOACA-TE, in care poti folosi
# ACELASI cod ca sa vezi REAL cat platesti tu, lunar, pe abonamente.
#
#
# CE AI DE FACUT
# --------------
# Scrie 4 functii:
#
# 1. abonamente_peste(conn, prag)      -> NUMELE abonamentelor cu
#                                        pret_lunar > prag, ordonate
#                                        DESCRESCATOR dupa pret.
# 2. actualizeaza_pret(conn, nume, pret_nou) -> pune pret_lunar la
#                                        valoarea data (si commit);
#                                        intoarce cate randuri au fost
#                                        modificate (cur.rowcount).
# 3. sterge_abonament(conn, nume)      -> sterge abonamentul dupa nume
#                                        (si commit); intoarce cur.rowcount.
# 4. adauga_abonament(conn, nume, pret_lunar, categorie) -> insereaza
#                                        un abonament nou (si commit).
#
#
# CERINTE
# -------
#   - foloseste  cur.execute(SQL, (param,))  cu  %s  (parametrizare!)
#   - dupa INSERT/UPDATE/DELETE nu uita  conn.commit()
#   - pentru "cate randuri afectate":  cur.rowcount  (citeste-l INAINTE
#     de a inchide cursorul / a face commit, ca la exemplele din
#     28.python_mysql.py)
#
#
# OUTPUT ASTEPTAT (din codul de test de mai jos)
# ----------------------------------------------
#   peste 20 (initial): ['Sala', 'Netflix', 'Revista', 'Spotify']
#   randuri modificate: 1
#   peste 20 (dupa update Spotify): ['Sala', 'Spotify', 'Netflix', 'Revista']
#   randuri sterse: 1
#   peste 20 (dupa stergere Revista): ['Sala', 'Spotify', 'Netflix']
#   peste 20 (dupa adaugare Disney+): ['Sala', 'Spotify', 'Netflix', 'Disney+']
#
#
# INDICII
# -------
#   - filtrare+ordonare:  "... WHERE pret_lunar > %s ORDER BY pret_lunar DESC"
#   - numele intr-o lista:  [r[0] for r in cur.fetchall()]
#   - UPDATE:  "UPDATE ex27_abonamente SET pret_lunar = %s WHERE nume = %s"
#   - DELETE:  "DELETE FROM ex27_abonamente WHERE nume = %s"
#   - INSERT:  "INSERT INTO ex27_abonamente (nume, pret_lunar, categorie) VALUES (%s, %s, %s)"
# =============================================================

import pymysql

DB_CONFIG = {
    "host": "localhost", "port": 3306,
    "user": "cursant", "password": "parola123", "database": "curs",
}


# ---- PREGATIRE (dat - nu modifica) --------------------------
def get_conn():
    return pymysql.connect(**DB_CONFIG)


def pregateste(conn):
    with conn.cursor() as cur:
        cur.execute("DROP TABLE IF EXISTS ex27_abonamente")
        cur.execute("""
            CREATE TABLE ex27_abonamente (
                id         INT AUTO_INCREMENT PRIMARY KEY,
                nume       VARCHAR(100) NOT NULL UNIQUE,
                pret_lunar DECIMAL(10,2) NOT NULL,
                categorie  VARCHAR(50)
            )
        """)
        cur.executemany(
            "INSERT INTO ex27_abonamente (nume, pret_lunar, categorie) VALUES (%s, %s, %s)",
            [
                ("Netflix",       45.00, "streaming"),
                ("Spotify",       25.00, "streaming"),
                ("Sala",         150.00, "sport"),
                ("Cloud Storage", 15.00, "altele"),
                ("Revista",       30.00, "altele"),
            ],
        )
    conn.commit()


# ---- ZONA TA DE LUCRU ---------------------------------------
def abonamente_peste(conn, prag):
    # TODO: numele abonamentelor cu pret_lunar > prag, descrescator dupa pret
    with conn.cursor() as c:
        c.execute("""
        SELECT nume FROM ex28_obiective
        WHERE pret_lunar > %s 
        ORDER BY pret_lunar DESC""")
        return [r[0] for r in cur.fetchall()]

def actualizeaza_pret(conn, nume, pret_nou):
    # TODO: UPDATE pret_lunar pentru abonamentul `nume` + commit; return rowcount
    with conn.cursoer() as c:
        c.execute("""
        UPDATE ex27_abonamente 
        SET pret_lunar = %s 
        WHERE nume = %s""")
    conn.commit()


def sterge_abonament(conn, nume):
    # TODO: DELETE abonamentul `nume` + commit; return rowcount
    ...
    with conn.cursoer() as c:
        c.execute("""
        DELETE FROM ex27_abonamente 
        WHERE nume = %s""")
    conn.commit()


def adauga_abonament(conn, nume, pret_lunar, categorie):
    # TODO: INSERT parametrizat + commit
    with conn.cursoer() as c:
        c.execute("""
        INSERT INTO ex27_abonamente (nume, pret_lunar, categorie)
        VALUES (%s, %s, %s)"""), (nume, pret_lunar, categorie)
    conn.commit()


# ---- COD DE TEST (nu trebuie sa-l modifici) -----------------
conn = get_conn()
pregateste(conn)

print("peste 20 (initial):", abonamente_peste(conn, 20))
# ['Sala', 'Netflix', 'Revista', 'Spotify']

print("randuri modificate:", actualizeaza_pret(conn, "Spotify", 60.00))  # 1
print("peste 20 (dupa update Spotify):", abonamente_peste(conn, 20))
# ['Sala', 'Spotify', 'Netflix', 'Revista']

print("randuri sterse:", sterge_abonament(conn, "Revista"))              # 1
print("peste 20 (dupa stergere Revista):", abonamente_peste(conn, 20))
# ['Sala', 'Spotify', 'Netflix']

adauga_abonament(conn, "Disney+", 35.00, "streaming")
print("peste 20 (dupa adaugare Disney+):", abonamente_peste(conn, 20))
# ['Sala', 'Spotify', 'Netflix', 'Disney+']

with conn.cursor() as cur:
    cur.execute("DROP TABLE ex27_abonamente")
conn.commit()
conn.close()
