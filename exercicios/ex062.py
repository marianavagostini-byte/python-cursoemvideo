# ex062 - Super Progressão Aritmética v3.0
# Fonte: Curso em Vídeo - desafio oficial (seu código)

print('GERADOR DE P.A')
print('-=' * 20)
primeiro = int(input('Qual o numero da P.A ?  '))
razao = int(input('Qual a razao da P.A ?   '))

pa = primeiro
contador = 1
totalfinal = 0
usuariopedir = 10

while usuariopedir != 0:
    totalfinal = totalfinal + usuariopedir
    while contador <= totalfinal:
        print(f'{pa} -> ', end='')
        pa += razao        # ALINHADO DENTRO DO SEGUNDO WHILE
        contador += 1      # ALINHADO DENTRO DO SEGUNDO WHILE
        
    print('PAUSA')         # FORA DO SEGUNDO WHILE
    usuariopedir = int(input('Quantos termos voce quer mostrar a mais ? '))  # FORA DO SEGUNDO WHILE

print(f'Progressao finalizada com {totalfinal} termos mostrados.')
