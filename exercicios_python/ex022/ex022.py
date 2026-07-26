# ex022 - Analisador de Textos
# Fonte: Curso em Vídeo - desafio oficial (complementado)

nome = input('Digite seu nome completo: ').strip()
print('Analisando seu nome...')
print('Seu nome em maiúsculas é: {}'.format(nome.upper()))
print('Seu nome em minúsculas é: {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(''.join(nome.split()))))
print('Seu primeiro nome tem {} letras'.format(len(nome.split()[0])))
