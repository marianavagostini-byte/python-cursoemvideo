# ex027 - Primeiro e Último Nome de uma Pessoa
# Fonte: Curso em Vídeo - desafio oficial (complementado)

nome = input('Digite seu nome completo: ').strip()
partes = nome.split()
print('Muito prazer em te conhecer!')
print('Seu primeiro nome é {}'.format(partes[0]))
print('Seu último nome é {}'.format(partes[-1]))
