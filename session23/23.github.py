# =============================================================
# GIT  +  GITHUB  -  GHID PRACTIC
# =============================================================
# `git`     - sistem de control al versiunilor (LOCAL pe calculator)
# `GitHub`  - serviciu ONLINE care gazduieste repo-uri git si adauga
#              colaborare (PR, issues, CI, releases, etc.)
#
# Acest fisier este, in mare, COMENTARII si COMENZI bash, NU cod
# Python care ruleaza. La final avem un mic helper Python care
# genereaza un .gitignore standard pentru proiecte Python.
#
# CONCEPTE CHEIE:
#   REPOSITORY (repo) - "proiectul" in care git tine versiunile
#   COMMIT             - "salvare" cu un mesaj, devine punct de istorie
#   BRANCH             - linie paralela de dezvoltare (ex: main, feature/x)
#   MERGE              - combinare a doua branch-uri
#   REMOTE             - copia de pe server (ex: GitHub) a repo-ului
#   PULL  /  PUSH      - descarci / urci modificari de la / la remote
#   PULL REQUEST (PR)  - cerere de a integra un branch in altul (GitHub)
# =============================================================


# =============================================================
# 1.  CONFIGURARE INITIALA  (o singura data pe calculatorul tau)
# =============================================================
#
#   $ git config --global user.name "Numele Tau"
#   $ git config --global user.email "tu@example.com"
#   $ git config --global init.defaultBranch main
#
# Verifici cu:
#   $ git config --list


# =============================================================
# 2.  REPO NOU LOCAL  (pornit din 0)
# =============================================================
#
#   $ mkdir proiect && cd proiect
#   $ git init                      # creaza folderul .git
#   $ echo "# Proiect" > README.md
#   $ git status                    # vezi ce a observat git
#   $ git add README.md             # pune in "staging area"
#   $ git commit -m "primul commit" # salveaza ca punct de istorie


# =============================================================
# 3.  CICLU TIPIC DE LUCRU
# =============================================================
#
#   $ git status                    # ce s-a schimbat?
#   $ git diff                       # ce DIFERENTE sunt?
#   $ git add fisier.py              # adaug in staging
#   $ git add .                       # adaug TOT ce s-a modificat
#   $ git commit -m "fix: bug X"     # commit cu mesaj
#   $ git log --oneline               # istoricul scurt
#
# Mesaje de commit BUNE:
#   - "feat: adauga export in Excel"
#   - "fix: corecteaza calcul TVA"
#   - "docs: actualizeaza README"
#
# Mesaje de commit SLABE:
#   - "update", "merge", "stuff", "asdf", "fix"


# =============================================================
# 4.  BRANCH-URI
# =============================================================
#
#   $ git branch                       # lista branch-urilor; cel curent are *
#   $ git branch feature/login         # creaza branch nou
#   $ git checkout feature/login       # comuta pe branch
#   $ git checkout -b feature/login    # creaza si comuta in 1 pas
#   $ git switch feature/login          # alternativa moderna pentru checkout
#   $ git merge feature/login           # uneste branch-ul in cel curent
#   $ git branch -d feature/login       # sterge branch-ul (dupa merge)


# =============================================================
# 5.  GITHUB  -  legare repo local cu remote
# =============================================================
#
# Pasi pentru a publica un proiect existent:
#   1) creeaza repo gol pe GitHub (nu adauga README/gitignore - le
#      ai deja local)
#   2) urmezi instructiunile "push existing":
#
#        $ git remote add origin git@github.com:user/proiect.git
#        $ git branch -M main
#        $ git push -u origin main
#
#   "origin" este NUMELE conventional al remote-ului principal.
#
# Verifici cu:
#   $ git remote -v


# =============================================================
# 6.  CLONE  -  pornesti de la un repo existent
# =============================================================
#
#   $ git clone git@github.com:user/proiect.git
#   $ cd proiect
#
# Avantaj: clonezi cu tot cu istoric, branch-uri, remote-uri.


# =============================================================
# 7.  PUSH  /  PULL  -  comunicare cu remote-ul
# =============================================================
#
#   $ git push                       # urci commit-urile locale
#   $ git pull                        # iei modificarile de pe remote
#
# La inceput poate fi necesar:  git push -u origin main
# (asta seteaza tracking-ul intre local si remote pentru branch-ul main)


# =============================================================
# 8.  WORKFLOW TIPIC DE ECHIPA  (pull request)
# =============================================================
#
#   1)  $ git checkout main
#       $ git pull                       # ia ultimele schimbari
#   2)  $ git checkout -b feature/raport  # branch pentru lucru
#   3)  ... codezi, commits, ...
#   4)  $ git push -u origin feature/raport
#   5)  pe GitHub: "Compare & pull request"
#       descrie schimbarea, ceri review
#   6)  dupa aprobare:  Merge pull request
#   7)  local:  $ git checkout main
#               $ git pull
#               $ git branch -d feature/raport


# =============================================================
# 9.  CONFLICTE LA MERGE
# =============================================================
#
# Cand 2 oameni schimba aceeasi linie pe branch-uri diferite,
# git nu stie pe care sa o pastreze. Iti afiseaza:
#
#   <<<<<<< HEAD
#   varianta de pe branch-ul curent
#   =======
#   varianta din branch-ul ce vine
#   >>>>>>> feature/altul
#
# Editezi fisierul, lasi varianta corecta, stergi marcajele,
# apoi:
#   $ git add fisier.py
#   $ git commit


# =============================================================
# 10.  UNDO  /  REPARARI  uzuale
# =============================================================
#
# - vad ce am schimbat dar nu am facut commit:
#       $ git diff
#
# - "anulez" modificarile dintr-un fisier (NEINREGISTRATE):
#       $ git restore fisier.py
#
# - scot un fisier din staging (dar pastrez modificarile):
#       $ git restore --staged fisier.py
#
# - schimb mesajul ULTIMULUI commit (daca NU a fost push-uit):
#       $ git commit --amend -m "alt mesaj"
#
# - ma intorc cu un commit (creeaza un commit care anuleaza):
#       $ git revert HEAD
#
# - vad istoria:
#       $ git log
#       $ git log --oneline --graph --all


# =============================================================
# 11.  README.md  -  prima impresie a repo-ului
# =============================================================
#
# Scrie in README.md:
#   - Titlu si scop scurt
#   - Cum se INSTALEAZA / RULEAZA proiectul
#   - Exemple de utilizare
#   - Linkuri / contacte
#
# Sablon minimal:
#
#   # Numele Proiectului
#
#   Scop in 1-2 propozitii.
#
#   ## Instalare
#       git clone ...
#       pip install -r requirements.txt
#
#   ## Utilizare
#       python main.py
#
#   ## Licenta
#   MIT


# =============================================================
# 12.  .gitignore  -  ce NU urcam pe GitHub
# =============================================================
#
# Reguli simple:
#   - NU urci secrete (api keys, parole, fisiere .env)
#   - NU urci fisiere generate (.pyc, __pycache__, build/, dist/)
#   - NU urci dependinte mari (venv/, node_modules/)
#   - NU urci fisiere personale de IDE (.idea, .vscode/settings.json)
#
# Github are template-uri "gitignore for Python" gata facute. Mai jos
# avem un helper Python care creeaza un .gitignore standard pentru
# proiecte Python.


# =============================================================
# 13.  Helper PYTHON: genereaza un .gitignore standard
# =============================================================

GITIGNORE_PYTHON = """\
# =============================================================
# .gitignore  -  ce NU trimitem pe GitHub, si de ce
# =============================================================
# Git urmareste FIECARE fisier dintr-un folder, by default. Un
# .gitignore spune explicit "ignora astea" - fisiere care nu au ce
# cauta in istoricul proiectului, pentru unul din motivele de mai jos.

# Bytecode Python - fisiere COMPILATE automat de Python la rulare
# (cache intern, .pyc). Se regenereaza singure de fiecare data; a le
# urca ar umple istoricul cu fisiere binare diferite de la un
# calculator la altul, fara niciun folos.
__pycache__/
*.py[cod]
*$py.class

# Secrete - chei API, parole, token-uri (de obicei intr-un fisier
# .env). Daca ajung pe GitHub, mai ales pe un repo PUBLIC, oricine le
# poate vedea si folosi - inclusiv dupa ce le stergi mai tarziu,
# pentru ca raman in ISTORICUL vechi de commit-uri.
.env

# Medii virtuale - folderul cu Python + toate librariile instalate
# pentru acest proiect (poate avea sute de MB). Se poate RECREA oricand
# din requirements.txt - n-are rost sa il urci.
.venv/
venv/
env/
ENV/

# Build / distributie - fisiere generate cand "impachetezi" proiectul
# ca librarie (ex: pip build). Se regenereaza mereu din codul sursa.
build/
dist/
*.egg-info/
*.egg

# Setari personale de editor - fiecare coleg are alt IDE, alte
# extensii, alte preferinte de afisare. Nu sunt parte din proiect, ci
# strict personale.
.idea/
.vscode/
*.swp

# Loguri si cache - fisiere generate la rulare/testare (loguri, cache
# de teste, rapoarte de acoperire a codului). Cresc repede si nu ajuta
# pe nimeni in istoricul de cod.
*.log
.cache/
.pytest_cache/
.coverage
htmlcov/

# Fisiere specifice sistemului de operare - create automat de macOS/
# Windows la simpla navigare prin foldere, fara nicio legatura cu codul.
.DS_Store
Thumbs.db

# Date generate de aplicatie - rapoarte/exporturi create cand RULEZI
# codul (nu scrise de tine manual). ATENTIE: e o regula GENERALA - daca
# ai fisiere .csv/.json/.xlsx pe care CHIAR vrei sa le urci (ex: date
# demo pentru un proiect), adauga o exceptie explicita, cu "!" in fata:
#   !cale/catre/fisierul_tau.csv
output/
*.xlsx
*.csv
*.json
"""


def creeaza_gitignore(folder=".", continut=GITIGNORE_PYTHON):
    """Scrie un .gitignore standard in folderul dat."""
    import os
    cale = os.path.join(folder, ".gitignore")
    with open(cale, "w", encoding="utf-8") as f:
        f.write(continut)
    print(f"[ok] .gitignore creat la {cale}")
    return cale


# Demo - generam un .gitignore intr-un folder local dedicat
# (separat, ca sa nu ascunda din greseala alte fisiere):
import os
folder = "data_s23_git"
os.makedirs(folder, exist_ok=True)
cale = creeaza_gitignore(folder)
with open(cale, encoding="utf-8") as f:
    print(f.read()[:120], "...")


# =============================================================
# 14.  COMENZI MAI AVANSATE  (la cerere, in proiecte mari)
# =============================================================
#
#   $ git stash               # pune temporar la o parte ce ai modificat
#   $ git stash pop            # readuce modificarile
#
#   $ git tag v1.0.0           # marcheaza un punct ca "release"
#   $ git push --tags          # urca tag-urile pe remote
#
#   $ git rebase main          # mut commit-urile mele peste main (alterneaza
#                                merge - mai liniar in istoric)
#
#   $ git fetch                # ia info de pe remote, dar NU le aplica


# =============================================================
# 15.  OBICEIURI BUNE
# =============================================================
#
# - commit-uri MICI si CLARE  (nu "salvez tot pe la sfarsit")
# - mesaje de commit care explica DE CE, nu doar CE
# - main / master sa fie mereu STABIL
# - lucreaza pe branch-uri pentru orice feature / bugfix
# - face PR si cere review chiar daca esti singur (oblige sa "explici")
# - .gitignore  setat de la inceput
# - foloseste branch protection pe main daca esti in echipa


# =============================================================
# 16.  RESURSE
# =============================================================
#
# - https://git-scm.com/doc            (documentatia oficiala git)
# - https://docs.github.com            (documentatia GitHub)
# - "Pro Git" book (gratis online)     - cea mai buna referinta
# - https://learngitbranching.js.org   - tutorial vizual interactiv


# =============================================================
# CONCLUZIE
# =============================================================
# Cu  init / add / commit / push / pull / branch / merge  acoperi
# 90% din ce vei face in fiecare zi.
# Restul (rebase, stash, tag, cherry-pick, reset, reflog) le
# inveti pe parcurs, cand le intalnesti.
#
# Cel mai important: faci commit-uri DES, mesaje CLARE, lucrezi
# pe branch-uri si folosesti pull request-uri pentru review.
# =============================================================
