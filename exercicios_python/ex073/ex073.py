# ex073 - Tuplas com Times de Futebol
# Fonte: Curso em Vídeo - desafio oficial (seu código)

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
