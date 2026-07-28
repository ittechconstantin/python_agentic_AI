# QUIZ INTERVIU
# =============================================================
# Pe baza a tot ce s-a predat in 11.functions.py.
# Fiecare intrebare contine:
#   - o SECVENTA DE COD (de tip "ce afiseaza? / ce eroare apare?")
#   - 4 variante A/B/C/D
#   - EXPLICATIE obligatorie dupa raspuns (afisata si cand
#     raspunzi corect — la interviu conteaza sa stii DE CE)
#
# Gotcha-urile clasice despre functii:
#   - print vs return  (functia fara return -> None)
#   - return opreste executia (cod mort dupa return)
#   - parametri cu default + REGULA ordinii (SyntaxError)
#   - argumente pozitionale vs keyword (positional after keyword)
#   - return multiplu = TUPLU + unpacking
#   - SCOPE: variabila locala nu se vede in afara (NameError)
#   - argument imutabil: reasignarea in functie NU schimba exteriorul
#   - lambda
#   - functiile sunt OBIECTE (in dict, pasate ca argument)
#   - type hints NU sunt verificate la rulare
#   - functii care cheama functii
#
# Cum se ruleaza:
#   python3 11.2.quiz_interviu.py
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
    # ---------- RUNDA 1: BAZE — DEF, RETURN, NONE ----------
    {"runda": 1, "categorie": "print-vs-return", "puncte": 2,
     "cod": 'def f(x):\n    print(x * 2)\n\nr = f(5)\nprint(r)',
     "intrebare": "Ce afiseaza? (atentie la cele DOUA linii)",
     "optiuni": {"A": "10 apoi 10", "B": "10 apoi None",
                 "C": "doar 10", "D": "None apoi 10"},
     "corect": "B",
     "explicatie": "Functia AFISEAZA 10 (print), dar NU are return, deci INTOARCE None. Acel None ajunge in r, iar al doilea print afiseaza None. print != return."},

    {"runda": 1, "categorie": "return-opreste", "puncte": 2,
     "cod": 'def f():\n    return 1\n    return 2\n\nprint(f())',
     "intrebare": "Ce afiseaza?",
     "optiuni": {"A": "1", "B": "2", "C": "1 apoi 2", "D": "None"},
     "corect": "A",
     "explicatie": "return OPRESTE imediat executia functiei. Primul return 1 iese din functie; 'return 2' e cod mort, nu se executa niciodata."},

    {"runda": 1, "categorie": "return-none", "puncte": 2,
     "cod": 'def saluta(n):\n    mesaj = "Salut " + n\n\nprint(saluta("Ana"))',
     "intrebare": "Ce afiseaza?",
     "optiuni": {"A": "Salut Ana", "B": "Ana",
                 "C": "None", "D": "eroare"},
     "corect": "C",
     "explicatie": "Functia construieste mesaj dar nu il RETURNEAZA. O functie fara return explicit intoarce None. (Variabila locala mesaj se pierde la final.)"},

    {"runda": 1, "categorie": "return-valoare", "puncte": 1,
     "cod": 'def add(a, b):\n    return a + b\n\nprint(add(2, 3) * 2)',
     "intrebare": "Ce afiseaza?",
     "optiuni": {"A": "10", "B": "7", "C": "23", "D": "None"},
     "corect": "A",
     "explicatie": "return da o VALOARE pe care o poti folosi mai departe in expresii. add(2,3) = 5, apoi 5 * 2 = 10. (Cu print in loc de return n-ai fi putut inmulti rezultatul.)"},

    {"runda": 1, "categorie": "return-conditionat", "puncte": 2,
     "cod": 'def semn(n):\n    if n > 0:\n        return "pozitiv"\n    return "non-pozitiv"\n\nprint(semn(-4))',
     "intrebare": "Ce afiseaza?",
     "optiuni": {"A": "pozitiv", "B": "non-pozitiv",
                 "C": "None", "D": "eroare"},
     "corect": "B",
     "explicatie": "n=-4 nu e > 0, deci if-ul e sarit si se executa al doilea return -> 'non-pozitiv'. Daca n>0, primul return ar fi iesit deja din functie."},


    # ---------- RUNDA 2: PARAMETRI — DEFAULT, KEYWORD ----------
    {"runda": 2, "categorie": "default", "puncte": 1,
     "cod": 'def putere(b, e=2):\n    return b ** e\n\nprint(putere(3))',
     "intrebare": "Ce afiseaza?",
     "optiuni": {"A": "9", "B": "6", "C": "3", "D": "eroare"},
     "corect": "A",
     "explicatie": "e nu e trimis, deci se foloseste valoarea DEFAULT e=2 -> 3**2 = 9."},

    {"runda": 2, "categorie": "default-regula", "puncte": 3,
     "cod": 'def f(a, b=1, c):\n    return a + b + c',
     "intrebare": "Ce se intampla la definirea functiei?",
     "optiuni": {"A": "merge normal", "B": "SyntaxError",
                 "C": "TypeError la apel", "D": "c devine 0"},
     "corect": "B",
     "explicatie": "REGULA: parametrii cu default trebuie pusi DUPA cei fara default. Aici c (fara default) vine dupa b=1 (cu default) -> SyntaxError: parameter without a default follows parameter with a default. Corect: def f(a, c, b=1)."},

    {"runda": 2, "categorie": "keyword", "puncte": 2,
     "cod": 'def info(nume, varsta):\n    return f"{nume}-{varsta}"\n\nprint(info(varsta=10, nume="Ana"))',
     "intrebare": "Ce afiseaza?",
     "optiuni": {"A": "10-Ana", "B": "Ana-10",
                 "C": "eroare (ordine gresita)", "D": "nume-varsta"},
     "corect": "B",
     "explicatie": "La argumente KEYWORD ordinea NU conteaza — fiecare valoare merge la parametrul numit. Deci nume='Ana', varsta=10 -> 'Ana-10'."},

    {"runda": 2, "categorie": "pozitional-keyword", "puncte": 3,
     "cod": 'def f(a, b):\n    return a - b\n\nprint(f(a=10, 5))',
     "intrebare": "Ce se intampla?",
     "optiuni": {"A": "afiseaza 5", "B": "afiseaza -5",
                 "C": "SyntaxError", "D": "afiseaza 10"},
     "corect": "C",
     "explicatie": "Un argument POZITIONAL (5) NU poate veni DUPA unul KEYWORD (a=10) -> SyntaxError: positional argument follows keyword argument. Pozitionalele trebuie sa fie mereu inaintea celor keyword."},

    {"runda": 2, "categorie": "default-suprascris", "puncte": 1,
     "cod": 'def saluta(nume, mesaj="Salut"):\n    return mesaj + ", " + nume\n\nprint(saluta("Ana", "Buna"))',
     "intrebare": "Ce afiseaza?",
     "optiuni": {"A": "Salut, Ana", "B": "Buna, Ana",
                 "C": "Ana, Buna", "D": "Buna, Salut"},
     "corect": "B",
     "explicatie": "Al doilea argument 'Buna' SUPRASCRIE default-ul mesaj='Salut'. Rezultat: 'Buna, Ana'."},


    # ---------- RUNDA 3: RETURN TUPLU & SCOPE ----------
    {"runda": 3, "categorie": "return-tuplu", "puncte": 2,
     "cod": 'def f():\n    return 1, 2\n\nx = f()\nprint(type(x).__name__)',
     "intrebare": "Ce TIP are x?",
     "optiuni": {"A": "list", "B": "int", "C": "tuple", "D": "set"},
     "corect": "C",
     "explicatie": "return a, b returneaza de fapt UN TUPLU (a, b). Deci x este un tuple, iar type(x).__name__ afiseaza 'tuple'."},

    {"runda": 3, "categorie": "unpacking", "puncte": 2,
     "cod": 'def min_max(nums):\n    return min(nums), max(nums)\n\na, b = min_max([3, 1, 5])\nprint(a, b)',
     "intrebare": "Ce afiseaza?",
     "optiuni": {"A": "1 5", "B": "5 1",
                 "C": "(1, 5)", "D": "3 5"},
     "corect": "A",
     "explicatie": "Functia returneaza tuplul (1, 5). Prin  a, b = ...  se face DESPACHETAREA (unpacking): a=1, b=5. print afiseaza '1 5'."},

    {"runda": 3, "categorie": "scope", "puncte": 3,
     "cod": 'def f():\n    x = 10\n\nf()\nprint(x)',
     "intrebare": "Ce se intampla?",
     "optiuni": {"A": "afiseaza 10", "B": "afiseaza None",
                 "C": "NameError", "D": "afiseaza 0"},
     "corect": "C",
     "explicatie": "x e o variabila LOCALA — traieste doar in interiorul functiei f si dispare la final. Din afara nu poate fi accesata -> NameError: name 'x' is not defined."},

    {"runda": 3, "categorie": "argument-imutabil", "puncte": 3,
     "cod": 'def add_one(n):\n    n = n + 1\n\nx = 5\nadd_one(x)\nprint(x)',
     "intrebare": "Ce afiseaza?",
     "optiuni": {"A": "5", "B": "6", "C": "None", "D": "eroare"},
     "corect": "A",
     "explicatie": "In functie, n = n + 1 doar REASIGNEAZA variabila locala n; nu modifica variabila x de afara (int-urile sunt imuabile). x ramane 5. Ca sa folosesti rezultatul, ar trebui return n + 1."},


    # ---------- RUNDA 4: LAMBDA, FUNCTII CA OBIECTE, TYPE HINTS ----------
    {"runda": 4, "categorie": "lambda", "puncte": 1,
     "cod": 'cub = lambda x: x ** 3\nprint(cub(2))',
     "intrebare": "Ce afiseaza?",
     "optiuni": {"A": "6", "B": "8", "C": "9", "D": "eroare"},
     "corect": "B",
     "explicatie": "lambda e o functie mica, pe o linie. cub(2) -> 2**3 = 8. Rezultatul expresiei e returnat automat, fara cuvantul return."},

    {"runda": 4, "categorie": "functie-obiect", "puncte": 3,
     "cod": 'def add(a, b): return a + b\ndef mul(a, b): return a * b\n\nop = {"+": add, "*": mul}\nprint(op["+"](4, 5))',
     "intrebare": "Ce afiseaza?",
     "optiuni": {"A": "9", "B": "20", "C": "45", "D": "eroare"},
     "corect": "A",
     "explicatie": "Functiile sunt OBIECTE, deci pot fi valori intr-un dict. op['+'] intoarce functia add, apoi (4, 5) o APELEAZA: add(4, 5) = 9."},

    {"runda": 4, "categorie": "functie-argument", "puncte": 3,
     "cod": 'def dublu(x): return x * 2\n\ndef aplica(f, val):\n    return f(val)\n\nprint(aplica(dublu, 10))',
     "intrebare": "Ce afiseaza?",
     "optiuni": {"A": "10", "B": "20", "C": "dublu", "D": "eroare"},
     "corect": "B",
     "explicatie": "O functie poate fi PASATA ca argument altei functii (sunt obiecte). aplica primeste functia dublu in f, apoi f(10) = dublu(10) = 20."},

    {"runda": 4, "categorie": "type-hints", "puncte": 3,
     "cod": 'def add(a: int, b: int) -> int:\n    return a + b\n\nprint(add("x", "y"))',
     "intrebare": "Ce afiseaza?",
     "optiuni": {"A": "xy", "B": "TypeError",
                 "C": "0", "D": "eroare la definire"},
     "corect": "A",
     "explicatie": "Type hints (int) sunt doar ADNOTARI pentru cititor/IDE — Python NU le verifica la rulare. 'x' + 'y' (concatenare de string) merge -> 'xy'."},

    {"runda": 4, "categorie": "functii-cheama-functii", "puncte": 2,
     "cod": 'def patrat(x): return x * x\n\ndef suma_patrate(a, b):\n    return patrat(a) + patrat(b)\n\nprint(suma_patrate(3, 4))',
     "intrebare": "Ce afiseaza?",
     "optiuni": {"A": "7", "B": "25", "C": "49", "D": "14"},
     "corect": "B",
     "explicatie": "Functii care cheama functii: suma_patrate apeleaza patrat de doua ori. patrat(3)=9, patrat(4)=16, 9+16 = 25."},
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
print("===       QUIZ INTERVIU JUNIOR PYTHON  -  FUNCTII        ===")
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
            1: "BAZE — DEF, RETURN, NONE",
            2: "PARAMETRI — DEFAULT & KEYWORD",
            3: "RETURN TUPLU & SCOPE",
            4: "LAMBDA, FUNCTII CA OBIECTE, TYPE HINTS",
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