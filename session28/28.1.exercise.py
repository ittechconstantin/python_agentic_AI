# EXERCITIUL 1  (PYTHON + MySQL)  -  OBIECTIVE DE ECONOMISIRE
# =============================================================
#
# CONTEXT (caz real)
# ------------------
# Tii evidenta obiectivelor tale de economisire (vacanta, fond de
# urgenta, un laptop nou...), cu datele intr-o tabela MySQL
# `ex28_obiective`. Trebuie sa scrii FUNCTII care raspund la intrebari
# despre obiective si adauga obiective noi - fiecare functie primeste
# conexiunea `conn` si ruleaza SQL parametrizat.
#
# Codul de PREGATIRE (conexiune + creare tabela + date DEMO) e deja
# scris mai jos - tu completezi doar functiile din ZONA TA DE LUCRU.
# La finalul fisierului ai si o sectiune JOACA-TE, in care poti folosi
# ACELASI cod ca sa-ti tii REAL evidenta economiilor tale.
#
#
# CE AI DE FACUT
# --------------
# Scrie 4 functii:
#
# 1. nr_obiective(conn)               -> cate obiective sunt in total.
# 2. obiective_neatinse(conn)         -> NUMELE obiectivelor la care
#                                        suma_economisita < suma_tinta
#                                        (nu sunt inca atinse), ordonate
#                                        CRESCATOR dupa data_limita (cel
#                                        mai urgent primul).
# 3. adauga_obiectiv(conn, nume, suma_tinta, suma_economisita, data_limita)
#                                      -> insereaza un obiectiv nou (si
#                                        commit). data_limita e text
#                                        'AAAA-LL-ZZ', ex: '2026-12-01'.
# 4. cauta_dupa_nume(conn, fragment)  -> NUMELE obiectivelor al caror
#                                        nume CONTINE `fragment`
#                                        (foloseste LIKE), alfabetic.
#
#
# CERINTE
# -------
#   - foloseste  cur.execute(SQL, (param,))  cu  %s  (parametrizare!)
#   - la INSERT nu uita  conn.commit()
#   - pentru un singur rezultat:  cur.fetchone()[0]
#   - la punctul 4, tiparul LIKE se construieste in Python:
#       f"%{fragment}%"
#     si se trimite CA PARAMETRU (nu lipit direct in SQL)
#
#
# OUTPUT ASTEPTAT (din codul de test de mai jos)
# ----------------------------------------------
#   nr obiective: 5
#   neatinse: ['Vacanta Grecia', 'Laptop nou', 'Renovare bucatarie']
#   dupa adaugare: 6
#   cauta 'de': ['Fond de urgenta']
#
#
# INDICII
# -------
#   - COUNT:  "SELECT COUNT(*) FROM ex28_obiective"  -> fetchone()[0]
#   - filtrare+ordonare:
#       "... WHERE suma_economisita < suma_tinta ORDER BY data_limita ASC"
#   - numele intr-o lista:  [r[0] for r in cur.fetchall()]
#   - INSERT:  "INSERT INTO ex28_obiective (nume_obiectiv, suma_tinta,
#               suma_economisita, data_limita) VALUES (%s, %s, %s, %s)"
#   - LIKE:    "... WHERE nume_obiectiv LIKE %s ORDER BY nume_obiectiv ASC",
#              (f"%{fragment}%",)
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
        cur.execute("DROP TABLE IF EXISTS ex28_obiective")
        cur.execute("""
            CREATE TABLE ex28_obiective (
                id                INT AUTO_INCREMENT PRIMARY KEY,
                nume_obiectiv     VARCHAR(100) NOT NULL,
                suma_tinta        DECIMAL(10,2) NOT NULL,
                suma_economisita  DECIMAL(10,2) NOT NULL DEFAULT 0,
                data_limita       DATE
            )
        """)
        cur.executemany(
            """INSERT INTO ex28_obiective
               (nume_obiectiv, suma_tinta, suma_economisita, data_limita)
               VALUES (%s, %s, %s, %s)""",
            [
                ("Vacanta Grecia",      5000.00,  2000.00, "2026-06-01"),
                ("Fond de urgenta",    10000.00, 10000.00, "2026-01-01"),  # deja atins
                ("Laptop nou",          6000.00,  1500.00, "2026-12-01"),
                ("Renovare bucatarie", 15000.00,  3000.00, "2027-03-01"),
                ("Curs certificare",    2000.00,  2000.00, "2026-02-01"),  # deja atins
            ],
        )
    conn.commit()


# ---- ZONA TA DE LUCRU ---------------------------------------
def nr_obiective(conn):
    # TODO: COUNT(*) din ex28_obiective
    ...
    with conn.cursor() as c:
        c.execute("SELECT COUNT(*) FROM ex28_obiective;")
        return c.fetchone()[0]


def obiective_neatinse(conn):
    # TODO: numele obiectivelor cu suma_economisita < suma_tinta,
    # ordonate crescator dupa data_limita
    ...
    with conn.cursor() as c:
        c.execute("""
        SELECT nume_obiectiv FROM ex28_obiective
        WHERE suma_economisita < suma_tinta
        ORDER BY data_limita ASC;
        """)
        return [obiectiv_neatins[0] for obiectiv_neatins in c.fetchall()]


def adauga_obiectiv(conn, nume, suma_tinta, suma_economisita, data_limita):
    # TODO: INSERT parametrizat + commit
    ...

    with conn.cursor() as c:
        c.execute("""
        INSERT INTO ex28_obiective (nume_obiectiv, suma_tinta, suma_economisita, data_limita)
            VALUES (%s, %s, %s, %s)""",  (nume, suma_tinta, suma_economisita, data_limita )
        )

    conn.commit()


def cauta_dupa_nume(conn, fragment):
    # TODO: numele obiectivelor al caror nume CONTINE fragment (LIKE)
    with conn.cursor() as c:
        c.execute(""" 
        SELECT nume_obiectiv FROM ex28_obiective WHERE nume_obiectiv LIKE %s ORDER BY nume_obiectiv ASC
        """, (f"%{fragment}%",))
    return [obiectiv[0] for obiectiv in c.fetchall()]

# ---- COD DE TEST (nu trebuie sa-l modifici) -----------------
conn = get_conn()
pregateste(conn)

print("nr obiective:", nr_obiective(conn))              # nr obiective: 5
print("neatinse:", obiective_neatinse(conn))
# ['Vacanta Grecia', 'Laptop nou', 'Renovare bucatarie']

adauga_obiectiv(conn, "Masina noua", 40000.00, 5000.00, "2028-01-01")
print("dupa adaugare:", nr_obiective(conn))              # dupa adaugare: 6

print("cauta 'de':", cauta_dupa_nume(conn, "de"))        # ['Fond de urgenta']

# with conn.cursor() as cur:
#     cur.execute("DROP TABLE ex28_obiective")
conn.commit()
conn.close()