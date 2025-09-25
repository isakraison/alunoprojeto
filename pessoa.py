class SerVivo:
    def __init__(self,nome,idade):
        self.nome=nome
        self.idade=idade

    def respirar(self):
        print(f"{self.nome}está respirando...")

    def dormir(self):
        print(f"{self.nome}está dormindo...")

class Pessoa(SerVivo):
    def falar(self,mensagem):
        print("f{self.nome}diz:{mensagem}")

    def andar(self,destino):
        print("f{self.nome}está andando até{destino}")


    def comer(self,comida):
        print("f{self.nome}está comendo{comida}")

    p1=Pessoa ("isac hayson",16)
    p2=Pessoa ("kadu",12)

    p1.respirar()
    p1.dormir()
    p1.falar()
    p1.andar()
    p1.comer()

p1.respirar()
p1.dormir()
 p1.falar()
 p1.andar()
    p1.comer()

    
