# QUIZ INTERVIU  -  SQL + PyMySQL  (sesiunile 26 si 28)
# =============================================================
# Pe baza a tot ce s-a predat in 26.teorie.sql si
# 28.python_mysql.py (+ exercitiile 28.1 si 28.2).
# Fiecare intrebare contine:
#   - o SECVENTA DE COD (SQL sau Python+PyMySQL)
#   - 4 variante A/B/C/D
#   - EXPLICATIE obligatorie dupa raspuns (afisata si cand
#     raspunzi corect - la interviu conteaza sa stii DE CE)
#
# Gotcha-urile clasice din sesiunile 26 si 28:
#   CREATE TABLE & TIPURI (26):
#     - NOT NULL fara valoare in INSERT -> Error, randul e refuzat
#     - UNIQUE -> Duplicate entry daca incerci sa repeti valoarea
#     - DEFAULT CURRENT_TIMESTAMP -> completat automat de MySQL
#     - DECIMAL pentru bani, NICIODATA FLOAT (rotunjeste aproximativ)
#   SELECT / WHERE / LIKE / ORDER BY (26):
#     - NULL nu e "egal" cu nimic, nici macar cu el insusi ->
#       IS NULL, NICIODATA = NULL
#     - LIKE: % = orice secventa, _ = exact UN caracter
#     - ORDER BY cu mai multe coloane: a doua e "sortare de rezerva",
#       intra in joc doar la egalitate pe prima
#     - IN e prescurtare pentru mai multe OR-uri pe aceeasi coloana
#   UPDATE / DELETE / FOREIGN KEY / JOIN (26):
#     - UPDATE / DELETE FARA WHERE = afecteaza TOT tabelul
#     - FK impiedica INSERT-uri "orfane" (referinte catre ce nu exista)
#     - FK impiedica si DELETE pe un "parinte" care are randuri "copil"
#     - JOIN simplu = INNER JOIN -> pastreaza DOAR potrivirile;
#       randurile fara potrivire raman in afara (nevoie de LEFT JOIN)
#   PyMySQL - CONECTARE & SIGURANTA (28):
#     - SQL injection: text lipit direct in SQL (f-string) poate
#       schimba STRUCTURA comenzii -> NICIODATA asa
#     - parametrizare (%s + tuplu): driverul trateaza mereu valorile
#       ca DATE, nu ca bucati de comanda SQL
#     - `with conn.cursor() as c:` -> cursorul se inchide automat,
#       chiar daca apare o eroare pe drum (ca la open() cu fisiere)
#   PyMySQL - EXECUTEMANY, FETCH, COMMIT, ROWCOUNT (28):
#     - executemany() = o singura calatorie la server pentru toate
#       randurile, in loc de un execute() per rand
#     - fetchone() -> UN tuplu (sau None); fetchall() -> tuplu de tupluri
#     - conn.commit() OBLIGATORIU dupa INSERT/UPDATE/DELETE, altfel
#       modificarea se pierde
#     - cur.rowcount -> cate randuri au fost AFECTATE (poate fi 0,
#       fara nicio eroare, daca WHERE nu se potriveste cu nimic)
#
# Cum se ruleaza:
#   python3 29.0.quiz_interviu.py
#
# Apasa Q oricand pentru iesire.
# =============================================================


# =============================================================
# BANCA DE INTREBARI
# =============================================================
# Fiecare intrebare e un DICT cu:
#   runda       (int)    1..5
#   categorie   (str)
#   puncte      (int)    1 / 2 / 3 - dificultate
#   cod         (str)    secventa de cod (triple-quoted)
#   intrebare   (str)    intrebarea propriu-zisa
#   optiuni     (dict)   {"A": ..., "B": ..., "C": ..., "D": ...}
#   corect      (str)    "A" / "B" / "C" / "D"
#   explicatie  (str)    DE CE - afisata mereu dupa raspuns

intrebari = [
    # ---------- RUNDA 1: CREATE TABLE, TIPURI DE DATE & CONSTRANGERI ----------
    {"runda": 1, "categorie": "not-null-constraint", "puncte": 2,
     "cod": 'CREATE TABLE useri(\n    id    INT AUTO_INCREMENT PRIMARY KEY,\n    nume  VARCHAR(50) NOT NULL,\n    email VARCHAR(100) UNIQUE\n);\n\nINSERT INTO useri (email) VALUES (\'a@test.ro\');',
     "intrebare": "Ce se intampla la acest INSERT?",
     "optiuni": {"A": "se insereaza cu nume = NULL", "B": "Error - nume nu poate fi NULL (NOT NULL)",
                 "C": "se insereaza cu nume = ''", "D": "Error - email trebuie completat"},
     "corect": "B",
     "explicatie": "nume are NOT NULL si nu e specificat in INSERT. MySYL REFUZA randul, exact ca un `raise` din Python: problema nu trece neobservata."},

    {"runda": 1, "categorie": "unique-vs-primary-key", "puncte": 2,
     "cod": "INSERT INTO useri (nume, email) VALUES ('Ana', 'ana@test.ro');\nINSERT INTO useri (nume, email) VALUES ('Alt Ana', 'ana@test.ro');",
     "intrebare": "Ce se intampla la al doilea INSERT?",
     "optiuni": {"A": "se insereaza normal, doua randuri cu acelasi email", "B": "Error - Duplicate entry pentru email (UNIQUE)",
                 "C": "se insereaza dar email devine NULL", "D": "Error - nume trebuie sa fie unic"},
     "corect": "B",
     "explicatie": "email e declarat UNIQUE - doua randuri NU pot avea aceeasi valoare. Al doilea INSERT e respins cu 'Duplicate entry'."},

    {"runda": 1, "categorie": "default-current-timestamp", "puncte": 1,
     "cod": "CREATE TABLE log(\n    id       INT AUTO_INCREMENT PRIMARY KEY,\n    mesaj    VARCHAR(100),\n    creat_la DATETIME DEFAULT CURRENT_TIMESTAMP\n);\n\nINSERT INTO log (mesaj) VALUES ('test');",
     "intrebare": "Ce valoare are creat_la dupa acest INSERT?",
     "optiuni": {"A": "NULL", "B": "data si ora curenta, completata automat de MySQL",
                 "C": "Error - creat_la nu a fost specificat", "D": "0000-00-00 00:00:00"},
     "corect": "B",
     "explicatie": "DEFAULT CURRENT_TIMESTAMP inseamna: daca nu specifici tu o valoare, MySQL pune singur data/ora curenta la momentul INSERT-ului."},

    {"runda": 1, "categorie": "decimal-vs-float", "puncte": 2,
     "cod": None,
     "intrebare": "De ce se recomanda DECIMAL(10,2) in loc de FLOAT pentru preturi?",
     "optiuni": {"A": "DECIMAL ocupa mai putin spatiu pe disc", "B": "FLOAT nu poate stoca numere negative",
                 "C": "FLOAT rotunjeste aproximativ, ceea ce poate produce erori la sume de bani", "D": "nu exista nicio diferenta practica"},
     "corect": "C",
     "explicatie": "FLOAT stocheaza zecimale APROXIMATIV (probleme de reprezentare binara). Pentru bani ai nevoie de precizie EXACTA - de asta se foloseste DECIMAL(10,2), nu FLOAT."},


    # ---------- RUNDA 2: SELECT, WHERE, LIKE, ORDER BY ----------
    {"runda": 2, "categorie": "is-null-vs-egal", "puncte": 3,
     "cod": "SELECT nume FROM useri WHERE varsta = NULL;",
     "intrebare": "Cate randuri returneaza aceasta interogare, presupunand ca exista useri cu varsta necompletata?",
     "optiuni": {"A": "toti userii cu varsta necompletata", "B": "niciunul - trebuie IS NULL, nu = NULL",
                 "C": "Error de sintaxa", "D": "toti userii din tabela"},
     "corect": "B",
     "explicatie": "In SQL, NULL nu e 'egal' cu nimic, nici cu el insusi. `= NULL` nu returneaza NICIODATA randuri - trebuie folosit IS NULL / IS NOT NULL."},

    {"runda": 2, "categorie": "like-wildcard", "puncte": 3,
     "cod": "SELECT nume FROM useri WHERE nume LIKE '_a%';",
     "intrebare": "Ce nume se potrivesc acestui tipar?",
     "optiuni": {"A": "nume care contin litera 'a' oriunde", "B": "nume care incep cu 'a'",
                 "C": "nume care au 'a' EXACT pe a doua pozitie", "D": "nume care se termina in 'a'"},
     "corect": "C",
     "explicatie": "_ inseamna exact UN caracter oarecare -> pozitia 1 e orice caracter. Apoi 'a' trebuie sa fie EXACT pe pozitia 2. % la final permite orice urmeaza."},

    {"runda": 2, "categorie": "order-by-multiplu", "puncte": 2,
     "cod": "SELECT nume, varsta FROM useri ORDER BY varsta DESC, nume ASC;",
     "intrebare": "Cand intra in joc a doua coloana (nume ASC) din ORDER BY?",
     "optiuni": {"A": "niciodata, doar prima coloana conteaza", "B": "doar cand doi useri au aceeasi varsta",
                 "C": "inainte de varsta DESC", "D": "inlocuieste complet sortarea dupa varsta"},
     "corect": "B",
     "explicatie": "A doua coloana e o 'sortare de rezerva' - decide ordinea DOAR intre randurile care sunt egale pe prima coloana (aceeasi varsta)."},

    {"runda": 2, "categorie": "in-vs-or", "puncte": 1,
     "cod": "SELECT nume FROM useri WHERE nume IN ('Ana', 'Ion');",
     "intrebare": "Ce interogare echivalenta descrie acelasi rezultat?",
     "optiuni": {"A": "WHERE nume = 'Ana' AND nume = 'Ion'", "B": "WHERE nume = 'Ana' OR nume = 'Ion'",
                 "C": "WHERE nume LIKE 'Ana%' OR nume LIKE 'Ion%'", "D": "WHERE nume != 'Ana' AND nume != 'Ion'"},
     "corect": "B",
     "explicatie": "IN e o scurtatura pentru mai multe OR-uri legate de ACEEASI coloana. AND ar fi imposibil de satisfacut - o coloana nu poate fi in acelasi timp 'Ana' si 'Ion'."},


    # ---------- RUNDA 3: UPDATE, DELETE, FOREIGN KEY & JOIN ----------
    {"runda": 3, "categorie": "update-fara-where", "puncte": 3,
     "cod": "UPDATE useri SET varsta = 0;",
     "intrebare": "Ce se intampla la aceasta comanda?",
     "optiuni": {"A": "Error - lipseste WHERE", "B": "se modifica DOAR primul rand",
                 "C": "se modifica varsta la TOATE randurile din tabela", "D": "nu se intampla nimic, comanda e ignorata"},
     "corect": "C",
     "explicatie": "UPDATE fara WHERE afecteaza TOATE randurile. Nu exista 'undo' automat in SQL simplu. Regula de aur: verifici INTAI cu un SELECT + acelasi WHERE."},

    {"runda": 3, "categorie": "foreign-key-insert-orfan", "puncte": 3,
     "cod": "INSERT INTO comenzi (user_id, produs_id, cantitate)\nVALUES (999, 1, 1);",
     "intrebare": "Presupunand ca nu exista niciun user cu id=999, ce se intampla?",
     "optiuni": {"A": "se insereaza normal, cu user_id=999", "B": "Error - a foreign key constraint fails",
                 "C": "MySQL creeaza automat un user cu id=999", "D": "se insereaza cu user_id=NULL"},
     "corect": "B",
     "explicatie": "FOREIGN KEY verifica automat legatura. Nu poti insera o comanda cu un user_id care NU exista - asta e 'integritate referentiala', te protejeaza de date orfane."},

    {"runda": 3, "categorie": "fk-delete-parinte", "puncte": 3,
     "cod": "DELETE FROM useri WHERE nume = 'Ana Popescu';",
     "intrebare": "Presupunand ca Ana are comenzi in tabela comenzi (FK spre useri), ce se intampla?",
     "optiuni": {"A": "se sterge userul si toate comenzile lui, automat", "B": "se sterge userul, comenzile raman cu user_id invalid",
                 "C": "Error - foreign key constraint fails, nu poti sterge un 'parinte' cu randuri 'copil'", "D": "se sterge doar userul, comenzile devin NULL"},
     "corect": "C",
     "explicatie": "FK protejeaza si invers: nu poti sterge un user care ARE comenzi, ca sa nu ramana comenzi orfane. Trebuie sterse INTAI comenzile lui."},

    {"runda": 3, "categorie": "inner-join-vs-left-join", "puncte": 2,
     "cod": "SELECT u.nume, c.cantitate\nFROM useri u\nJOIN comenzi c ON u.id = c.user_id;",
     "intrebare": "Ce se intampla cu userii care NU au nicio comanda?",
     "optiuni": {"A": "apar in rezultat, cu cantitate = NULL", "B": "NU apar deloc in rezultat (INNER JOIN pastreaza doar potrivirile)",
                 "C": "Error", "D": "apar o singura data, indiferent de numarul de comenzi"},
     "corect": "B",
     "explicatie": "JOIN simplu = INNER JOIN: pastreaza DOAR randurile unde legatura chiar exista de-o parte si de alta. Pentru a pastra si userii fara comenzi, ai nevoie de LEFT JOIN."},


    # ---------- RUNDA 4: PYMYSQL - CONECTARE, PARAMETRIZARE & SQL INJECTION ----------
    {"runda": 4, "categorie": "sql-injection", "puncte": 3,
     "cod": 'nume = "x\'; DROP TABLE useri; --"\ncur.execute(f"INSERT INTO useri (nume) VALUES (\'{nume}\')")',
     "intrebare": "De ce este periculos acest cod?",
     "optiuni": {"A": "nu e periculos, doar ineficient", "B": "textul din nume poate fi interpretat ca SQL si poate executa comenzi neintentionate (SQL injection)",
                 "C": "f-string nu functioneaza cu SQL", "D": "VARCHAR nu poate contine ghilimele"},
     "corect": "B",
     "explicatie": "Textul lipit direct in comanda poate contine BUCATI DE SQL care schimba complet intelesul comenzii - aici, un INSERT nevinovat devine INSERT + DROP TABLE."},

    {"runda": 4, "categorie": "parametrizare-corecta", "puncte": 2,
     "cod": 'cur.execute(\n    "INSERT INTO useri (nume, email) VALUES (%s, %s)",\n    (nume, email)\n)',
     "intrebare": "De ce este aceasta varianta sigura, spre deosebire de f-string?",
     "optiuni": {"A": "%s si tuplul de parametri sunt trimise SEPARAT de SQL - driverul le trateaza mereu ca DATE, nu ca bucati de comanda", "B": "%s e mai rapid decat f-string",
                 "C": "nu exista nicio diferenta reala, doar stil de scriere", "D": "%s converteste automat textul in numere"},
     "corect": "A",
     "explicatie": "Cu %s + tuplu, valorile ajung la server pe un canal separat de comanda SQL. Oricat de 'rautacios' ar fi textul, nu poate schimba STRUCTURA interogarii."},

    {"runda": 4, "categorie": "with-cursor", "puncte": 2,
     "cod": 'with conn.cursor() as c:\n    c.execute("SELECT * FROM useri")',
     "intrebare": "Care e principalul beneficiu al lui `with conn.cursor() as c:` fata de `c = conn.cursor()`?",
     "optiuni": {"A": "e mai rapid la executie", "B": "cursorul se inchide automat la finalul blocului, chiar daca apare o eroare pe drum",
                 "C": "permite executarea a mai multor interogari simultan", "D": "evita nevoia de conn.commit()"},
     "corect": "B",
     "explicatie": "Exact ca la open() pentru fisiere: `with` inchide AUTOMAT cursorul la iesirea din bloc, chiar si cand apare o exceptie - nu mai trebuie sa scrii tu c.close()."},


    # ---------- RUNDA 5: PYMYSQL - EXECUTEMANY, FETCH, COMMIT & ROWCOUNT ----------
    {"runda": 5, "categorie": "fetchone-vs-fetchall", "puncte": 2,
     "cod": 'cur.execute("SELECT COUNT(*) FROM useri")\nrezultat = cur.fetchone()\nprint(rezultat)',
     "intrebare": "Ce tip de date returneaza fetchone() aici?",
     "optiuni": {"A": "un numar intreg simplu", "B": "un tuplu, ex (5,)",
                 "C": "o lista de tupluri", "D": "None"},
     "corect": "B",
     "explicatie": "fetchone() returneaza mereu UN TUPLU (chiar si cu o singura valoare) sau None daca nu mai e niciun rand. Ca sa obtii doar numarul, trebuie rezultat[0]."},

    {"runda": 5, "categorie": "commit-obligatoriu", "puncte": 3,
     "cod": 'with conn.cursor() as c:\n    c.execute("INSERT INTO useri (nume) VALUES (%s)", ("Test",))\nconn.close()',
     "intrebare": "Ce se intampla cu acest INSERT, avand in vedere ca lipseste conn.commit()?",
     "optiuni": {"A": "se salveaza normal la inchiderea conexiunii", "B": "modificarea NU se salveaza in baza de date (se pierde)",
                 "C": "Error la close()", "D": "se salveaza, dar doar temporar, pana la urmatorul restart"},
     "corect": "B",
     "explicatie": "conn.commit() e OBLIGATORIU dupa INSERT/UPDATE/DELETE. Fara el, modificarea ramane doar intr-o tranzactie deschisa si se pierde la close()."},

    {"runda": 5, "categorie": "executemany", "puncte": 1,
     "cod": 'cur.executemany(\n    "INSERT INTO useri (nume) VALUES (%s)",\n    [("Ana",), ("Ion",), ("Maria",)]\n)',
     "intrebare": "Care e principalul avantaj al executemany() fata de un for cu execute() repetat?",
     "optiuni": {"A": "trimite toate randurile intr-o singura calatorie la server, mai rapid decat cate un execute() pentru fiecare rand", "B": "executemany() valideaza automat datele",
                 "C": "executemany() face commit automat", "D": "nu exista nicio diferenta, doar sintaxa mai scurta"},
     "corect": "A",
     "explicatie": "Cu un for + execute(), fiecare rand inseamna un 'du-te-vino' separat la server. executemany() trimite acelasi SQL cu TOATE randurile deodata."},

    {"runda": 5, "categorie": "rowcount", "puncte": 3,
     "cod": "with conn.cursor() as c:\n    c.execute(\"UPDATE useri SET varsta = 99 WHERE nume = 'Nume Inexistent'\")\n    afectate = c.rowcount\nconn.commit()\nprint(afectate)",
     "intrebare": "Ce afiseaza, presupunand ca niciun user nu are acel nume?",
     "optiuni": {"A": "Error", "B": "0",
                 "C": "None", "D": "1"},
     "corect": "B",
     "explicatie": "cur.rowcount spune cate randuri au fost AFECTATE de comanda. Daca WHERE nu se potriveste cu niciun rand, UPDATE-ul ruleaza FARA erori, dar afecteaza 0 randuri."},

    {"runda": 5, "categorie": "like-parametrizat", "puncte": 3,
     "cod": 'fragment = "an"\ncur.execute(\n    "SELECT nume FROM useri WHERE nume LIKE %s",\n    (f"%{fragment}%",)\n)',
     "intrebare": "De ce se construieste tiparul LIKE (%...%) in Python, si NU direct in SQL ca \"...LIKE '%%s%'\"?",
     "optiuni": {"A": "SQL nu suporta wildcard-uri langa %s", "B": "%s e locul gol pentru INTREAGA valoare parametrizata; wildcard-urile trebuie incluse in valoarea trimisa ca parametru, nu amestecate cu sintaxa SQL",
                 "C": "e doar o conventie de stil, fara efect real", "D": "LIKE nu functioneaza cu parametri deloc"},
     "corect": "B",
     "explicatie": "%s reprezinta INTREAGA valoare parametrizata. De aceea tiparul complet (%text%) se construieste in Python si se trimite CA PARAMETRU - la fel ca orice alta valoare, in siguranta."},
]


# =============================================================
# CONFIGURARE INITIALA
# =============================================================
punctaj_maxim = 0
for q in intrebari:
    punctaj_maxim += q["puncte"]

scor                  = 0
intrebari_corecte     = 0
categorii_stapanite   = set()
intrebari_gresite     = []
runda_curenta         = 0


print("=" * 62)
print("===   QUIZ INTERVIU JUNIOR PYTHON  -  SQL + PyMySQL   ===")
print("=" * 62)
print()
print("Fiecare intrebare are o secventa de COD (SQL sau Python)")
print("si o EXPLICATIE dupa raspuns. Citeste codul cu atentie")
print("inainte sa raspunzi.")
print()

nume = input("Numele jucatorului (Enter -> 'Candidat'): ").strip()
if nume == "":
    nume = "Candidat"
print(f"\nSucces, {nume}!  Q + Enter = iesire devreme.\n")


# =============================================================
# MOTORUL QUIZ-ULUI
# =============================================================

i = 0
abandonat = False

while i < len(intrebari) and not abandonat:
    q = intrebari[i]

    # Antet de runda
    if q["runda"] != runda_curenta:
        runda_curenta = q["runda"]
        titluri = {
            1: "SQL - CREATE TABLE, TIPURI DE DATE & CONSTRANGERI",
            2: "SQL - SELECT, WHERE, LIKE, ORDER BY",
            3: "SQL - UPDATE, DELETE, FOREIGN KEY & JOIN",
            4: "PYMYSQL - CONECTARE, PARAMETRIZARE & SQL INJECTION",
            5: "PYMYSQL - EXECUTEMANY, FETCH, COMMIT & ROWCOUNT",
        }
        print()
        print("=" * 62)
        print(f"  RUNDA {runda_curenta}:  {titluri[runda_curenta]}")
        print("=" * 62)
        print()

    # Afisam intrebarea cu codul
    print(f"Q{i + 1}  [{q['categorie']}, {q['puncte']}p]  -  {q['intrebare']}")
    print()
    if q["cod"]:
        print("    --- COD ---")
        for linie in q["cod"].split("\n"):
            print(f"    {linie}")
        print("    -----------")
        print()
    for litera in ("A", "B", "C", "D"):
        print(f"    {litera})  {q['optiuni'][litera]}")
    print()

    # Validare input
    raspuns = ""
    while True:
        raspuns = input("Raspunsul tau (A/B/C/D, Q=iesire): ").strip().upper()
        if raspuns in ("A", "B", "C", "D", "Q"):
            break
        print("  ! Alege A, B, C, D — sau Q ca sa iesi.")

    if raspuns == "Q":
        abandonat = True
        print("\n(ai iesit din quiz)\n")
        break

    # Verificare + AFISARE EXPLICATIE (mereu)
    corect = (raspuns == q["corect"])
    if corect:
        scor += q["puncte"]
        intrebari_corecte += 1
        categorii_stapanite.add(q["categorie"])
        print(f"  >>> CORECT! +{q['puncte']}p   (scor: {scor}/{punctaj_maxim})")
    else:
        intrebari_gresite.append({
            "nr": i + 1,
            "categorie": q["categorie"],
            "raspuns_dat": raspuns,
            "raspuns_corect": q["corect"],
        })
        print(f"  >>> Hmm, nu. Raspuns corect: {q['corect']}) {q['optiuni'][q['corect']]}")
        print(f"      (scor: {scor}/{punctaj_maxim})")

    # Explicatia se afiseaza MEREU (si la corect, si la gresit)
    print(f"  DE CE: {q['explicatie']}")
    print()
    i += 1


# =============================================================
# RAPORT FINAL
# =============================================================
print("=" * 62)
print(f"===          RAPORT INTERVIU  -  {nume}          ===")
print("=" * 62)

procent = (scor / punctaj_maxim * 100) if punctaj_maxim > 0 else 0
print(f"\n  scor:                {scor} / {punctaj_maxim} puncte  ({procent:.0f}%)")
print(f"  intrebari corecte:   {intrebari_corecte} / {i}")

# Evaluare in stil interviu
print()
if procent >= 85:
    print(f"  *** {nume}: profil JUNIOR SOLID — gata de proiecte reale cu SQL/PyMySQL.")
elif procent >= 65:
    print(f"  ** {nume}: profil JUNIOR DECENT — mai cizelam gotcha-urile.")
elif procent >= 45:
    print(f"  * {nume}: profil INCEPATOR — fundamentele sunt, ne trebuie practica.")
else:
    print(f"  {nume}: revizuiti materialul; aproape sigur reusiti la a doua iteratie.")

# Categorii stapanite
print()
print(f"  categorii stapanite ({len(categorii_stapanite)}):")
if categorii_stapanite:
    for cat in sorted(categorii_stapanite):
        print(f"    + {cat}")
else:
    print("    (inca niciuna)")

# Punctele slabe — categorii greșite
if intrebari_gresite:
    print()
    print(f"  zone slabe (de reluat inainte de interviu):")
    zone_slabe = set()
    for g in intrebari_gresite:
        zone_slabe.add(g["categorie"])
    for cat in sorted(zone_slabe):
        print(f"    - {cat}")

    print()
    print(f"  intrebari de revazut:")
    for g in intrebari_gresite:
        print(f"    Q{g['nr']}  [{g['categorie']}]  ai zis {g['raspuns_dat']}, corect {g['raspuns_corect']}")

print()
print("=" * 62)
print("Pregateste-te de interviu: relueaza intrebarile gresite,")
print("apoi reia quiz-ul. La interviu, EXPLICATIA conteaza la fel")
print("de mult cat raspunsul.")
print("=" * 62)