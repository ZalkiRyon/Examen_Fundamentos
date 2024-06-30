def sueldos():
    global sueldos
    sueldos= []
    for i in range(len(trabajadores)):
        sueldo = random.randint(500000, 3000000)
        sueldos.append(sueldo)
        

sueldos()
print(sueldos)

