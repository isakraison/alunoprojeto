class Animal:
    def __init__(self,nome):
        self.nome=nome 
    def falar(self):
        print("som do animal")

class Cachorro(Animal):
    def falar(self):
        print("au au!")

class gato(Animal):
    def falar(self):
        print("miau")

        
dog= Cachorro("spayk")
cat=gato("raimundo")

dog.falar()
cat.falar()
