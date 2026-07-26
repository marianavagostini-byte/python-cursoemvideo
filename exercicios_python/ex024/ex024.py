# ex024 - Verificando as Primeiras Letras
# Fonte: Curso em Vídeo - desafio oficial (complementado)

cid = input('Em que cidade você nasceu? ').strip()
print('Sua cidade começa com "SANTO"? {}'.format(cid[:5].upper() == 'SANTO'))
