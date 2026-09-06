from banco import ContaBancaria, OperacaoInvalida, encontrar_conta


def ler_valor(mensagem):
    return input(mensagem).replace(",", ".")


def criar_conta(contas):
    titular = input("Nome do titular: ").strip()
    numero = len(contas) + 1
    try:
        conta = ContaBancaria(numero, titular)
    except OperacaoInvalida as erro:
        print(f"Erro: {erro}")
        return
    contas.append(conta)
    print(f"Conta criada com sucesso. Número: {conta.numero}")


def selecionar_conta(contas):
    if not contas:
        print("Nenhuma conta cadastrada.")
        return None
    try:
        numero = int(input("Número da conta: "))
        return encontrar_conta(contas, numero)
    except (ValueError, OperacaoInvalida) as erro:
        print(f"Erro: {erro}")
        return None


def movimentar(contas, operacao):
    conta = selecionar_conta(contas)
    if conta is None:
        return
    try:
        valor = ler_valor("Valor: ")
        operacao(conta, valor)
        print("Operação realizada com sucesso.")
    except (ValueError, OperacaoInvalida) as erro:
        print(f"Erro: {erro}")


def listar_contas(contas):
    if not contas:
        print("Nenhuma conta cadastrada.")
        return
    for conta in contas:
        print(f"{conta.numero} - {conta.titular} - Saldo: R$ {conta.saldo:.2f}")


def executar():
    contas = []
    while True:
        print("\n=== BANCO PYTHON ===")
        print("1. Criar conta")
        print("2. Depositar")
        print("3. Sacar")
        print("4. Ver extrato")
        print("5. Listar contas")
        print("0. Sair")
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            criar_conta(contas)
        elif opcao == "2":
            movimentar(contas, lambda conta, valor: conta.depositar(valor))
        elif opcao == "3":
            movimentar(contas, lambda conta, valor: conta.sacar(valor))
        elif opcao == "4":
            conta = selecionar_conta(contas)
            if conta:
                print(conta.extrato())
        elif opcao == "5":
            listar_contas(contas)
        elif opcao == "0":
            print("Até logo!")
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    executar()
