class Veiculo:
    def __init__(self, marca: str, modelo: str):
        self.marca = marca
        self.modelo = modelo
        self.ligado = False

    def ligar(self):
        self.ligado = True
        print(f"{self.marca} {self.modelo} ligado.")

    def desligar(self):
        self.ligado = False
        print(f"{self.marca} {self.modelo} desligado.")


class Carro(Veiculo):
    def __init__(self, marca: str, modelo: str, portas: int):
        super().__init__(marca, modelo)
        self.portas = portas

    def abrir_porta(self):
        print(f"Abrindo uma das {self.portas} portas do {self.modelo}.")


class Moto(Veiculo):
    def __init__(self, marca: str, modelo: str, cilindradas: int):
        super().__init__(marca, modelo)
        self.cilindradas = cilindradas

    def empinar(self):
        if self.ligado:
            print(f"{self.modelo} de {self.cilindradas}cc empinando com sucesso!")
        else:
            print(f"Ligue a moto antes de tentar empinar.")


c = Carro("Toyota", "Corolla", 4)
c.ligar()
c.abrir_porta()

m = Moto("Yamaha", "MT-07", 689)
m.empinar()
m.ligar()
m.empinar()