# ex176
# Fonte: Curso em Vídeo / prática (seu código)

oficina = list()


def cadastra(lista):
    while True:
        dados = {}
        dados['cliente'] = input('Cliente: ')
        dados['veiculo'] = input('Veiculo: ')
        dados['servico'] = input('Servico: ')
        dados['valor'] = float(input('Valor: R$ '))
        lista.append(dados)

        resp = input('Quer continuar? [S/N] ').upper()[0]
        if resp == 'N':
            break



def ordens(lista):
    for p in lista:
        print(f'{p['cliente']} ------ {p['veiculo']}   {p['servico']} R$ {p['valor']}')

def caros(lista):
    acima = []
    for p in lista:
        if p['valor'] > 500:
            acima.append(p['cliente'])
    return acima
     
def maior(lista):
    campeao=lista [0]
    for p in lista:
        if p['valor'] > campeao['valor']:
            campeao=p
    return campeao['cliente']
              
cadastra(oficina)
ordens(oficina)
print(f'Servico acima de R$ 500: {caros(oficina)}')
print(f'Maior servico: {maior(oficina)}')

valores=[]
for p in oficina:
    valores.append(p['valor'])
faturamento= sum(valores)
media=faturamento/len(valores)
print(f'Faturamento do dia: {faturamento:.2f} ')
print(f'Ticket medio: {media:.2f}')

