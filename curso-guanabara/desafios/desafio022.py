# ex207 - Desafio 22 POO: Controle remoto
# Fonte: Curso em Vídeo - Guanabara

from rich import print
from rich.panel import Panel
from rich import box


class ControleRemoto:
    canal_min: int = 1
    canal_max: int = 5
    volume_min: int = 1
    volume_max: int = 5

    def __init__(self, canal: int = 1, volume: int = 2):
        self.canal_atual: int = canal
        self.volume_atual: int = volume

    def aumentar_volume(self):
        if self.volume_atual < ControleRemoto.volume_max:
            self.volume_atual += 1

    def diminuir_volume(self):
        if self.volume_atual > ControleRemoto.volume_min:
            self.volume_atual -= 1

    def mudar_canal(self, novo_canal: int):
        if ControleRemoto.canal_min <= novo_canal <= ControleRemoto.canal_max:
            self.canal_atual = novo_canal

    def canal_avancar(self):
        if self.canal_atual < ControleRemoto.canal_max:
            self.canal_atual += 1
        else:
            self.canal_atual = ControleRemoto.canal_min

    def canal_voltar(self):
        if self.canal_atual > ControleRemoto.canal_min:
            self.canal_atual -= 1
        else:
            self.canal_atual = ControleRemoto.canal_max

    def mostrar_tv(self):
        canais_str = ""
        for c in range(ControleRemoto.canal_min, ControleRemoto.canal_max + 1):
            if c == self.canal_atual:
                canais_str += f"[black on yellow] {c} [/] "
            else:
                canais_str += f"{c} "

        volume_str = ""
        for v in range(ControleRemoto.volume_min, ControleRemoto.volume_max + 1):
            if v <= self.volume_atual:
                volume_str += "[on cyan]  [/]"
            else:
                volume_str += "[on white]  [/]"

        conteudo = (
            f"CANAL  = {canais_str.strip()}\n"
            f"VOLUME = {volume_str}"
        )
        painel = Panel(conteudo, title="TV", box=box.ROUNDED, expand=False)
        print(painel)


def leiaInt(msg):
    while True:
        entrada = str(input(msg)).strip()
        try:
            n = int(entrada)
        except:
            print(f'ERRO! "{entrada}" não é um número inteiro válido.')
        else:
            return n


def menu(lista):
    print('-' * 40)
    print('CONTROLE REMOTO'.center(40))
    print('-' * 40)
    for c in range(0, len(lista)):
        print(f'[ {c+1} ] {lista[c]}')
    print('-' * 40)
    opc = leiaInt('Sua opção: ')
    return opc


controle = ControleRemoto()

opcoes = ['Aumentar volume', 'Diminuir volume', 'Avançar canal',
          'Voltar canal', 'Escolher canal', 'Sair']

while True:
    controle.mostrar_tv()
    opc = menu(opcoes)

    if opc == 1:
        controle.aumentar_volume()

    elif opc == 2:
        controle.diminuir_volume()

    elif opc == 3:
        controle.canal_avancar()

    elif opc == 4:
        controle.canal_voltar()

    elif opc == 5:
        novo = leiaInt('Para qual canal (1 a 5)? ')
        controle.mudar_canal(novo)

    elif opc == 6:
        print('Desligando... Até logo!')
        break

    else:
        print('ERRO! Digite uma opção válida.')