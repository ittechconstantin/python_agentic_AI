# DECORATORI IN PYTHON  (@decorator)
# =============================================================
# Un DECORATOR este o functie care primeste o ALTA functie si
# intoarce o varianta "infasurata" a ei - de obicei cu ceva
# in plus (logare, masurare timp, cache, validare, autorizare).

#
# DE CE sunt utili?
#   - codul devine clar la citire: vezi imediat ce face "in plus"
#       @necesita_login          <-  citesti si stii instant regula
#       def vezi_facturi(): ...
#   - separa logica functiei (ce face) de logica "din jur"
#     (logare, timp, securitate) - nu le amesteci
#   - REFOLOSIRE: acelasi decorator pe zeci de functii, fara
#     sa copiezi acelasi cod peste tot
#
# De ce ai nevoie ca sa intelegi decoratorii (recap sesiuni 11-13):
#   - functiile sunt OBIECTE: le poti pune in variabile, le poti
#     da ca argument, le poti intoarce din alte functii
#   - closures: o functie interioara "tine minte" variabile din
#     functia exterioara
#   - *args / **kwargs: impachetezi ORICE argumente si le trimiti
#     mai departe
# =============================================================


# #############################################################
# PARTEA 1 - BAZELE, PAS CU PAS
# #############################################################


# 1. RECAP: O FUNCTIE POATE INTOARCE O ALTA FUNCTIE
# -------------------------------------------------------------

# Problema: avem magazine in mai multe tari, fiecare cu alt TVA:
#   Romania = 21% ,  Ungaria = 27%.

# --- VARIANTA 1: o singura functie ---------------------------
# Merge, DAR trebuie sa scriu procentul de TVA la FIECARE apel.

def pret_cu_tva(pret, tva):
    return pret + (pret * tva / 100)

print(pret_cu_tva(100, 21))  # 121.0
print(pret_cu_tva(250,21))  # 302.5
print(pret_cu_tva(100, 27))  # 127.0

# Probleme:
#   - repet "21" peste tot (usor de gresit, scrii din greseala 12)
#   - daca se schimba TVA-ul, trebuie sa-l modific in toate locurile
#   - amestec doua lucruri: "ce procent" si "ce suma"

# --- VARIANTA 2: functie care INTOARCE o functie -------------
# Configurez procentul O SINGURA DATA si primesc inapoi o functie
# gata "setata" pe acel procent. Functia interioara TINE MINTE
# procentul (asta se numeste closure) - de aici nevoia de imbricare.

def creeaza_calcul_tva(procent):
    def calcul_tva(suma):    # functia interioara stie deja 'procent'
        return suma + (suma * procent / 100)
    return calcul_tva        # o intoarce ca OBIECT, fara paranteza


# Configurez o data, pe tara:
tva_ro = creeaza_calcul_tva(21)  # tva_ro este o functie setata pentru 21%
tva_hu = creeaza_calcul_tva(27)  # tva_hu este o functie setata pentru 27%


# Acum apelez curat, FARA sa mai repet procentul:
print(tva_ro(100))      # 121.0
print(tva_ro(250))      # 302.5
print(tva_hu(100))      # 127.5

# Asta e exact motivul pentru "functie in functie":
#   functia exterioara = CONFIGURAREA (procentul, o data)
#   functia interioara = MUNCA propriu-zisa (pe fiecare suma)
#
# Tine minte si diferenta: `tva_ro` e functia (obiectul),
# iar `tva_ro(100)` o ruleaza si da rezultatul.

print(tva_ro)        # o functie <function...
print(tva_ro(200))   # 241  -> rezultatul functiei calcul_tva


# 2. PRIMUL DECORATOR, SCRIS MANUAL
# -------------------------------------------------------------
# La fel ca la TVA: intai vedem PROBLEMA, apoi solutia.
#
# Vrem sa afisam in consola un mesaj CAND incepe si un mesaj CAND
# se termina o operatiune, ca sa vedem ce se executa si in ce ordine.

# --- VARIANTA 1: scriem print-urile DIRECT in fiecare functie ---
# Merge, dar daca avem 3 operatiuni, copiem aceleasi 2 print-uri
# in toate. Si amestecam doua lucruri: "ce face functia" cu
# "ce afisam in jurul ei".

def genereaza_raport_v1():
    print("-> incepe genereaza_raport_v1")
    print("   ... construiesc raportul ...")    # treaba ADEVARATA
    print("<- gata genereaza_raport_v1")

def trimite_email_v1():
    print("-> incepe trimite_email_v1")
    print("   ... trimit email-ul ...")         # treaba ADEVARATA
    print("<- gata trimite_email_v1")

genereaza_raport_v1()
trimite_email_v1()


# Probleme:
#   - acelasi cod de logare copiat in fiecare functie
#   - daca vreau sa schimb formatul logului, modific in N locuri
#   - functia nu mai e "curata": treaba reala e ingropata printre log-uri

# --- VARIANTA 2: scriem logarea O DATA, ca DECORATOR -------------
# Un decorator e o functie care:
#   - PRIMESTE o functie  (fn)
#   - construieste o functie NOUA (wrapper) care o "infasoara":
#     face ceva inainte, apeleaza fn, face ceva dupa
#   - INTOARCE functia noua
#

def cu_log(fn):
    def wrapper():
        print(f"-> incepe {fn.__name__}()")
        rezultat = fn()  # <- Aici apelam functia orginala
        print(f"<- gata {fn.__name__}()")
        return rezultat # intoarcem ceea ce a intors functia fn
    return wrapper

# Functii raman CURATE, doar treaba lor, fara cod de logare.
def genereaza_raport():
    print("   ... construiesc raportul ...")

def trimite_email():
    print("   ... trimit email-ul ...")

# "Decoram" MANUAL: inlocuim functia veche cu varianta infasurata.
# cu_log(genereaza_raport) intoarce `wrapper`; il punem inapoi in
# acelasi nume, deci de acum `genereaza_raport` = functia cu log.

genereaza_raport = cu_log(genereaza_raport)
trimite_email = cu_log(trimite_email())


# -> incepe genereaza_raport
#    ... construiesc raportul ...
# <- gata genereaza_raport

# acelasi decorator, refolosit -> asta e castigul: scris o data, aplicat oriunde
# -> incepe trimite_email
#    ... trimit email-ul ...
# <- gata trimite_email


# 3. SINTAXA  @decorator  -  acelasi lucru, dar elegant
# -------------------------------------------------------------
# La sectiunea 2 am scris reasignarea de mana, de doua ori:
#       genereaza_raport = cu_log(genereaza_raport)
#       trimite_email    = cu_log(trimite_email)
# E plictisitor si usor de uitat. Python ne da o scurtatura:
# punem @nume_decorator DEASUPRA functiei.
#
#   @cu_log
#   def x(): ...
#
# este EXACT acelasi lucru cu:
#
#   def x(): ...
#   x = cu_log(x)
#
# Adica @cu_log de mai jos inseamna, dupa def, automat:
#   backup_baza_date = cu_log(backup_baza_date)

@cu_log
def backup_baza_date():
    print("   ... backup-ul datelor ...")


backup_baza_date()
# Nicio reasignare manuala - @cu_log a facut-o pentru noi.


# 4. DECORATOR CARE MERGE PE ORICE FUNCTIE  (*args, **kwargs)
# -------------------------------------------------------------
# Atentie la `cu_log` de mai sus: wrapper-ul lui era  def wrapper():
# adica NU primeste niciun argument. A mers pe genereaza_raport()
# pentru ca nici aceasta nu avea argumente.
#
# Dar ce se intampla daca decoram o functie CU argumente, ca aduna(a, b)?
# Wrapper-ul ar fi apelat ca wrapper(3, 5), insa el nu accepta argumente.

@cu_log
def aduna_gresit(a, b):
    return a + b

try:
    aduna_gresit(3, 5)
except TypeError as e:
    print(f"Eroare: {e}")

# Problema: decoratorul NU stie cate argumente are functia decorata.
# Solutia: wrapper-ul primeste *args, **kwargs (= "orice argumente")
# si le trimite mai departe, neschimbate, catre fn.

def cu_log_v2(fn):
    def wrapper(*args, **kwargs):
        print(f"<- incepe {fn.__name__} apelata cu argumente:args =  {args}, kwargs = {kwargs}")
        rezultat = fn(*args, **kwargs) # le trimitem mai departe
        print(f"-> gata {fn.__name__} apelata cu argumente:args =  {args}, kwargs = {kwargs}")
        return rezultat
    return wrapper

@cu_log_v2
def aduna(a, b):
    return a + b

aduna(3, 5)

@cu_log_v2
def saluta(nume, mesaj = "Salut"):
    return f"{mesaj} {nume}!"

print(saluta("Ana"))
print(saluta("Ana", mesaj = 'Buna ziua,'))

# 5. GRESEALA #1: SA UITI SA INTORCI REZULTATUL
# -------------------------------------------------------------
# In wrapper, daca apelezi fn(...) dar uiti `return`, apelantul
# primeste None - desi functia originala calculase corect.
# E cea mai frecventa greseala la inceput si e perfida: codul nu
# crapa, doar da rezultate gresite (None) pe care le observi tarziu.


def fara_return(fn):
    def wrapper(*args, **kwargs):
        rezultat = fn(*args, **kwargs)
        return rezultat
    return wrapper

@fara_return
def pret_total(bucati, pret_per_bucata):
    return bucati * pret_per_bucata

print(pret_total(5, 10))


# Corect: wrapper-ul TREBUIE sa returneze ce intoarce fn.


# 6. GRESEALA #2: SE PIERDE "IDENTITATEA" FUNCTIEI
# -------------------------------------------------------------
# Tine minte de la sectiunea 3: @deco inlocuieste functia cu `wrapper`.
# Deci dupa decorare, Python "crede" ca functia se numeste wrapper -
# numele real si docstring-ul (descrierea functiei) se pierd.
#
# Fiecare functie are niste etichete despre ea insasi:
#   __name__  = numele functiei (text)
#   __doc__   = docstring-ul (descrierea dintre """ ... """)

def deco_simplu(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper

@deco_simplu
def calculeaza_tva(suma):
    """Calcula TVA pentru o suma de bani."""
    return suma * 0.21

print(calculeaza_tva.__name__)    # wrapper <- pierde numere real
print(calculeaza_tva.__doc__)     # None

# De ce conteaza: la debugging vezi "wrapper" peste tot (nu stii ce functie e),
# help(functie) nu mai arata descrierea, iar unele framework-uri (Flask,
# pytest) se bazeaza pe __name__ si se incurca daca toate se cheama "wrapper".


# 7. SOLUTIA: functools.wraps  (foloseste-l MEREU)
# -------------------------------------------------------------
# `functools.wraps` e un mic decorator gata facut care copiaza
# etichetele (__name__, __doc__, ...) de la functia originala in
# wrapper. Practic: o singura linie reapara tot ce am pierdut la pct.6.
# Regula de aur: pune @wraps(fn) pe ORICE wrapper pe care il scrii.


from functools import wraps

def deco_simplu(fn):

    @wraps(fn)   # <- aici copiem etichetele din fn in wrapper
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper

@deco_simplu
def calculeaza_tva(suma):
    """Calcula TVA pentru o suma de bani."""
    return suma * 0.21

print(calculeaza_tva.__name__)    # calculeaza_tva
print(calculeaza_tva.__doc__)     # Calcula TVA pentru o suma de bani.



# #############################################################
# PARTEA 2 - DECORATORI REALI (business logic)
# #############################################################
# De aici incolo, exact tiparele pe care le vei vedea in aplicatii
# reale. Folosim o mini-tema: un sistem de comenzi / cont bancar.


# 8. AUDIT  -  "cine a facut ce si cand" (cu modulul logging)
# -------------------------------------------------------------
# La sectiunea 2 am scris cu print(). In aplicatii reale,
# pentru asta exista un tool mai bun: modulul `logging`.
#
# Ce e `logging`, pe scurt:
#   - e ca print(), DAR fiecare mesaj are un NIVEL de importanta:
#       log.info("...")     -> mesaj normal, informativ
#       log.warning("...")  -> ceva suspect, atrage atentia
#       log.error("...")    -> o problema serioasa
#   - de aceea scriem `.info` si nu `print`: spunem ca acest mesaj
#     e unul informativ (INFO), nu o eroare.
#
# Compara:
#       print("comanda plasata")     ->  comanda plasata
#       log.info("comanda plasata")  ->  INFO | comanda plasata
#   adica logging adauga singur eticheta de nivel (INFO/WARNING/...).

import logging
import sys
import time

# basicConfig = REGLAJUL jurnalului, facut O SINGURA DATA la pornire.
# Gandeste-te la el ca la setarile generale ale mesajelor:
#   level  = de la ce nivel in sus sa AFISEZE mesajele.
#            level=INFO  -> arata INFO, WARNING, ERROR
#            (daca am pune level=WARNING, mesajele .info NU ar mai aparea -
#             e ca un buton de "volum" pentru cat de multe mesaje vezi)
#   format = cum arata fiecare rand. "{levelname} | {message}"
#            inseamna:  NIVELUL  apoi  " | "  apoi  textul mesajului.
#            E un SABLON: logging completeaza {levelname} si {message}
#            la fiecare mesaj (de-aia nu e f-string - nu se umple acum).
#   style  = "{" ii spune lui logging sa foloseasca acolade {} in format
#            (in loc de stilul vechi cu %(...)s).
#   stream = UNDE scrie mesajele. Implicit logging scrie pe "stderr"
#            (fluxul de erori), care in unele editoare apare separat,
#            cu rosu, sau la sfarsit. Il punem pe stdout ca sa apara
#            la rand cu print()-urile noastre.

logging.basicConfig(level=logging.INFO, format="{levelname} | {message}", style="{", stream=sys.stdout)


# getLogger = ne da obiectul "jurnal" pe care chemam .info / .warning.
# Ii dam un nume ("magazin") - util ca sa stii din ce parte vine mesajul.

log = logging.getLogger("magazin")

# `audit` = decorator care scrie in jurnal CE functie a fost apelata,
# cu ce argumente, si CE a returnat. Tipic pentru istoric/conformitate.

def audit(fn):
    def wrapper(*args, **kwargs):
        log.info(f"ACTIUNE: {fn.__name__} args={args} kwargs={kwargs}")
        rezultat = fn(*args, **kwargs)
        log.error(f"REZULTAT: {fn.__name__} -> {rezultat}")
        return rezultat
    return wrapper


@audit
def plaseaza_comanda(nume_client, produs, cantitate):
    return f"Comanda #1001 pentru {nume_client}: {cantitate}x {produs}"

plaseaza_comanda("Ana", "tastatura", 2)

# Pe ecran apar 2 randuri (intrarea si rezultatul), prefixate cu "INFO |":
# INFO | ACTIUNE: plaseaza_comanda args=('Ana', 'tastatura', 2) kwargs={}
# INFO | REZULTAT: plaseaza_comanda -> 'comanda #1001 pentru Ana: 2x tastatura'

# 9. TIMING  -  cat de lenta e o operatiune?
# -------------------------------------------------------------
# Cand un raport / o interogare / un export e lent, vrei sa stii
# CAT dureaza. Ideea: noteaza ora INAINTE, ora DUPA, si scazi.
#
# Tool: time.perf_counter() = un "cronometru" precis. Iti da un
# numar de secunde; singur, numarul nu inseamna nimic, dar DIFERENTA
# dintre doua citiri = cat timp a trecut intre ele.
#
# De ce decorator si nu sa scriem cronometrarea in functie? Ca sa nu
# amestecam "ce face functia" cu "cat dureaza" - exact ca la log.

def cronometru(fn):
    def wrapper(*args,  **kwargs):
        start = time.perf_counter()
        rezultat = fn(*args, **kwargs)
        stop = time.perf_counter()
        durata = stop - start
        log.info(f"{fn.__name__} a durat {durata:.2f} ms")
        return rezultat
    return wrapper

@cronometru
def genereaza_raport_vanzari(numar_linii):
    total = 0
    for i in range(numar_linii):
        total += i
    return total

# print(genereaza_raport_vanzari(500000000))


# Pe ecran vezi intai durata (logata de decorator), apoi rezultatul:
# INFO | [timp] genereaza_raport_vanzari a durat 9.8 ms
# 249999500000


# 10. CACHE  -  nu recalcula acelasi lucru de doua ori
# -------------------------------------------------------------
# Daca o functie e "scumpa" (calcul greu, citire din fisier, apel pe
# internet) si o chemi de mai multe ori cu ACELEASI argumente, e risipa
# sa o recalculezi de fiecare data - rezultatul e mereu acelasi.
#
# Solutia: tinem un dictionar in care notam, pentru fiecare
# set de argumente, rezultatul. Asta se numeste CACHE / "memoization".
#   - cheia  = argumentele primite
#   - valoarea = rezultatul calculat pentru ele
# Data viitoare cand vin aceleasi argumente, dam raspunsul din dictionar,
# instant, fara sa mai rulam functia.
#   HIT  = "l-am gasit in dictionar" (rapid)
#   MISS = "nu e in caiet, il calculez si il notez" (prima oara)


def cache_simplu(fn):
    memorie = {}
    def wrapper(*args, **kwargs):
        if args in memorie:
            log.info(f"HIT: {fn.__name__} args={args} kwargs={kwargs}")
            return memorie[args]  # dam rezultatul din memorie
        else:
            log.info(f"MISS: {fn.__name__} args={args} kwargs={kwargs}")
            rezultat = fn(*args, **kwargs) # apelam functia
            memorie[args] = rezultat       # stocam rezultatul in memorie
            return rezultat                # returnam rezultatul
    return wrapper

@cache_simplu
def pret_cu_discount(pret, discount):
    time.sleep(0.05)
    return round(pret * (1 - discount/100), 2)


print(pret_cu_discount(100, 10))
print(pret_cu_discount(100, 10))
print(pret_cu_discount(200, 30))



# Pe ecran: doua MISS-uri si un HIT, apoi rezultatele 80.0 / 80.0 / 225.0
# Nota: cache-ul merge doar daca rezultatul depinde DOAR de argumente
# (pentru aceleasi argumente, mereu acelasi raspuns).
#
#
# 11. VALIDARE  -  respinge inputuri gresite INAINTE de executie
# -------------------------------------------------------------
# "A valida" = a verifica daca datele primite respecta niste reguli
# inainte de a face treaba (ex: o suma de bani nu poate fi negativa).
#
# Cum oprim functia daca regula nu e respectata? Cu `raise`:
#   raise ValueError("mesaj")
# inseamna "arunca o eroare" - executia se opreste pe loc si sare la
# blocul try/except care prinde eroarea (daca exista unul).
#
# De ce ca decorator? Scrii regula O DATA si o pui pe orice functie
# care primeste o suma - fara sa copiezi acelasi `if` peste tot.

def suma_pozitiva(fn):
    def wrapper(suma, *args, **kwargs):
        if suma < 0:
            raise ValueError("Suma nu poate fi negativa")
        return fn(suma, *args, **kwargs)
    return wrapper


@suma_pozitiva
def depunere(suma):
    return f"Am retras suma {suma}"

try:
    depunere(-500)
except ValueError as e:
    print(e)


# 12. AUTORIZARE  -  "cine are voie sa apeleze functia"
# -------------------------------------------------------------
# Tiparul clasic din aplicatiile web (ex: @login_required din Django).
# Verificam un "utilizator curent" inainte de a permite operatiunea.
#
# NOU: acesta e un decorator CU ARGUMENT -> @necesita_rol("admin").
# Cand decoratorul are paranteze, avem 3 NIVELE de functii:
#   @necesita_rol("admin")  inseamna  fn = necesita_rol("admin")(fn)
#   - intai ruleaza necesita_rol("admin") -> primeste CONFIGURAREA ("admin")
#     si intoarce un decorator
#   - acel decorator primeste apoi functia (fn)
# De aceea:
#   def necesita_rol(rol_cerut):   <- nivel 1: primeste configurarea
#       def decorator(fn):          <- nivel 2: primeste functia
#           def wrapper(*a, **kw):  <- nivel 3: ruleaza la fiecare apel
# Regula: @nume -> 2 nivele;  @nume(...) -> 3 nivele.

# Stare globala simpla, ca sa simulam sesiunea unui utilizator logat.


utilizator_curent = {'nume': 'Ana', 'rol': 'admin'}


def necesita_rol(rol_cerut):            # nivel 1: configurare (ce rol e necesar)
    def decorator(fn):                  # nivel 2: functia de projetat
        def wrapper(*args, **kwargs):   # nivel 3: rulat la fiecare apel
            if utilizator_curent['rol'] == rol_cerut:
                return fn(*args, **kwargs)
            else:
                raise PermissionError("Nu ai permisiunea de a accesa aceasta pagina")
            return fn(*args, **kwargs)
        return wrapper
    return decorator


@necesita_rol("admin")
def sterge_baza_date():
    print("Baza de date a fost stearsa!")

try:
    sterge_baza_date()
except PermissionError as e:
    print(e)


# 13. MAI MULTI DECORATORI PE ACEEASI FUNCTIE  (ordinea conteaza!)
# -------------------------------------------------------------
# Poti pune mai multi decoratori pe aceeasi functie ("ii stivuiesti").
# Se aplica DE JOS IN SUS:
#
#   @audit
#   @cronometreaza
#   def f(): ...
#
# inseamna:  f = audit(cronometreaza(f))
# (cel de jos se aplica primul, apoi cel de deasupra il inveleste)
#
# La APEL, ordinea e ca niste cutii una in alta: cel de DEASUPRA (audit)
# e cutia Exterioara - ruleaza primul si ultimul; cel de JOS (cronometreaza)
# e mai aproape de functia reala.


# Ordinea afisarilor:
#   1) audit logheaza ACTIUNEA (intrarea)
#   2) cronometreaza porneste ceasul si ruleaza functia
#   3) cronometreaza afiseaza timpul
#   4) audit logheaza REZULTATUL (iesirea)


# =============================================================
# RECAP / GRESELI FRECVENTE
# =============================================================
# - In wrapper foloseste *args / **kwargs ca sa mearga pe orice functie
# - Mereu RETURNEAZA  fn(*args, **kwargs)  (altfel pierzi rezultatul)
# - Pune @wraps(fn) pe wrapper ca sa pastrezi numele si docstring-ul
# - Decoratorul fara argument  = 2 nivele:  deco(fn) -> wrapper
# - Decoratorul cu argument    = 3 nivele:  deco(arg) -> decorator(fn) -> wrapper
# - Decoratorii stivuiti se aplica DE JOS IN SUS:  @a @b f  ==  a(b(f))
# - Cei mai folositi nu ii scrii tu: @property, @staticmethod,
#   @classmethod, @lru_cache, @dataclass
#
# SABLON CANONIC (fara argumente):
#     def deco(fn):
#         @wraps(fn)
#         def wrapper(*args, **kwargs):
#             # cod INAINTE
#             rezultat = fn(*args, **kwargs)
#             # cod DUPA
#             return rezultat
#         return wrapper
#
# SABLON CU ARGUMENTE:
#     def deco(config):
#         def decorator(fn):
#             @wraps(fn)
#             def wrapper(*args, **kwargs):
#                 # foloseste config + fn
#                 return fn(*args, **kwargs)
#             return wrapper
#         return decorator
#
# =============================================================


