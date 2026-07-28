class Cont:

    def __init__(self, titular, sold):
        self.titular = titular  # atribute de instanta  public
        self.sold = sold        # atribute de instanta  public

    def depune(self, suma):
        self.sold += suma

    def retrage(self, suma):
        self.sold -= suma

    def __str__(self):
        return f"Contul {self.titular} are soldul {self.sold}"

    def __repr__(self):
        return f"Contul {self.titular} -  soldul {self.sold}"


# cont_george = Cont("George Popescu", 1000)
# print(cont_george.sold)
# print(cont_george.titular)
# cont_george.retrage(500)
# print(cont_george.sold)


class ContBancar:

    def __init__(self, titular, sold_initial):
        self.titular = titular       # atribut de instanta public
        self.__sold = sold_initial   # atribut de instanta privat

    @property                  # GETTER -> se apeleaza cont_nou.sold
    def sold(self):
        return self.__sold

    @sold.setter                # SETTER -> se apeleaza cont_nou.sold = X
    def sold(self, valoare):
        if valoare < 0:
            raise ValueError("Valoarea nu poate fi negativa")
        self.__sold = valoare

    def depunere(self, suma):
        if suma <= 0:
            raise ValueError("Suma depusa trebuie sa fie pozitiva")
        self.sold = self.sold + suma

    def retragere(self, suma):
        if suma > self.sold:
            raise ValueError("Fonduri insuficiente")
        self.sold -= suma


    def __str__(self):
        return f"Contul lui {self.titular} are soldul {self.sold} lei"

# cont_horia = ContBancar("Horia Popescu", 2000)
# print(cont_horia.titular)
# cont_horia.titular = "Horia Ionescu"
# print(cont_horia.titular)
#
# print(cont_horia.sold)
# cont_horia.sold = -5000
# print(cont_horia.sold)



class ContPrivat:

    def __init__(self, titular, sold):
        self.titular = titular
        self._sold = sold      # atribut PROTEJAT


# cont = ContPrivat("Florin", 500)
# print(cont._sold)
# cont._sold = 1000
# print(cont._sold)



class ContBancar:

    def __init__(self, titular, sold_initial):
        self.titular = titular       # atribut de instanta public
        self.__sold = sold_initial   # atribut de instanta privat

    @property
    def sold(self):
        return self.__sold

    @sold.setter
    def sold(self, valoare):
        if valoare < 0:
            raise ValueError("Valoarea nu poate fi negativa")
        self.__sold = valoare

    def depunere(self, suma):
        if suma <= 0:
            raise ValueError("Suma depusa trebuie sa fie pozitiva")
        self.sold = self.sold + suma

    def retragere(self, suma):
        if suma > self.sold:
            raise ValueError("Fonduri insuficiente")
        self.sold -= suma



    def __str__(self):
        return f"Contul lui {self.titular} are soldul {self.sold} lei"


cont = ContBancar("Ana", 1000)
print(cont.sold)
cont.sold = 500
print(cont.sold)
cont.retragere(5)
print(cont.sold)