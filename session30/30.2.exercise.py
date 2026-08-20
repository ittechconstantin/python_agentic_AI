# EXERCITIUL 2  (SQLAlchemy - bazele)  -  COSURI ABANDONATE
# =============================================================
#
# CONTEXT (caz real)
# ------------------
# Magazinul tine evidenta cosurilor de cumparaturi, intr-o tabela MySQL
# (`ex30_cosuri`). Un cos e "abandonat" pana clientul finalizeaza comanda
# (`finalizat=True`). Vrei sa vezi cosurile abandonate (posibil de
# recuperat cu un email de reamintire) si sa cureti cosurile deja
# finalizate.
#
# Codul de PREGATIRE (engine, model, creare tabela + date DEMO) e deja
# scris mai jos - tu completezi doar functiile din ZONA TA DE LUCRU.
#
#
# CE AI DE FACUT
# --------------
# Scrie 4 functii:
#
# 1. adauga_cos(client, valoare)     -> creeaza un Cos nou (finalizat=False
#                                       implicit) si il intoarce.
# 2. cosuri_abandonate()             -> NUMELE clientilor cu cosuri
#                                       finalizat=False, ordonate
#                                       DESCRESCATOR dupa valoare (cele
#                                       mai valoroase primele - cele mai
#                                       importante de recuperat).
# 3. finalizeaza_cos(cos_id)         -> muta cosul in finalizat=True.
#                                       Daca id-ul nu exista: ValueError.
# 4. sterge_cosurile_finalizate()    -> sterge TOATE cosurile finalizate
#                                       si intoarce CATE a sters.
#
#
# CERINTE
# -------
#   - foloseste  with Session(engine) as s:  la fiecare functie
#   - la (4): nu exista o comanda "delete in bloc" invatata - iei toate
#     obiectele cu finalizat=True, le stergi UNUL CATE UNUL (s.delete in
#     bucla), apoi UN SINGUR commit la final; intorci lungimea listei
#
#
# OUTPUT ASTEPTAT (din codul de test de mai jos)
# ----------------------------------------------
#   cos nou: George
#   abandonate: ['Vlad', 'George', 'Ana', 'Mihai']
#   dupa finalizare: abandonate ramase 3
#   sterse: 3
#   total dupa curatare: 3
#
#
# INDICII
# -------
#   - filtrare + ordonare:
#       select(Cos).where(Cos.finalizat == False).order_by(Cos.valoare.desc())
#   - update: s.get -> schimbi atributul -> s.commit()
#   - stergere in bloc: obtii lista cu s.scalars(...).all(), apoi
#       for c in lista: s.delete(c)
#       s.commit()
#       return len(lista)
# =============================================================

from sqlalchemy import create_engine, select, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session
from session28.date import username, password

URL = f"mysql+pymysql://{username}:{password}@localhost:3306/curs"
engine = create_engine(URL, echo=False)


class Base(DeclarativeBase):
    pass


class Cos(Base):
    __tablename__ = "ex30_cosuri"

    id:          Mapped[int]   = mapped_column(primary_key=True, autoincrement=True)
    client:      Mapped[str]   = mapped_column(String(100))
    valoare:     Mapped[float]
    finalizat:   Mapped[bool]  = mapped_column(default=False)

    def __repr__(self):
        return f"<Cos {self.client!r} ({self.valoare})>"


# ---- PREGATIRE (dat - nu modifica) --------------------------
def pregateste():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    with Session(engine) as s:
        s.add_all([
            Cos(client="Ana",   valoare=250.0),
            Cos(client="Mihai", valoare=80.0),
            Cos(client="Vlad",  valoare=500.0),
            Cos(client="Maria", valoare=120.0, finalizat=True),
            Cos(client="Radu",  valoare=60.0,  finalizat=True),
        ])
        s.commit()


# ---- ZONA TA DE LUCRU ---------------------------------------
def adauga_cos(client: str, valoare: float):
    # TODO: creeaza Cos(client=..., valoare=...), add + commit + return
    with Session(engine, expire_on_commit=False) as s:
        cos_nou = Cos(client=client, valoare=valoare, finalizat=False)
        s.add(cos_nou)
        s.commit()
        return cos_nou

def cosuri_abandonate():
    # TODO: numele clientilor cu finalizat=False, ordonate descrescator
    #       dupa valoare
    with Session(engine) as s:
        nume_clienti = select(Cos.client).where(Cos.finalizat == False).order_by(Cos.valoare.desc())
        return [client for client in s.scalars(nume_clienti)]

def finalizeaza_cos(cos_id: int):
    # TODO: s.get -> daca None: raise ValueError
    #       altfel: finalizat = True, commit
    with Session(engine) as s:
        p = s.get(Cos, cos_id)
        if p is None:
            raise ValueError("Nu exista cos")
        p.finalizat = True
        s.commit()


def sterge_cosurile_finalizate():
    # TODO: ia toate cosurile cu finalizat=True, sterge-le, intoarce cate erau
    with Session(engine) as s:
        toate_cosurile = s.scalars(select(Cos).where(Cos.finalizat == True)).all()
        for c in toate_cosurile:
            s.delete(c)
        s.commit()
        return len(toate_cosurile)



# ---- COD DE TEST (nu trebuie sa-l modifici) -----------------
if __name__ == "__main__":
    pregateste()

    nou = adauga_cos("George", 300.0)
    print("cos nou:", nou.client)                                  # George

    print("abandonate:", cosuri_abandonate())
    # ['Vlad', 'George', 'Ana', 'Mihai']

    with Session(engine) as s:
        id_vlad = s.scalar(select(Cos.id).where(Cos.client == "Vlad"))
    finalizeaza_cos(id_vlad)
    print("dupa finalizare: abandonate ramase", len(cosuri_abandonate()))  # 3

    nr = sterge_cosurile_finalizate()
    print("sterse:", nr)                                           # 3
    with Session(engine) as s:
        print("total dupa curatare:", len(s.scalars(select(Cos)).all()))  # 3
