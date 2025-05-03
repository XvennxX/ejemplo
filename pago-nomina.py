
def nomina():
    try:

        salario_basico = float(1423000)
        auxilio_trasporte = float(200000)


        #pedimos el documento 
        documentos = str(input("Ingrese su documento: "))

        #pedimos el nombre
        nombres = str(input("Ingrese su nombre: "))
        
        #pedimos los dias laborados
        dias_laborados = int(input("Ingrese los dias laborados: "))

        #pedimos la cantidad de horas extras diurnas
        diurnas = int(input("Ingrese la cantidad de horas extras diurnas: "))

        #pedimos la cantidad de horas extras nocturnas
        nocturnas = int(input("Ingrese la cantidad de horas extras nocturnas: "))

        #pedimos el monto de los prestamos
        comision = float(input("Ingrese el valor de la comision: "))

        #pedimos el monto de los prestamos
        prestamo = float(input("Ingrese el valor en pesos del prestamo: "))

        print ( )


        print (f"Empleado : {nombres} con numero de cedula {documentos}")

        if dias_laborados <= 30:
            salario_neto = (salario_basico / 30) * dias_laborados  
            print (f"El salario neto es de $ {salario_neto}")                
        else:
            print("Error: los días laborados no pueden ser mayores a 30")


        if dias_laborados <= 30:
            auxilio = (auxilio_trasporte / 30) * dias_laborados   
            print (f"El valor de auxilio de trassporte es de $ {auxilio}")                
        else:
            print("Error: los días laborados no pueden ser mayores a 30")


        if nocturnas+diurnas <= 48:
            valor_diurna = ((salario_basico / 240) * 1.25) * diurnas
            print (f"El valor de las horas extras diurnas es de $ {valor_diurna}")                
        else:
            print("Error: las horas extras mensuales no pueden ser mayor a 48 horas")

        
        if diurnas+nocturnas <= 48:
            valor_nocturna = ((salario_basico / 240) * 1.75) * nocturnas
            print (f"El valor de las horas extras nocturnas es de $ {valor_nocturna}")                 
        else:
            print("Error: las horas extras mensuales no pueden ser mayor a 48 horas")


        total_devengado = (salario_neto + auxilio + diurnas + nocturnas + comision)
        print (f"El total devengado es de $ {total_devengado}")

#DEDUCIDOS

        salud = (salario_neto * 0.04)
        print (f"El total de aporte a salud es de $ {salud}")

        pension = (salario_neto * 0.04)
        print (f"El total de aporte a pension es de $ {pension}")

        total_deducido = (salud + pension + prestamo)
        print (f"El total deducido es de $ {total_deducido}")

        total_pagar = (total_devengado-total_deducido)
        print (f"El total del salario a pagar es de $ {total_pagar}")

            



        
    
    except ZeroDivisionError:
        print("Error: división por cero")

nomina()


        
