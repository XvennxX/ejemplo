import math

def calculadora():
    try:
        # Solicitar el primer número
        num1 = float(input("Ingrese el primer número: "))
        
        # Solicitar el segundo número
        num2 = float(input("Ingrese el segundo número: "))
        
        # Solicitar el operador
        operador = input("Ingrese el operador (+, -, *, /, **, //): ")

        # Selección de operación según el operador ingresado
        if operador == '+':
            resultado = num1 + num2
        elif operador == '-':
            resultado = num1 - num2
        elif operador == '*':
            resultado = num1 * num2
        elif operador == '/':
            if num2 == 0:
                raise ValueError("Error: No se puede dividir por cero.")
            resultado = num1 / num2
        elif operador == '':
            resultado = num1 ** num2
        elif operador == '//':
            if num2 == 0:
                raise ValueError("Error: No se puede dividir por cero.")
            resultado = num1 // num2
        else:
            raise ValueError("Error: Operador no válido. Por favor, ingrese un operador válido.")

        # Mostrar el resultado
        print(f"Resultado: {num1} {operador} {num2} = {resultado}")
    
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

# Llamar a la función
calculadora()
