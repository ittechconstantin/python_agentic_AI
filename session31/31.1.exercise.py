# EXERCITIUL 4  (SQLAlchemy - bazele)  -  STOCURI DE PRODUSE
# =============================================================

# CONTEXT (caz real)
# ------------------
# Un magazin are mai multe produse si tine evidenta
# pretului si a stocului fiecarui produs, intr-o tabela MySQL
# (`ex31_produse`).
#
# Practici din nou tiparul CRUD, plus doua cazuri noi:
# modificarea pretului pe baza unui procent si gasirea produsului
# cu cel mai mare stoc.


# CE AI DE FACUT
# --------------
# Scrie 4 functii:
#
# 1. adauga_produs(nume, categorie, pret, stoc)
#       -> creeaza si intoarce un Produs nou.
#
# 2. produse_din_categorie(categorie)
#       -> INTOARCE NUMELE produselor din categoria respectiva,
#          in ordine ALFABETICA.
#
# 3. mareste_pret(produs_id, procent)
#       -> creste pretul cu `procent`%
#          (ex: 10 -> pret * 1.10),
#          rotunjit la 2 zecimale.
#
# 4. produs_cu_stoc_maxim()
#       -> INTOARCE NUMELE produsului cu cel mai mare stoc.


# CERINTE
# -------
#   - foloseste  with Session(engine) as s:  la fiecare functie
#   - la (3): calculezi noul pret in Python, apoi il pui pe atribut
#   - la (4): ordoneaza descrescator dupa stoc si ia primul rand -
#     `s.scalars(stmt).first()`


# OUTPUT ASTEPTAT (din codul de test de mai jos)
# ----------------------------------------------
# Electronice: ['Laptop', 'Mouse']
# pret Laptop dupa marire: 3300.0
# produsul cu stoc maxim: Mouse


# =============================================================

from sqlalchemy import create_engine, select, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session
from session28.date import username, password


URL = f"mysql+pymysql://{username}:{password}@localhost:3306/curs"
engine = create_engine(URL, echo=False)


class Base(DeclarativeBase):
    pass


class Produs(Base):
    __tablename__ = "ex31_produse"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nume: Mapped[str] = mapped_column(String(50))
    categorie: Mapped[str] = mapped_column(String(50))
    pret: Mapped[float]
    stoc: Mapped[int]

    def __repr__(self):
        return f"<Produs {self.nume!r} -> {self.categorie!r}>"


# ---- PREGATIRE (dat - nu modifica) --------------------------

def pregateste():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    with Session(engine) as s:
        s.add_all([
            Produs(
                nume="Laptop",
                categorie="Electronice",
                pret=3000.0,
                stoc=10
            ),
            Produs(
                nume="Mouse",
                categorie="Electronice",
                pret=100.0,
                stoc=50
            ),
            Produs(
                nume="Scaun",
                categorie="Mobila",
                pret=500.0,
                stoc=20
            ),
            Produs(
                nume="Birou",
                categorie="Mobila",
                pret=800.0,
                stoc=15
            ),
        ])

        s.commit()


# ---- ZONA TA DE LUCRU ---------------------------------------

def adauga_produs(
    nume: str,
    categorie: str,
    pret: float,
    stoc: int
):
    # TODO: creeaza Produs(...), add + commit + return
    with Session(engine) as s:
        produs_nou = Produs(
            nume=nume,
            categorie=categorie,
            pret=pret,
            stoc=stoc
    )
    s.add(produs_nou)
    s.commit()
    return produs_nou


def produse_din_categorie(categorie: str):
    # TODO: numele produselor din categoria respectiva,
    #       ordonate alfabetic
    with Session(engine) as s:
        nume_produse = select(Produs.nume).where(Produs.categorie == categorie).order_by(Produs.nume.asc())
        return [nume for nume in s.scalars(nume_produse)]

def mareste_pret(produs_id: int, procent: float):
    # TODO:
    #       s.get -> daca None: raise ValueError
    #       altfel:
    #       pret = round(pret * (1 + procent / 100), 2)
    #       commit
    with Session(engine) as s:
        p = s.get(Produs, produs_id)
        if p is None:
            raise ValueError("Nu exista produs")
        p.pret = round(p.pret * (1 + procent / 100), 2)
        s.commit()

def produs_cu_stoc_maxim():
    # TODO: produsul cu cel mai mare stoc
    with Session(engine) as s:
        cel_mai_mare_stoc = (select(Produs).order_by(Produs.stoc.desc()))
        produsul_cu_cel_mai_mare_stoc = [Produs.stoc for Produs in s.scalars(cel_mai_mare_stoc)]
        return produsul_cu_cel_mai_mare_stoc[0]

# ---- COD DE TEST (nu trebuie sa-l modifici) -----------------

pregateste()

print(
    "Electronice:",
    produse_din_categorie("Electronice")
)
# ['Laptop', 'Mouse']


with Session(engine) as s:
    id_laptop = s.scalar(
        select(Produs.id).where(
            Produs.nume == "Laptop",
            Produs.categorie == "Electronice"
        )
    )


mareste_pret(id_laptop, 10)


with Session(engine) as s:
    print(
        "pret Laptop dupa marire:",
        s.get(Produs, id_laptop).pret
    )
    # 3300.0


print(
    "produsul cu stoc maxim:",
    produs_cu_stoc_maxim()
)
# Mouse