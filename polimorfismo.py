class pato:
    def quack(self):
        print("o pato faz quack")

class pessoa:
    def quack(self):
        print("a pessoa imita o som do pato: quack")

def comer(self):
    print("a pessoa está comendo")

def fazer_quack(obj):
    obj.quack()

p=pato()
h=pessoa()

fazer_quack(p)
fazer_quack(h)

class gravação:
    def quack(self):
        print("som gravado: quack")

class robo:
    def quack(self):
        print("robo:Q-U-A-C-K em som metalico")

objetos=[pato(), pessoa(), gravação(), robo()]

for obj in objetos:
    obj.quack()
