# EXERCITIUL 3  (SQLAlchemy - bazele)  -  COSTURI DE LIVRARE
# =============================================================
#
# CONTEXT (caz real)
# ------------------
# Magazinul lucreaza cu mai multi transportatori si tine evidenta
# costului fiecarei livrari, intr-o tabela MySQL (`ex30_livrari`).
# Practici inca o data tiparul CRUD, plus doua cazuri noi: actualizare pe
# baza unui calcul (scumpire de combustibil) si gasirea unui singur rand
# "cel mai...".
#
# Codul de PREGATIRE (engine, model, creare tabela + date DEMO) e deja
# scris mai jos - tu completezi doar functiile din ZONA TA DE LUCRU.
#
#
# CE AI DE FACUT
# --------------
# Scrie 4 functii:
#
# 1. adauga_livrare(oras, transportator, cost)  -> creeaza si intoarce o
#                                                 Livrare noua.
# 2. livrari_din_oras(oras)                     -> TRANSPORTATORII care
#                                                 au livrat in acel oras,
#                                                 in ordine ALFABETICA.
# 3. mareste_cost(livrare_id, procent)          -> creste costul cu
#                                                 `procent`% (ex: 10 ->
#                                                 cost * 1.10), rotunjit
#                                                 la 2 zecimale.
# 4. cel_mai_scump_transportator()              -> TRANSPORTATORUL
#                                                 livrarii cu cel mai
#                                                 mare cost.
#
#
# CERINTE
# -------
#   - foloseste  with Session(engine) as s:  la fiecare functie
#   - la (3): calculezi noul cost in Python, apoi il pui pe atribut (nu
#     exista un "UPDATE ... SET cost = cost * 1.1" invatat inca)
#   - la (4): ordoneaza descrescator dupa cost si ia primul rand -
#     `s.scalars(stmt).first()`  (ca  .all()[0]  dar nu pica daca-i gol)
#
#
# OUTPUT ASTEPTAT (din codul de test de mai jos)
# ----------------------------------------------
#   Cluj: ['DPD', 'FanCourier']
#   cost FanCourier dupa marire: 16.5
#   cel mai scump transportator: Cargus
#
#
# INDICII
# -------
#   - filtrare + ordonare alfabetica:
#       select(Livrare).where(Livrare.oras == oras)
#                       .order_by(Livrare.transportator)
#   - update calculat:
#       l = s.get(Livrare, livrare_id)
#       l.cost = round(l.cost * (1 + procent / 100), 2)
#   - "cel mai...":
#       select(Livrare).order_by(Livrare.cost.desc())
# =============================================================

from sqlalchemy import create_engine, select, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session
from session28.date import username, password

URL = f"mysql+pymysql://{username}:{password}@localhost:3306/curs"
engine = create_engine(URL, echo=False)


class Base(DeclarativeBase):
    pass


class Livrare(Base):
    __tablename__ = "ex30_livrari"

    id:             Mapped[int]   = mapped_column(primary_key=True, autoincrement=True)
    oras:           Mapped[str]   = mapped_column(String(50))
    transportator:  Mapped[str]   = mapped_column(String(50))
    cost:           Mapped[float]

    def __repr__(self):
        return f"<Livrare {self.transportator!r} -> {self.oras!r}>"


# ---- PREGATIRE (dat - nu modifica) --------------------------
def pregateste():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    with Session(engine) as s:
        s.add_all([
            Livrare(oras="Cluj",       transportator="FanCourier", cost=15.0),
            Livrare(oras="Cluj",       transportator="DPD",        cost=15.0),
            Livrare(oras="Bucuresti",  transportator="Cargus",     cost=25.0),
            Livrare(oras="Bucuresti",  transportator="DPD",        cost=18.0),
        ])
        s.commit()


# ---- ZONA TA DE LUCRU ---------------------------------------
def adauga_livrare(oras: str, transportator: str, cost: float):
    # TODO: creeaza Livrare(...), add + commit + return
    with Session(engine) as s:
        livrare = Livrare(oras=oras, transportator=transportator, cost=cost)
        s.add(livrare)
        s.commit()
        l =s.get(Livrare, livrare.id)
        return l

def livrari_din_oras(oras: str):
    # TODO: transportatorii livrarilor din acel oras, ordonati alfabetic
    with Session(engine) as s:
        nume_transportatori = select(Livrare).where(Livrare.oras == oras).order_by(Livrare.transportator.asc())
        return [l.transportator for l in s.scalars(nume_transportatori)]


def mareste_cost(livrare_id: int, procent: float):
    # TODO: s.get -> daca None: raise ValueError
    #       altfel: cost = round(cost * (1 + procent/100), 2), commit
    with Session(engine) as s:
        p = s.get(Livrare, livrare_id)
        if p is None:
            raise ValueError("Nu exista livrare")
        p.cost =round(p.cost * (1 + procent/100), 2)
        s.commit()


def cel_mai_scump_transportator():
    # TODO: transportatorul livrarii cu cel mai mare cost
    with Session(engine) as s:
        cel_mai_scump = s.scalars(select(Livrare.transportator).order_by(Livrare.cost.desc())).first()
        return cel_mai_scump


# ---- COD DE TEST (nu trebuie sa-l modifici) -----------------
pregateste()

print("Cluj:", livrari_din_oras("Cluj"))                       # ['DPD', 'FanCourier']

with Session(engine) as s:
    id_fan = s.scalar(
        select(Livrare.id).where(
            Livrare.oras == "Cluj", Livrare.transportator == "FanCourier"
        )
    )
mareste_cost(id_fan, 10)
with Session(engine) as s:
    print("cost FanCourier dupa marire:", s.get(Livrare, id_fan).cost)  # 16.5

print("cel mai scump transportator:", cel_mai_scump_transportator())    # Cargus
