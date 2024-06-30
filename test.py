

trabajadores = ["Juan Pérez","María García","Carlos López","Ana Martínez","Pedro Rodríguez","Laura Hernández","Miguel Sánchez","Isabel Gómez","Francisco Díaz","Elena Fernández"]
sueldos = [1000000, 2000000, 3000000, 4000000, 5000000, 6000000, 7000000, 8000000, 9000000, 10000000]

merged_list = [f"{trabajador}: {sueldo}" for trabajador, sueldo in zip(trabajadores, sueldos)]

for item in merged_list:
    print(item)

reporte = []
for i in range(len(trabajadores)): 
#for i in range(10):
    sueldo_base = sueldos[i]
    descuento_salud = int(sueldo_base * 0.07)
    descuento_afp = int(sueldo_base * 0.12)
    sueldo_liquido = sueldo_base - descuento_salud - descuento_afp
    reporte.append([trabajadores[i], sueldo_base, descuento_salud, descuento_afp, sueldo_liquido])

for item in reporte:
    print(item)