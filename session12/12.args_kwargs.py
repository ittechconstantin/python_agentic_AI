# *args, **kwargs si SCOPE
# =============================================================
# In sesiunea 11 am scris functii cu un numar FIX de parametri.
# Aici invatam sa primim ORICAT de multi parametri:
#   *args    -> argumente POZITIONALE variabile  (vin ca TUPLU)
#   **kwargs -> argumente KEYWORD    variabile   (vin ca DICT)
# Apoi vedem SCOPE: unde este "vizibila" o variabila .
# =============================================================


# =============================================================
# PARTEA 1:  *args  -  numar variabil de argumente pozitionale
# =============================================================
# Fara *args, o functie ar fi legata de un numar fix de parametri.
# Pui un * inaintea numelui si TOATE argumentele "in plus" sunt
# PACHETATE intr-un TUPLU, pe care il parcurgi normal.
# Poti avea parametri FIXI (inainte) urmati de *args.

def total_cos(client, pret1, pret2, pret3, pret4):
    return f"{client} a cumparat de {pret1+pret2+pret3+pret4} lei"

def total_cos(client, *preturi):
    return f"{client} a cumparat de {sum(preturi)} lei"



total_cos("Ana", 10, 20, 30, 15)  # Ana : 75 lei
total_cos("Bob", 15)              # Bob : 15 lei


# "args" este doar conventie - "*preturi" merge la fel.
# Steluta * face magia, nu numele.

# UNPACKING la apel: daca ai deja datele intr-o lista, le trimiti
# despachetate cu * inainte. FARA *, lista ar intra ca UN SINGUR
# element in tuplu, iar sum() ar da TypeError.

preturi = [10, 20, 30, 95]
print(total_cos("Ana", *preturi))

# * merge cu ORICE iterabil, nu doar cu liste: tuplu, set, range, string.


# =============================================================
# PARTEA 2:  **kwargs  -  numar variabil de argumente keyword
# =============================================================
# Argumentele de forma  cheie=valoare  sunt PACHETATE intr-un DICT.
# Util cand o functie are OPTIUNI care pot lipsi. Exemplu: o comanda
# de cafea, unde tipul e obligatoriu, dar extra-urile sunt optionale.
# Citesti fiecare optiune cu .get(cheie, valoare_daca_lipseste).

def comanda_cafe(tip, **optiuni):
    zahar = optiuni.get("zahar", 0)
    lapte = optiuni.get("lapte", "fara lapte")
    print(f"Tipul de cafea este {tip} cu {zahar} zahar si lapte {lapte}")


comanda_cafe("latte", zahar=2, lapte="vegetal")
comanda_cafe("Cappuccino", lapte="normal")


# =============================================================
# PARTEA 3:  COMBINATIE  parametri + *args + **kwargs
# =============================================================
# Le poti folosi pe toate in aceeasi functie, dar in ORDINEA:
#   parametri normali -> *args -> **kwargs
#   ex:  def f(a, *args, **kwargs): ...
#
# Exemplu concret - o comanda la restaurant:
#   client  -> parametru normal (obligatoriu)
#   produse -> *args   (oricate produse)
#   extra   -> **kwargs (optiuni: livrare, reducere...)

def comanda(client, *produse, **extra):
    print(f"Comanda de la {client}:")
    for produs in produse:
        print(f"  -{produs}")

    print("Informatii suplimentare")
    for cheie, valoare in extra.items():
        print(f"  {cheie}: {valoare}")



comanda("Ana", "pizza", "salata", "tiramisu", livrare="curier", reducere=20, observatii="Mancarea expira in 2 zile")
comanda("George", "burger", livrare="Ridicare din locatie")