# ex029 - Radar Eletrônico
# Fonte: Curso em Vídeo - desafio oficial (complementado)

vel = float(input('Qual a velocidade atual do carro? '))
if vel > 80:
    multa = (vel - 80) * 7
    print('MULTADO! Você excedeu o limite permitido de 80Km/h.')
    print('Você deve pagar uma multa de R${:.2f}!'.format(multa))
print('Tenha um bom dia! Dirija com segurança!')
