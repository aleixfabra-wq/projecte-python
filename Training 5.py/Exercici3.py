from Exercici2 import aplicar_descompte

def calcular_iva(preu):
    return preu * 0.21

def calcular_factura(preu, tipus_client):
    preu_amb_descompte = aplicar_descompte(preu, tipus_client)
    iva = calcular_iva(preu_amb_descompte)
    return preu_amb_descompte + iva

preu = float(input("Introdueix el preu: "))
tipus_client = input("Tipus de client: ")
total = calcular_factura(preu, tipus_client)
print(f"Total factura: {total:.2f} €")