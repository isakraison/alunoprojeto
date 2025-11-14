class Policia:
    def __init__(self,nome:str=None):
        if nome is None:
            nome=input("nome da policia:")
    
        self.nome=nome

    def armamento(self):
         print("tem arma")

 

class Batalhão(Policia):
    def __init__(self,localizaçãodobt:str=None ,numerodobatalhão:str=None, nome:str=None,nome:str=None):
        super().__init__(nome)

        if localizaçãodobt is None:
            localizaçãodobt=input("localização do batalhão:")
        
        if numerodobatalhão is None:
            numerodobatalhão=int(input("numero do batalhão:"))
            self.localizaçãodobt=localizaçãodobt
            self.numerodobatalhão=numerodobatalhão     
        def armamento(self):
            print("tem arma")
class Policiamilitar(Batalhão):
    def __init__(self,patente:str=None,nomedopolicial:str=None,idade:int=None,numerodearma:int=None,sexo:str=None,localizaçãodobt:str=None ,numerodobatalhão:str=None):
   
        if patente is None:
            patente=input("patente do policial:")
        
        if nomedopolicial is None:
            nomedopolicial=input("nome do policial:")
        
        if idade is None:
            idade=int(input("idade do policial:"))
        
        if numerodearma is None:
            numerodearma=int(input("número de arma do policial:"))
        if sexo is None:
            sexo=input("sexo do policial:")

            super().__init__(numerodobatalhão)
            self.patente=patente
            self.nomedopolicial=nomedopolicial
            self.idade=idade
            self.numerodearma=numerodearma
    def armamento(self):
        print("tem arma")


class Presidiario(Policiamilitar):
    def __init__(self,nomedopresidiario:str=None,idade:int=None,crime:str=None,numerodecelula:int=None,numerodevezespreso:int=None,numerodearma:int=None):
      
        if nomedopresidiario is None:
            nomedopresidiario=input("nome do presidiario:")
        
        if idade is None:
            idade=int(input("idade do presidiario:"))
        
        if crime is None:
            crime=input("crime do presidiario:")

        if numerodevezespreso is None:
            numerodevezespreso=int(input("número de vezes que foi preso:"))
        
        if numerodecelula is None:
            numerodecelula=int(input("número da cela do presidiario:"))
            super().__init__(numerodearma)
            self.nomedopresidiario=nomedopresidiario
            self.idade=idade
            self.crime=crime
            self.numerodecelula=numerodecelula
            self.numerodevezespreso=numerodevezespreso
    def armamento(self):
        print("tem arma")
for obj in [Policia(), Batalhão(), Policiamilitar(), Presidiario()]:
    obj.armamento()

p=Policia()
# Bt=Batalhão()
# pm=Policiamilitar()
# psd=Presidiario()
