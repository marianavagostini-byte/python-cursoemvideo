class CofreInteligente:
    def __init__(self, senha: str):
        self.senha = senha
        self.aberto = False
        self.saldo = 0.0

    def abrir(self, senha_informada: str):
        if senha_informada == self.senha:
            self.aberto = True
            print("Cofre aberto com sucesso!")
        else:
            print("Senha incorreta! O cofre continua trancado.")

    def fechar(self):
        self.aberto = False
        print("Cofre trancado.")

    def guardar(self, valor: float):
        if not self.aberto:
            print("Operação negada: o cofre está trancado.")
            return

        if valor > 0:
            self.saldo += valor
            print(f"Guardado R$ {valor:.2f} com sucesso.")
        else:
            print("Valor inválido para guardar.")

    def consultar_saldo(self):
        if not self.aberto:
            print("Operação negada: o cofre está trancado.")
        else:
            print(f"Saldo no cofre: R$ {self.saldo:.2f}")

cofre = CofreInteligente("1234")
cofre.guardar(50.0)
cofre.abrir("1234")
cofre.guardar(150.0)
cofre.consultar_saldo()
cofre.fechar()