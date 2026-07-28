# EXERCITIUL 5  -  MINI-BOT: decoratorul care INREGISTREAZA comenzi
# =============================================================
#
# CONTEXT
# ------------------
# Faci un bot de chat (ca pe Discord/Slack) sau un mini-terminal.
# Userul scrie comenzi text:  "salut Ana",  "aduna 3 5",  "ajutor".
# Tu vrei ca fiecare comanda sa fie o FUNCTIE separata, curata.
#
# Problema: cum leaga botul textul "aduna" de functia `aduna`? Varianta
# urata ar fi un lant urias de  if text == "salut": ... elif "aduna": ...
# Se umple si trebuie modificat de fiecare data cand adaugi o comanda.
#
# Solutia eleganta (exact cum face Flask cu @app.route si Discord cu
# @bot.command): un decorator  @comanda("nume")  care, in loc sa
# INFASOARE functia, doar o INREGISTREAZA intr-un dictionar de comenzi.
# Asta e un TIP NOU de decorator: nu modifica functia, doar o "noteaza".
#
#
# CE AI DE FACUT
# --------------
# Scrie un decorator CU ARGUMENT  comanda(nume)  care:
#   - primeste numele comenzii (ex: "salut")
#   - pune functia decorata in dictionarul  COMENZI, sub cheia `nume`
#         COMENZI[nume] = fn
#   - INTOARCE functia NESCHIMBATA  (return fn)  <- NU un wrapper!
#
# DE CE intoarce functia neschimbata: noi nu vrem sa schimbam ce face
# functia. Vrem doar sa o "trecem in agenda" botului. De aceea aici NU
# scrii  def wrapper(): ...  -  doar inregistrezi si dai functia inapoi.
#
# Apoi pune  @comanda("...")  pe fiecare functie de mai jos.
# Dispatcher-ul `ruleaza(text)` ti-l dam noi gata (vezi mai jos).
#
#
# CERINTE
# -------
#   - decorator CU ARGUMENT = 3 nivele... DAR nivelul 3 nu e un wrapper,
#     ci doar  return fn  (functia ramane exact aceeasi)
#         def comanda(nume):
#             def decorator(fn):
#                 COMENZI[nume] = fn
#                 return fn
#             return decorator
#   - NU modifica functia `ruleaza` (e dispatcher-ul, dat gata)
#
#
# OUTPUT ASTEPTAT
# ---------------
#   Salut, Ana!
#   rezultat: 8
#   comenzi disponibile: aduna, ajutor, salut
#   comanda necunoscuta: zbor
#
#
# INDICII
# -------
#   - `COMENZI` e un dictionar global  nume -> functie
#   - decoratorul care inregistreaza e cel mai simplu tip: fara wrapper
#   - dispatcher-ul ia primul cuvant ca nume, restul ca argumente
#   - daca vrei sa vezi cat e de tare: adauga o comanda noua doar punand
#     inca un  @comanda("...")  pe o functie - botul o "stie" automat
# =============================================================


# Agenda botului: nume_comanda -> functie. Decoratorul scrie aici.
COMENZI = {}
# def comanda(nume,*args,**kwargs):
#     def decorator(fn):
#         if args in COMENZI:
#             COMENZI[nume] = fn
#             return fn
#         else:
#             return
#     return decorator
#

    # ---- ZONA TA DE LUCRU ---------------------------------------


def comanda(nume):
    def decorator(fn):
        COMENZI[nume] = fn
        return fn
    return decorator


# TODO: pune cate un  @comanda("...")  deasupra fiecarei functii.

@comanda("salut")
def salut(nume="prietene"):
    return f"Salut, {nume}!"

@comanda("aduna")
def aduna(a, b):
    return f"rezultat: {int(a) + int(b)}"

@comanda("ajutor")
def ajutor():
    return "comenzi disponibile: " + ", ".join(sorted(COMENZI))


# ---- DISPATCHER-UL BOTULUI (dat gata; NU-l modifica) --------
# Ia un text, desparte primul cuvant (numele comenzii) de restul
# (argumentele) si apeleaza functia inregistrata sub acel nume.
def ruleaza(text):
    parti = text.split()
    nume = parti[0]
    argumente = parti[1:]
    if nume not in COMENZI:
        return f"comanda necunoscuta: {nume}"
    return COMENZI[nume](*argumente)


print(ruleaza("salut Ana"))     # Salut, Ana!
print(ruleaza("aduna 3 5"))     # rezultat: 8
print(ruleaza("ajutor"))        # comenzi disponibile: aduna, ajutor, salut
print(ruleaza("zbor"))          # comanda necunoscuta: zbor