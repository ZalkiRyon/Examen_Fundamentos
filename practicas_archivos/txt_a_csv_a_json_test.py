trabajadores = ["Juan Pérez", "María García", "Carlos López", "Ana Martínez", "Pedro Rodríguez",
                "Laura Hernández", "Miguel Sánchez", "Isabel Gómez", "Francisco Díaz", "Elena Fernández"]

with open("trabajadores.txt", "w") as file:
    for i in trabajadores:
        file.write(i + "\n")
        