# SQLAlchemy ORM (2.0+)  -  PARTEA 1: BAZELE  (tabele ca CLASE, randuri ca OBIECTE)
# =============================================================
# ATENTIE: e prima ta intalnire cu un ORM. Mergem INCET si explicam
# fiecare cuvant nou. Daca stii sesiunea 27 (SQL prin mysql.connector),
# aici o sa vezi cum acelasi lucru se face mult mai natural, cu obiecte.
#
# Aceasta sesiune se opreste la un SINGUR model (o singura tabela) si CRUD.
# Relatiile intre tabele (o a doua tabela legata de prima), agregarile si
# proiectul complet vin in SESIUNEA 31 (partea 2) - dupa ce te-ai obisnuit
# cu ideile de aici.
#
# CE ESTE UN ORM? (ideea in 4 randuri)
# ------------------------------------
# ORM = Object-Relational Mapper = un "traducator" intre doua lumi:
#   - lumea Python:  clase si obiecte  (User, ana.email)
#   - lumea bazei:   tabele si randuri  (tabela useri, un rand)
# Tu scrii cod Python cu obiecte; ORM-ul scrie SQL-ul in locul tau si
# vorbeste cu baza de date. Nu mai lipesti siruri de SQL de mana.
#
# ANALOGIE: in sesiunea 27 vorbeai cu baza "in limba ei" (SQL). ORM-ul e
# un translator: tu vorbesti Python, el traduce in SQL si inapoi.
#
# HARTA de termeni (tine minte aceasta corespondenta):
#   o CLASA   (User)          <->  o TABELA   (useri)
#   un OBIECT (User(nume=..))  <->  un RAND    (o inregistrare)
#   un ATRIBUT (user.email)    <->  o COLOANA  (email)
#
# CERINTE ca sa ruleze:
#   - server MySQL pornit; user 'cursant', parola 'parola123', DB 'curs'
#   - pip install sqlalchemy pymysql
#
# Ce trebuie sa stii deja (recap):
#   - clase si obiecte (self, atribute) - sesiunea 17+
#   - SQL de baza (SELECT/INSERT/UPDATE/DELETE) - sesiunile 26-27
# =============================================================

from typing import Optional

from sqlalchemy import create_engine, select, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session


# 1. ENGINE  -  "linia telefonica" spre baza de date
# -------------------------------------------------------------
# ENGINE-ul e obiectul care STIE cum sa se conecteze la baza. Il creezi
# O SINGURA DATA pentru toata aplicatia si il refolosesti peste tot.
#
# El primeste un "connection string" - o adresa cu toate detaliile.
# Sa o citim bucata cu bucata:
#
#   mysql      +  pymysql  ://  cursant : parola123 @ localhost : 3306 / curs
#   |             |              |         |           |           |      |
#   ce baza      ce driver      user      parola      host        port   DB
#   (dialect)    (biblioteca)
#
# "pymysql" e biblioteca prin care SQLAlchemy vorbeste efectiv cu MySQL.
from session28.date import username, password

DB_CONFIG ={
    "host": "localhost",
    "port": 3306,
    "user": username,     # root
    "password": password,  # parola_voastra,
    "database": "curs"
}


URL = f"mysql+pymysql://{DB_CONFIG['user']}:{DB_CONFIG['password']}@{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['database']}"
engine = create_engine(URL, echo=False)

# PONT: pune  echo=True  ca sa vezi in consola EXACT ce SQL genereaza
# SQLAlchemy pentru fiecare operatie. Foarte util cand inveti.


# 2. BASE  -  "parintele" tuturor modelelor
# -------------------------------------------------------------
# Toate clasele-tabela vor MOSTENI din aceasta clasa Base. Rolul ei: sa
# tina evidenta tuturor modelelor (ca sa poata crea tabelele mai tarziu).
# O scrii o data, goala, si o folosesti mai jos.

class Base(DeclarativeBase):
    pass


# 3. PRIMUL MODEL  -  o clasa care ESTE o tabela
# -------------------------------------------------------------
# Reguli:
#   - clasa mosteneste  Base
#   - __tablename__  spune cum se cheama tabela in baza
#   - fiecare atribut e o COLOANA, scris asa:
#         nume: Mapped[TIP] = mapped_column(optiuni)
#     unde  Mapped[int]  inseamna "aceasta coloana tine un intreg", iar
#     mapped_column(...)  da detalii (cheie primara, unic, valoare implicita).
#   - Mapped[Optional[int]]  = coloana care POATE fi goala (NULL in SQL).

class User(Base):
    __tablename__ = "ex30_useri"

    id : Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nume: Mapped[str] = mapped_column(String(50))
    email : Mapped[str] = mapped_column(String(100), unique=True)
    varsta : Mapped[int] = mapped_column(default=None)


    def __str__(self):
        return f"Nume {self.nume}, email {self.email}, varsta {self.varsta} "


# Ce SQL genereaza clasa de mai sus, in spate (echivalentul din sesiunea 27):
#   CREATE TABLE sa_useri (
#       id INT AUTO_INCREMENT PRIMARY KEY,
#       nume VARCHAR(50),
#       email VARCHAR(100) UNIQUE,
#       varsta INT
#   );
#
# NOTA: in sesiunea 31 mai adaugam o a DOUA tabela (Comanda), legata de
# aceasta cu un FOREIGN KEY + un `relationship`. Deocamdata lucram cu o
# singura tabela, ca sa te obisnuiesti cu tiparul de baza.


# 4. CREAREA TABELEI in baza
# -------------------------------------------------------------
# Pana acum am DESCRIS tabela (clasa). Acum o CREAM efectiv in MySQL.
# Base.metadata stie toate modelele care mostenesc Base.
#   drop_all   -> sterge tabelele (ca sa pornim curat la fiecare rulare)
#   create_all -> le creeaza din nou dupa descrierea din clase

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)
print(f"[ok] a fost adaugata tabela useri")

# 5. SESSION + CREATE  -  cum ADAUGI date
# -------------------------------------------------------------
# SESSION = spatiul tau de lucru cu baza. ANALOGIE: un COS de cumparaturi.
# Pui obiecte in cos (add), iar la final "platesti" (commit) - abia atunci
# se scriu in baza. Fara commit, nu s-a salvat nimic (exact ca la sesiunea 27).
#
#   with Session(engine) as s:   -> deschide un cos si il inchide singur la final

with Session(engine) as s:

    ana = User(nume="Ana", email ="ana@gmail.com", varsta = 30)
    george = User(nume="George", email="george@gmail.com", varsta =40)

    # s.add_all([ana, george])
    s.add(ana)
    s.add(george)
    s.commit()

    print("[ok] datele au fost salvate")


# In spate: INSERT INTO sa_useri (nume, email, varsta) VALUES ('Ana', ...);


# 6. READ  -  cum CITESTI date
# -------------------------------------------------------------
# Trei moduri des folosite:
with Session(engine) as s:
    # a) dupa cheia primara - cel mai simplu:  s.get(Model, id)
    print("A)")
    print(s.get(User, 1))

    # b) toate randurile:  select(Model) + scalars() -> OBIECTE
    #    (scalars = "da-mi obiectele", nu tupluri)
    print("B)")
    toti = s.scalars(select(User)).all()
    for user in toti:
        print(user)

    # c) cu filtru + ordonare (echivalent SQL: WHERE ... ORDER BY ...)
    print("C)")
    useri_gte_30 = select(User).where(User.varsta > 30).order_by(User.varsta.desc())
    for user in s.scalars(useri_gte_30):
      print(user)

# In spate (b): SELECT * FROM sa_useri;
# In spate (c): SELECT * FROM sa_useri WHERE varsta > 30 ORDER BY varsta DESC;


# 7. UPDATE  -  MAGIA: schimbi obiectul, session-ul observa
# -------------------------------------------------------------
# Nu scrii "UPDATE". Iei obiectul, ii schimbi un atribut, si la commit
# session-ul isi da seama singur ce s-a schimbat si trimite UPDATE-ul.

with Session(engine) as s:
    user_curent = s.get(User, 1)  # aduc userul curent
    user_curent.varsta = 50
    s.commit()
    print(f"Userul a fost actualizat")


# In spate: UPDATE sa_useri SET varsta = 29 WHERE id = 1;


# 8. DELETE  -  scoti obiectul din baza
# -------------------------------------------------------------

with Session(engine) as s:
    user_curent = s.get(User, 1)
    s.delete(user_curent)
    s.commit()

    print("Userul a fost sters")



# In spate: DELETE FROM sa_useri WHERE id = 2;


# 9. CURATARE (stergem tabela de test la final)
# -------------------------------------------------------------
Base.metadata.drop_all(engine)
print(f"[ok] gata")


# =============================================================
# RECAP / IDEI CHEIE  (+ greseli de inceput)
# =============================================================
# HARTA:  clasa=tabela, obiect=rand, atribut=coloana.
#
# Pasii tipici:
#   1) engine = create_engine(URL)              # o data pentru toata aplicatia
#   2) class Model(Base): atribut: Mapped[tip] = mapped_column(...)
#   3) Base.metadata.create_all(engine)         # creeaza tabela
#   4) with Session(engine) as s:               # "cosul" de lucru
#         s.add(obj);  s.commit()               # scriere
#         s.get(Model, id)                       # citire dupa cheie
#         s.scalars(select(Model))               # citire -> OBIECTE
#         s.delete(obj);  s.commit()             # stergere
#
# GRESELI DE INCEPUT:
#   - uiti  s.commit()  -> modificarile NU se salveaza (ca la sesiunea 27).
#   - pui  echo=True  in create_engine ca sa VEZI SQL-ul generat - foloseste-l
#     cand nu intelegi ce se intampla.
#
# URMEAZA IN SESIUNEA 31 (partea 2):
#   - o a doua tabela legata de User printr-un FOREIGN KEY + `relationship`
#     (navighezi intre obiecte fara sa scrii JOIN-uri de mana)
#   - cascade (stergi parintele, dispar copiii)
#   - agregari (func.count, func.avg) si diferenta scalars() vs execute()
#   - sessionmaker + rollback
#   - un PROIECT complet (Job Application Tracker) care foloseste toate astea
# =============================================================