class ContaBancaria:
    def __init__(self,nome:str):
        self.nome=nome
        self.saldo=0
        self.extrato=[]
        
    def depositar(self,deposito=0):
        if deposito > 0:
            self.saldo += deposito
            self.extrato.append(f'Deposito de: R$ {deposito} realizado.')
        else:
            print('Deposito negado !! Digite um valor acima de " 0 ".')
    
    def sacar(self, saque=0):
        if saque > 0 and saque <= self.saldo:
            self.saldo -= saque
            self.extrato.append(f'Saque de: R$ {saque} realizado. ')
        else:
            print('Saque negado !! Digite um valor valido.')
    
    def ver_saldo(self):
        print(f'Titular: {self.nome} | Saldo: R$ {self.saldo:.2f}')
    
    def ver_extrato(self):
        print('-'*42)
        print(f'EXTRATO - {self.nome}'.center(42))
        print('-'*42)
        if not self.extrato:
            print('Nenhum extrato.')
        else:
            for item in self.extrato:
                print(item)
            print(f'Saldo atual: R$ {self.saldo:.2f}')
nome_cliente=input('Nome do titular: ')
conta=ContaBancaria(nome_cliente)
while True:
    print("-" * 25)
    print(f"Conta de: {conta.nome}")
    print("[ 1 ] Depositar")
    print("[ 2 ] Sacar")
    print("[ 3 ] Ver Saldo")
    print("[ 4 ] Ver Extrato")
    print("[ 5 ] Sair")
    print("-" * 25)
    
    opc=int(input('Sua opcao: '))
    if opc == 1:
        v = float(input('Valor do deposito: R$ '))
        conta.depositar(v)
    elif opc == 2:
        v = float(input('Valor do saque: R$ '))
        conta.sacar(v)
    elif opc == 3:
        conta.ver_saldo()
    elif opc == 4:
        conta.ver_extrato()
    elif opc == 5:
        print('Finalizando programa.')
        break
    else:
        print('Numero invalido, digite novamente..')