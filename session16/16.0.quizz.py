# QUIZ INTERVIU  -  SESIUNEA 16  (GENERATORI / yield)
# =============================================================
# Pe baza a tot ce s-a predat in 16.generators.py.
# Fiecare intrebare contine:
#   - o SECVENTA DE COD (de tip "ce afiseaza? / ce se intampla?")
#     sau o intrebare de CONCEPT din teorie
#   - 4 variante A/B/C/D
#   - EXPLICATIE obligatorie dupa raspuns (afisata si cand
#     raspunzi corect — la interviu conteaza sa stii DE CE)
#
# Gotcha-urile clasice din sesiunea 16:
#   BAZE:
#     - o functie cu `yield` devine functie GENERATOR
#     - apeland-o, corpul NU ruleaza; primesti un obiect generator
#     - consumi cu for / next(); la final next() arunca StopIteration
#     - LAZY: corpul ruleaza in reprize, pana la urmatorul yield
#   EPUIZARE & EXPRESII:
#     - un generator se consuma O SINGURA DATA (list(g) apoi [])
#     - (x for x in ...) = generator ;  [x for x in ...] = lista
#     - memorie mica: zeci de bytes indiferent de n
#   CAZURI REALE:
#     - pipeline: sursa -> filtru -> transformare, cate un element
#     - fluxuri INFINITE cu while True + yield (control cu break)
#     - da generatorul direct lui sum/join ca sa eviti liste
#   UNELTE:
#     - itertools: count, islice, chain
#     - yield from = retransmite valorile altui generator
#
# Cum se ruleaza:
#   python3 16.0.quiz.py
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
#   cod         (str)    secventa de cod (sau "" pentru intrebari de concept)
#   intrebare   (str)    intrebarea propriu-zisa
#   optiuni     (dict)   {"A": ..., "B": ..., "C": ..., "D": ...}
#   corect      (str)    "A" / "B" / "C" / "D"
#   explicatie  (str)    DE CE — afisata mereu dupa raspuns

intrebari = [
    # ---------- RUNDA 1: BAZELE — yield, obiect generator, lazy ----------
    {"runda": 1, "categorie": "ce-e-un-generator", "puncte": 1,
     "cod": 'def gen():\n    yield 1\n    yield 2\n\nprint(type(gen()).__name__)',
     "intrebare": "Ce afiseaza?",
     "optiuni": {"A": "function", "B": "generator",
                 "C": "list", "D": "tuple"},
     "corect": "B",
     "explicatie": "O functie care contine `yield` devine automat o FUNCTIE GENERATOR. Cand o apelezi, intoarce un obiect de tip 'generator' (nu o lista, nu rezultatul)."},

    {"runda": 1, "categorie": "corpul-nu-ruleaza", "puncte": 3,
     "cod": 'def gen():\n    print("start")\n    yield 1\n\ng = gen()\nprint("creat")',
     "intrebare": "Ce afiseaza, in ce ordine?",
     "optiuni": {"A": "start apoi creat", "B": "creat (doar atat)",
                 "C": "start (doar atat)", "D": "creat apoi start"},
     "corect": "B",
     "explicatie": "Apeland functia generator, corpul NU ruleaza inca! Primesti doar obiectul generator (o promisiune). 'start' s-ar afisa abia cand ceri prima valoare. Deci aici se vede doar 'creat'."},

    {"runda": 1, "categorie": "next-prima-valoare", "puncte": 1,
     "cod": 'def gen():\n    yield 10\n    yield 20\n\ng = gen()\nprint(next(g))',
     "intrebare": "Ce afiseaza?",
     "optiuni": {"A": "10", "B": "20",
                 "C": "[10, 20]", "D": "<generator>"},
     "corect": "A",
     "explicatie": "next(g) ruleaza corpul pana la PRIMUL yield si intoarce valoarea oferita -> 10. Abia urmatorul next(g) ar continua pana la al doilea yield -> 20."},

    {"runda": 1, "categorie": "stopiteration", "puncte": 2,
     "cod": 'def gen():\n    yield 1\n\ng = gen()\nnext(g)\nnext(g)',
     "intrebare": "Ce se intampla la al DOILEA next(g)?",
     "optiuni": {"A": "intoarce 1 din nou", "B": "intoarce None",
                 "C": "arunca StopIteration", "D": "arunca ValueError"},
     "corect": "C",
     "explicatie": "Dupa ce s-au epuizat valorile, next() arunca StopIteration. Un `for` prinde asta automat si se opreste; manual cu next() o vezi ca exceptie."},

    {"runda": 1, "categorie": "lazy-reprize", "puncte": 3,
     "cod": 'def gen():\n    print("A")\n    yield 1\n    print("B")\n    yield 2\n\ng = gen()\nprint(next(g))',
     "intrebare": "Ce afiseaza, in ce ordine?",
     "optiuni": {"A": "A apoi 1", "B": "1 (doar atat)",
                 "C": "A B apoi 1", "D": "A 1 2"},
     "corect": "A",
     "explicatie": "LAZY: next(g) ruleaza corpul pana la primul yield -> afiseaza 'A', apoi yield intoarce 1, pe care print il afiseaza. 'B' apare abia la urmatorul next. Deci: 'A' apoi '1'."},


    # ---------- RUNDA 2: EPUIZARE & GENERATOR EXPRESSIONS ----------
    {"runda": 2, "categorie": "consuma-o-data", "puncte": 3,
     "cod": 'def gen():\n    yield 1\n    yield 2\n\ng = gen()\nprint(list(g))\nprint(list(g))',
     "intrebare": "Ce afiseaza cele doua print-uri?",
     "optiuni": {"A": "[1, 2] apoi [1, 2]", "B": "[1, 2] apoi []",
                 "C": "[1, 2] apoi StopIteration", "D": "[] apoi [1, 2]"},
     "corect": "B",
     "explicatie": "Un generator se parcurge O SINGURA DATA. Primul list(g) il consuma tot -> [1, 2]. Acum e gol, deci al doilea list(g) -> []. Pentru reutilizare: pune-l intr-o lista sau refa-l."},

    {"runda": 2, "categorie": "gen-expr-tip", "puncte": 2,
     "cod": 'g = (x for x in range(3))\nprint(type(g).__name__)',
     "intrebare": "Ce afiseaza?",
     "optiuni": {"A": "list", "B": "tuple",
                 "C": "generator", "D": "range"},
     "corect": "C",
     "explicatie": "Parantezele ROTUNDE () dau un GENERATOR (lazy), nu un tuplu. Doar parantezele patrate [] ar construi o lista. type(g).__name__ -> 'generator'."},

    {"runda": 2, "categorie": "gen-expr-vs-lista", "puncte": 2,
     "cod": 'g = (x + 1 for x in range(3))\nprint(list(g))',
     "intrebare": "Ce afiseaza?",
     "optiuni": {"A": "[1, 2, 3]", "B": "[0, 1, 2]",
                 "C": "<generator object>", "D": "[1, 2, 3, 4]"},
     "corect": "A",
     "explicatie": "Generator expression-ul produce x+1 pentru x in 0,1,2 -> 1,2,3. list() il consuma si aduna valorile intr-o lista -> [1, 2, 3]."},

    {"runda": 2, "categorie": "gen-direct-in-sum", "puncte": 2,
     "cod": 'print(sum(x for x in range(5)))',
     "intrebare": "Ce afiseaza?",
     "optiuni": {"A": "5", "B": "10",
                 "C": "[0, 1, 2, 3, 4]", "D": "15"},
     "corect": "B",
     "explicatie": "Dai generatorul DIRECT lui sum(), fara lista intermediara. sum(0+1+2+3+4) = 10. Asa economisesti memorie: nu se construieste nicio lista."},

    {"runda": 2, "categorie": "memorie-concept", "puncte": 2,
     "cod": "",
     "intrebare": "Un generator creat pentru 1.000.000 de valori ocupa in memorie aproximativ:",
     "optiuni": {"A": "cat o lista de 1 milion de elemente",
                 "B": "cateva zeci de bytes, indiferent de n",
                 "C": "exact 1.000.000 de bytes",
                 "D": "jumatate cat o lista echivalenta"},
     "corect": "B",
     "explicatie": "Generatorul NU tine valorile in memorie — produce una la un moment dat. Ocupa cateva zeci de bytes indiferent de cate valori va genera. Asta e marele avantaj de memorie."},


    # ---------- RUNDA 3: CAZURI REALE — pipeline, infinit, flux ----------
    {"runda": 3, "categorie": "pipeline", "puncte": 3,
     "cod": 'def comenzi():\n    yield {"platita": True,  "suma": 100}\n    yield {"platita": False, "suma": 250}\n    yield {"platita": True,  "suma": 75}\n\nplatite = (c for c in comenzi() if c["platita"])\nprint(sum(c["suma"] for c in platite))',
     "intrebare": "Ce afiseaza?",
     "optiuni": {"A": "425", "B": "175",
                 "C": "250", "D": "100"},
     "corect": "B",
     "explicatie": "Pipeline: etapa 1 filtreaza doar comenzile platite (100 si 75; 250 e exclusa), etapa 2 extrage sumele, etapa 3 le aduna -> 100 + 75 = 175. Totul curge cate un element, fara liste intermediare."},

    {"runda": 3, "categorie": "flux-infinit-break", "puncte": 3,
     "cod": 'def numere(start):\n    n = start\n    while True:\n        yield n\n        n += 1\n\ng = numere(10)\nfor x in g:\n    if x >= 13:\n        break\n    print(x, end=" ")',
     "intrebare": "Ce afiseaza?",
     "optiuni": {"A": "10 11 12 13", "B": "10 11 12",
                 "C": "bucla infinita (se blocheaza)", "D": "10 11 12 13 14"},
     "corect": "B",
     "explicatie": "Generatorul produce 10, 11, 12, 13... La x=13 conditia opreste bucla cu break INAINTE de print. Deci se afiseaza 10 11 12. Fluxul infinit e OK pentru ca e lazy: produce doar cat ceri."},

    {"runda": 3, "categorie": "de-ce-nu-se-blocheaza", "puncte": 2,
     "cod": "",
     "intrebare": "Un generator cu `while True: yield n` NU blocheaza programul. De ce?",
     "optiuni": {"A": "Python limiteaza automat la 1000 de valori",
                 "B": "e LAZY: produce o valoare doar cand i se cere",
                 "C": "range il opreste singur",
                 "D": "de fapt se blocheaza mereu"},
     "corect": "B",
     "explicatie": "Generatorul e LENES (lazy): la fiecare yield se opreste si asteapta urmatorul next/for. Bucla infinita ruleaza doar cate o repriza pe cerere; TU controlezi cate iei (cu break sau islice)."},

    {"runda": 3, "categorie": "numara-in-flux", "puncte": 2,
     "cod": 'def linii():\n    yield "ERROR a"\n    yield "INFO b"\n    yield "ERROR c"\n\nprint(sum(1 for l in linii() if l.startswith("ERROR")))',
     "intrebare": "Ce afiseaza?",
     "optiuni": {"A": "3", "B": "1",
                 "C": "2", "D": "['ERROR a', 'ERROR c']"},
     "corect": "C",
     "explicatie": "sum(1 for ... if conditie) numara elementele care trec filtrul, fara sa tina liniile in memorie. Doua linii incep cu 'ERROR' -> 2. Tipar uzual pentru procesarea fisierelor mari."},

    {"runda": 3, "categorie": "gen-direct-in-join", "puncte": 2,
     "cod": 'print("-".join(str(x) for x in range(3)))',
     "intrebare": "Ce afiseaza?",
     "optiuni": {"A": "0-1-2", "B": "012",
                 "C": "[0, 1, 2]", "D": "0 1 2"},
     "corect": "A",
     "explicatie": "Dai generatorul direct lui join(), fara lista intermediara. Produce '0','1','2' si le lipeste cu '-' -> '0-1-2'. La fel poti da generatorul lui sum/max/min/any/all."},


    # ---------- RUNDA 4: UNELTE — itertools & yield from ----------
    {"runda": 4, "categorie": "islice-count", "puncte": 2,
     "cod": 'from itertools import count, islice\n\nprint(list(islice(count(10), 3)))',
     "intrebare": "Ce afiseaza?",
     "optiuni": {"A": "[10, 11, 12]", "B": "[10, 13]",
                 "C": "[0, 1, 2]", "D": "[10, 11, 12, 13]"},
     "corect": "A",
     "explicatie": "count(10) e un generator infinit 10, 11, 12, ... islice(..., 3) ia primele 3 elemente ca o 'felie'. Rezultat: [10, 11, 12]."},

    {"runda": 4, "categorie": "chain", "puncte": 2,
     "cod": 'from itertools import chain\n\nprint(list(chain([1, 2], [3], [4, 5])))',
     "intrebare": "Ce afiseaza?",
     "optiuni": {"A": "[[1, 2], [3], [4, 5]]", "B": "[1, 2, 3, 4, 5]",
                 "C": "[1, 2, 3]", "D": "[4, 5]"},
     "corect": "B",
     "explicatie": "chain lipeste mai multi iteratori unul dupa altul, tot lazy, intr-un singur flux: 1, 2, 3, 4, 5. list() le aduna -> [1, 2, 3, 4, 5]."},

    {"runda": 4, "categorie": "yield-from", "puncte": 3,
     "cod": 'def a():\n    yield 1\n    yield 2\n\ndef b():\n    yield from a()\n    yield 3\n\nprint(list(b()))',
     "intrebare": "Ce afiseaza?",
     "optiuni": {"A": "[1, 2, 3]", "B": "[[1, 2], 3]",
                 "C": "[3]", "D": "[1, 2]"},
     "corect": "A",
     "explicatie": "`yield from a()` retransmite TOATE valorile lui a (1, 2), apoi `yield 3` adauga 3. Deci list(b()) -> [1, 2, 3]. yield from inlocuieste un `for x in a(): yield x`."},

    {"runda": 4, "categorie": "islice-pe-infinit", "puncte": 2,
     "cod": 'from itertools import islice\n\ndef numere():\n    n = 0\n    while True:\n        yield n\n        n += 1\n\nprint(list(islice(numere(), 4)))',
     "intrebare": "Ce afiseaza?",
     "optiuni": {"A": "se blocheaza (flux infinit)", "B": "[0, 1, 2, 3]",
                 "C": "[1, 2, 3, 4]", "D": "[0, 1, 2, 3, 4]"},
     "corect": "B",
     "explicatie": "islice 'taie' curat un flux infinit, fara break manual: ia primele 4 valori -> [0, 1, 2, 3]. Nu se blocheaza pentru ca generatorul e lazy si islice cere doar 4."},

    {"runda": 4, "categorie": "cand-nu-folosesti", "puncte": 2,
     "cod": "",
     "intrebare": "Cand NU e potrivit un generator (si folosesti mai bine o lista)?",
     "optiuni": {"A": "cand procesezi un fisier mare linie cu linie",
                 "B": "cand vrei un pipeline sursa -> filtru -> transformare",
                 "C": "cand ai nevoie de toata colectia (indexare, len, reparcurgere)",
                 "D": "cand vrei sa economisesti memorie"},
     "corect": "C",
     "explicatie": "Generatorul e o singura trecere si nu suporta indexare/len. Cand chiar ai nevoie de TOATA colectia (sa o indexezi, sa-i iei len, sa o parcurgi de mai multe ori), folosesti o lista. A, B, D sunt exact cazurile in care generatorul straluceste."},
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
print("===       QUIZ INTERVIU JUNIOR PYTHON  -  GENERATORI       ===")
print("=" * 62)
print()
print("Unele intrebari au o secventa de COD, altele sunt de CONCEPT.")
print("Dupa fiecare raspuns apare o EXPLICATIE (DE CE). Citeste cu atentie.")
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
            1: "BAZELE — yield, OBIECT GENERATOR, LAZY",
            2: "EPUIZARE & GENERATOR EXPRESSIONS",
            3: "CAZURI REALE — PIPELINE, FLUX INFINIT",
            4: "UNELTE — ITERTOOLS & YIELD FROM",
        }
        print()
        print("=" * 62)
        print(f"  RUNDA {runda_curenta}:  {titluri[runda_curenta]}")
        print("=" * 62)
        print()

    # Afisam intrebarea (cu cod, daca exista)
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
    print(f"  *** {nume}: profil JUNIOR SOLID — stapanesti generatorii.")
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