# =============================================================
# SQLAlchemy  -  modelul si persistenta (Bounty Board)
# =============================================================
# Task-urile nu mai stau intr-o lista Python (s36-37) - le salvam in
# MySQL. Fisierul NU are FastAPI/Pydantic - doar persistenta.
#
# CERINTE:  MySQL pornit (cursant/parola123 @ curs);  pip install sqlalchemy pymysql
# Recap (s30): engine, Base, Session, select, where, order_by,
# scalars/.all(), s.get(), s.delete()
# =============================================================

from sqlalchemy import create_engine, String, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker
user = 'horia'
password = 'admin'
engine = create_engine(f"mysql+pymysql://{user}:{password}@localhost:3306/curs")
SessionLocal = sessionmaker(bind=engine, expire_on_commit=False)


# #############################################################
# PARTEA 1 - MODELUL: o clasa care ESTE o tabela
# #############################################################


# nume: Mapped[TIP] = mapped_column(optiuni) - fiecare atribut e o coloana.
class Base(DeclarativeBase):
    pass


# TODO: scrie clasa Task
#   - __tablename__ = "s38_task"
#   - coloane: id (primary_key, autoincrement), titlu (String(200)),
#     limbaj (String(20)), dificultate (String(10)), recompensa (float),
#     rezolvat (bool, default=False)
class Task(Base):
    __tablename__ = "s38_task"

    id:          Mapped[int]   = mapped_column(primary_key=True, autoincrement=True)
    titlu:       Mapped[str]   = mapped_column(String(200))
    limbaj:      Mapped[str]   = mapped_column(String(20))
    dificultate: Mapped[str]   = mapped_column(String(10))
    recompensa:  Mapped[float]
    rezolvat:    Mapped[bool]  = mapped_column(default=False)


# reset_db() -> sterge tot si reincepe curat (demo/teste)
# init_db()  -> creeaza tabela doar daca lipseste + seed doar daca e goala
def reset_db():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


def adauga_date_initiale(s):
    if not s.scalars(select(Task)).all():
        s.add_all([
            Task(titlu="Fix bug la login",     limbaj="Python",     dificultate="usor",  recompensa=50),
            Task(titlu="Adauga dark mode",      limbaj="JavaScript", dificultate="mediu", recompensa=150),
            Task(titlu="Optimizeaza query SQL", limbaj="Python",     dificultate="greu",  recompensa=300, rezolvat=True),
        ])
        s.commit()


def init_db():
    Base.metadata.create_all(engine)
    with SessionLocal() as s:
        adauga_date_initiale(s)


# #############################################################
# PARTEA 2 - CRUD, DIRECT CU SESIUNEA (fara API deocamdata)
# #############################################################
# Tipar: with SessionLocal() as s: ... + s.commit() la scriere.


# TODO: scrie adauga_task(s, titlu, limbaj, dificultate, recompensa)
#   - creeaza Task(...) din argumente
#   - s.add(t), apoi s.commit()
#   - return t
def adauga_task(s, titlu, limbaj, dificultate, recompensa):
    t = Task(titlu=titlu, limbaj=limbaj, dificultate=dificultate, recompensa=recompensa)
    s.add(t)          # doar il pune in "cos" - inca nu exista in MySQL
    s.commit()        # ACUM se salveaza, si ACUM primeste t.id de la baza
    return t

# TODO: scrie toate_task_urile(s)
#   - select(Task).order_by(Task.id)
#   - s.scalars(...).all()
def toate_task_urile(s):
    rezultat = select(Task).order_by(Task.id)
    return s.scalars(rezultat).all()

# TODO: scrie un_task(s, task_id)
#   - return s.get(Task, task_id)
def un_task(s, task_id):
    task_cautat = s.get(Task, task_id)
    return task_cautat

# TODO: scrie marcheaza_rezolvat(s, task_id)
#   - s.get(Task, task_id), daca None -> return None
#   - t.rezolvat = True, s.commit(), return t
def marcheaza_rezolvat(s, task_id):
    task_cautat = s.get(Task, task_id)
    if task_cautat is None:
        return None
    task_cautat.rezolvat = True
    s.commit()
    return task_cautat

# TODO: scrie sterge_task(s, task_id)
#   - s.get(Task, task_id), daca None -> return False
#   - s.delete(t), s.commit(), return True
def sterge_task(s, task_id):
    task_cautat = s.get(Task, task_id)
    if task_cautat is None:
        return False
    s.delete(task_cautat)
    s.commit()
    return True


# TODO: scrie recompensa_disponibila(s)
#   - select(Task).where(Task.rezolvat == False), s.scalars(...).all()
#   - suma recompenselor, cu sum() peste task-urile nerezolvate
def recompensa_disponibila(s):
    nerezolvate = s.scalars(select(Task).where(Task.rezolvat == False)).all()
    return float(sum(t.recompensa for t in nerezolvate))

init_db()