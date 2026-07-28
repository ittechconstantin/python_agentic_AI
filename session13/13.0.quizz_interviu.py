# QUIZ INTERVIU  -  SESIUNEA 13  (SCOPE + EXCEPTII)
# =============================================================
# Pe baza a tot ce s-a predat in 13.scope.py si 13.2.exceptions.py.
# Fiecare intrebare contine:
#   - o SECVENTA DE COD (de tip "ce afiseaza? / ce eroare apare?")
#   - 4 variante A/B/C/D
#   - EXPLICATIE obligatorie dupa raspuns (afisata si cand
#     raspunzi corect — la interviu conteaza sa stii DE CE)
#
# Gotcha-urile clasice din sesiunea 13:
#   SCOPE:
#     - regula LEGB (local castiga in fata global)
#     - variabila locala nu se vede in afara (NameError)
#     - UnboundLocalError la  total += 1  fara `global`
#     - lista: modificare in-place (fara global) vs reasignare (cu global)
#     - `nonlocal` in closures (contor care tine minte)
#     - shadowing peste un built-in (list = [...] strica list())
#   EXCEPTII:
#     - ce tip de eroare arunca fiecare situatie
#     - ordinea except: specific INAINTEA general
#     - except ValueError NU prinde un TypeError
#     - else ruleaza doar pe succes; finally ruleaza MEREU
#     - return in finally SUPRASCRIE return-ul din try
#     - raise / re-raise
#
# Cum se ruleaza:
#   python3 13.0.quiz_interviu.py
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
    # ---------- RUNDA 1: SCOPE — LEGB & LOCAL ----------
    {"runda": 1, "categorie": "legb-local-castiga", "puncte": 2,
     "cod": 'mesaj = "global"\n\ndef f():\n    mesaj = "local"\n    print(mesaj)\n\nf()',
     "intrebare": "Ce afiseaza?",
     "optiuni": {"A": "global", "B": "local",
                 "C": "None", "D": "eroare"},
     "corect": "B",
     "explicatie": "Regula LEGB: Python cauta numele intai LOCAL. In f exista un `mesaj` local, deci el castiga in fata celui global. Afiseaza 'local'. Cel global ramane neatins."},

    {"runda": 1, "categorie": "citire-globala", "puncte": 1,
     "cod": 'APP = "shop"\n\ndef afiseaza():\n    print(APP)\n\nafiseaza()',
     "intrebare": "Ce afiseaza?",
     "optiuni": {"A": "shop", "B": "APP",
                 "C": "None", "D": "NameError"},
     "corect": "A",
     "explicatie": "A CITI o variabila globala dintr-o functie merge DIRECT, fara nimic special. Nu exista un APP local, deci Python urca la nivel global -> 'shop'."},

    {"runda": 1, "categorie": "local-invizibil", "puncte": 3,
     "cod": 'def f():\n    x = 10\n\nf()\nprint(x)',
     "intrebare": "Ce se intampla?",
     "optiuni": {"A": "afiseaza 10", "B": "afiseaza None",
                 "C": "NameError", "D": "afiseaza 0"},
     "corect": "C",
     "explicatie": "x e o variabila LOCALA — traieste doar in interiorul lui f si dispare la final. Din afara nu poate fi accesata -> NameError: name 'x' is not defined."},

    {"runda": 1, "categorie": "scope-per-apel", "puncte": 2,
     "cod": 'def f(s):\n    s = s + 1\n    return s\n\nprint(f(10), f(100))',
     "intrebare": "Ce afiseaza?",
     "optiuni": {"A": "11 101", "B": "11 11",
                 "C": "111", "D": "10 100"},
     "corect": "A",
     "explicatie": "Fiecare apel are PROPRIUL scope local. `s` din primul apel (10->11) nu are legatura cu `s` din al doilea (100->101). Afiseaza '11 101'."},

    {"runda": 1, "categorie": "enclosing-citire", "puncte": 2,
     "cod": 'def exterioara():\n    x = "enclosing"\n    def interioara():\n        print(x)\n    interioara()\n\nexterioara()',
     "intrebare": "Ce afiseaza?",
     "optiuni": {"A": "NameError", "B": "enclosing",
                 "C": "None", "D": "x"},
     "corect": "B",
     "explicatie": "interioara nu are `x` local, deci Python urca un pas (ENCLOSING) si gaseste `x` din exterioara. A CITI variabila exterioara merge direct, fara `nonlocal` -> 'enclosing'."},


    # ---------- RUNDA 2: SCOPE — GLOBAL, NONLOCAL, SHADOWING ----------
    {"runda": 2, "categorie": "unbound-local", "puncte": 3,
     "cod": 'total = 0\n\ndef f():\n    total += 1\n\nf()',
     "intrebare": "Ce se intampla?",
     "optiuni": {"A": "total devine 1", "B": "UnboundLocalError",
                 "C": "NameError", "D": "nimic, total ramane 0"},
     "corect": "B",
     "explicatie": "Pentru ca ATRIBUI `total` in functie, Python il considera LOCAL. Dar `total += 1` il citeste inainte sa-i fi dat o valoare -> UnboundLocalError. Solutia: `global total` in functie."},

    {"runda": 2, "categorie": "global-keyword", "puncte": 2,
     "cod": 'c = 0\n\ndef inc():\n    global c\n    c += 1\n\ninc()\ninc()\nprint(c)',
     "intrebare": "Ce afiseaza?",
     "optiuni": {"A": "0", "B": "1", "C": "2", "D": "UnboundLocalError"},
     "corect": "C",
     "explicatie": "`global c` spune ca lucram cu variabila de la nivel de fisier, nu cream una locala. Doua apeluri o cresc de la 0 la 2."},

    {"runda": 2, "categorie": "lista-modificare", "puncte": 2,
     "cod": 'log = []\n\ndef add(x):\n    log.append(x)\n\nadd("a")\nadd("b")\nprint(log)',
     "intrebare": "Ce afiseaza? (atentie: NU are `global`)",
     "optiuni": {"A": "[]", "B": "['a', 'b']",
                 "C": "UnboundLocalError", "D": "NameError"},
     "corect": "B",
     "explicatie": "`.append` MODIFICA lista existenta (in-place), nu o REASIGNEAZA. Modificarea in-place nu cere `global`. Rezultat: ['a', 'b']."},

    {"runda": 2, "categorie": "lista-reasignare", "puncte": 3,
     "cod": 'log = [1, 2]\n\ndef reset():\n    log = []\n\nreset()\nprint(log)',
     "intrebare": "Ce afiseaza?",
     "optiuni": {"A": "[]", "B": "[1, 2]",
                 "C": "None", "D": "UnboundLocalError"},
     "corect": "B",
     "explicatie": "`log = []` e o REASIGNARE -> creeaza o variabila LOCALA `log`, fara legatura cu cea globala. Cea de afara ramane [1, 2]. Ca sa o golesti, ai nevoie de `global log`."},

    {"runda": 2, "categorie": "nonlocal-closure", "puncte": 3,
     "cod": 'def contor():\n    n = 0\n    def pas():\n        nonlocal n\n        n += 1\n        return n\n    return pas\n\nc = contor()\nprint(c(), c(), c())',
     "intrebare": "Ce afiseaza?",
     "optiuni": {"A": "1 1 1", "B": "1 2 3",
                 "C": "0 1 2", "D": "eroare"},
     "corect": "B",
     "explicatie": "`nonlocal n` leaga la `n` din functia exterioara, iar closure-ul tine minte valoarea intre apeluri. Deci 1, apoi 2, apoi 3 — nu se reseteaza."},

    {"runda": 2, "categorie": "shadowing-builtin", "puncte": 3,
     "cod": 'list = [1, 2, 3]\nprint(list(range(3)))',
     "intrebare": "Ce se intampla?",
     "optiuni": {"A": "[0, 1, 2]", "B": "[1, 2, 3]",
                 "C": "TypeError", "D": "SyntaxError"},
     "corect": "C",
     "explicatie": "Ai UMBRIT built-in-ul `list` cu o lista. Acum `list(range(3))` incearca sa 'apeleze' o lista -> TypeError: 'list' object is not callable. De aceea nu folosesti nume ca list/dict/str/sum."},


    # ---------- RUNDA 3: EXCEPTII — BAZE & TIPURI DE ERORI ----------
    {"runda": 3, "categorie": "try-except-baza", "puncte": 2,
     "cod": 'try:\n    x = 10 / 0\nexcept ZeroDivisionError:\n    print("zero")\nprint("gata")',
     "intrebare": "Ce afiseaza?",
     "optiuni": {"A": "doar 'zero'", "B": "'zero' apoi 'gata'",
                 "C": "doar 'gata'", "D": "crapa cu eroare"},
     "corect": "B",
     "explicatie": "Exceptia ZeroDivisionError e PRINSA -> se afiseaza 'zero'. Pentru ca a fost tratata, programul CONTINUA si afiseaza si 'gata'."},

    {"runda": 3, "categorie": "tip-eroare-value", "puncte": 1,
     "cod": 'int("abc")',
     "intrebare": "Ce eroare arunca?",
     "optiuni": {"A": "TypeError", "B": "ValueError",
                 "C": "KeyError", "D": "niciuna, da 0"},
     "corect": "B",
     "explicatie": "Tipul primit (str) e ok pentru int(), dar VALOAREA 'abc' nu poate fi convertita la numar -> ValueError. (TypeError ar aparea pentru un TIP nepotrivit, ex \"a\" + 5.)"},

    {"runda": 3, "categorie": "tip-eroare-key", "puncte": 2,
     "cod": 'd = {"a": 1}\nprint(d["b"])',
     "intrebare": "Ce eroare arunca?",
     "optiuni": {"A": "IndexError", "B": "ValueError",
                 "C": "KeyError", "D": "None"},
     "corect": "C",
     "explicatie": "Accesul la o CHEIE inexistenta intr-un dict arunca KeyError. (La liste, un index inexistent ar fi IndexError.)"},

    {"runda": 3, "categorie": "ordine-except", "puncte": 3,
     "cod": 'try:\n    x = {"a": 1}["b"]\nexcept Exception:\n    print("general")\nexcept KeyError:\n    print("key")',
     "intrebare": "Ce afiseaza?",
     "optiuni": {"A": "key", "B": "general",
                 "C": "general apoi key", "D": "SyntaxError"},
     "corect": "B",
     "explicatie": "Python sare la PRIMUL except care se potriveste. `Exception` prinde tot (inclusiv KeyError), deci se executa el -> 'general'. Ramura KeyError nu mai e atinsa NICIODATA. Regula: specific INAINTEA general."},

    {"runda": 3, "categorie": "except-nu-prinde", "puncte": 3,
     "cod": 'try:\n    x = "a" + 5\nexcept ValueError:\n    print("val")',
     "intrebare": "Ce se intampla?",
     "optiuni": {"A": "afiseaza 'val'", "B": "afiseaza 'a5'",
                 "C": "crapa cu TypeError", "D": "nu afiseaza nimic"},
     "corect": "C",
     "explicatie": '"a" + 5 arunca TypeError, dar except-ul prinde doar ValueError. Tipul nu se potriveste, deci exceptia NU e prinsa -> programul crapa cu TypeError. Prinde exact ce te astepti.'},

    {"runda": 3, "categorie": "tuplu-except", "puncte": 2,
     "cod": 'try:\n    int("x")\nexcept (ValueError, TypeError):\n    print("invalid")',
     "intrebare": "Ce afiseaza?",
     "optiuni": {"A": "invalid", "B": "x",
                 "C": "0", "D": "crapa"},
     "corect": "A",
     "explicatie": "Un singur except poate prinde MAI MULTE tipuri printr-un tuplu. int('x') arunca ValueError, care e in tuplu -> se afiseaza 'invalid'."},


    # ---------- RUNDA 4: EXCEPTII — ELSE / FINALLY / RAISE ----------
    {"runda": 4, "categorie": "else-pe-succes", "puncte": 2,
     "cod": 'try:\n    n = int("42")\nexcept ValueError:\n    print("err")\nelse:\n    print("ok")',
     "intrebare": "Ce afiseaza?",
     "optiuni": {"A": "err", "B": "ok",
                 "C": "err apoi ok", "D": "nimic"},
     "corect": "B",
     "explicatie": "int('42') reuseste, deci NU e exceptie. Ramura `else` ruleaza DOAR pe succes (cand try a mers fara erori) -> 'ok'."},

    {"runda": 4, "categorie": "finally-mereu", "puncte": 3,
     "cod": 'def f():\n    try:\n        return "try"\n    finally:\n        print("finally")\n\nprint(f())',
     "intrebare": "Ce afiseaza, in ce ordine?",
     "optiuni": {"A": "try apoi finally", "B": "finally apoi try",
                 "C": "doar try", "D": "doar finally"},
     "corect": "B",
     "explicatie": "`finally` ruleaza MEREU, chiar si cand try are return — si chiar INAINTE ca valoarea sa fie returnata. Deci se printeaza 'finally', apoi f() intoarce 'try', pe care il afiseaza print -> 'finally' apoi 'try'."},

    {"runda": 4, "categorie": "finally-return", "puncte": 3,
     "cod": 'def f():\n    try:\n        return 1\n    finally:\n        return 2\n\nprint(f())',
     "intrebare": "Ce afiseaza?",
     "optiuni": {"A": "1", "B": "2",
                 "C": "1 apoi 2", "D": "eroare"},
     "corect": "B",
     "explicatie": "Capcana clasica: un `return` in `finally` SUPRASCRIE return-ul din try. finally ruleaza ultimul si 'castiga' -> functia intoarce 2. (De aceea se evita return in finally.)"},

    {"runda": 4, "categorie": "raise-propriu", "puncte": 2,
     "cod": 'def varsta(v):\n    if v < 0:\n        raise ValueError("varsta negativa")\n    return v\n\ntry:\n    varsta(-1)\nexcept ValueError as e:\n    print(e)',
     "intrebare": "Ce afiseaza?",
     "optiuni": {"A": "-1", "B": "varsta negativa",
                 "C": "ValueError", "D": "None"},
     "corect": "B",
     "explicatie": "`raise ValueError(\"...\")` arunca o exceptie cu mesajul dat. `except ValueError as e` o prinde, iar print(e) afiseaza MESAJUL -> 'varsta negativa'."},

    {"runda": 4, "categorie": "re-raise", "puncte": 3,
     "cod": 'def f():\n    try:\n        return int("x")\n    except ValueError:\n        print("log")\n        raise\n\ntry:\n    f()\nexcept ValueError:\n    print("sus")',
     "intrebare": "Ce afiseaza?",
     "optiuni": {"A": "doar 'log'", "B": "log apoi sus",
                 "C": "doar 'sus'", "D": "crapa neprins"},
     "corect": "B",
     "explicatie": "f prinde ValueError, printeaza 'log', apoi `raise` (gol) RE-ARUNCA aceeasi exceptie mai sus. Codul de afara o prinde si printeaza 'sus'. Pattern: logheaza local, trateaza sus."},

    {"runda": 4, "categorie": "pattern-default", "puncte": 1,
     "cod": 'def ca_int(t, d=0):\n    try:\n        return int(t)\n    except ValueError:\n        return d\n\nprint(ca_int("abc"))',
     "intrebare": "Ce afiseaza?",
     "optiuni": {"A": "abc", "B": "0",
                 "C": "None", "D": "crapa"},
     "corect": "B",
     "explicatie": "Pattern uzual 'incearca, altfel default': int('abc') arunca ValueError, e prinsa, iar functia intoarce valoarea default d=0."},
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
print("===     QUIZ INTERVIU JUNIOR PYTHON  -  SCOPE + EXCEPTII   ===")
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
            1: "SCOPE — LEGB & LOCAL",
            2: "SCOPE — GLOBAL, NONLOCAL, SHADOWING",
            3: "EXCEPTII — BAZE & TIPURI DE ERORI",
            4: "EXCEPTII — ELSE / FINALLY / RAISE",
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