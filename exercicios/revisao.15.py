class Banco:
    def __init__(self,nome:str):
        self.nome=nome
        self.saldo_inicial=0.0
        self.extrato=[]
        
    def depositar(self,deposito=0):
        if deposito > 0:
             self.saldo_inicial +=deposito
             self.extrato.append(f"Deposito: R$ {deposito:.2f} , realizado com sucesso !!")
        else:
            print('ERRO!! Deposito invalido.')
    def sacar(self,saque):
        if saque > 0 and saque <= self.saldo_inicial:
            self.saldo_inicial -= saque
            self.extrato.append(f"Saque: R$ {saque:.2f}")
            print("Saque realizado com sucesso!")
        else:
            print("Operação recusada: saldo insuficiente ou valor inválido.")
            
    def ver_saldo(self):
        print(f"Titular: {self.nome} | Saldo atual: R$ {self.saldo_inicial:.2f}")
        
    def ver_extrato(self):
        print(f"--- Extrato de {self.nome} ---")
        if not self.extrato:
            print("Não há movimentações.")
        else:
            for item in self.extrato:
                print(item)
        print(f"Saldo atual: R$ {self.saldo_inicial:.2f}")
            
nome_cliente=str(input("Nome do titular: "))
conta= Banco(nome_cliente)

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
    if opc==1:
        v = float(input('Valor do deposito: R$ '))
        conta.depositar(v)
    elif opc ==2:
        v= float(input('Valor do saque: R$ '))
        conta.sacar(v)
    elif opc ==3:
        conta.ver_saldo()
    elif opc==4:
        conta.ver_extrato()
    elif opc ==5:
        print('Saindo do banco...')
        break
    else:
        print('Opcao invalida!')
    

