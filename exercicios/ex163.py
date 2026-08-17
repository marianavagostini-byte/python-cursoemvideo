# ex163
# Fonte: Curso em Vídeo / prática (seu código)

def area(largura,comprimento):
    return largura * comprimento


largura=float(input('Largura do terreno: '))
comprimento=float(input('Comprimento do terreno: '))

print(f'A area do terreno tem {largura} x {comprimento} = {area(largura,comprimento)}m².')
