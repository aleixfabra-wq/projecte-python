def calcular_preu (a, b):
    r = int(a) + int(b)
    return r

a = input("Preu de les peces: ")
b = input("Cost ma d'obra: ")
preu = calcular_preu (a, b)
print("Cost total", preu, "€")