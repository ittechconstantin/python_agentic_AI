# QUIZ RECAP s1-s9  -  versiune INTERACTIVA cu input()
# =============================================================
# Cum functioneaza:
#   - programul afiseaza o intrebare cu 4 variante (A, B, C, D)
#   - tu (sau cursantul) tastezi litera raspunsului
#   - programul verifica, puncteaza, afiseaza scor curent
#   - la final: scor total, procent, ce categorii ai stapanit
#
# Acoperire (recap din s1-s9):
#   Runda 1: variabile, tipuri, string-uri (s1, s2)
#   Runda 2: liste, dict, tuple, set        (s3, s4, s5)
#   Runda 3: if/elif/else, lambda, ternar   (s7)
#   Runda 4: for, while, range              (s8, s9)
#
# Codul ÎNSUSI recapituleaza tot:
#   input(), if/elif, while (loop + validare), for (afisare),
#   dict (intrebari, scor), list (banca), set (categorii stapanite),
#   string formatting f"...{x:>5}..."
# =============================================================


# =============================================================
# BANCA DE INTREBARI
# =============================================================
# Fiecare intrebare este un DICT cu:
#   - runda      (int)     1..4
#   - categorie  (str)     ex: "string-uri", "while", "lambda"
#   - puncte     (int)     1 / 2 / 3 — in functie de dificultate
#   - text       (str)     intrebarea
#   - optiuni    (dict)    {"A": "...", "B": "...", "C": "...", "D": "..."}
#   - corect     (str)     "A" / "B" / "C" / "D"

intrebari = [
    # ---------- RUNDA 1: VARIABILE & STRING-URI ----------
    {"runda": 1, "categorie": "tipuri", "puncte": 1,
     "text": "Ce tip are valoarea 'hello' ?",
     "optiuni": {"A": "int", "B": "str", "C": "float", "D": "list"},
     "corect": "B"},

    {"runda": 1, "categorie": "tipuri", "puncte": 1,
     "text": "Ce afiseaza print(type(3.14)) ?",
     "optiuni": {"A": "<class 'int'>", "B": "<class 'str'>",
                 "C": "<class 'float'>", "D": "<class 'double'>"},
     "corect": "C"},

    {"runda": 1, "categorie": "string-uri", "puncte": 2,
     "text": "Ce afiseaza print('python'[::-1]) ?",
     "optiuni": {"A": "python", "B": "nohtyp", "C": "p y t h o n", "D": "eroare"},
     "corect": "B"},

    {"runda": 1, "categorie": "string-uri", "puncte": 2,
     "text": "Ce afiseaza print('abc' * 3) ?",
     "optiuni": {"A": "abc abc abc", "B": "abcabcabc",
                 "C": "[abc, abc, abc]", "D": "eroare"},
     "corect": "B"},

    {"runda": 1, "categorie": "string-uri", "puncte": 2,
     "text": "Ce afiseaza print(len('Salut Lume')) ?",
     "optiuni": {"A": "9", "B": "10", "C": "11", "D": "2"},
     "corect": "B"},

    # ---------- RUNDA 2: LISTE / DICT / TUPLE / SET ----------
    {"runda": 2, "categorie": "lista", "puncte": 2,
     "text": "Ce afiseaza print(len([1, [2, 3], 4])) ?",
     "optiuni": {"A": "2", "B": "3", "C": "4", "D": "5"},
     "corect": "B"},

    {"runda": 2, "categorie": "set", "puncte": 2,
     "text": "Cate elemente are setul {1, 2, 3, 2, 1} ?",
     "optiuni": {"A": "2", "B": "3", "C": "4", "D": "5"},
     "corect": "B"},

    {"runda": 2, "categorie": "dict", "puncte": 2,
     "text": "d = {'a': 1, 'b': 2}  ; ce afiseaza print(d['a']) ?",
     "optiuni": {"A": "a", "B": "1", "C": "'a'", "D": "KeyError"},
     "corect": "B"},

    {"runda": 2, "categorie": "lista", "puncte": 2,
     "text": "Ce afiseaza print([1, 2, 3] + [4, 5]) ?",
     "optiuni": {"A": "[5, 7, 8]", "B": "[1, 2, 3, 4, 5]",
                 "C": "[[1,2,3],[4,5]]", "D": "eroare"},
     "corect": "B"},

    {"runda": 2, "categorie": "tuple", "puncte": 3,
     "text": "Care e DIFERENTA principala intre [1,2,3] si (1,2,3) ?",
     "optiuni": {"A": "nu exista diferenta",
                 "B": "tuple-ul e MUTABIL, lista e imuabila",
                 "C": "lista e MUTABILA, tuple-ul e imuabil",
                 "D": "tuple-ul e mai rapid de cautat"},
     "corect": "C"},

    # ---------- RUNDA 3: IF / LAMBDA / TERNAR ----------
    {"runda": 3, "categorie": "if", "puncte": 1,
     "text": "if 0: print('A')  else: print('B')   -> ce afiseaza ?",
     "optiuni": {"A": "A", "B": "B", "C": "0", "D": "eroare"},
     "corect": "B"},

    {"runda": 3, "categorie": "lambda", "puncte": 2,
     "text": "Ce returneaza (lambda x: x * 2)(5) ?",
     "optiuni": {"A": "5", "B": "7", "C": "10", "D": "25"},
     "corect": "C"},

    {"runda": 3, "categorie": "in", "puncte": 2,
     "text": "Ce afiseaza print('a' in 'banana') ?",
     "optiuni": {"A": "True", "B": "False", "C": "3", "D": "eroare"},
     "corect": "A"},

    {"runda": 3, "categorie": "ternar", "puncte": 2,
     "text": "x = 10  ; ce afiseaza print('mare' if x > 5 else 'mic') ?",
     "optiuni": {"A": "mare", "B": "mic", "C": "True", "D": "eroare"},
     "corect": "A"},

    {"runda": 3, "categorie": "lambda", "puncte": 3,
     "text": "Ce returneaza (lambda x, y: x + y)(3, 4) ?",
     "optiuni": {"A": "3", "B": "4", "C": "7", "D": "12"},
     "corect": "C"},

    # ---------- RUNDA 4: FOR & WHILE ----------
    {"runda": 4, "categorie": "for", "puncte": 1,
     "text": "Cate iteratii face  for i in range(5) ?",
     "optiuni": {"A": "4", "B": "5", "C": "6", "D": "infinit"},
     "corect": "B"},

    {"runda": 4, "categorie": "for", "puncte": 2,
     "text": "Ce afiseaza  for i in range(2, 5): print(i, end=' ')  ?",
     "optiuni": {"A": "1 2 3 4", "B": "2 3 4", "C": "2 3 4 5", "D": "3 4 5"},
     "corect": "B"},

    {"runda": 4, "categorie": "while", "puncte": 2,
     "text": "i = 0  ; while i < 3: i += 1   -> ce valoare are i la final ?",
     "optiuni": {"A": "2", "B": "3", "C": "4", "D": "infinit"},
     "corect": "B"},

    {"runda": 4, "categorie": "for", "puncte": 3,
     "text": "Cate iteratii face  for i in range(10, 0, -2) ?",
     "optiuni": {"A": "4", "B": "5", "C": "6", "D": "10"},
     "corect": "B"},

    {"runda": 4, "categorie": "accumulator", "puncte": 3,
     "text": "s = 0 ; for i in [1,2,3,4]: s += i   -> ce afiseaza print(s) ?",
     "optiuni": {"A": "4", "B": "7", "C": "10", "D": "24"},
     "corect": "C"},
]


# =============================================================
# CONFIGURARE INITIALA
# =============================================================
# Punctaj maxim posibil — pentru raport final.
punctaj_maxim = 0
for q in intrebari:
    punctaj_maxim += q["puncte"]

# Structuri de evidenta:
scor                  = 0           # punctaj acumulat
intrebari_corecte     = 0           # cate raspunsuri corecte
categorii_stapanite   = set()       # categorii in care a raspuns corect
intrebari_gresite     = []          # lista pentru raportul final
runda_curenta         = 0           # marker pentru antete de runda


# Nume jucator (poate fi "Clasa", numele unui cursant, etc.)
print("=" * 60)
print("===          QUIZ RECAP  s1 - s9          ===")
print("=" * 60)
nume = input("Numele jucatorului (sau Enter pentru 'Clasa'): ").strip()
if nume == "":
    nume = "Clasa"
print(f"\nSalut, {nume}!  Apasa Q oricand vrei sa iesi mai devreme.\n")


# =============================================================
# MOTORUL QUIZ-ULUI  (WHILE peste banca de intrebari)
# =============================================================

i = 0
abandonat = False

while i < len(intrebari) and not abandonat:
    q = intrebari[i]

    # Antet de runda noua
    if q["runda"] != runda_curenta:
        runda_curenta = q["runda"]
        titluri_runda = {
            1: "VARIABILE & STRING-URI",
            2: "COLECTII  (lista, dict, tuple, set)",
            3: "IF / LAMBDA / TERNAR",
            4: "FOR & WHILE",
        }
        print()
        print("-" * 60)
        print(f"  RUNDA {runda_curenta}: {titluri_runda[runda_curenta]}")
        print("-" * 60)
        print()

    # Afisam intrebarea cu variantele
    print(f"Q{i + 1}  [{q['categorie']}, {q['puncte']}p]")
    print(f"  {q['text']}")
    print()
    for litera in ("A", "B", "C", "D"):
        print(f"    {litera})  {q['optiuni'][litera]}")
    print()

    # VALIDARE input — re-intrebam pana primim A/B/C/D (sau Q)
    raspuns = ""
    while True:
        raspuns = input("Raspunsul tau (A/B/C/D, sau Q pentru iesire): ").strip().upper()
        if raspuns in ("A", "B", "C", "D", "Q"):
            break
        print("  ! Te rog alege A, B, C, D — sau Q sa iesi.")

    # Iesire devreme
    if raspuns == "Q":
        abandonat = True
        print("\n(ai iesit din quiz)\n")
        break

    # Verificare raspuns
    if raspuns == q["corect"]:
        scor += q["puncte"]
        intrebari_corecte += 1
        categorii_stapanite.add(q["categorie"])
        print(f"  >>> CORECT! +{q['puncte']}p   (scor curent: {scor}/{punctaj_maxim})")
    else:
        corect_text = q["optiuni"][q["corect"]]
        intrebari_gresite.append({
            "nr": i + 1,
            "intrebare": q["text"],
            "raspuns_dat": raspuns,
            "raspuns_corect": q["corect"],
            "explicatie": corect_text,
        })
        print(f"  >>> Hmm, nu. Raspuns corect: {q['corect']}) {corect_text}")
        print(f"      (scor curent: {scor}/{punctaj_maxim})")

    print()
    i += 1


# =============================================================
# RAPORT FINAL
# =============================================================
print("=" * 60)
print(f"===              RAPORT FINAL pentru {nume}              ===")
print("=" * 60)

procent = (scor / punctaj_maxim * 100) if punctaj_maxim > 0 else 0
print(f"\n  scor:                {scor} / {punctaj_maxim} puncte  ({procent:.0f}%)")
print(f"  intrebari corecte:   {intrebari_corecte} / {i}")

# Mesaj in functie de procent (if / elif / else — recap!)
if procent >= 90:
    print(f"\n  *** EXCELENT, {nume}! Stii materia ca pe palma.")
elif procent >= 70:
    print(f"\n  ** Foarte bine, {nume}! Mai cizelam cateva detalii.")
elif procent >= 50:
    print(f"\n  * Bun, {nume}. Ai bazele. Reluam ce a fost greu.")
else:
    print(f"\n  Fara stres, {nume}. Reluam impreuna materialul.")

# Categorii stapanite (FOR pe set sortat)
print()
print(f"  categorii stapanite ({len(categorii_stapanite)}):")
if categorii_stapanite:
    for cat in sorted(categorii_stapanite):
        print(f"    + {cat}")
else:
    print("    (inca niciuna — relueaza si reia quiz-ul)")

# Intrebari gresite — pentru lectia urmatoare
if intrebari_gresite:
    print()
    print(f"  intrebari de re-explicat la urmatoarea ora:")
    for g in intrebari_gresite:
        print(f"    Q{g['nr']}: {g['intrebare']}")
        print(f"         ai zis: {g['raspuns_dat']}   corect: {g['raspuns_corect']}) {g['explicatie']}")

print()
print("=" * 60)