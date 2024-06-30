import random
import csv

# Lista de trabajadores
trabajadores = ["Juan Pérez", "María García", "Carlos López", "Ana Martínez", "Pedro Rodríguez",
                "Laura Hernández", "Miguel Sánchez", "Isabel Gómez", "Francisco Díaz", "Elena Fernández"]

# Función para generar sueldos aleatorios
def generar_sueldos():
    sueldos = [random.randint(300000, 2500000) for i in range(10)]
    return sueldos

# Función para clasificar sueldos
def clasificar_sueldos(sueldos):
    clasificacion = {
        "Menores a $800.000": [],
        "Entre $800.000 y $1.500.000": [],
        "Entre $1.500.000 y $2.000.000": [],
        "Mayores a $2.000.000": []
    }
    for i in sueldos:
        if i < 800000:
            clasificacion["Menores a $800.000"].append(i)
        elif 800000 <= i <= 1500000:
            clasificacion["Entre $800.000 y $1.500.000"].append(i)
        elif 1500000 < i <= 2000000:
            clasificacion["Entre $1.500.000 y $2.000.000"].append(i)
        else:
            clasificacion["Mayores a $2.000.000"].append(i)
    return clasificacion

# Función para generar reporte de sueldos
def generar_reporte(sueldos):
    reporte = []
    for i in range(len(trabajadores)):
        sueldo_base = sueldos[i]
        descuento_salud = int(sueldo_base * 0.07)
        descuento_afp = int(sueldo_base * 0.12)
        sueldo_liquido = sueldo_base - descuento_salud - descuento_afp
        reporte.append([trabajadores[i], sueldo_base, descuento_salud, descuento_afp, sueldo_liquido])
    return reporte

# Función para guardar el reporte en un archivo CSV
def guardar_reporte_csv(reporte):
    with open('reporte_sueldos.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Nombre empleado", "Sueldo Base", "Descuento Salud", "Descuento AFP", "Sueldo Líquido"])
        writer.writerows(reporte)

# Función principal para el menú
def main():
    sueldos = []
    while True:
        print("\nMenú de opciones:")
        print("1. Asignar sueldos aleatorios")
        print("2. Clasificar sueldos")
        print("3. Reporte de sueldos")
        print("4. Salir del programa")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            sueldos = generar_sueldos()
            print("Sueldos asignados aleatoriamente.")

        elif opcion == '2':
            if not sueldos:
                print("Primero debe asignar los sueldos aleatorios (opción 1).")
            else:
                clasificacion = clasificar_sueldos(sueldos)
                for categoria, lista_sueldos in clasificacion.items():
                    print(f"{categoria}: {len(lista_sueldos)}")
                    for i in lista_sueldos:
                        print(f"${i}")

        elif opcion == '3':
            if not sueldos:
                print("Primero debe asignar los sueldos aleatorios (opción 1).")
            else:
                reporte = generar_reporte(sueldos)
                print("Reporte de sueldos:")
                print(f"{'Nombre empleado':<20}{'Sueldo Base':<15}{'Descuento Salud':<15}{'Descuento AFP':<15}{'Sueldo Líquido':<15}")
                for fila in reporte:
                    print(f"{fila[0]:<20}{fila[1]:<15}{fila[2]:<15}{fila[3]:<15}{fila[4]:<15}")
                guardar_reporte_csv(reporte)
                print("Reporte guardado en 'reporte_sueldos.csv'.")

        elif opcion == '4':
            print("Finalizando programa...")
            print("Desarrollado por Carlos Vergara")
            print("RUT 12.345.678-9")
            break

        else:
            print("Opción no válida. Intente nuevamente.")

main()
