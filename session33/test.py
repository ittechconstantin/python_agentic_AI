from sqlalchemy import values

dict_plin = {
    "Biziday" : 20,
    "Antena 5": 10,
    "OTV"     : 5
}


print(max(dict_plin, key = lambda values: dict_plin[values]))