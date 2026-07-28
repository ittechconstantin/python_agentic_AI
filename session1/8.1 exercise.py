# 1. Conversie de la int la float
# Defineste un numar intreg si converteste-l in float. Afiseaza rezultatul.

numar_int = 7
numar_float = float(numar_int)
print(numar_float)

# 2. Conversie de la float la int
# Defineste un numar zecimal si converteste-l in intreg. Afiseaza rezultatul.

numar_float = 7.6
numar_int = int(numar_float)
print(numar_int)

# 3. Conversie de la string la int
# Defineste un string numeric si transforma-l in intreg. Afiseaza tipul variabilei inainte si dupa conversie.

numar_string = '56'
numar_int = int(numar_string)
print(numar_int)
print(type(numar_string))
print(type(numar_int))

# 4. Conversie de la int la string
# Defineste un numar intreg si converteste-l in string. Concateaneaza-l cu un alt text si afiseaza rezultatul.

numar_int = 42
numar_string = str(numar_int)
print("Eu am " + numar_string + " la picior.")

# 5. Conversie de la string la float
# Defineste un string care contine un numar zecimal si converteste-l in float. Afiseaza rezultatul.

numar_str = 7.25
numar_float = float(numar_str)
print(numar_float)

# 6. Conversie de la boolean la int
# Defineste doua variabile booleene (True si False) si converteste-le in intregi.

boolean = True
valoare_int = int(boolean)
print(valoare_int)
boolean1 = False
valoare_int1 = int(boolean1)
print(valoare_int1)

# 7. Conversie de la int la boolean
# Defineste un numar intreg si converteste-l in boolean. Afiseaza rezultatul.

numar_int = 3
boolean = bool(numar_int)
print(boolean)

# 8. Conversie combinata
# Defineste un string numeric si converteste-l mai intai in int, apoi in float si boolean. Afiseaza rezultatele.

numar_string = '2647'
numar_int = int(numar_string)
numar_float = float(numar_string)
boolean = bool(numar_string)
print(numar_int, numar_float, boolean)