# QUIZ INTERVIU  -  intrebari tip interviu junior Python
#                   (*args, **kwargs, SCOPE)
# =============================================================
# Pe baza a tot ce s-a predat in 12.args_kwargs_scope.py.
# Fiecare intrebare contine:
#   - o SECVENTA DE COD (de tip "ce afiseaza? / ce eroare apare?")
#   - 4 variante A/B/C/D
#   - EXPLICATIE obligatorie dupa raspuns (afisata si cand
#     raspunzi corect — la interviu conteaza sa stii DE CE)
#
# Gotcha-urile clasice despre *args / **kwargs / scope:
#   - *args  -> argumentele pozitionale in plus vin ca TUPLU
#   - **kwargs -> argumentele keyword in plus vin ca DICT
#   - .get(cheie, default) pentru optiuni care pot lipsi
#   - unpacking la apel:  *lista  si  **dict
#   - capcana: lista trimisa fara *  -> un singur element in tuplu
#   - ordinea obligatorie:  normali -> *args -> **kwargs
#   - SCOPE: variabila locala nu se vede in afara (NameError)
#   - CITIT vs SCRIS la globale: nevoia de `global`
#   - obiecte mutabile: .append fara `global`
#   - nonlocal pentru functii imbricate
#
# Cum se ruleaza:
#   python3 12.1.quiz_interviu.py
#
# Apasa Q oricand pentru iesire.
# =============================================================


# =============================================================
# BANCA DE INTREBARI
# =============================================================
# Fiecare intrebare e un DICT cu:
#   runda       (int)    1..4
#   categorie   (str)
#   puncte      (int)    1 / 2 / 3 — dificultate
#   cod         (str)    secventa de cod (triple-quoted)
#   intrebare   (str)    intrebarea propriu-zisa
#   optiuni     (dict)   {"A": ..., "B": ..., "C": ..., "D": ...}
#   corect      (str)    "A" / "B" / "C" / "D"
#   explicatie  (str)    DE CE — afisata mereu dupa raspuns

intrebari = [
    # ---------- RUNDA 1: *args ----------
    {"runda": 1, "categorie": "args-suma", "puncte": 1,
     "cod": 'def aduna(*args):\n    return sum(args)\n\nprint(aduna(1, 2, 3))',
     "intrebare": "Ce afiseaza?",
     "optiuni": {"A": "6", "B": "123", "C": "(1, 2, 3)", "D": "eroare"},
     "corect": "A",
     "explicatie": "*args strange toate argumentele intr-un TUPLU (1, 2, 3). sum() il aduna -> 6."},

    {"runda": 1, "categorie": "args-tip", "puncte": 2,
     "cod": 'def f(*args):\n    print(type(args).__name__)\n\nf(1, 2)',
     "intrebare": "Ce afiseaza?",
     "optiuni": {"A": "list", "B": "tuple", "C": "dict", "D": "int"},
     "corect": "B",
     "explicatie": "Argumentele pozitionale in plus sunt PACHETATE intr-un TUPLU, nu intr-o lista. type(args).__name__ -> 'tuple'."},

    {"runda": 1, "categorie": "args-fix-plus-args", "puncte": 2,
     "cod": 'def eticheta(prefix, *valori):\n    return f"{prefix}: {len(valori)}"\n\nprint(eticheta("X", 10, 20, 30))',
     "intrebare": "Ce afiseaza?",
     "optiuni": {"A": "X: 4", "B": "X: 3", "C": "X: 0", "D": "eroare"},
     "corect": "B",
     "explicatie": "Primul argument ('X') intra in parametrul FIX prefix. Restul (10, 20, 30) merg in *valori -> tuplu cu 3 elemente -> 'X: 3'."},

    {"runda": 1, "categorie": "args-gol", "puncte": 1,
     "cod": 'def f(*args):\n    return len(args)\n\nprint(f())',
     "intrebare": "Ce afiseaza daca nu trimiti niciun argument?",
     "optiuni": {"A": "0", "B": "1", "C": "None", "D": "eroare"},
     "corect": "A",
     "explicatie": "Fara argumente, *args este un TUPLU GOL (). len(()) = 0. *args accepta si zero argumente."},

    {"runda": 1, "categorie": "args-unpacking", "puncte": 2,
     "cod": 'def aduna(*args):\n    return sum(args)\n\nnums = [1, 2, 3]\nprint(aduna(*nums))',
     "intrebare": "Ce afiseaza?",
     "optiuni": {"A": "[1, 2, 3]", "B": "6", "C": "eroare", "D": "123"},
     "corect": "B",
     "explicatie": "* la APEL DESPACHETEAZA lista: aduna(*nums) e ca aduna(1, 2, 3). args devine (1, 2, 3), sum -> 6."},


    # ---------- RUNDA 2: **kwargs ----------
    {"runda": 2, "categorie": "kwargs-len", "puncte": 1,
     "cod": 'def f(**kwargs):\n    return len(kwargs)\n\nprint(f(a=1, b=2, c=3))',
     "intrebare": "Ce afiseaza?",
     "optiuni": {"A": "3", "B": "6", "C": "1", "D": "eroare"},
     "corect": "A",
     "explicatie": "**kwargs strange argumentele keyword intr-un DICT {'a':1,'b':2,'c':3}. len -> 3 (numarul de chei)."},

    {"runda": 2, "categorie": "kwargs-tip", "puncte": 2,
     "cod": 'def f(**kwargs):\n    print(type(kwargs).__name__)\n\nf(x=1)',
     "intrebare": "Ce afiseaza?",
     "optiuni": {"A": "tuple", "B": "list", "C": "dict", "D": "set"},
     "corect": "C",
     "explicatie": "Argumentele de forma cheie=valoare sunt PACHETATE intr-un DICT. type(kwargs).__name__ -> 'dict'."},

    {"runda": 2, "categorie": "kwargs-get-default", "puncte": 2,
     "cod": 'def config(**opt):\n    return opt.get("port", 8080)\n\nprint(config(host="localhost"))',
     "intrebare": "Ce afiseaza?",
     "optiuni": {"A": "8080", "B": "None", "C": "localhost", "D": "eroare"},
     "corect": "A",
     "explicatie": "'port' nu a fost trimis, deci .get('port', 8080) intoarce valoarea DEFAULT 8080. Asa citesti optiuni care pot lipsi."},

    {"runda": 2, "categorie": "kwargs-unpacking", "puncte": 2,
     "cod": 'def f(**kwargs):\n    return kwargs.get("nume")\n\ndate = {"nume": "Ana", "varsta": 30}\nprint(f(**date))',
     "intrebare": "Ce afiseaza?",
     "optiuni": {"A": "30", "B": "Ana", "C": "None", "D": "eroare"},
     "corect": "B",
     "explicatie": "** la APEL despacheteaza dict-ul in argumente keyword: f(nume='Ana', varsta=30). kwargs.get('nume') -> 'Ana'."},

    {"runda": 2, "categorie": "kwargs-doar-keyword", "puncte": 3,
     "cod": 'def f(**kwargs):\n    return kwargs\n\nprint(f(1, 2))',
     "intrebare": "Ce se intampla?",
     "optiuni": {"A": "afiseaza (1, 2)", "B": "afiseaza {1: 2}",
                 "C": "TypeError", "D": "afiseaza {}"},
     "corect": "C",
     "explicatie": "**kwargs accepta DOAR argumente keyword (cheie=valoare). 1 si 2 sunt pozitionale -> TypeError: f() takes 0 positional arguments but 2 were given."},


    # ---------- RUNDA 3: COMBINATIE & UNPACKING ----------
    {"runda": 3, "categorie": "ordine-semnatura", "puncte": 3,
     "cod": 'def f(**kwargs, *args):\n    pass',
     "intrebare": "Ce se intampla la definirea functiei?",
     "optiuni": {"A": "merge normal", "B": "SyntaxError",
                 "C": "TypeError la apel", "D": "args devine gol"},
     "corect": "B",
     "explicatie": "ORDINEA obligatorie e: parametri normali -> *args -> **kwargs. **kwargs trebuie sa fie ULTIMUL. Aici vine inainte de *args -> SyntaxError."},

    {"runda": 3, "categorie": "combinatie", "puncte": 3,
     "cod": 'def f(a, *args, **kwargs):\n    return a + len(args) + len(kwargs)\n\nprint(f(10, 1, 2, x=5))',
     "intrebare": "Ce afiseaza?",
     "optiuni": {"A": "13", "B": "10", "C": "18", "D": "eroare"},
     "corect": "A",
     "explicatie": "a=10 (pozitional), args=(1, 2) -> len 2, kwargs={'x':5} -> len 1. 10 + 2 + 1 = 13."},

    {"runda": 3, "categorie": "default-plus-args", "puncte": 3,
     "cod": 'def f(a, b=2, *args):\n    return (a, b, args)\n\nprint(f(1, 3, 5, 7))',
     "intrebare": "Ce afiseaza?",
     "optiuni": {"A": "(1, 2, (5, 7))", "B": "(1, 3, (5, 7))",
                 "C": "(1, 3, 5, 7)", "D": "eroare"},
     "corect": "B",
     "explicatie": "a=1, apoi b ia 3 (SUPRASCRIE default-ul 2), iar restul (5, 7) merg in *args. Rezultat: (1, 3, (5, 7))."},

    {"runda": 3, "categorie": "capcana-fara-stea", "puncte": 3,
     "cod": 'def aduna(*args):\n    return sum(args)\n\nnums = [1, 2, 3]\nprint(aduna(nums))',
     "intrebare": "Ce se intampla? (atentie: nu e * la apel)",
     "optiuni": {"A": "6", "B": "[1, 2, 3]", "C": "TypeError", "D": "0"},
     "corect": "C",
     "explicatie": "Fara *, lista intra ca UN SINGUR element: args = ([1, 2, 3],). sum() incearca 0 + [1,2,3] -> TypeError. Trebuia aduna(*nums)."},

    {"runda": 3, "categorie": "unpacking-dict", "puncte": 2,
     "cod": 'def conecteaza(host, port):\n    return f"{host}:{port}"\n\ndate = {"host": "localhost", "port": 8080}\nprint(conecteaza(**date))',
     "intrebare": "Ce afiseaza?",
     "optiuni": {"A": "localhost:8080", "B": "8080:localhost",
                 "C": "host:port", "D": "eroare"},
     "corect": "A",
     "explicatie": "** despacheteaza dict-ul potrivind CHEILE cu numele parametrilor: conecteaza(host='localhost', port=8080) -> 'localhost:8080'."},

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
print("===   QUIZ INTERVIU JUNIOR PYTHON  -  *args / **kwargs   ===")
print("=" * 62)
print()
print("Fiecare intrebare are o secventa de COD si o EXPLICATIE")
print("dupa raspuns. Citeste codul cu atentie inainte sa raspunzi.")
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
            1: "*ARGS — ARGUMENTE POZITIONALE VARIABILE",
            2: "**KWARGS — ARGUMENTE KEYWORD VARIABILE",
            3: "COMBINATIE & UNPACKING",
            4: "SCOPE — LOCAL, GLOBAL, NONLOCAL",
        }
        print()
        print("=" * 62)
        print(f"  RUNDA {runda_curenta}:  {titluri[runda_curenta]}")
        print("=" * 62)
        print()

    # Afisam intrebarea cu codul
    print(f"Q{i + 1}  [{q['categorie']}, {q['puncte']}p]  -  {q['intrebare']}")
    print()
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
    print(f"  *** {nume}: profil JUNIOR SOLID — gata de proiecte reale.")
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