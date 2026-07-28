# QUIZ INTERVIU  -  intrebari tip interviu junior Python (s1-s9)
# =============================================================
# Fiecare intrebare contine:
#   - o SECVENTA DE COD (de tip "ce afiseaza? / ce eroare apare?")
#   - 4 variante A/B/C/D
#   - EXPLICATIE obligatorie dupa raspuns (afisata si cand
#     raspunzi corect — la interviu conteaza sa stii DE CE)
#
# Toate gotcha-urile clasice de interviu:
#   - aliasing si mutabilitate (b = a vs b = a[:])
#   - integer vs float division (//  vs  /  vs  %)
#   - mutarea unei liste in timpul iterarii (remove + index shift)
#   - string-uri imuabile (TypeError la s[0] = 'X')
#   - split() fara argument vs split(' ')
#   - dict.get() vs d[cheie] (KeyError)
#   - tuple ca cheie de dict (hashable) vs lista (unhashable)
#   - set: operatii (& | - ^) si TypeError la list neHashable
#   - while/for + else
#   - range descendent
#   - truthy / falsy ([], "", 0, None toate False)
#
# Cum se ruleaza:
#   python3 10.2.quiz_interviu.py
#
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
    # ---------- RUNDA 1: OPERATORI & STRING-URI ----------
    {"runda": 1, "categorie": "operatori", "puncte": 2,
     "cod": "print(7 // 2 + 7 % 2)",
     "intrebare": "Ce afiseaza?",
     "optiuni": {"A": "3", "B": "3.5", "C": "4", "D": "7"},
     "corect": "C",
     "explicatie": "// e impartirea INTREAGA (7//2 = 3), % e RESTUL (7%2 = 1). 3 + 1 = 4."},

    {"runda": 1, "categorie": "string-uri", "puncte": 2,
     "cod": 'print("python"[::-1])',
     "intrebare": "Ce afiseaza?",
     "optiuni": {"A": "python", "B": "nohtyp", "C": "p y t h o n", "D": "eroare"},
     "corect": "B",
     "explicatie": "Slicing-ul [start:stop:step] cu step=-1 parcurge invers. [::-1] e idiomul standard pentru inversare."},

    {"runda": 1, "categorie": "string-uri", "puncte": 2,
     "cod": 's = "hello"\ns[0] = "H"\nprint(s)',
     "intrebare": "Ce se intampla?",
     "optiuni": {"A": "afiseaza Hello", "B": "afiseaza hello",
                 "C": "TypeError: string immutable", "D": "afiseaza H"},
     "corect": "C",
     "explicatie": "STRING-URILE SUNT IMUABILE in Python. Nu poti modifica un caracter — trebuie sa creezi un string nou: s = 'H' + s[1:]."},

    {"runda": 1, "categorie": "string-uri", "puncte": 2,
     "cod": 'print("banana".replace("a", "o", 2))',
     "intrebare": "Ce afiseaza?",
     "optiuni": {"A": "bonono", "B": "bonona", "C": "banana", "D": "boonono"},
     "corect": "B",
     "explicatie": "Al 3-lea parametru al lui replace() e numarul MAXIM de inlocuiri. Doar primii 2 'a' devin 'o': b-o-n-o-n-a."},

    {"runda": 1, "categorie": "string-uri", "puncte": 2,
     "cod": 'print("a b  c".split())',
     "intrebare": "Ce afiseaza? (atentie: DOUA spatii intre b si c)",
     "optiuni": {"A": "['a', 'b', '', 'c']", "B": "['a', 'b', 'c']",
                 "C": "['a b  c']", "D": "['a', ' ', 'b', ' ', ' ', 'c']"},
     "corect": "B",
     "explicatie": "split() FARA argument trateaza orice succesiune de whitespace (chiar mai multe spatii la rand) ca UN SINGUR separator si NU produce string-uri goale. Daca scriam split(' ') cu argument explicit, ar fi iesit ['a', 'b', '', 'c']."},


    # ---------- RUNDA 2: LISTE & MUTABILITATE ----------
    {"runda": 2, "categorie": "aliasing", "puncte": 3,
     "cod": "a = [1, 2, 3]\nb = a\nb.append(4)\nprint(a)",
     "intrebare": "Ce afiseaza?",
     "optiuni": {"A": "[1, 2, 3]", "B": "[1, 2, 3, 4]",
                 "C": "[4, 1, 2, 3]", "D": "eroare"},
     "corect": "B",
     "explicatie": "b = a NU copiaza lista — creeaza un ALIAS. Ambele variabile arata catre acelasi obiect. Modificarea lui b se vede in a."},

    {"runda": 2, "categorie": "copy", "puncte": 2,
     "cod": "a = [1, 2, 3]\nb = a[:]\nb.append(4)\nprint(a)",
     "intrebare": "Ce afiseaza?",
     "optiuni": {"A": "[1, 2, 3]", "B": "[1, 2, 3, 4]",
                 "C": "[4, 1, 2, 3]", "D": "eroare"},
     "corect": "A",
     "explicatie": "a[:] (sau list(a)) creeaza o COPIE noua. b e o lista independenta — modificarea lui b nu afecteaza a."},

    {"runda": 2, "categorie": "iteratie", "puncte": 3,
     "cod": "nums = [1, 2, 3, 4]\nfor n in nums:\n    if n % 2 == 0:\n        nums.remove(n)\nprint(nums)",
     "intrebare": "Ce afiseaza?",
     "optiuni": {"A": "[1, 3]", "B": "[1, 3, 4]",
                 "C": "[2, 4]", "D": "[]"},
     "corect": "A",
     "explicatie": "Trap clasic: NU modifica lista pe care iterezi! Trace: index 0 -> n=1, no remove. index 1 -> n=2, remove (nums=[1,3,4]). index 2 -> n=4 (nu 3, pentru ca indicii s-au mutat!), remove (nums=[1,3]). index 3 -> out. 3 a fost SARIT peste. Rezultat: [1, 3]. La interviu: foloseste copie  for n in nums[:]:  sau o lista filtrata noua."},

    {"runda": 2, "categorie": "operatori", "puncte": 1,
     "cod": "print([1, 2] * 3 + [0])",
     "intrebare": "Ce afiseaza?",
     "optiuni": {"A": "[1, 2, 1, 2, 1, 2, 0]", "B": "[3, 6, 0]",
                 "C": "[1, 2, 3, 0]", "D": "eroare"},
     "corect": "A",
     "explicatie": "* la lista = REPETARE, + = CONCATENARE. Precedenta: * inainte de +. Deci [1,2]*3 = [1,2,1,2,1,2], apoi + [0]."},

    {"runda": 2, "categorie": "referinte", "puncte": 3,
     "cod": "a = [1, 2, 3]\nb = [a, a]\na.append(4)\nprint(b)",
     "intrebare": "Ce afiseaza?",
     "optiuni": {"A": "[[1,2,3], [1,2,3]]",
                 "B": "[[1,2,3,4], [1,2,3,4]]",
                 "C": "[[1,2,3,4], [1,2,3]]",
                 "D": "eroare"},
     "corect": "B",
     "explicatie": "b contine de DOUA ori aceeasi referinta catre a. Modificand a o singura data, o vezi 'reflectata' de doua ori in b."},


    # ---------- RUNDA 3: DICT / TUPLE / SET ----------
    {"runda": 3, "categorie": "dict", "puncte": 1,
     "cod": 'd = {"a": 1, "b": 2}\nprint(d.get("c", 99))',
     "intrebare": "Ce afiseaza?",
     "optiuni": {"A": "None", "B": "99", "C": "KeyError", "D": "c"},
     "corect": "B",
     "explicatie": ".get(cheie, default) returneaza default daca cheia LIPSESTE. Avantaj fata de d['c']: nu arunca KeyError."},

    {"runda": 3, "categorie": "dict", "puncte": 2,
     "cod": 'd = {"a": 1}\nprint(d["b"])',
     "intrebare": "Ce se intampla?",
     "optiuni": {"A": "afiseaza None", "B": "afiseaza 0",
                 "C": "KeyError", "D": "afiseaza 'b'"},
     "corect": "C",
     "explicatie": "Accesul direct cu d[cheie] arunca KeyError daca cheia nu exista. La interviu: cand vrei fallback safe, foloseste .get()."},

    {"runda": 3, "categorie": "set", "puncte": 3,
     "cod": "s = {1, 2, 3}\ns.add([4, 5])\nprint(s)",
     "intrebare": "Ce se intampla?",
     "optiuni": {"A": "{1, 2, 3, [4, 5]}",
                 "B": "{1, 2, 3, 4, 5}",
                 "C": "TypeError: unhashable type: 'list'",
                 "D": "{1, 2, 3}"},
     "corect": "C",
     "explicatie": "Elementele unui set TREBUIE sa fie HASHABLE (imuabile). Lista e MUTABILA -> neHashable -> TypeError. Pentru a stoca o secventa intr-un set foloseste TUPLE: s.add((4, 5)) ar fi mers."},

    {"runda": 3, "categorie": "set", "puncte": 2,
     "cod": "print({1, 2, 3} & {2, 3, 4})",
     "intrebare": "Ce afiseaza?",
     "optiuni": {"A": "{1, 2, 3, 4}", "B": "{2, 3}",
                 "C": "{1, 4}", "D": "set()"},
     "corect": "B",
     "explicatie": "& = INTERSECTIE (elementele comune). Alte operatii: | reuniune, - diferenta, ^ diferenta simetrica."},

    {"runda": 3, "categorie": "tuple", "puncte": 3,
     "cod": 'd = {(1, 2): "a"}\nprint(d[(1, 2)])',
     "intrebare": "Ce afiseaza?",
     "optiuni": {"A": "a", "B": "KeyError", "C": "TypeError", "D": "(1, 2)"},
     "corect": "A",
     "explicatie": "Tuple-urile sunt HASHABLE (imuabile) deci pot fi chei de dict. ATENTIE: o LISTA nu poate fi cheie — e mutabila, neHashable. (print afiseaza 'a' fara ghilimele.)"},


    # ---------- RUNDA 4: CONTROL FLOW & BUCLELE ----------
    {"runda": 4, "categorie": "truthy", "puncte": 2,
     "cod": 'if [] or "":\n    print("A")\nelif 0 or None:\n    print("B")\nelse:\n    print("C")',
     "intrebare": "Ce afiseaza?",
     "optiuni": {"A": "A", "B": "B", "C": "C", "D": "eroare"},
     "corect": "C",
     "explicatie": "Valori FALSY in Python: 0, 0.0, '', [], {}, set(), None, False. Toate cele din if/elif sunt falsy -> intra in else."},

    {"runda": 4, "categorie": "while-else", "puncte": 3,
     "cod": 'i = 0\nwhile i < 3:\n    i += 1\nelse:\n    print("done")\nprint(i)',
     "intrebare": "Ce afiseaza?",
     "optiuni": {"A": "done apoi 3 (doua linii)",
                 "B": "done apoi 2 (doua linii)",
                 "C": "doar 3 (fara done)",
                 "D": "eroare"},
     "corect": "A",
     "explicatie": "while/else: else-ul ruleaza cand conditia devine FALSE (FARA break). Aici nu e break -> ruleaza, deci 'done' se afiseaza. Apoi print(i) afiseaza i=3."},

    {"runda": 4, "categorie": "for-else", "puncte": 3,
     "cod": 'for n in [1, 2, 3]:\n    if n == 2:\n        break\nelse:\n    print("done")\nprint("end")',
     "intrebare": "Ce afiseaza?",
     "optiuni": {"A": "done apoi end (doua linii)",
                 "B": "doar end",
                 "C": "doar done",
                 "D": "(nimic)"},
     "corect": "B",
     "explicatie": "for/else: else-ul NU ruleaza daca a fost break. Aici break la n=2 -> sare peste else. Doar 'end' printeaza."},

    {"runda": 4, "categorie": "range", "puncte": 2,
     "cod": "print(list(range(5, 0)))",
     "intrebare": "Ce afiseaza?",
     "optiuni": {"A": "[5, 4, 3, 2, 1]", "B": "[0, 1, 2, 3, 4, 5]",
                 "C": "[]", "D": "eroare"},
     "corect": "C",
     "explicatie": "range(start, stop) are step=+1 default. De la 5 cu pas +1, nu ajungi la 0. Lista goala. Pentru descrescator: range(5, 0, -1)."},

    {"runda": 4, "categorie": "while-nested", "puncte": 3,
     "cod": "i, total = 0, 0\nwhile i < 3:\n    j = 0\n    while j < 2:\n        total += 1\n        j += 1\n    i += 1\nprint(total)",
     "intrebare": "Ce afiseaza?",
     "optiuni": {"A": "3", "B": "5", "C": "6", "D": "9"},
     "corect": "C",
     "explicatie": "Bucla EXTERIOARA face 3 iteratii (i: 0,1,2), iar INTERIOARA face 2 la fiecare (j: 0,1). Total: 3 * 2 = 6."},
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
print("===        QUIZ INTERVIU JUNIOR PYTHON  -  s1 - s9        ===")
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
            1: "OPERATORI & STRING-URI",
            2: "LISTE & MUTABILITATE",
            3: "DICT / TUPLE / SET",
            4: "CONTROL FLOW & BUCLELE",
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
    # adunam categoriile greșite intr-un set
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