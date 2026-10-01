try:
    numero = int(input("Digite um número: "))
    resultado = 100 / numero
    print(f"Resultado: {resultado}")

except ValueError:
    print("Digite apenas números.")

except ZeroDivisionError:
    print("Não é possível dividir por zero.")
