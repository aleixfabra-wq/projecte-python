número1 = int(input("Introdueix el número 1: "))
número2 = int(input("Introdueix el número 2: "))
número3 = int(input("Introdueix el número 3: "))
if número1 > número2 and número1 > número3:
    print("El numero 1 es mes gran")
elif número2 > número1 and número2 > número3:
    print("El numero 2 es mes gran")
else:
    print("EL numero 3 es mes gran")