#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Organizador de exercícios Python — Curso em Vídeo (Guanabara)

Cria uma pasta para cada exercício (ex001, ex002, ...) e salva dentro
o arquivo .py correspondente.

Fontes marcadas no cabeçalho de cada arquivo:
  [curso]        código enviado por você, identificado como desafio do curso
  [complemento]  desafio do curso que faltava — solução padrão adicionada
  [extra]        código seu que não corresponde a um desafio do curso
                 (numerado em sequência a partir do ex076)
"""
import os

BASE = "exercicios_python"

ROTULOS = {
    "curso": "Curso em Vídeo - desafio oficial (seu código)",
    "complemento": "Curso em Vídeo - desafio oficial (complementado)",
    "extra": "Extra - fora do curso (seu código / variação)",
}

EXERCICIOS = [
    # (pasta, título, fonte, código)
    ("ex001", "Olá, Mundo!", "complemento", r"""
print('Olá, Mundo!')
"""),
    ("ex002", "Respondendo ao Usuário", "curso", r"""
nome = input('Digite seu nome: ')
print('É um prazer te conhecer, {}!'.format(nome))
"""),
    ("ex003", "Somando Dois Números", "curso", r"""
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1 + n2
print('A soma entre {} e {} é igual a {}!'.format(n1, n2, s))
"""),
    ("ex004", "Dissecando uma Variável", "curso", r"""
a = input('Digite algo: ')
print('O tipo primitivo desse valor é ', type(a))
print('Só tem espaços? ', a.isspace())
print('É um número? ', a.isnumeric())
print('É alfabético? ', a.isalpha())
print('É alfanumérico? ', a.isalnum())
print('Está em maiúsculas? ', a.isupper())
print('Está em minúsculas? ', a.islower())
print('Está capitalizada? ', a.istitle())
"""),
    ("ex005", "Antecessor e Sucessor", "curso", r"""
n = int(input('Digite um número: '))
print('Analisando o valor {}, seu antecessor é {} e o sucessor é {}'.format(n, (n-1), (n+1)))
"""),
    ("ex006", "Dobro, Triplo, Raiz Quadrada", "curso", r"""
n = int(input('Digite un número: '))
print('O dobro de {} vale {}.'.format(n, (n*2)))
print('O triplo de {} vale {}.'.format(n, (n*3)))
print('A raiz quadrada de {} é igual a {:.2f}.'.format(n, (n**(1/2))))
"""),
    ("ex007", "Média Aritmética", "curso", r"""
n1 = float(input('Primeira nota do aluno: '))
n2 = float(input('Segunda nota do aluno: '))
média = (n1 + n2) / 2
print('A média entre {:.1f} e {:.1f} é igual a {:.1f}'.format(n1, n2, média))
"""),
    ("ex008", "Conversor de Medidas", "curso", r"""
medida = float(input('Uma distância em metros: '))
cm = medida * 100
mm = medida * 1000
print('A medida de {}m corresponde a {:.0f}cm e {:.0f}mm'.format(medida, cm, mm))
"""),
    ("ex009", "Tabuada", "complemento", r"""
n = int(input('Digite um número para ver sua tabuada: '))
print('-' * 12)
for c in range(1, 11):
    print('{} x {:2} = {}'.format(n, c, n * c))
print('-' * 12)
"""),
    ("ex010", "Conversor de Moedas", "complemento", r"""
real = float(input('Quanto dinheiro você tem na carteira? R$ '))
dolar = real / 5.40  # ajuste a cotação do dia
print('Com R${:.2f} você pode comprar US${:.2f}'.format(real, dolar))
"""),
    ("ex011", "Pintando Parede", "complemento", r"""
larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
area = larg * alt
tinta = area / 2
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m².'.format(larg, alt, area))
print('Para pintá-la, você precisará de {}l de tinta.'.format(tinta))
"""),
    ("ex012", "Calculando Descontos", "complemento", r"""
preco = float(input('Qual é o preço do produto? R$ '))
desc = preco - (preco * 5 / 100)
print('O produto que custava R${:.2f}, na promoção com 5% de desconto vai custar R${:.2f}'.format(preco, desc))
"""),
    ("ex013", "Reajuste Salarial", "complemento", r"""
salario = float(input('Qual é o salário do funcionário? R$ '))
novo = salario + (salario * 15 / 100)
print('Um funcionário que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}'.format(salario, novo))
"""),
    ("ex014", "Conversor de Temperaturas", "complemento", r"""
c = float(input('Informe a temperatura em ºC: '))
f = c * 1.8 + 32
print('A temperatura de {}ºC corresponde a {}ºF!'.format(c, f))
"""),
    ("ex015", "Aluguel de Carros", "complemento", r"""
dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos km rodados? '))
pago = (dias * 60) + (km * 0.15)
print('O total a pagar é de R${:.2f}'.format(pago))
"""),
    ("ex016", "Quebrando um Número", "complemento", r"""
from math import trunc
num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, trunc(num)))
"""),
    ("ex017", "Catetos e Hipotenusa", "complemento", r"""
from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))
"""),
    ("ex018", "Seno, Cosseno e Tangente", "complemento", r"""
from math import radians, sin, cos, tan
ang = float(input('Digite o ângulo que você deseja: '))
seno = sin(radians(ang))
cosseno = cos(radians(ang))
tangente = tan(radians(ang))
print('O ângulo de {} tem o SENO de {:.2f}'.format(ang, seno))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(ang, cosseno))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(ang, tangente))
"""),
    ("ex019", "Sorteando um Item na Lista", "complemento", r"""
from random import choice
a1 = input('Primeiro aluno: ')
a2 = input('Segundo aluno: ')
a3 = input('Terceiro aluno: ')
a4 = input('Quarto aluno: ')
lista = [a1, a2, a3, a4]
escolhido = choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))
"""),
    ("ex020", "Sorteando uma Ordem na Lista", "complemento", r"""
from random import shuffle
a1 = input('Primeiro aluno: ')
a2 = input('Segundo aluno: ')
a3 = input('Terceiro aluno: ')
a4 = input('Quarto aluno: ')
lista = [a1, a2, a3, a4]
shuffle(lista)
print('A ordem de apresentação será: ')
print(lista)
"""),
    ("ex021", "Tocando um MP3", "complemento", r"""
# Requer: pip install pygame  +  um arquivo de áudio 'ex021.mp3' na mesma pasta
import pygame
pygame.mixer.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
input('Tocando... pressione ENTER para encerrar.')
pygame.mixer.music.stop()
"""),
    ("ex022", "Analisador de Textos", "complemento", r"""
nome = input('Digite seu nome completo: ').strip()
print('Analisando seu nome...')
print('Seu nome em maiúsculas é: {}'.format(nome.upper()))
print('Seu nome em minúsculas é: {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(''.join(nome.split()))))
print('Seu primeiro nome tem {} letras'.format(len(nome.split()[0])))
"""),
    ("ex023", "Separando Dígitos de um Número", "complemento", r"""
num = int(input('Digite um número de 0 a 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o número {}'.format(num))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))
"""),
    ("ex024", "Verificando as Primeiras Letras", "complemento", r"""
cid = input('Em que cidade você nasceu? ').strip()
print('Sua cidade começa com "SANTO"? {}'.format(cid[:5].upper() == 'SANTO'))
"""),
    ("ex025", "Procurando uma String Dentro da Outra", "complemento", r"""
nome = input('Digite seu nome completo: ').strip()
print('Seu nome tem "Silva"? {}'.format('SILVA' in nome.upper()))
"""),
    ("ex026", "Primeira e Última Ocorrência de uma String", "complemento", r"""
frase = input('Digite uma frase: ').strip().upper()
print('A letra A aparece {} vezes na frase.'.format(frase.count('A')))
print('A primeira letra A apareceu na posição {}.'.format(frase.find('A') + 1))
print('A última letra A apareceu na posição {}.'.format(frase.rfind('A') + 1))
"""),
    ("ex027", "Primeiro e Último Nome de uma Pessoa", "complemento", r"""
nome = input('Digite seu nome completo: ').strip()
partes = nome.split()
print('Muito prazer em te conhecer!')
print('Seu primeiro nome é {}'.format(partes[0]))
print('Seu último nome é {}'.format(partes[-1]))
"""),
    ("ex028", "Jogo da Adivinhação v1.0", "complemento", r"""
from random import randint
computador = randint(0, 5)
print('-=-' * 15)
print('Vou pensar em um número de 0 a 5. Tente adivinhar...')
print('-=-' * 15)
jogador = int(input('Em que número eu pensei? '))
if jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}!'.format(computador, jogador))
"""),
    ("ex029", "Radar Eletrônico", "complemento", r"""
vel = float(input('Qual a velocidade atual do carro? '))
if vel > 80:
    multa = (vel - 80) * 7
    print('MULTADO! Você excedeu o limite permitido de 80Km/h.')
    print('Você deve pagar uma multa de R${:.2f}!'.format(multa))
print('Tenha um bom dia! Dirija com segurança!')
"""),
    ("ex030", "Par ou Ímpar?", "complemento", r"""
num = int(input('Digite um número: '))
if num % 2 == 0:
    print('O número {} é PAR!'.format(num))
else:
    print('O número {} é ÍMPAR!'.format(num))
"""),
    ("ex031", "Custo da Viagem", "complemento", r"""
distancia = float(input('Qual é a distância da sua viagem em Km? '))
print('Você está prestes a começar uma viagem de {}Km.'.format(distancia))
preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print('E o preço da sua passagem será de R${:.2f}'.format(preco))
"""),
    ("ex032", "Ano Bissexto", "complemento", r"""
from datetime import date
ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é BISSEXTO'.format(ano))
else:
    print('O ano {} NÃO é BISSEXTO'.format(ano))
"""),
    ("ex033", "Maior e Menor Valores", "curso", r"""
a=int(input('Digite o primeiro valor: '))
b=int(input('Digite o segundo valor:'))
c=int(input('Digite o terceiro valor:'))
menor=a
if b < a and b < c:
    menor=b
if c < a and c < b:
    menor=c
maior=a
if b > a and b > c:
    maior=b
if c > a and c > b:
    maior=c
print('O menor valor digitado e: {}\n'.format(menor))
print('O maior valor digitado e: {}\n '.format(maior))
"""),
    ("ex034", "Aumentos Múltiplos", "curso", r"""
salario=float(input('Qual o valor do seu salario? R$ '))
if salario <= 1250:
    novo = salario + (salario*15/100)
else:
    novo= salario+(salario*10/100)
print('Quem ganhava {:.2f} reais passa a ganhar {:.2f} reais'.format(salario,novo))
"""),
    ("ex035", "Analisando Triângulo v1.0", "curso", r"""
r1=float(input('Primeiro segmento: '))
r2=float(input('Segundo segmento: '))
r3=float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1:
    print('Os segmentos acima \33[32mPODEM FORMAR\33[m um triangulo')
else:
    print('\33[31mNAO\33[m podem formar um triangulo')
"""),
    ("ex036", "Aprovando Empréstimo", "curso", r"""
print('-='*20)
valorcasa=float(input('Qual o valor da casa? ').replace('.','').replace(',','.'))
print('-='*20)
salario=float(input("qual o salario do comprador? ").replace('.','').replace(',','.'))
print('-='*20)
anos=int(input('Em quantos anos vai pagar? '))
meses= anos * 12
prestacao= valorcasa / meses
limite= salario * 30 / 100
print('-='*20)
print('Para pagar uma casa de R${} em {} anos'.format(valorcasa,anos))
print('-='*20)
print('A prestacao sera de R${:.2f}'.format(prestacao))
print('-='*20)
if prestacao <= limite:
    print('Emprestimo \033[32m PODE SER \033[m concedido')
else:
    print('Emprestimo \033[31m NAO PODE \033[m ser concedido, exede 30% do seu salario ')
print('-='*20)
"""),
    ("ex037", "Conversor de Bases Numéricas", "curso", r"""
numero= int(input('Digite um numero inteiro:  '))
print('''Escolha uma das bases para conversao: 
      
    [ 1 ] - converter para BINARIO
    [ 2 ] - converter para OCTAL
    [ 3 ] - converter para HEXADECIMAL''')
opcao=int(input('Sua opcao: '))
if opcao ==1:
    print('{} convertido para BINARIO fica {}'.format(numero,bin(numero)))
elif opcao ==2:
    print('{} convertido para OCTAL fica {}'.format(numero,oct(numero)))
elif opcao ==3:
    print('{} convertido para HEXADECIMAL fica {}'.format(numero,hex(numero)))
"""),
    ("ex038", "Comparando Números", "curso", r"""
n1=int(input('Digite um valor inteiro: '))
n2=int(input('Digite outro valor inteiro: '))
if n1 > n2:
    print('O \033[42mprimeiro\33[m valor e \33[32mMAIOR!!!\33[m]')
elif n2  > n1:
    print('O \033[42msegundo\33[m valor e \33[32mMAIOR!!!\33[m]')
elif n1 == n2:
    print('\033[31mNAO existe valor maior, sao IGUAIS!!!\33[m]')
"""),
    ("ex039", "Alistamento Militar", "curso", r"""
ano = int(input('Em que ano voce nasceu ? '))
idade = 2026 - ano

# 1. Primeiro testamos a menor idade
if idade < 18:
    faltam = 18 - idade
    print('Você ainda não tem 18 anos mas faltam {} anos para conseguir se alistar!!!'.format(faltam))

# 2. Depois testamos a maior exceção (mais de 30 anos)
elif idade >= 30:
    print('Vish, mais de 30 anos la passou da idade!')

# 3. Depois os maiores de 18 genéricos (entre 19 e 29 anos)
elif idade > 18:
    print('Voce ja se alistou? Porque voce tem {} anos !!!'.format(idade))

# 4. E por fim, quem tem exatamente 18
elif idade == 18:
    print('Esta na hora de se alistar, 18 anos!!')
"""),
    ("ex040", "Aquele Clássico da Média", "curso", r"""
n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
media = (n1 + n2) / 2
print(f'Sua média foi: {media:.1f}')
if media < 5.0:
    print('Sua média foi abaixo de 5.0, REPROVADO!!')
elif 5.0 <= media <= 6.9:
    print('Sua média foi entre 5.0 e 6.9, RECUPERAÇÃO!!')
else:
    print('Sua média foi 7.0 ou superior, APROVADO!!')
"""),
    ("ex041", "Classificando Atletas", "curso", r"""
ano=int(input('Qual o ano de nascimento do atleta? '))
idade=2026-ano
print(f'Sua idade e {idade} anos')
if idade <=9:
    print('MIRIM')
elif idade <= 14:
    print('INFANTIL')
elif idade <=19:
    print('JUNIOR')
elif idade <=20:
    print('SENIOR')
elif idade >20:
    print('MASTER')
"""),
    ("ex042", "Analisando Triângulo v2.0", "complemento", r"""
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR um triângulo ', end='')
    if r1 == r2 == r3:
        print('EQUILÁTERO!')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO!')
    else:
        print('ISÓSCELES!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo!')
"""),
    ("ex043", "Índice de Massa Corporal (IMC)", "curso", r"""
peso=float(input('Qual o seu peso? '))
altura=float(input('Qual a sua altura? '))
imc= peso / ( altura ** 2 )
print(f'Seu IMC {imc:.1f}%')
if imc <18.5:
    print('esta abaixo do peso')
elif imc <25:
    print('Esta no peso ideal')
elif imc<30:
    print('Esta com sobrepeso')
elif imc <=40:
    print('Esta com obesidade')
else:
    print('Obesidade morbida')
"""),
    ("ex044", "Elevador de Pagamento", "curso", r"""
preco=float(input('Qual o valor total da compra? R$'))
print('''OPÇÕES DE PAGAMENTO:
[ 1 ] DINHEIRO/CHEQUE -- 10% DESCONTO
[ 2 ] À VISTA CARTÃO -- 5% DESCONTO
[ 3 ] 2X NO CARTÃO
[ 4 ] 3X OU MAIS NO CARTÃO -- 20% JUROS''')
opcao=int(input('Qual a opcao de pagamento?'))
if opcao == 1:
    total=preco-(preco*10/100)
elif opcao == 2:
    total=preco-(preco*5/100)
elif opcao == 3:
    total=preco
    parcela=total/2
    print(f'A sua compra sera parcelada em 2x sem juros, no valor de R${parcela} cada parcela')
elif opcao ==4:
    total=preco+(preco*20/100)
    parcelas=int(input('Qual o total de parcelas? '))
    parcela=total/parcelas
    print(f'A sua compra sera parcelada em {parcelas} parcelas, no valor de R${parcela:.2f} com juros ')
print(f'A sua compra de R${preco:.2f} vai custar no final R${total:.2f}')
"""),
    ("ex045", "Gnabry, Pedra, Papel e Tesoura (Jokenpô)", "curso", r"""
from random import randint

computador = randint(0, 2)
jogador = int(input('Escolha (0=Pedra, 1=Papel, 2=Tesoura): '))

print(f'Computador: {computador} | Jogador: {jogador}')
print('---')

if computador == 0:  
    if jogador == 0:
        print('Empate!')
    elif jogador == 1:
        print('Você venceu! Papel ganha de Pedra.')
    elif jogador == 2:
        print('Computador venceu! Pedra ganha de Tesoura.')

elif computador == 1:  
    if jogador == 0:
        print('Computador venceu! Papel ganha de Pedra.')
    elif jogador == 1:
        print('Empate!')
    elif jogador == 2:
        print('Você venceu! Tesoura ganha de Papel.')

elif computador == 2:  
    if jogador == 0:
        print('Você venceu! Pedra ganha de Tesoura.')
    elif jogador == 1:
        print('Computador venceu! Tesoura ganha de Papel.')
    elif jogador == 2:
        print('Empate!')
"""),
    ("ex046", "Contagem Regressiva", "curso", r"""
from time import sleep 
print('-='*20)
print('-- CONTAGEM REGRESSIVA --')
print('-='*20)
for c in range(10,-1,-1):
    print(c)
    sleep(1)
print('BOOOMM!!!!')
"""),
    ("ex047", "Contagem de Pares", "complemento", r"""
for c in range(2, 51, 2):
    print(c, end=' ')
print('Acabou!')
"""),
    ("ex048", "Soma dos Ímpares Múltiplos de Três", "complemento", r"""
soma = cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma += c
        cont += 1
print('A soma de todos os {} valores solicitados é {}'.format(cont, soma))
"""),
    ("ex049", "A Tabuada v2.0", "curso", r"""
numero=int(input('Digite um numero e veja sua tabuada:  '))
for c in range (1,11):
    print( '{} x {} = {}'.format(numero,c,numero*c))
"""),
    ("ex050", "Soma dos Pares", "curso", r"""
soma = 0 

for c in range(1, 7): 
    num = int(input('Digite o {}º número: '.format(c))) 
    
    if num % 2 == 0: 
        soma = soma + num 

print('A soma de todos os números PARES digitados é: {}'.format(soma))
"""),
    ("ex051", "Progressão Aritmética v1.0", "complemento", r"""
print('-' * 30)
print('   10 TERMOS DE UMA P.A.')
print('-' * 30)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da P.A.: '))
decimo = primeiro + (10 - 1) * razao
for c in range(primeiro, decimo + razao, razao):
    print('{}'.format(c), end=' -> ')
print('ACABOU')
"""),
    ("ex052", "Números Primos", "curso", r"""
num=int(input('Digite um numero: '))
tot=0
for c in range (1, num+1):
    if num % c ==0:
        print ('\033[33m', end='')
        tot +=1
    else:
        print('\033[31m', end='')
    print(' {} '.format(c), end='')
print('\n\033[mO numero {} foi divisivel {} vezes'.format(num,tot))
if tot == 2:
    print('E por isso ele e PRIMO')
else:
    print('Por isso ele NAO e primo')
"""),
    ("ex053", "Detector de Palíndromo", "curso", r"""
frase=str(input('Digite uma frase: ')).upper().strip()
palavras=frase.split()
junto= ''.join(palavras)
inverso=junto[::-1]
print('O inverso de {} e {}'.format(junto,inverso))
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')
"""),
    ("ex054", "Grupo da Maioridade", "curso", r"""
from datetime import date
ano = date.today().year
totmaior = 0
totmenor = 0
for c in range(1,8):
    nascimento=int(input(f'Em que ano a {c} pessoa nasceu?  '))
    idade = ano - nascimento 

    if idade >=21:
        totmaior += 1
    else:
        totmenor += 1
print(f'Ao todo tivemos {totmaior} pessoas maior de idade')
print(f'Ao todo tivemos {totmenor} pessoas menores de idade')
"""),
    ("ex055", "Maior e Menor da Sequência", "curso", r"""
for c in range(1,6):
    peso=float(input('Peso da {} pessoa: '.format(c)))
    if c ==1:
        maior=peso
        menor=peso
    else:
        if peso > maior:
            maior=peso
        if peso < menor:
            menor=peso
print(f'O maior peso lido foi de {maior}Kg')
print(f'O menor peso lido foi de {menor}Kg')
"""),
    ("ex056", "Analisador Completo", "curso", r"""
nomevelho=''
totmulher20=0
somaidade = 0  # correção: esta variável precisava ser inicializada antes do laço
for c in range (1,5):
    print(f'------ {c} PESSOA -------')
    nome=str(input('Qual o seu nome:  ')).strip()
    idade=int(input('Qual a sua idade: '))
    sexo=str(input('Qual o seu sexo [F/M]: ')).strip()
    somaidade += idade 
    if c ==1 and sexo in 'Mm':
        maioridadehomem=idade
        nomevelho=nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem= idade
        nomevelho=nome
    if sexo in "Ff" and idade > 20:
        totmulher20 += 1
        
mediaidade= somaidade / 4 
print(f'A media de idade do grupo foi de {mediaidade} anos')
print(f'O homem mais velho se chama {nomevelho} e ele tem {maioridadehomem} anos ')
print(f'Ao todo sao {totmulher20} mulheres com menos de 20 anos')
"""),
    ("ex057", "Validação de Dados", "curso", r"""
from time import sleep
sexo=input('Informa seu sexo -- [F/M]: ').strip().upper()
while sexo != 'M' and sexo != 'F':
    print('Dados invalidos...')
    sleep(1)
    print('Tente novamente digitando o que foi pedido.')
    sleep(0.5)
    sexo=input('Informe seu sexo -- [F/M]: ').strip().upper()
print(f'Sexo {sexo} registrado com sucesso')
"""),
    ("ex058", "Jogo da Adivinhação v2.0", "curso", r"""
from random import randint
computador=randint(0,10)
print('Eu sou o computador e acabei de pensar em um numero entre 0 e 10 ...')
print('Sera se voce vai acertar o meu numero? ...')
acerto=False
tentativa=0
while not acerto:
    jogador=int(input('Qual o seu palpite?  '))
    tentativa+=1
    if jogador == computador:
        acerto=True
        print('Parabens voce acertou o numero')
    else:
        if jogador < computador:
            print('Mais...')
        if jogador > computador:
            print('Menos...')
print(f'O seu total de tentativas foi: {tentativa}')
"""),
    ("ex059", "Criando um Menu de Opções", "curso", r"""
print('-='*20)
n1=float(input('Digite um numero:  '))
print('-='*20)
n2=float(input('Digite outro valor:  '))
print('-='*20)
opcao=0
while opcao !=5:
    print('''    [1] - SOMAR
    [2] - MULTIPLICAR
    [3] - MAIOR
    [4] - NOVOS NÚMEROS
    [5] - SAIR DO PROGRAMA''')
    print('-='*20)
    opcao=int(input('Qual a sua opcao ? '))
    print('-='*20)
    if opcao ==1:
        soma=n1+n2
        print(f'A soma de {n1} e {n2} e: {soma:.2f}')
        print('-='*20)
    elif opcao ==2:
        multiplicacao=n1*n2
        print(f'A multiplicacao entre {n1} e {n2} e: {multiplicacao}')
        print('-='*20)
    elif opcao ==3:
        if n1>n2:
            maior=n1
        else:
            maior=n2
        print(f'Entre {n1} e {n2} o maior e: {maior}')
        print('-='*20)
    elif opcao ==4:
        print('Informe os numeros novamente: ')
        n1=int(input('Primeiro valor:  '))
        n2=int(input('Segundo valor:  '))
    elif opcao ==5:
        print('Finalizando..')
    else:
        print('Incorreto, tente novamente')
print('Fim do programa!!')
"""),
    ("ex060", "Cálculo do Fatorial", "curso", r"""
from math import factorial
numero=int(input('Digite um numero e veja sua fatorial:  '))
f = factorial(numero)
print(f'O fatorial do numero {numero} e: {f}')
"""),
    ("ex061", "Progressão Aritmética v2.0", "complemento", r"""
print('Gerador de P.A. (10 primeiros termos, usando while)')
print('-' * 30)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} -> '.format(termo), end='')
    termo += razao
    cont += 1
print('FIM')
"""),
    ("ex062", "Super Progressão Aritmética v3.0", "curso", r"""
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
"""),
    ("ex063", "Sequência de Fibonacci", "curso", r"""
n=int(input('Digite a quantidade de numeros da sequencia FIBONACCI:  '))
t1=0
t2=1
print(f'{t1} -> {t2}',end='')
c=3
while c <=n:
    t3=t1+t2
    print(f'-> {t3}',end='')
    t1=t2
    t2=t3
    c+=1
print(' - FIM')
"""),
    ("ex064", "Tratando Vários Valores v1.0", "curso", r"""
soma = 0
cont = 0

numero = int(input('Digite um numero, para parar digite 999: '))

while numero != 999:
    soma += numero
    cont += 1
    numero = int(input('Digite um numero, para parar digite 999: '))

print(f'Voce digitou {cont} numeros e a soma foi {soma}.')
"""),
    ("ex065", "Maior e Menor Valores com Flag", "curso", r"""
resp = 'S'
soma = quant = media = maior = menor = 0

while resp in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    quant += 1
    
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
            
    resp = input('Quer continuar? [S/N] ').strip().upper()[0]

media = soma / quant

print(f'Você digitou {quant} números e a média foi {media:.2f}')
print(f'O maior valor foi {maior} e o menor foi {menor} , e a soma deles e {soma}')
"""),
    ("ex066", "Vários Valores com Flag (break)", "curso", r"""
sum = 0
c = 0

while True:
    n = int(input('Type a number [999 to stop]: '))
    if n == 999:
        break
    sum += n
    c += 1

print(f'You typed {c} numbers and the sum was {sum}.')
"""),
    ("ex067", "Tabuada v3.0", "curso", r"""
c=0
while True:
    numero=int(input('Voce quer ver a tabuada de que numero?  '))
    if numero <0:
        break
    c+=1
    for c in range (1,101):
        print(f'{numero} x {c} = {numero*c}')
"""),
    ("ex068", "Jogo do Par ou Ímpar", "curso", r"""
from random import randint
soma=0
v=0
d=0
while True:
    jogador=int(input('Digite um valor: '))
    computador=randint(0,10)
    soma=jogador+computador
    opcao=' '
    while opcao not in 'PI':
        opcao=str(input('Par ou Impar [P/I] ?  ')).upper().strip()[0]
    print(f'Voce jogou {jogador} e o computador jogou {computador} , total de: {soma}')
    if opcao =='P':
        if soma %2==0:
            print('Voce VENCEU ')
            v+=1
        else:
            print('Voce PERDEU')
            d+=1
            break 
            
    elif opcao == 'I':
        if soma %2 !=0:
            print('voce VENCEU')
            v+=1
        else:
            print('Voce PERDEU')
            d+=1
            break
    print('Vamos jogar novamente ..')
print(f' GAME OVER .. Voce venceu {v} vezes e perdeu {d} vezes. ')
"""),
    ("ex069", "Análise de Dados do Grupo", "curso", r"""
pessoas18=homens=mulheres20=0
while True:
    idade=int(input('Qual a sua idade ?  '))
    sexo=str(input('Qual o seu sexo [M/F] ? ')).strip().upper()[0]
    continuar=str(input('Quer continuar [S/N] ? ')).strip().upper()[0]
    if continuar == 'N':
        print('Fim do programa.. ')
        break

    if idade >18:
        pessoas18+=1
    if sexo == 'M':
        homens+=1
    if sexo == 'F' and idade < 20:
        mulheres20+=1
print(f'Tem {pessoas18} pessoas maiores de 18 anos ..',end='')
print(f'Foram cadastrados {homens} homens..',end='')
print(f'Tem {mulheres20} mulheres abaixo de 20 anos')
"""),
    ("ex070", "Estatísticas em Produtos", "curso", r"""
tot=p1000=0
pbarato=''
valorbarato=0
c=0
while True:
    nome=str(input('Nome do Produto: '))
    preco=int(input('Preco do Produto: '))
    continuar=' '
    c+=1
    tot+=preco

    while continuar not in 'SN':
        continuar=str(input('Quer continuar [S/N] ?')).strip().upper()[0]
        
    if preco >=1000:
        p1000+=1
    if c ==1 or preco < valorbarato:
        valorbarato=preco
        pbarato=nome
    if continuar == 'N':
            print('FIM do programa..')
            break

print(f'total da compra: {tot}')
print(f'{p1000} produtos custam mais de 1.000,00 ')
print(f'O nome do produto mais barato e: {pbarato} , e seu valor e: {valorbarato}')
"""),
    ("ex071", "Simulador de Caixa Eletrônico", "curso", r"""
valor=int(input('Qual o valor a ser sacado? '))
cedula=50
totced=0
total=valor
while True:
    if total >= cedula:
        total-=cedula
        totced+=1
    else:
        if totced >0:
            print(f'Total de {totced} cedula de R$ {cedula}')
        if cedula ==50:
            cedula=20
        elif cedula ==20:
            cedula= 10
        elif cedula ==10:
            cedula=1
        totced=0
        if total ==0:
            break
"""),
    ("ex072", "Número por Extenso", "curso", r"""
contagem = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 
            'seis', 'sete', 'oito', 'nove', 'dez', 
            'onze', 'doze', 'treze', 'quatorze', 'quinze', 
            'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if 0 <= num <= 20:
        break
    print('Tente novamente. ', end='')

print(f'Você digitou o número {contagem[num]}.')
"""),
    ("ex073", "Tuplas com Times de Futebol", "curso", r"""
AMARELO = '\033[1;33m'
VERDE   = '\033[1;32m'
AZUL    = '\033[1;34m'
CYAN    = '\033[1;36m'
ROXO    = '\033[1;35m'
RESET   = '\033[m'

LINHA   = '-=' * 30

times = (
    'Palmeiras', 'Flamengo', 'Athletico-PR', 'Fluminense', 'Red Bull Bragantino',
    'Bahia', 'Corinthians', 'Cruzeiro', 'Botafogo', 'Coritiba',
    'Vitória', 'São Paulo', 'Atlético-MG', 'Internacional', 'Grêmio',
    'Santos', 'Vasco da Gama', 'Mirassol', 'Remo', 'Chapecoense'
)

print(LINHA)
print(f'{AMARELO}Os 5 primeiros colocados:{RESET}')
for pos, t in enumerate(times[:5], start=1):
    print(f'   {pos}º - {t}')

print(LINHA)
print(f'{VERDE}Os 4 últimos colocados (Zona de Rebaixamento):{RESET}')
for pos, t in enumerate(times[-4:], start=17):
    print(f'   {pos}º - {t}')

print(LINHA)
print(f'{AZUL}Times em ordem alfabética:{RESET}')
print(f'   {", ".join(sorted(times))}')

print(LINHA)
posicao = times.index('Chapecoense') + 1
print(f'{CYAN}O Chapecoense está na {ROXO}{posicao}ª{CYAN} posição da tabela.{RESET}')
print(LINHA)
"""),
    ("ex074", "Maior e Menor Valores em Tupla", "curso", r"""
from random import randint

numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))

print(f'Os valores sorteados sao {numeros}',end='')
for n in numeros:
    print(f'{n}',end='')

print(f'\nO maior valor sorteado foi: {max(numeros)}')
print(f'\nO menor valor sorteado foi: {min(numeros)}')
"""),
    ("ex075", "Análise de Dados em uma Tupla", "curso", r"""
def ler_numero(mensagem):
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print('Erro! Digite apenas números inteiros!!')

num = (
    ler_numero('Digite o 1 valor: '),
    ler_numero('Digite o 2 valor: '),
    ler_numero('Digite o 3 valor: '),
    ler_numero('Digite o 4 valor: ')
)

print(f'\nVocê digitou os valores: {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes.')
if 3 in num:
    print(f'O primeiro valor 3 foi digitado na posicao: {num.index(3)+1}')
else:
    print('O valor 3 nao foi digitado em nenhuma posicao.')
print(f'Os numeros pares foram:',end='')
for n in num:
    if n %2==0:
        print(f'{n} ',end='')
"""),
    # ------------------- EXTRAS (fora do curso / variações suas) -------------------
    ("ex076", "Comparando dois números (versão simples)", "extra", r"""
x = int(input('Digite o primeiro número inteiro: '))
y = int(input('Digite o segundo número inteiro: '))

if x > y:
    print('O primeiro número é maior que o segundo número')
else : 
    print(' O segundo número é maior do que o primeiro número')
"""),
    ("ex077", "Franga ou Maromba", "extra", r"""
treino =int(input('Há quantos anos você treina? '))
if treino <2:
    print('Aí você é franga')
else:
    print('Aí você é maromba')
"""),
    ("ex078", "Média com operador ternário", "extra", r"""
n1=float(input('Sua primeira nota foi: '))
n2=float(input('Sua segunda nota foi: '))
média = (n1+n2)/2
print('A sua média foi {:.1f}'.format(média))
print('Parabéns'if média>=6.0 else 'Recuperação')
"""),
    ("ex079", "Jokenpô (versão 1 a 3)", "extra", r"""
from random import randint 
computador = randint(1,3)
jogador=int(input('Escolha um numero - [1]pedra  [2]papel  [3]tesoura: '))
print(f'   Computador: {computador}    |    jogador:  {jogador}')
if computador == 1:
    if jogador== 1:
        print('EMPATE!!')
    elif jogador ==2:
        print('Voce venceu, papel ganha da pedra')
    elif jogador ==3: 
        print('Voce perdeu, tesoura perde da pedra')
if computador == 2:
    if jogador == 2:
        print('EMPATE')
    if jogador == 3:
        print('GANHOU, tesoura ganha do papel ')
    if jogador ==1:
        print('PERDEU, pedra nao mata papel  ')
if computador ==3:
    if jogador ==3:
        print('EMPATE')
    if jogador ==1:
        print('GANHOU, pedra mata tesoura')
    if jogador ==2:
        print('GANHOU, papel mata pedra')
"""),
    ("ex080", "Categorias de natação (versão com date.today)", "extra", r"""
from datetime import date

atual = date.today().year 

nascimento = int(input('Qual a sua data de nascimento?  '))

idade = atual - nascimento 

if idade <=9:
    categoria=('MIRIM')
elif idade <=14:
    categoria=('INFANTIL')
elif idade <=19:
    categoria=('JUNIOR')
elif idade <=25:
    categoria=('SENIOR')
else:
    categoria=int(input('MASTER'))

print(f'Voce tem {idade} anos, por isso compete na categoria: {categoria}')
"""),
    ("ex081", "Adivinhação com contador de tentativas", "extra", r"""
from time import sleep
from random import randint
tentativas=0

computador=randint(0,10)
print('Vou pensar em um numero entre 0 e 10, tente advinhar... ')
sleep(2)

jogador=int(input('Pensou em qual numero?  '))

while jogador != computador:
        print('PROCESSANDO...')
        sleep(0.5)
        print('Numero ERRADO, tente novamente...')
        sleep(0.5)
        jogador=int(input('Qual o seu novo palpite? '))
        tentativas+=1
print('PROCESSANDO..')
sleep(1)
print('PARABENS, voce acertou o numero !!!')
"""),
    ("ex082", "Fatorial com while (versão manual)", "extra", r"""
numero=int(input('Escolha um numero para virar fatorial : '))
contador=numero
multiplicacao=1
while contador > 0:
    multiplicacao *=contador
    contador -=1
print(f'Seu numero {numero} vira {multiplicacao}')
"""),
    ("ex083", "Menu de opções (primeira versão)", "extra", r"""
from time import sleep
opcao=soma=0
n1=float(input('Digite um valor:  '))
n2=float(input('Digite outro valor: '))
print('''
[1] - SOMAR
[2] - MULTIPLICAR
[3] - MAIOR
[4] - NOVOS NÚMEROS
[5] - SAIR DO PROGRAMA
''')
while opcao != 5:
    opcao=int(input('Qual a sua escolha ? '))
    if opcao ==1:
        soma=n1+n2
        print(f'A soma dos dois numeros foi: {soma:.1f}')
    elif opcao ==2:
        multiplica=n1*n2
        print(f'A multiplicacao resultou: {multiplica}')
    elif opcao ==3:
        if n1>n2:
            print(f'O {n1} e maior que {n2}')
        if n1<n2:
            print(f'O {n2} e maior que {n1}')
        else:
            print('os valores sao iguais !!')
    elif opcao ==4:
        print('Informe novos numeros : ')
        n11=float(input('Digite um valor: '))
        n22=float(input('Digite outro valor:  '))
    elif opcao ==5:
        print('Finalizando o programa ..')
    else:
        print('Opcao invalida')
"""),
    ("ex084", "Adivinhação 'mais para cima'", "extra", r"""
from random import randint
from time import sleep
computador=randint(0,10)
sleep(2)
print('Sou seu computador... acabei de pensar em um numero entre 0 e 10..')
sleep(0.5)
print('Tente advinhar qual foi ..')
sleep(0.5)
jogador=int(input('Qual e o seu palpite ?  '))
sleep(0.5)
while jogador != computador:
        print(f'Errou...')
        if computador > jogador:
                print('Tente mais para cima...')
        jogador=int(input('Digite outro numero:  '))
print(f'ACERTOU !! Pensamos no numero: {computador}')
"""),
    ("ex085", "Tabuada com while", "extra", r"""
numero=int(input('Quer ver a tabuada de que numero?  '))
c=1
while c <=10:
    print(f'{c} x {numero} = {c*numero}')
    c+=1
print('FIM')
"""),
    ("ex086", "Sequência multiplicativa", "extra", r"""
n=int(input('Qual quantidade da sequencia?  '))
t1=1
t2=2
c=3
print(f'{t1} -- {t2}  ',end='')
while c <=n:
    t3=t1*t2
    print(f'-- {t3}',end='')
    t1=t2
    t2=t3
    c+=1
print('--FIM')
"""),
    ("ex087", "Sequência de Tribonacci", "extra", r"""
n=int(input('Escolha quantos termos para a sequencia de TRIBONACCI:  '))
t1=0
t2=0
t3=1
c=4
print(f'{t1} -- {t2} -- {t3}',end='')
while c <=n:
    t4=t1+t2+t3
    print(f'-- {t4}',end='')
    t1=t2
    t2=t3
    t3=t4
    c+=1
print('--FIM')
"""),
    ("ex088", "Detector de Palíndromo (versão colorida)", "extra", r"""
print('\033[36m-=\033[m' * 20) 
print('\033[1;36m       DETECTOR DE PALÍNDROMO\033[m') 
print('\033[36m-=\033[m' * 20)

frase = str(input('\n\033[34mDigite uma frase: \033[m')).strip().upper()

palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]

print('\n\033[33mAnalisando...\033[m\n') 
print('O inverso de \033[1;33m{}\033[m é \033[1;33m{}\033[m'.format(junto, inverso))
print('-' * 40) 

if inverso == junto:
    print('\033[1;32m✅ Temos um palíndromo!\033[m') 
else:
    print('\033[1;31m❌ A frase digitada não é um palíndromo!\033[m')

print()
"""),
    ("ex089", "Soma de números S/N (versão while True)", "extra", r"""
soma=cont=maiorvalor=menorvalor=0

while True:
    numero=int(input('Digite um numero:  '))
    opcao=input('Quer continuar ? [S/N]  ').strip().upper()
    if cont ==1:
        maiorvalor+=numero
        menorvalor+=numero
    elif numero > maiorvalor:
        maiorvalor=numero
    elif numero < menorvalor:
        menorvalor=numero
    soma+=numero
    cont+=1
    media=soma/cont
    if opcao =='N':
        print(f'Voce digitou {cont} numeros e a media foi de: {media}',end='')
        print(f'O maior valor foi {maiorvalor} e o menor foi {menorvalor}')
        break
"""),
    ("ex090", "Gerador de P.A. com pausa (versão 2)", "extra", r"""
print('-=' * 20)
print('GERADOR DE P.A')
print('-=' * 20)

cont = 1
Primeiro = int(input('Digite um numero para a P.A: '))
razao = int(input('Digite sua razao: '))

termo = Primeiro
mais = 10
total = 0

while mais != 0:
    total += mais
    
    while cont <= total:
        print(f'{termo} -> ', end='')
        cont += 1
        termo += razao
        
    print('PAUSA')
    mais = int(input('Quantos termos quer mostrar a mais? '))

print(f'Progressao finalizada com {total} termos mostrados.')
"""),
    ("ex091", "Gerador de P.A. com nomes descritivos (REVISAR)", "extra", r"""
# Você marcou este desafio para REVISAR
print('-=' * 20)
print('GERADOR DE P.A')
print('-=' * 20)

numero_inicial = int(input('Digite o numero inicial da P.A: '))
razao = int(input('Digite a razao (de quanto em quanto pula): '))

valor_que_vai_aparecer = numero_inicial
quantidade_pedida = 10
limite_da_sequencia = 0
numero_atual_da_contagem = 1

while quantidade_pedida != 0:
    limite_da_sequencia += quantidade_pedida
    
    while numero_atual_da_contagem <= limite_da_sequencia:
        print(f'{valor_que_vai_aparecer} -> ', end='')
        numero_atual_da_contagem += 1
        valor_que_vai_aparecer += razao
        
    print('PAUSA')
    quantidade_pedida = int(input('Quantos termos quer mostrar a mais? '))

print(f'Progressao finalizada com {limite_da_sequencia} termos mostrados.')
"""),
    ("ex092", "Par ou Ímpar (versão 2, com 'Deu PAR')", "extra", r"""
from random import randint
soma=0
v=0
d=0
while True:
    jogador=int(input('Digite um valor: '))
    computador=randint(0,10)
    soma=jogador+computador
    opcao=' '
    while opcao not in 'PI':
        opcao=str(input('Par ou Impar [P/I] ?  ')).upper().strip()[0]
    print(f'Voce jogou {jogador} e o computador jogou {computador} , total de: {soma}')
    print('Deu PAR ' if soma %2 ==0 else 'Deu IMPAR')
    if opcao =='P':
        if soma %2==0:
            print('Voce VENCEU ')
            v+=1
        else:
            print('Voce PERDEU')
            d+=1
            break 
            
    elif opcao == 'I':
        if soma %2 !=0:
            print('voce VENCEU')
            v+=1
        else:
            print('Voce PERDEU')
            d+=1
            break
    print('Vamos jogar novamente ..')
print(f' GAME OVER .. Voce venceu {v} vezes e perdeu {d} vezes. ')
"""),
    ("ex093", "Menu com 4 opções", "extra", r"""
n1=int(input('Digite o 1 numero:  '))
n2=int(input('Digite o 2 numero: '))
opcao=0
while opcao !=4:
    print('''          [1] SOMA  
          [2] MULTIPLICA
          [3] NOVOS NUMEROS
          [4] SAIR''')
    opcao=int(input('Qual a sua opcao? '))
    if opcao ==1:
        soma=n1+n2
        print(f'A soma de {n1} + {n2} = {soma}')
    elif opcao ==2:
        multi=n1*n2
        print(f'A multiplicacao de {n1} x {n2} = {multi}')
    elif opcao ==3:
        print('Digite os novos numeros ..')
        n1=int(input('Numero 1: '))
        n2=int(input('Numero 2: '))
    elif opcao ==4:
        print('Desligando programa..')
    else:
        print('Resposta invalida, tente novamente...')
        opcao=int(input('Qual a sua opcao?'))
print('Programa finalizado..')
"""),
]


def main():
    for pasta, titulo, fonte, codigo in EXERCICIOS:
        caminho = os.path.join(BASE, pasta)
        os.makedirs(caminho, exist_ok=True)
        arquivo = os.path.join(caminho, f"{pasta}.py")
        cabecalho = f"# {pasta} - {titulo}\n# Fonte: {ROTULOS[fonte]}\n\n"
        with open(arquivo, "w", encoding="utf-8") as f:
            f.write(cabecalho + codigo.strip() + "\n")
        print(f"[OK] {arquivo}")

    print(f"\nTotal: {len(EXERCICIOS)} exercícios criados na pasta '{BASE}/'")
    curso = sum(1 for e in EXERCICIOS if e[2] == "curso")
    comp = sum(1 for e in EXERCICIOS if e[2] == "complemento")
    extra = sum(1 for e in EXERCICIOS if e[2] == "extra")
    print(f"  - {curso} desafios do curso (seus códigos)")
    print(f"  - {comp} desafios complementados (faltavam)")
    print(f"  - {extra} extras/variações suas (ex076 em diante)")


if __name__ == "__main__":
    main()
