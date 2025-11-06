class peão:
    def reclamar(self):
        print("o peão reclama do patrão")

class entregador:
    def reclamar(self):
        print("o entregador reclama do patrão e dos clientes")



def reclamar(obj):
    obj.reclamar()

p=peão()
e=entregador()

reclamar(p)
reclamar(e)

class zelador:
    def reclamar(self):
        print("zelador limpa reclamando")

class robo:
    def reclamar(self):
        print("robo: PATRÃO BAITOLA em som metalico")

objetos=[peão(), entregador(), zelador(), robo()]

for obj in objetos:
    obj.reclamar()
