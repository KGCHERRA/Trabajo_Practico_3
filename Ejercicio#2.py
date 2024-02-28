def contador_numeros():
    try:
        numero = int(input("Ingrese un número entero: "))
        if numero <= 0:
            print("Por favor, ingrese un número entero positivo mayor que cero.")
            return
        for i in range(1, numero + 1):
            print(i)
    except ValueError:
        print("Por favor, ingrese un número entero válido.")

contador_numeros()