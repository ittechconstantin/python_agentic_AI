# EXERCITIUL 2  -  ECHIPA DE EROI CA UN CONTAINER
# =============================================================
#
# CONTEXT (caz real)
# ------------------
# Formezi o echipa de eroi pentru o misiune. Vrei ca obiectul Echipa sa
# se comporte ca o colectie "din fabrica":
#   - len(echipa)            -> cati eroi are
#   - "Fulger" in echipa     -> exista eroul?
#   - echipa[0]               -> eroul de pe pozitia 0
#   - for erou in echipa      -> parcurgi eroii
# Le obtii implementand dunder-urile de container: __len__,
# __contains__, __getitem__, __iter__.
#
#
# CE AI DE FACUT
# --------------
# Scrie o clasa  Echipa  cu:
#
# 1. __init__(self, nume): salveaza numele echipei si initializeaza
#    self._eroi = []  (lista de perechi (nume_erou, putere)).
#
# 2. recruteaza(self, nume_erou, putere): adauga perechea
#    (nume_erou, putere) in lista.
#
# 3. __len__(self): cati eroi sunt in echipa.
#
# 4. __contains__(self, nume_erou): True daca EXISTA un erou cu acel
#    nume (compari doar dupa nume, nu dupa putere).
#
# 5. __getitem__(self, i): intoarce eroul de pe pozitia i
#    (perechea (nume_erou, putere)).
#
# 6. __iter__(self): permite  for erou in echipa  (parcurge eroii).
#
# 7. putere_totala(self): suma puterilor tuturor eroilor.

# ---- ZONA TA DE LUCRU ---------------------------------------

class Echipa:
    def __init__(self, nume):
        # TODO: salveaza nume, self._eroi = []
        self.nume =nume
        self._eroi = []

    def recruteaza(self, nume_erou, putere):
        # TODO: adauga (nume_erou, putere)
        self._eroi.append((nume_erou, putere))

    def __len__(self):
        # TODO: cati eroi
        return len(self._eroi)

    def __contains__(self, nume_erou):
        # TODO: exista un erou cu acel nume?
        for (n, p) in self._eroi:
            if n == nume_erou:
                return True

        return False

    def __getitem__(self, i):
        # TODO: eroul de pe pozitia i
        return self._eroi[i]

    def __iter__(self):
        # TODO: permite for erou in echipa
        for erou in self._eroi:
            yield (erou)

    def putere_totala(self):
        # TODO: suma puterilor
        suma = 0
        for putere in self._eroi:
            suma += putere[1]
        return suma


# ---- COD DE TEST (nu trebuie sa-l modifici) -----------------
echipa = Echipa("Gardienii Orasului")
echipa.recruteaza("Fulger", 80)
echipa.recruteaza("Titan", 95)
echipa.recruteaza("Umbra", 65)

print("nr eroi:", len(echipa))                    # nr eroi: 3
print("Titan in echipa?", "Titan" in echipa)       # True
print("Superman in echipa?", "Superman" in echipa) # False
print("primul:", echipa[0])                        # ('Fulger', 80)

print("--- echipa ---")
for nume_erou, putere in echipa:
    print(f"- {nume_erou}: {putere} putere")

print("putere totala:", echipa.putere_totala())    # putere totala: 240
