# TEMA PENTRU ACASA 3  -  CHEIE API CU RATE LIMITING (mostenire + __call__ + __bool__)
# =============================================================
#
# CONTEXT (caz real)
# ------------------
# Orice API real (Google Maps, Anthropic, Stripe) iti da o CHEIE cu un
# numar limitat de credite - cand se termina, cererile sunt refuzate
# ("rate limit depasit"). De obicei, un TIER GRATUIT costa mai mult per
# cerere (throttling) decat unul PLATIT. Combinam TREI idei din
# lectie/tema, intr-un singur exercitiu:
#   1) MOSTENIRE + override  (CheieAPI e baza; CheieGratuita/CheiePremium
#      suprascriu CAT COSTA o cerere);
#   2) __call__  (folosesti cheia ca pe o FUNCTIE:  cheie(3)  =
#      "fa 3 cereri catre API");
#   3) __bool__  -  un dunder NOU, nevazut inca: ii spune lui Python ce
#      inseamna ca obiectul tau sa fie "adevarat" intr-un  if.
#      Implicit, orice obiect e True. Cu __bool__ decizi TU: o cheie
#      fara credite trebuie sa fie False, ca sa poti scrie simplu
#      if cheie: ...  in loc de  if cheie.credite > 0: ...
#
#
# CE AI DE FACUT
# --------------
# 1. class CheieAPI (clasa de BAZA):
#      __init__(self, nume, credite): salveaza nume si credite.
#
#      __call__(self, nr_cereri): calculeaza  cost = self._cost(nr_cereri)
#      (metoda pe care o suprascriu subclasele - CheieAPI nu stie SINGURA
#      cat costa o cerere). Daca  self.credite >= cost:
#          - scade  self.credite  cu  cost
#          - printeaza  f"Cerere reusita: {nr_cereri} cereri ({cost} credite, {self.credite} ramase)"
#        altfel (nu sunt destule credite):
#          - printeaza  f"Rate limit depasit pentru {nr_cereri} cereri!"
#
#      __bool__(self): True daca  credite > 0, altfel False.
#
#      _cost(self, nr_cereri): in clasa de baza, doar  pass  (subclasele
#      DEFINESC pretul real - asta e polimorfismul prin mostenire).
#
# 2. class CheieGratuita(CheieAPI):
#      suprascrie  _cost(self, nr_cereri): intoarce  nr_cereri * 2
#      (tier gratuit, throttling - fiecare cerere "costa" dublu).
#
# 3. class CheiePremium(CheieAPI):
#      suprascrie  _cost(self, nr_cereri): intoarce  nr_cereri * 1
#      (tier platit, pret normal).
# =============================================================


# ---- ZONA TA DE LUCRU ---------------------------------------

class CheieAPI:
    def __init__(self, nume, credite):
        # TODO: salveaza nume si credite
        self.nume = nume
        self.credite = credite

    def __call__(self, nr_cereri):
        # TODO: calculeaza cost = self._cost(nr_cereri); daca ai destule
        #       credite, scade-le si printeaza succesul; altfel printeaza
        #       mesajul de rate limit depasit
        cost = self._cost(nr_cereri)
        if self.credite >= cost:
            self.credite -= cost
            print(f"Cerere reusita: {nr_cereri} cereri ({cost} credite, {self.credite} ramase)")
        else:
            print(f"Rate limit depasit pentru {nr_cereri} cereri!")

    def __bool__(self):
        # TODO: True daca mai are credite
        return True if self.credite > 0 else False

    def _cost(self, nr_cereri):
        pass    # subclasele suprascriu asta


class CheieGratuita(CheieAPI):
    def _cost(self, nr_cereri):
        # TODO: 2 credite/cerere
        return nr_cereri * 2


class CheiePremium(CheieAPI):
    def _cost(self, nr_cereri):
        # TODO: 1 credit/cerere
        return nr_cereri * 1


# ---- COD DE TEST (nu trebuie sa-l modifici) -----------------
gratuita = CheieGratuita("Ana", 10)
gratuita(3)     # Cerere reusita: 3 cereri (6 credite, 4 ramase)
gratuita(2)     # Cerere reusita: 2 cereri (4 credite, 0 ramase)
print("mai are credite (gratuita)?", bool(gratuita))   # False
gratuita(1)     # Rate limit depasit pentru 1 cereri!

premium = CheiePremium("Radu", 10)
premium(7)      # Cerere reusita: 7 cereri (7 credite, 3 ramase)
print("mai are credite (premium)?", bool(premium))   # True
