from random import randint

jogadas = []
while True:
    computador = randint(1, 100)
    tentativas = 0
    print("Vou escolher um numero entre 1 e 100..Tente advinhar !")
    while True:
        try:
            jogador = int(input("Seu palpite: "))
        except ValueError:
            print("ERRO! Digite um numero valido.")
            continue
        if jogador < 1 or jogador > 100:
            print("ERRO! Digite um numero entre 1 e 100..")
            continue
        tentativas += 1

        if jogador < computador:
            print(f"E MAIOR que {jogador} ")
        elif jogador > computador:
            print(f"E MENOR que {jogador}")
        else:
            print(f"ACERTOU !! Com {tentativas} tentativas.")
            break
    jogadas.append(tentativas)

    while True:
        resp = input("Deseja jogar novamente? [S/N]")
        if resp.upper() in ["S", "N"]:
            break
        print("ERRO! Digite apenas S ou N.")
    if resp.upper() == "N":
        break
print("-" * 30)
print(f"Voce jogou {len(jogadas)} partidas.")
print(f"Sua melhor partida foi com {min(jogadas)} tentativas.")
