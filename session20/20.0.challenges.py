from abc import ABC, abstractmethod

# CHALLENGE 1  -  EXPORTATOR DE DATE CU ANTET COMUN
# #############################################################
#
# CONTEXT (caz real)
# ------------------
# O aplicatie de raportare trebuie sa exporte aceleasi date in mai
# multe formate: azi doar CSV, dar maine poate JSON sau XML pentru alt
# client. Indiferent de format, fiecare fisier exportat trebuie sa
# inceapa cu un ANTET clar (titlul raportului), ca cel care il primeste
# sa stie imediat ce contine - si acest antet trebuie sa arate IDENTIC,
# indiferent de format.
#
# Daca ati pune logica antetului in FIECARE exportator (CSV, JSON...),
# ati repeta acelasi cod de 3-4 ori si, la o schimbare de format al
# antetului, ati uita sa il modificati peste tot.
#
# CE TREBUIE SA FACA SOLUTIA
# --------------------------
# 1. O clasa abstracta `Exporter(ABC)` cu o metoda abstracta
#    `exporta(self, date)` care intoarce STRING-ul cu datele, in
#    formatul specific (fara antet).
# 2. O metoda CONCRETA `exporta_cu_antet(self, date, titlu)`, scrisa o
#    singura data in clasa abstracta: apeleaza `self.exporta(date)` si
#    lipeste deasupra o linie `=== {titlu} ===`.
# 3. O implementare concreta `ExporterCSV(Exporter)` care transforma o
#    lista de tupluri `(nume, varsta)` intr-un text CSV (o linie per
#    persoana, valorile separate prin virgula).
#
# CERINTE
# -------
#   - `Exporter` nu poate fi instantiata direct.
#   - `ExporterCSV.exporta` NU include antetul - doar datele brute.
#   - antetul se adauga DOAR in `exporta_cu_antet`, o singura data,
#     in clasa parinte (nu il duplicati in ExporterCSV).
#
# OUTPUT ASTEPTAT (pentru date = [("Ana", 29), ("Bogdan", 34)])
# ---------------------------------------------------------------
#   2)
#   === Raport Useri ===
#   Ana,29
#   Bogdan,34
# =============================================================

print("\n--- Exercitiul 1 ---")
class Exporter(ABC):

    @abstractmethod
    def exporta(self):
        pass

    def exporta_cu_antet(self):
        return f"Titlu"


class ExporterCSV(Exporter):

    def exporta(self):
        return "....date CSV...."

class ExporterJSON(Exporter):
    def exporta(self):
        return "....date JSON...."


# fisier_json = ExporterJSON()
# fisier_json.exporta([("Ana", 29), ("Bogdan", 34)])

# #############################################################
# CHALLENGE 2  -  LOG HANDLER CU FORMATARE COMUNA
# #############################################################
#
# CONTEXT (caz real)
# ------------------
# O aplicatie trimite loguri catre destinatii diferite: azi doar in
# consola, dar in productie poate si intr-un fisier, sau catre un
# serviciu extern (Sentry, Datadog). Indiferent UNDE ajunge mesajul,
# FORMATUL lui - `[NIVEL] mesaj` - trebuie sa fie acelasi peste tot, ca
# oricine citeste logurile sa recunoasca imediat structura.
#
# Problema: daca fiecare handler isi formateaza singur mesajul, cineva
# poate uita nivelul, sau il poate scrie altfel (`ERROR:` in loc de
# `[ERROR]`) intr-un handler nou.
#
# CE TREBUIE SA FACA SOLUTIA
# --------------------------
# 1. O clasa abstracta `LogHandler(ABC)` cu o metoda abstracta
#    `scrie(self, mesaj_formatat)` - primeste mesajul GATA formatat si
#    decide doar UNDE il trimite.
# 2. O metoda CONCRETA `logheaza(self, nivel, mesaj)`, scrisa o singura
#    data in parinte: construieste `mesaj_formatat = f"[{nivel}] {mesaj}"`
#    si il paseaza catre `self.scrie(...)`.
# 3. O implementare concreta `ConsoleHandler(LogHandler)` a carei
#    `scrie` doar afiseaza mesajul cu `print`.
#
# CERINTE
# -------
#   - formatarea (`[NIVEL] mesaj`) exista o SINGURA DATA, in `logheaza`
#     din clasa abstracta - NU in `ConsoleHandler`.
#   - `ConsoleHandler.scrie` nu stie nimic despre nivel - primeste
#     mesajul deja gata format.
#
# OUTPUT ASTEPTAT (pentru logheaza("ERROR", "Conexiune pierduta..."))
# ---------------------------------------------------------------
#   3) Log:
#   [ERROR] Conexiune pierduta la baza de date
# =============================================================

print("\n--- Exercitiul 2 ---")
class LogHandler(ABC):

    @abstractmethod
    def scrie(self, mesaj_formatat):
        pass

    @abstractmethod
    def logheaza(self, nivel, mesaj):
        return f"[{nivel}] {mesaj}"

class ConsoleHandler(LogHandler):
    def scrie(self, mesaj_formatat):
        self.mesaj_formatat = mesaj_formatat

print(LogHandler.logheaza("3)", "ERROR", "Conexiune pierduta la baza de date"))

# #############################################################
# CHALLENGE 3  -  VALIDATOR DE CAMPURI DE FORMULAR
# #############################################################
#
# CONTEXT (caz real)
# ------------------
# Un formular de inregistrare are mai multe campuri (email, varsta,
# telefon...), fiecare cu propria regula de validare. Dar mesajul
# afisat userului - "valoarea asta e valida sau nu" - trebuie sa arate
# LA FEL pentru orice camp, ca interfata sa fie consistenta.
#
# Fara un contract comun, fiecare camp ar putea intoarce rezultatul
# altfel (True/False, "ok"/"eroare", 1/0...), si codul care afiseaza
# rezultatul ar trebui sa stie particularitatile fiecarui camp.
#
# CE TREBUIE SA FACA SOLUTIA
# --------------------------
# 1. O clasa abstracta `Camp(ABC)` cu o metoda abstracta
#    `valideaza(self, valoare)` care intoarce STRICT True sau False.
# 2. O metoda CONCRETA `raporteaza(self, valoare)`, scrisa o singura
#    data in parinte: apeleaza `valideaza` si intoarce un mesaj uniform
#    - `"'{valoare}' -> valid"` sau `"'{valoare}' -> INVALID"`.
# 3. Doua implementari concrete: `CampEmail` (valid daca are `@` SI `.`
#    in text) si `CampNumeric` (valid daca `valoare.isdigit()`).
#
# CERINTE
# -------
#   - `valideaza` intoarce DOAR True/False, niciodata mesajul final.
#   - mesajul ("valid"/"INVALID") se construieste o singura data, in
#     `raporteaza`, nu in fiecare tip de camp.
#
# OUTPUT ASTEPTAT
# ---------------
#   4) 'ana@test.com' -> valid
#   4) 'nu-e-email' -> INVALID
#   4) '12345' -> valid
#   4) '12a45' -> INVALID
# =============================================================



# #############################################################
# CHALLENGE 4  -  REPOSITORY PATTERN PENTRU USERI
# #############################################################
#
# CONTEXT (caz real)
# ------------------
# Azi tineti userii intr-un dict, in memorie (pentru teste/prototip).
# Maine vreti sa treceti la o baza de date reala. Codul din restul
# aplicatiei care intreaba "exista userul cu ID-ul asta?" NU ar trebui
# sa se schimbe deloc cand schimbati implementarea - asta e ideea din
# spatele "Repository pattern".
#
# CE TREBUIE SA FACA SOLUTIA
# --------------------------
# 1. O clasa abstracta `Repository(ABC)` cu doua metode abstracte:
#    `gaseste_dupa_id(self, id)` (intoarce obiectul sau None) si
#    `salveaza(self, obiect)` (il retine undeva).
# 2. O metoda CONCRETA `exista(self, id)`, scrisa o singura data in
#    parinte, care se bazeaza DOAR pe `gaseste_dupa_id` (nu stie nimic
#    despre UNDE stau datele).
# 3. O implementare concreta `UserRepositoryMemorie(Repository)` care
#    tine userii intr-un dict `{id: obiect}`.
#
# CERINTE
# -------
#   - `obiect` salvat e un dict cu cheia `"id"` (ex: `{"id": 1, ...}`).
#   - `exista` nu atinge direct dict-ul intern - trece PRIN
#     `gaseste_dupa_id`, ca sa mearga la fel indiferent de implementare.
#   - bonus: un repository care uita `salveaza` ramane tot abstract.
#
# OUTPUT ASTEPTAT
# ---------------
#   5) Exista user 1? True
#   5) Exista user 2? False
#   5) RepositoryIncomplet e tot abstract (lipseste salveaza)
# =============================================================



# #############################################################
# CHALLENGE 5  -  PARSER DE CONFIGURARE CU VALIDARE OBLIGATORIE
# #############################################################
#
# CONTEXT (caz real)
# ------------------
# O aplicatie citeste configurarea dintr-un fisier text (azi un format
# simplu `cheie=valoare;cheie=valoare`, maine poate YAML sau JSON). Dar
# indiferent de format, daca lipseste o cheie CRITICA (ex: `host`),
# aplicatia NU trebuie sa porneasca tacut cu o configurare incompleta -
# trebuie sa opreasca totul cu o eroare clara, cat mai devreme posibil.
#
# CE TREBUIE SA FACA SOLUTIA
# --------------------------
# 1. O clasa abstracta `ConfigParser(ABC)` cu o metoda abstracta
#    `parseaza(self, continut)` care intoarce un dict.
# 2. O metoda CONCRETA `incarca_validat(self, continut, cheie_obligatorie)`,
#    scrisa o singura data in parinte: apeleaza `parseaza`, verifica
#    daca `cheie_obligatorie` exista in rezultat si, daca NU, ridica
#    `ValueError` cu un mesaj clar; altfel intoarce config-ul.
# 3. O implementare concreta `ConfigParserSimplu(ConfigParser)` care
#    desparte `continut` dupa `;` (fiecare bucata e `cheie=valoare`).
#
# CERINTE
# -------
#   - validarea cheii obligatorii sta O SINGURA DATA, in clasa
#     abstracta - orice format nou de parser o mosteneste automat.
#   - eroarea trebuie sa fie `ValueError`, cu mesajul exact
#     `"Lipseste cheia obligatorie: <cheie>"`.
#
# OUTPUT ASTEPTAT (pentru "host=localhost;port=8080")
# ---------------------------------------------------------------
#   6) Config incarcat: {'host': 'localhost', 'port': '8080'}
#   6) Eroare: Lipseste cheia obligatorie: secret_key
# =============================================================