class Moto:
    def __init__(self, marca, modelo, ano, cor):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.velocidade = 0

    def acelerar(self, valor1):
        self.velocidade += valor1
        print(f"Acelerou para {self.velocidade} km/h")

    def frear(self, valor1):
        self.velocidade -= valor1
        if self.velocidade < 0:
            self.velocidade = 0
        print(f"Reduziu para {self.velocidade} km/h")

    def mostrar(self):
        print(f"{self.marca} {self.modelo}, {self.ano}, {self.cor}, velocidade: {self.velocidade} km/h")


moto1 = Moto("Honda", "africa twin", 2025, "vermelha")
moto1.mostrar()
moto1.acelerar(200)
moto1.frear(60)
moto1.mostrar()
