from rich import print
from rich.panel import Panel
from rich import box


class ControleRemoto:
    # Atributos de Classe (Limites)
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
        # 1. Montagem da barra de canais
        canais_str = ""
        for c in range(ControleRemoto.canal_min, ControleRemoto.canal_max + 1):
            if c == self.canal_atual:
                canais_str += f"[black on yellow] {c} [/] "
            else:
                canais_str += f"{c} "

        # 2. Montagem da barra de volume
        volume_str = ""
        for v in range(ControleRemoto.volume_min, ControleRemoto.volume_max + 1):
            if v <= self.volume_atual:
                volume_str += "[on cyan]  [/]"
            else:
                volume_str += "[on white]  [/]"

        # 3. Montagem do painel da TV
        conteudo = (
            f"CANAL  = {canais_str.strip()}\n"
            f"VOLUME = {volume_str}"
        )

        painel = Panel(
            conteudo,
            title="TV",
            box=box.ROUNDED,
            expand=False
        )
        print(painel)


# Teste da classe:
controle = ControleRemoto()
controle.mostrar_tv()