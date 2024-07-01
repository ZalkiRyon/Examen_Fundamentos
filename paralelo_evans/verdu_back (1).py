import os
import time
import csv
# < >

lista_verduras = []

def lp():
    os.system("cls")

def ps():
    os.system("pause")
    
def salir():
    lp()
    des_salir = input("¿Esta seguro que quiere salir? S/N \nIngrese S/N: ").strip().upper()
    while not des_salir in ["S","N"]:
        lp()
        print("Error. Ingrese S/N.")
        des_salir = input("¿Esta seguro que quiere salir? S/N \nIngrese S/N: ").strip().upper()
    
    if des_salir == "S":
        print("¡Hasta luego!")
        time.sleep(0.5)
        return True
    else:
        return False

def registrar_verdura():
    lp()
    nombre = input("Ingrese nombre: ").strip().capitalize()
    while not (len(nombre)>0 and nombre.isalpha()):
        lp()
        print("Error. Ingrese un nombre válido.")
        nombre = input("Ingrese nombre: ").strip().capitalize()
    
    origen = input("Ingrese origen: ").strip().capitalize()
    while not (len(origen)>0 and origen.isalpha()):
        lp()
        print("Error. Ingrese un origen válido.")
        origen = input("Ingrese origen: ").strip().capitalize()
    
    while True:
        lp()
        try:
            valor_kilo = int(input("Ingrese el valor por kilo: "))
            if valor_kilo<=0:
                lp()
                print("Error. Ingrese un valor mayor a cero.")
                ps()
            else:
                break
        except:
            lp()
            print("Error. Ingrese un valor númerico.")
            ps()
    
    while True:
        lp()
        try:
            stock = int(input("Ingrese cantidad de stock: "))
            if stock<=0:
                lp()
                print("Error. Ingrese un valor mayor a cero.")
            else:
                break
        except:
            lp()
            print("Error. Ingrese un valor númerico.")

    verdura = {
        "nombre": nombre,
        "origen": origen,
        "valor_kilo": valor_kilo,
        "stock": stock
    }
    lista_verduras.append(verdura)
    ps()

def listar_verduras(lista_verduras):
    lp()
    if lista_verduras:
        print("Las verduras registradas son: ")
        for verdura in lista_verduras:
            print(f'''\n
            Nombre: {verdura["nombre"]}
            Origen: {verdura["origen"]}
            Valor por kg: {verdura["valor_kilo"]}
            Stock: {verdura["stock"]} \n''')
            print("-" * 30 + "\n")
        ps()
    else:
        lp()
        print("Debe añadir elementos a la lista de verduras antes de listar.")
        ps()

def crear_reporte_txt(lista_verduras):
    lp()
    # Nos aseguramos que exista la lista antes de, con booleanos.
    if lista_verduras:
        print("==== Crear reporte ====\n")
        busc_verd = input("Ingrese el origen de la verdura que desea buscar: ").strip().capitalize()
        while not (len(busc_verd)>0 and busc_verd.isalpha()):
            lp()
            print("Error. Ingrese un origen válido.")
            busc_verd = input("Ingrese el origen de la verdura que desea buscar: ").strip().capitalize()
        verduras_auxi = []
        
        for verdura in lista_verduras:
            if verdura["origen"] == busc_verd.capitalize():
                print(f'''\n
                Nombre: {verdura["nombre"]}
                Origen: {verdura["origen"]}
                Valor por kg: {verdura["valor_kilo"]}
                Stock: {verdura["stock"]} \n''')
                print("-" * 30 + "\n")
                verduras_auxi.append(verdura)
            
        cre_report = input("Desea crear el reporte con estos registros? S/N \nIngrese S/N: ").strip().upper()
        while not cre_report in ["S","N"]:
            lp()
            print("Error. Ingrese S/N")
            cre_report = input("Desea crear el reporte con estos registros? S/N \nIngrese S/N: ").strip().upper()
        if cre_report == "S":
            with open('reporte_verduras.txt', 'w', encoding='utf-8') as archivo:
                archivo.write(f"Las verduras registradas son: \n")
                for verdura in verduras_auxi:
                    archivo.write(f'''
                    Nombre: {verdura["nombre"]}
                    Origen: {verdura["origen"]}
                    Valor por kg: {verdura["valor_kilo"]}
                    Stock: {verdura["stock"]} \n''')
                    archivo.write("-" * 30 + "\n")
            print("Reporte creado exitosamente.")
            ps()   
        else:
            pass
     # si no existe, le diremos que debe añadir elementos a la lista antes de crear el reporte
    else:
        lp()
        print("Debe añadir elementos a la lista de verduras antes de crear el reporte.")
        ps()

#with open('reporte_verduras.csv', 'w', newline='', encoding='utf-8') as archivo:
    #escritor_csv = csv.writer(archivo)
    #escritor_csv.writerow(["Nombre", "Origen", "Valor por kg", "Stock"])
    #for verdura in verduras_auxi:
        #escritor_csv.writerow([verdura["nombre"], verdura["origen"], verdura["valor_kilo"], verdura["stock"]])
#print("Reporte CSV creado exitosamente.")