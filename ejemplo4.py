import math

numero1 = float(input("Ingrese un numero: "))

techo = math.ceil(numero1)
piso = math.floor(numero1)
redondeo = round(numero1, 2)

print(f'Ceiling: {techo} Floor: {piso} Round: {redondeo}')