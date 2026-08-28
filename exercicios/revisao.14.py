class Contador:
    def __init__(self):
        self.contagem = 0
    def somar(self):
        self.contagem += 1

    def zerar(self):
        self.contagem = 0

    def subtrair(self):
        self.contagem -=1 
        
    def mostrar(self):
            print(f"Contagem: {self.contagem}")
c = Contador()
    
while True:
    print("-" * 25)
    c.mostrar()
    print("-" * 25)
    print("[ 1 ] Somar")
    print("[ 2 ] Subtrair")
    print("[ 3 ] Zerar")
    print("[ 4 ] Sair")
    print("-" * 25)  
    while True:
        c.mostrar()
        opc=int(input('Sua opcao: '))
        if opc == 1:
            c.somar()
        elif opc ==2:
            c.subtrair()
        elif opc ==3:
            c.zerar()
        elif opc ==4:
            print("Encerrando...")
            break
        else:
            print("Opção inválida! Tente novamente.")
                
    c = Contador()

    c.somar()
    c.somar()
    c.somar()
    c.somar()
    c.somar()

    c.mostrar()