def calcular_preu (a, b):
    r = int(a) + int(b)
    return r

a = input("Preu de les peces: ")
b = input("Cost ma d'obra: ")
preu = calcular_preu (a, b)
print("Cost total", preu, "€")

#RESPON:
#Quants paràmetres té la funció? La funcio te 2 parametres

#Quin valor retorna? La suma dels 2 parametres, es a dir el preu total

#Què passaria si eliminéssim el return? Que la funcio no retornaria cap tipus de resultat