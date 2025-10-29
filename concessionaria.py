class Veiculo:
    def __init__(self, marca=None,modelo=None):
        self.marca = marca
        self.modelo = modelo

    def ligar(self):
            
        print(f"{self.marca} {self.modelo} está ligado.")
           

    def info(self):
        print(f"Veiculo: {self.marca} or modelo: {self.modelo}")

class Carro(Veiculo):
    def __init__(self, marca=None, modelo=None, portas=None):
        super().__init__(marca, modelo)
        self.portas = portas
    def info(self):
        return f"carro: {self.marca}"

class Moto(Veiculo):
    def __init__(self, marca=None, modelo=None, cilindradas=None):
        super().__init__(marca, modelo)
        self.cilindradas = cilindradas

    def info(self):
     return f"moto: {self}"

carro=Carro("toyota", "corolla", "4")
carro.info()
carro.ligar()

print("-----")
moto1=Moto("honda", "cb500", "500")
moto1.info()
moto1.ligar()

