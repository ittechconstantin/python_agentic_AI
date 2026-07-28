from abc import ABC, abstractmethod


class Masina(ABC):
    def __init__(self, roti, usi):
        self.roti = roti
        self.usi = usi
    @abstractmethod
    def claxon(self):
        ...

class Coupe(Masina):
    def __init__(self, roti, usi, capotata):
        super().__init__(roti, usi)
        self.capotata = capotata
    def claxon(self):
        print(f"Claxoneaza coupe")

class Jeep(Masina):
    def __init__(self, roti, usi, diferential):
        super().__init__(roti, usi)
        self.diferential = diferential
    def claxon(self):
        print(f"Claxoneaza jeep")

coupe = Coupe(4, 2,True)
jeep  = Jeep(4, 2 ,False)

coupe.claxon()
jeep.claxon()