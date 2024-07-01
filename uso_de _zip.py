"""
nombres = ["Ana", "Luis", "Juan"]
edades = [25, 30, 22]
ciudades = ["Madrid", "Barcelona", "Valencia"]

combinado = zip(nombres, edades, ciudades)

# Convertimos el objeto zip a una lista para verlo mejor
combinado_lista = list(combinado)
print(combinado_lista)
"""
trios = [("Ana", 25, "Madrid"), ("Luis", 30, "Barcelona"), ("Juan", 22, "Valencia")]

nombres, edades, ciudades = list(zip(*trios))
print(nombres)
print(edades)
print(ciudades)

print(type(nombres))