
ProgramasRegistrados = []

centinela = 0

while centinela == 0:

    CantidadEstudiantes = 0
    estudiantes = []
    totalPromedio = 0
    cantMujer = 0
    cantHombre = 0

    def lee_entero(string):
        intentos = 0
        while intentos < 5:

            valor = input(string)
            try:
                valor = int(valor)
                return valor

            except ValueError:
                intentos += 1
        raise ValueError("Valor incorrecto ingresado en 5 intentos")

    def calcularPromedio (notas):
        total = 0
        cantidad = 0
        prom = 0

        for x in notas:
            total += x
            cantidad += 1

        prom = total / cantidad
        return prom

    programa = input("ingrese el Nombre del programa que va a registrar ")
    for x in ProgramasRegistrados:
        if x != programa:
            break

        else:
            programa = input("Ese programa ya esta registrado, por favor seleccione otro ")

    indexEstudiantes = lee_entero("Ingrese la cantidad de estudiantes permitidos ")

    CantidadEstudiantes = indexEstudiantes


    for x in range(indexEstudiantes):
        
        notas = []
    
        nombre = input("Ingrese nombre del siguiente estudiante ")

        confirmacion = 1

        while confirmacion == 1:

            text = ""
            sexo = lee_entero("Ingrese 1 si es hombre 0 si es Mujer: ")

            if sexo == 0:
                cantMujer += 1
                confirmacion = 0

            elif sexo == 1:
                cantHombre += 1 
                confirmacion = 0

            else:
                confirmacion = 1
                text = "Error, " 
                    
        for x in range (5):
            notas.append(lee_entero(f"Ingrese la nota {x + 1} de {nombre} :"))
        

        promedio = calcularPromedio(notas)
        totalPromedio += promedio

        estudiante = {"programa" : programa}
        estudiante["nombre"] = nombre
        estudiante["promedio"] = promedio

        estudiantes.append(estudiante)

    promedioGeneral = totalPromedio / CantidadEstudiantes
    print (f"Programa {programa}")
    print (f"Cantidad total de estudiantes : {CantidadEstudiantes}")

    print (f"Promedio General del grupo : {promedioGeneral}")

    print (f"Cantidad de Mujeres: {cantMujer}")
    print (f"Cantidad de Hombre: {cantHombre}")

    print (f"lista de Estudiantes Inscritos")

    for estudiante in estudiantes:
        print(f"el estudiante {estudiante['nombre']} esta inscrito en {estudiante['programa']} con un promedio de {estudiante['promedio']}")

    control = 1

    while control == 1:
        valid = lee_entero("desea inscribir otro programa? escriba '1' si quiere inscribir otro, escriba '0' si no desea:")

        valid = int(valid)

        if valid == 0:
            control = 0
            centinela == 0

        elif valid == 1:
            control = 0
            centinela == 1 

        else:
            control = 1
            
print ("programas inscritos")
for x in ProgramasRegistrados:
  print(x)







