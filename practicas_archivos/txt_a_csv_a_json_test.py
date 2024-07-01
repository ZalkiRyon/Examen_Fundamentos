import csv
import json
import random

trabajadores = ["Juan Pérez", "María García", "Carlos López", "Ana Martínez", "Pedro Rodríguez",
                "Laura Hernández", "Miguel Sánchez", "Isabel Gómez", "Francisco Díaz", "Elena Fernández"]

with open("trabajadores.txt", "w") as file:
    for i in trabajadores:
        file.write(i + "\n")

with open("trabajadores.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(trabajadores)

with open("trabajadores.json", "w") as file:
    json.dump(trabajadores, file, indent=4)
    
archivo = open("trabajadores.txt", "r")
contenido = [archivo.read()]
print(contenido)

sueldos = [random.randint(300000, 2500000) for _ in range(len(contenido))]
print(sueldos)