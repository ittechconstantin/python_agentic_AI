# TEMA PENTRU ACASA 1  -  HEALTH CHECK PENTRU SERVICII WEB (duck typing)
# =============================================================
#
# CONTEXT (caz real)
# ------------------
# Orice aplicatie web reala e formata din mai multe SERVICII: un server
# web, o baza de date, un cache. Un dashboard de monitorizare (gen
# Grafana/Datadog) le verifica periodic pe TOATE, ca sa stie daca sistemul
# e sanatos - fara sa-i pese ce fel de serviciu e fiecare, cat timp stie
# sa raspunda la  verifica_status().
#
# ServerWeb, BazaDeDate si CacheRedis NU au niciun parinte comun (nu
# mostenesc dintr-o clasa Serviciu) - dar toate stiu sa faca
# verifica_status(). Asta e DUCK TYPING (vezi lectia, Partea 1,
# sectiunea 3): "daca stie sa raspunda, il tratez la fel", indiferent de
# tipul lui exact.
#
# Provocarea temei: scrii si cele 3 clase, SI functia care le foloseste
# polimorfic - fara niciun if pe tip - ca sa calculezi latenta totala.
#
#
# CE AI DE FACUT
# --------------
# 1. class ServerWeb:
#      __init__(self, nume, timp_ms)
#      verifica_status(self): timpul de raspuns e EXACT  timp_ms  (o
#      cerere HTTP simpla). Printeaza  f"{nume}: raspuns in {timp}ms"
#      si INTOARCE  timp.
#
# 2. class BazaDeDate:
#      __init__(self, nume, timp_ms)
#      verifica_status(self): timp = timp_ms + 50   (interogarile cu
#      JOIN-uri adauga intotdeauna un overhead fix).
#      Printeaza  f"{nume}: raspuns in {timp}ms"  si INTOARCE  timp.
#
# 3. class CacheRedis:
#      __init__(self, nume, timp_ms)
#      verifica_status(self): timp = timp_ms // 2   (cache-ul citeste
#      din memorie, nu de pe disc - e de doua ori mai rapid).
#      Printeaza  f"{nume}: raspuns in {timp}ms"  si INTOARCE  timp.
#
# 4. def verifica_toate(servicii): parcurge lista, apeleaza
#    .verifica_status()  pe FIECARE (nu conteaza tipul!) si intoarce
#    SUMA tuturor timpilor de raspuns.

# =============================================================


# ---- ZONA TA DE LUCRU ---------------------------------------

class ServerWeb:
    def __init__(self, nume, timp_ms):
        # TODO: salveaza nume si timp_ms
        self.nume = nume
        self.timp_ms = timp_ms

    def verifica_status(self):
        # TODO: printeaza mesajul, intoarce timpul (timp_ms)
        timp = self.timp_ms
        print(f"{self.nume}: raspuns in {timp}ms")
        return timp


class BazaDeDate:
    def __init__(self, nume, timp_ms):
        # TODO: salveaza nume si timp_ms
        self.nume = nume
        self.timp_ms = timp_ms

    def verifica_status(self):
        # TODO: printeaza mesajul, intoarce timpul (timp_ms + 50)
        timp = self.timp_ms + 50
        print(f"{self.nume}: raspuns in {timp}ms")
        return timp


class CacheRedis:
    def __init__(self, nume, timp_ms):
        # TODO: salveaza nume si timp_ms
        self.nume = nume
        self.timp_ms = timp_ms

    def verifica_status(self):
        # TODO: printeaza mesajul, intoarce timpul (timp_ms // 2)
        timp = self.timp_ms // 2
        print(f"{self.nume}: raspuns in {timp}ms")
        return timp


def verifica_toate(servicii):
    # TODO: apeleaza .verifica_status() pe fiecare, intoarce suma timpilor
    lista = []
    for s in servicii:
        lista.append(s.verifica_status())
    return sum(lista)






# ---- COD DE TEST (nu trebuie sa-l modifici) -----------------
servicii = [
    ServerWeb("API Gateway", 45),
    BazaDeDate("PostgreSQL", 80),
    CacheRedis("Redis", 20),
]

timp_total = verifica_toate(servicii)
print("timp total:", f"{timp_total}ms")   # timp total: 185ms
