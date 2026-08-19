# EXERCITIUL 1  (SQLAlchemy - bazele)  -  STOC PRODUSE (MAGAZIN ONLINE)
# =============================================================
#
# CONTEXT (caz real)
# ------------------
# Gestionezi stocul unui magazin online, intr-o tabela MySQL
# (`ex30_produse_stoc`). Fiecare produs are un nume, un pret si un stoc.
# Fiecare functie deschide o sesiune, face treaba si intoarce ceva
# folositor - exact tiparul din 30.sqlalchemy_bazele.py.
#
# Codul de PREGATIRE (engine, model, creare tabela + date DEMO) e deja
# scris mai jos - tu completezi doar functiile din ZONA TA DE LUCRU.
#
#
# CE AI DE FACUT
# --------------
# Scrie 4 functii:
#
# 1. nr_produse()                    -> cate produse sunt in total.
# 2. produse_stoc_redus(prag)        -> NUMELE produselor cu stoc < prag,
#                                       ordonate crescator dupa stoc (cel
#                                       mai putin stoc primul - cele mai
#                                       urgente de reaprovizionat).
# 3. reaprovizioneaza(produs_id, cantitate)  -> aduna `cantitate` la
#                                       stocul produsului. Daca id-ul nu
#                                       exista, ridica ValueError.
# 4. sterge_produs(produs_id)        -> sterge un produs dupa id.
#
#
# CERINTE
# -------
#   - foloseste  with Session(engine) as s:  la fiecare functie (tiparul
#     din 30.sqlalchemy_bazele.py)
#   - citire simpla:      s.scalars(select(Produs)).all()
#   - dupa id:             s.get(Produs, id)
#   - nu uita  s.commit()  dupa orice scriere (update / delete)
#
#
# OUTPUT ASTEPTAT (din codul de test de mai jos)
# ----------------------------------------------
#   nr produse: 4
#   stoc redus (<6): ['Mouse gaming', 'Casti wireless', 'Webcam HD']
#   stoc Mouse gaming dupa reaprovizionare: 11
#   dupa stergere, nr produse: 3
#

# =============================================================

from sqlalchemy import create_engine, select, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session

from session28.date import username, password

URL = f"mysql+pymysql://{username}:{password}@localhost:3306/curs"
engine = create_engine(URL, echo=False)


class Base(DeclarativeBase):
    pass


class Produs(Base):
    __tablename__ = "ex30_produse_stoc"

    id:     Mapped[int]   = mapped_column(primary_key=True, autoincrement=True)
    nume:   Mapped[str]   = mapped_column(String(100))
    pret:   Mapped[float]
    stoc:   Mapped[int]

    def __repr__(self):
        return f"<Produs {self.nume!r} (stoc={self.stoc})>"



# ---- PREGATIRE (dat - nu modifica) --------------------------
def pregateste():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    with Session(engine) as s:
        s.add_all([
            Produs(nume="Casti wireless",     pret=150.0, stoc=3),
            Produs(nume="Mouse gaming",       pret=80.0,  stoc=1),
            Produs(nume="Tastatura mecanica", pret=250.0, stoc=20),
            Produs(nume="Webcam HD",          pret=120.0, stoc=5),
        ])
        s.commit()


# ---- ZONA TA DE LUCRU ---------------------------------------
def nr_produse():
    # TODO: cate randuri sunt in ex30_produse_stoc
    with Session(engine) as s:
        toate_produse = s.scalars(select(Produs)).all() #[<Produs 'Casti wireless' (stoc=3)>, <Produs 'Mouse gaming' (stoc=1)>, <Produs 'Tastatura mecanica' (stoc=20)>, <Produs 'Webcam HD' (stoc=5)>, <Produs 'Casti wireless' (stoc=3)>, <Produs 'Mouse gaming' (stoc=1)>, <Produs 'Tastatura mecanica' (stoc=20)>, <Produs 'Webcam HD' (stoc=5)>]
        return len(toate_produse)



def produse_stoc_redus(prag: int):
    #                                       NUMELE produselor cu stoc < prag,
    #                                       ordonate crescator dupa stoc (cel
    #                                       mai putin stoc primul - cele mai
    #                                       urgente de reaprovizionat).
    # TODO: numele produselor cu stoc < prag, ordonate crescator dupa stoc
    with Session(engine) as s:
        produse_stoc_lte_5 = select(Produs).where(Produs.stoc < prag).order_by(Produs.stoc.asc())
        return [produs.nume  for produs in s.scalars(produse_stoc_lte_5)]



def reaprovizioneaza(produs_id: int, cantitate: int):
    # TODO: s.get -> daca None: raise ValueError
    #       altfel: stoc += cantitate, commit
    with Session(engine) as s:
        p = s.get(Produs, produs_id)
        if p is None:
            raise ValueError("Nu exista produsul")
        p.stoc += cantitate
        s.commit()




def sterge_produs(produs_id: int):
    # TODO: s.get -> s.delete -> commit
    with Session(engine) as s:
        p = s.get(Produs, produs_id)
        if p is None:
            raise ValueError("Produsul nu exista pentru a-l sterge")
        s.delete(p)
        s.commit()


# ---- COD DE TEST (nu trebuie sa-l modifici) -----------------
pregateste()

print("nr produse:", nr_produse())                            # 4
print("stoc redus (<6):", produse_stoc_redus(6))
# ['Mouse gaming', 'Casti wireless', 'Webcam HD']

with Session(engine) as s:
    id_mouse = s.scalar(select(Produs.id).where(Produs.nume == "Mouse gaming"))
reaprovizioneaza(id_mouse, 10)
with Session(engine) as s:
    print("stoc Mouse gaming dupa reaprovizionare:", s.get(Produs, id_mouse).stoc)  # 11

sterge_produs(id_mouse)
print("dupa stergere, nr produse:", nr_produse())              # 3