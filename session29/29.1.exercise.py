# EXERCITIUL 1  -  PROGRES QUIZ-URI
# =============================================================
#
# CONTEXT (caz real)
# ------------------
# Ai mai multe quiz-uri pe care le rezolvi de-a lungul timpului.
# Vrei sa pastrezi in MySQL fiecare incercare, pentru a putea vedea:
#
#   - ce quiz-uri ai facut
#   - de cate ori ai facut fiecare quiz
#   - care a fost cel mai bun scor
#   - cum a evoluat scorul tau in timp
#
# Spre deosebire de exercitiile cu date DEMO, tabela NU se sterge
# la final. Datele raman PERMANENTE in MySQL.
#
# Aplicatia va avea un mic MENIU in consola:
#
#   1) Vezi toate quiz-urile facute pana acum
#   2) Vezi istoricul unui quiz anume
#   3) Adauga un scor nou
#   4) Iesire
#
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


# =============================================================
# CONEXIUNE + TABELA
# =============================================================

def get_conn():
    return pymysql.connect(**DB_CONFIG)


def creeaza_tabel(conn):
    # CREATE TABLE IF NOT EXISTS este important deoarece vrem
    # sa pastram istoricul intre rulari.
    with conn.cursor() as cur:
        cur.execute("""
            CREATE TABLE IF NOT EXISTS ex29_scoruri_quiz (
                id               INT AUTO_INCREMENT PRIMARY KEY,
                nume_quiz        VARCHAR(150) NOT NULL,
                scor             INT NOT NULL,
                scor_maxim       INT NOT NULL,
                data_completare  DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        """)

    conn.commit()


# =============================================================
# FUNCTII DE BAZA DE DATE
# =============================================================

def listeaza_quizuri(conn):
    # TODO:
    # Returneaza toate quiz-urile distincte impreuna cu:
    #
    #   - numele quiz-ului
    #   - numarul de incercari
    #   - cel mai bun scor
    #
    # Trebuie sa folosesti:
    #
    #   GROUP BY
    #   COUNT(*)
    #   MAX(scor)
    #
    # Ordoneaza quiz-urile alfabetic.
    #
    # Rezultatul trebuie returnat cu fetchall().
    with conn.cursor() as c:
        c.execute("""
            SELECT nume_quiz, COUNT(*), MAX(scor)
            FROM ex29_scoruri_quiz
            GROUP BY nume_quiz
            ORDER BY  nume_quiz ASC
        """)
        return c.fetchall()


def istoric_scoruri(conn, nume_quiz):
    # TODO:
    # Returneaza istoricul complet pentru quiz-ul primit.
    #
    # Pentru fiecare incercare trebuie sa returnezi:
    #
    #   - scor
    #   - scor_maxim
    #   - data_completare
    #
    # Foloseste WHERE pentru numele quiz-ului.
    #
    # Parametrizarea trebuie facuta cu %s.
    #
    # Ordoneaza rezultatele crescator dupa data_completare.
    #
    # Returneaza rezultatul cu fetchall().

    with conn.cursor() as c:
        c.execute("""
            SELECT scor, scor_maxim, data_completare
            FROM ex29_scoruri_quiz
            WHERE nume_quiz = %s
            ORDER BY data_completare ASC
        """, (nume_quiz,))
    return c.fetchall()


def adauga_scor(conn, nume_quiz, scor, scor_maxim):
    # TODO:
    # Adauga un nou scor in tabela.
    #
    # Foloseste INSERT parametrizat cu %s.
    #
    # Dupa INSERT trebuie sa faci conn.commit().
    with conn.cursor() as c:
        c.execute(
            """ 
            INSERT INTO ex29_scoruri_quiz
            (nume_quiz, scor, scor_maxim)
            VALUES (%s, %s, %s)
            """, (nume_quiz, scor, scor_maxim)
        )
    conn.commit()


# =============================================================
# FUNCTII DE AFISARE (doar print, fara SQL)
# =============================================================

def afiseaza_lista_quizuri(conn):
    # TODO:
    # Apeleaza listeaza_quizuri(conn).
    #
    # Daca nu exista quiz-uri:
    #
    #   Nu ai inregistrat niciun quiz inca.
    #
    # Altfel, afiseaza fiecare quiz sub forma:
    #
    #   - Python Basics (3 incercari, cel mai bun scor: 9)
    #
    # Pentru o singura incercare foloseste "incercare",
    # iar pentru mai multe "incercari".
    quizuri = listeaza_quizuri(conn)

    if not quizuri:
        print("\n Nu ai inregistrat niciun quiz inca \n")
        return

    print("\n Quizurile tale sunt: \n")

    for nume_quiz, nr_incercari, scor_maxim in quizuri:
        print(f"   - {nume_quiz} ({nr_incercari} {'incercare' if nr_incercari == 1 else 'incercari'}), cel mai bun scor {scor_maxim} ")


def afiseaza_istoric(conn, nume_quiz):
    # TODO:
    # Apeleaza istoric_scoruri(conn, nume_quiz).
    #
    # Daca nu exista rezultate, afiseaza un mesaj si returneaza.
    #
    # Pentru fiecare incercare afiseaza:
    #
    #   data   scor/scor_maxim   procent
    #
    # Exemplu:
    #
    #   2026-08-10 18:30   6/10   (60.0%)
    #
    # Daca exista cel putin doua incercari:
    #
    #   - calculeaza procentul primei incercari
    #   - calculeaza procentul ultimei incercari
    #   - calculeaza diferenta dintre ele
    #
    # Daca diferenta > 0:
    #   afiseaza progresul.
    #
    # Daca diferenta < 0:
    #   afiseaza ca scorul a scazut.
    #
    # Daca diferenta == 0:
    #   afiseaza ca nu exista progres.
    istoric = istoric_scoruri(conn, nume_quiz)

    if not istoric:
        print("Nu exista istoric, mai incearca")
        return

    print(F"Istoric pentru quizul: {nume_quiz}")

    for scor, scor_maxim, data_completare in istoric:
        print(f"{data_completare}: {scor}/{scor_maxim}")



# =============================================================
# CITIRE SI VALIDARE INPUT
# =============================================================

def citeste_int(mesaj, minim=None):
    # Citim un numar intreg de la tastatura.
    # Repetam pana cand utilizatorul introduce o valoare valida.
    while True:
        text = input(mesaj).strip()

        try:
            valoare = int(text)
        except ValueError:
            print("  ! Introdu un numar intreg valid.")
            continue

        if minim is not None and valoare < minim:
            print(
                f"  ! Valoarea trebuie sa fie cel putin {minim}."
            )
            continue

        return valoare


def adauga_scor_interactiv(conn):
    nume_quiz = input("  Numele quiz-ului: ").strip()

    if not nume_quiz:
        print("  ! Numele quiz-ului nu poate fi gol.")
        return

    scor_maxim = citeste_int(
        "  Scor maxim posibil: ",
        minim=1
    )

    scor = citeste_int(
        f"  Scor obtinut (0-{scor_maxim}): ",
        minim=0
    )

    if scor > scor_maxim:
        print(
            "  ! Scorul obtinut nu poate fi mai mare "
            "decat scorul maxim."
        )
        return

    adauga_scor(
        conn,
        nume_quiz,
        scor,
        scor_maxim
    )

    print(
        f"  [ok] Scor salvat pentru "
        f"„{nume_quiz}”: {scor}/{scor_maxim}\n"
    )


# =============================================================
# MENIUL PRINCIPAL
# =============================================================

def meniu():
    conn = get_conn()
    creeaza_tabel(conn)

    print("=" * 56)
    print("===          PROGRES QUIZ-URI  (consola)          ===")
    print("=" * 56)

    while True:
        print("\n  1) Vezi toate quiz-urile facute")
        print("  2) Vezi istoricul unui quiz anume")
        print("  3) Adauga un scor nou")
        print("  4) Iesire")

        optiune = input(
            "\n  Alege o optiune (1-4): "
        ).strip()

        if optiune == "1":
            afiseaza_lista_quizuri(conn)

        elif optiune == "2":
            nume_quiz = input(
                "  Numele quiz-ului: "
            ).strip()

            afiseaza_istoric(conn, nume_quiz)

        elif optiune == "3":
            adauga_scor_interactiv(conn)

        elif optiune == "4":
            print("\n  La revedere!")
            break

        else:
            print("  ! Alege 1, 2, 3 sau 4.")

    conn.close()


# =============================================================
# COD DE TEST / PORNIRE
# =============================================================

meniu()


# =============================================================
# OUTPUT ASTEPTAT
# =============================================================
#
# La pornirea programului:
#
# ========================================================
# ===          PROGRES QUIZ-URI  (consola)          ===
# ========================================================
#
#   1) Vezi toate quiz-urile facute
#   2) Vezi istoricul unui quiz anume
#   3) Adauga un scor nou
#   4) Iesire
#
#
# Dupa ce alegi 3:
#
#   Alege o optiune (1-4): 3
#
#   Numele quiz-ului: Python Basics
#   Scor maxim posibil: 10
#   Scor obtinut (0-10): 6
#
#   [ok] Scor salvat pentru „Python Basics”: 6/10
#
#
# Daca mai adaugi:
#
#   Python Basics -> 8/10
#   Python Basics -> 9/10
#
# La optiunea 1:
#
#   QUIZ-URILE TALE:
#   --------------------------------------------------
#   - Python Basics  (3 incercari, cel mai bun scor: 9)
#
#
# La optiunea 2:
#
#   ISTORIC „Python Basics”:
#   --------------------------------------------------
#   2026-08-10 18:30   6/10   (60.0%)
#   2026-08-11 19:15   8/10   (80.0%)
#   2026-08-12 20:00   9/10   (90.0%)
#   --------------------------------------------------
#   Progres: +30.0 puncte procentuale fata de prima incercare!
#
# =============================================================