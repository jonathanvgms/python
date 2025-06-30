import json

# listas
numeros = [2, 3, 4, 6]
cadenas = ["hola", "mundo", "asdasd"]
cualquiercosa = [2, 3, "hola", True, 1.3]

#ciclos de repeticion - for
for numero in numeros:
    print(numero)

# imprimir lista completa
print(f"Numeros: {numeros}")

# imprimir un elemento de la lista
print(f"Indice: 2, Elemento: {numeros[-2]}")

# agregar elementos a la lista al final
# numeros.append("nuevo contenido")
numeros.append(1234)
# numeros.append(False)
numeros.append(3.3)
print(numeros)

# agregar elementos a una posicion en especifico
print(numeros)
numeros.insert(3, "dkansjd")
print(numeros)

# borrar elementos de una lista
numeros.remove("dkansjd")
print(numeros)

# borrar un elemento por indice
numeros.pop(1)
print(numeros)

# cantidad de elementos en la lista
cantidad = len(numeros)
print(cantidad)

# ordenar elementos en la lista
lista_ordenada = numeros.sort()
print(lista_ordenada) # la funcion sort modifica el orden de la lista (no crea una nueva)
print(numeros)

# listas de objetos JSON

# JSON - JavaScript Object Notation

# C#
# public class Persona {
#    public int id;
#    public string nombre;
#    public int dni;
# }

# JSON
# {
#     id: 1,
#     nombre: "asdasd",
#     dni: 2233322
# }

datosJSON = '{"id": 1, "nombre": "jonathan", "dni": 22333222}'
datos = json.loads(datosJSON)
print(datos)
print(datos["nombre"])



