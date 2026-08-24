# EXERCITIUL 5  (SQLAlchemy - bazele)  -  FILME LA CINEMA
# =============================================================

# CONTEXT (caz real)
# ------------------
# Un cinema tine evidenta filmelor programate, cu genul, pretul
# biletului si numarul de bilete vandute, intr-o tabela MySQL
# (`ex32_filme`).
#
# Practici din nou tiparul CRUD, plus doua cazuri noi:
# scaderea pretului cu un procent (ex: reducere/promotie) si
# gasirea filmului cu cele mai multe bilete vandute.


# CE AI DE FACUT
# --------------
# Scrie 4 functii:
#
# 1. adauga_film(titlu, gen, pret_bilet, bilete_vandute)
#       -> creeaza si intoarce un Film nou.
#
# 2. filme_din_gen(gen)
#       -> INTOARCE TITLURILE filmelor din genul respectiv,
#          in ordine ALFABETICA.
#
# 3. scade_pret(film_id, procent)
#       -> scade pretul biletului cu `procent`%
#          (ex: 10 -> pret * 0.90),
#          rotunjit la 2 zecimale.
#
# 4. film_cu_vanzari_maxime()
#       -> INTOARCE TITLUL filmului cu cele mai multe bilete
#          vandute.


# CERINTE
# -------
#   - foloseste  with Session(engine) as s:  la fiecare functie
#   - la (3): calculezi noul pret in Python, apoi il pui pe atribut
#   - la (4): ordoneaza descrescator dupa bilete_vandute si ia
#     primul rand - `s.scalars(stmt).first()`


# OUTPUT ASTEPTAT (din codul de test de mai jos)
# ----------------------------------------------
# SF: ['Dune', 'Interstelar']
# pret Interstelar dupa reducere: 40.5
# filmul cu vanzari maxime: Titanic


# =============================================================

from sqlalchemy import create_engine, select, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session
from session28.date import username, password


URL = f"mysql+pymysql://{username}:{password}@localhost:3306/curs"
engine = create_engine(URL, echo=False)


class Base(DeclarativeBase):
    pass


class Film(Base):
    __tablename__ = "ex32_filme"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    titlu: Mapped[str] = mapped_column(String(50))
    gen: Mapped[str] = mapped_column(String(50))
    pret_bilet: Mapped[float]
    bilete_vandute: Mapped[int]

    def __repr__(self):
        return f"<Film {self.titlu!r} -> {self.gen!r}>"


# ---- PREGATIRE (dat - nu modifica) --------------------------

def pregateste():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    with Session(engine) as s:
        s.add_all([
            Film(
                titlu="Interstelar",
                gen="SF",
                pret_bilet=45.0,
                bilete_vandute=300
            ),
            Film(
                titlu="Dune",
                gen="SF",
                pret_bilet=40.0,
                bilete_vandute=250
            ),
            Film(
                titlu="Titanic",
                gen="Romantic",
                pret_bilet=35.0,
                bilete_vandute=500
            ),
            Film(
                titlu="La La Land",
                gen="Romantic",
                pret_bilet=30.0,
                bilete_vandute=150
            ),
        ])

        s.commit()


# ---- ZONA TA DE LUCRU ---------------------------------------

def adauga_film(
    titlu: str,
    gen: str,
    pret_bilet: float,
    bilete_vandute: int
):
    # TODO: creeaza Film(...), add + commit + return
    with Session(engine) as s:
        film_nou = Film(
            titlu=titlu,
            gen=gen,
            pret_bilet=pret_bilet,
            bilete_vandute=bilete_vandute
        )
        s.add(film_nou)
        s.commit()
        return film_nou

def filme_din_gen(gen: str):
    # TODO: titlurile filmelor din genul respectiv,
    #       ordonate alfabetic
    with Session(engine) as s:
        titluri_filme = select(Film.titlu).where(Film.gen == gen).order_by(Film.titlu.asc())
        return [titlu for titlu in s.scalars(titluri_filme)]

def scade_pret(film_id: int, procent: float):
    # TODO:
    #       s.get -> daca None: raise ValueError
    #       altfel:
    #       pret = round(pret * (1 - procent / 100), 2)
    #       commit
    with Session(engine) as s:
        f = s.get(Film, film_id)
        if f is None:
            raise ValueError("Nu exista film")
        f.pret_bilet = round(f.pret_bilet * (1 - procent / 100), 2)
        s.commit()

def film_cu_vanzari_maxime():
    # TODO: filmul cu cele mai multe bilete vandute
    with Session(engine) as s:
        cele_mai_multe_bilete = (select(Film).order_by(Film.bilete_vandute.desc()))
        filmul_cu_cele_mai_multe_bilete = [Film.titlu for Film in s.scalars(cele_mai_multe_bilete)]
        return filmul_cu_cele_mai_multe_bilete[0]


# ---- COD DE TEST (nu trebuie sa-l modifici) -----------------

pregateste()

print(
    "SF:",
    filme_din_gen("SF")
)
# ['Dune', 'Interstelar']


with Session(engine) as s:
    id_interstelar = s.scalar(
        select(Film.id).where(
            Film.titlu == "Interstelar",
            Film.gen == "SF"
        )
    )


scade_pret(id_interstelar, 10)


with Session(engine) as s:
    print(
        "pret Interstelar dupa reducere:",
        s.get(Film, id_interstelar).pret_bilet
    )
    # 40.5


print(
    "filmul cu vanzari maxime:",
    film_cu_vanzari_maxime()
)
# Titanic