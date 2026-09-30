def dividir(numero1, numero2):

    try:
        resultado = numero1 / numero2
        return resultado

    except ZeroDivisionError:
        print("Não é possível dividir por zero.")
        return None


numero1 = 20
numero2 = 5

resultado = dividir(numero1, numero2)

if resultado is not None:
    print(f"Resultado: {resultado}")
