# Propuesto 2
# Van a crear un sistema de registros, listados y reporte
# Para la siguiente estructura JSON:
# verdura = {
#     "nombre": ...., str
#     "origen": ...., str
#     "valor_kilo": ...., int
#     "stock": ...., int
import os
import verdu_back as vb

# variables

menu_principal = '''
==== Verduras Don Fernando ====

1. Registrar verduras
2. Listar verduras
3. Crear reporte de verduras (csv)
4. Salir

Ingrese opción: '''

# código principal

while True:
    vb.lp()
    opcion = (input(menu_principal)).strip()
    while not opcion in ["1","2","3","4"]:
        vb.lp()
        print("Error. Ingrese una opción válida.")
        opcion = (input(menu_principal)).strip()
    
    if opcion == "1":
        vb.registrar_verdura()
    elif opcion == "2":
        vb.listar_verduras(vb.lista_verduras)
    elif opcion == "3":
        vb.crear_reporte_txt(vb.lista_verduras)
    elif opcion == "4":
        if vb.salir():
            break
        else:
            continue