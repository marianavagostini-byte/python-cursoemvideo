from datetime import datetime
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt, FloatPrompt

console = Console()


class ContaBancaria:
    def __init__(self, titular: str):
        self.titular = titular
        self.saldo = 0.0
        self.extrato = []  

    def depositar(self, valor: float):
        if valor > 0:
            self.saldo += valor
            registro = {
                "data": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
                "tipo": "Depósito",
                "valor": valor,
                "status": "Sucesso",
            }
            self.extrato.append(registro)
            console.print(
                f"[bold green]✓[/] Depósito de [bold green]R$ {valor:,.2f}[/] realizado com sucesso!"
            )
        else:
            console.print(
                "[bold red]✗ Operação recusada:[/] O valor de depósito deve ser maior que zero."
            )

    def sacar(self, valor: float):
        if valor <= 0:
            console.print(
                "[bold red]✗ Operação recusada:[/] O valor de saque deve ser maior que zero."
            )
        elif valor > self.saldo:
            console.print(
                f"[bold red]✗ Saldo insuficiente![/] Saldo atual: [bold yellow]R$ {self.saldo:,.2f}[/]"
            )
        else:
            self.saldo -= valor
            registro = {
                "data": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
                "tipo": "Saque",
                "valor": valor,
                "status": "Sucesso",
            }
            self.extrato.append(registro)
            console.print(
                f"[bold green]✓[/] Saque de [bold green]R$ {valor:,.2f}[/] realizado com sucesso!"
            )

    def ver_saldo(self):
        painel_saldo = Panel(
            f"[bold white]Titular:[/] [cyan]{self.titular}[/]\n"
            f"[bold white]Saldo Disponível:[/] [bold green]R$ {self.saldo:,.2f}[/]",
            title="[bold yellow]Consulta de Saldo[/]",
            expand=False,
            border_style="cyan",
        )
        console.print(painel_saldo)

    def ver_extrato(self):
        if not self.extrato:
            console.print(
                Panel(
                    "[yellow]Nenhuma movimentação registrada até o momento.[/]",
                    title="Extrato",
                    border_style="yellow",
                    expand=False,
                )
            )
            return

        tabela = Table(
            title=f"Extrato Bancário - {self.titular}",
            header_style="bold magenta",
            border_style="blue",
        )
        tabela.add_column("Data/Hora", style="dim", width=20)
        tabela.add_column("Operação", justify="center")
        tabela.add_column("Valor", justify="right")

        for item in self.extrato:
            cor = "green" if item["tipo"] == "Depósito" else "red"
            sinal = "+" if item["tipo"] == "Depósito" else "-"
            tabela.add_row(
                item["data"],
                f"[{cor}]{item['tipo']}[/]",
                f"[{cor}]{sinal} R$ {item['valor']:,.2f}[/]",
            )

        tabela.add_section()
        tabela.add_row(
            "[bold white]Total em Conta[/]",
            "",
            f"[bold green]R$ {self.saldo:,.2f}[/]",
        )

        console.print(tabela)



console.clear()
console.print(
    Panel.fit(
        "[bold cyan]SISTEMA BANCÁRIO DIGITAL[/]\n[dim]Ambiente Seguro de Operações[/]",
        border_style="bold blue",
    )
)

nome = Prompt.ask("\n[bold]Informe o nome do titular da conta[/]")
conta = ContaBancaria(nome)
console.print(f"[green]Conta de [bold]{conta.titular}[/] criada com sucesso![/]\n")


while True:
    console.print(
        Panel(
            "[1] [cyan]Depositar[/]\n"
            "[2] [cyan]Sacar[/]\n"
            "[3] [cyan]Ver Saldo[/]\n"
            "[4] [cyan]Ver Extrato Completo[/]\n"
            "[5] [red]Sair[/]",
            title="[bold yellow]Menu Principal[/]",
            border_style="blue",
            expand=False,
        )
    )

    opcao = Prompt.ask(
        "Selecione uma opção", choices=["1", "2", "3", "4", "5"], show_choices=False
    )

    console.print()

    if opcao == "1":
        valor = FloatPrompt.ask("Digite o valor do depósito: [green]R$[/]")
        conta.depositar(valor)

    elif opcao == "2":
        valor = FloatPrompt.ask("Digite o valor do saque: [green]R$[/]")
        conta.sacar(valor)

    elif opcao == "3":
        conta.ver_saldo()

    elif opcao == "4":
        conta.ver_extrato()

    elif opcao == "5":
        console.print(
            Panel.fit(
                f"[bold yellow]Obrigado por utilizar nossos serviços, {conta.titular}![/]\n[dim]Sessão encerrada com segurança.[/]",
                border_style="green",
            )
        )
        break

    console.print("\n" + "─" * 40 + "\n")