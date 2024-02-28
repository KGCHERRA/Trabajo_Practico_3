def calcular():
    operacion = input("Escriba la operacion: (+, -, *, /): ")
    num1 = float(input("Escriba el primer número: "))
    num2 = float(input("Escriba el segundo número: "))

    if operacion == '+':
        resultado = num1 + num2
    elif operacion == '-':
        resultado = num1 - num2
    elif operacion == '*':
        resultado = num1 * num2
    elif operacion == '/':
        if num2 != 0:
            resultado = num1 / num2
        else:
            print("No se puede dividir entre cero.")
            return

    print(f"El resultado de la operacion {operacion} es: {resultado}")

if __name__ == "__main__":
    calcular()