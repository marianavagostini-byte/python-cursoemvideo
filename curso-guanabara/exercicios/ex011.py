# ex011 - Pintando Parede
# Fonte: Curso em Vídeo - desafio oficial (complementado)

larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
area = larg * alt
tinta = area / 2
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m².'.format(larg, alt, area))
print('Para pintá-la, você precisará de {}l de tinta.'.format(tinta))
