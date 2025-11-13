class Pessoa :
    def __init__(self, nome: str, cpf : str) -> None:
            self.nome = nome
            self.cpf=cpf

    def apresentar(self) -> str:
        return f"Olá, meu nome é {self.nome}."
    
class Aluno(Pessoa):
    def __init__(self, nome=None, matricula= None, cpf=None):
        if cpf is None:
            cpf=input("cpf do aluno:")
        
        if nome is None:
          nome=input("nome do aluno:")
        if matricula is None:
            matricula=input("matricula do aluno:")

        super().__init__(nome,cpf)
        self.matricula= matricula

    def apresentar(self):
        base = super().apresentar()
        return f"{base} e sou aluno {self.matricula} "

class Professor(Aluno):
     def __init__(self, nome=None ,cpf= None , matricula=None, disciplina= None):
      if nome is None:
        nome=input("nome do professor:")
        if matricula is None:
            matricula=input("matricula do professor:")
        if cpf is None:
            cpf=input("cpf do professor:")
        if disciplina is None:
            disciplina=input("disciplina do professor:")
        
        super().__init__(nome, cpf, matricula)
        self.disciplina = disciplina
            

     def apresentar(self) -> str:
        base= super().apresentar()
        return f" Professor {self.nome} CPF: {self.cpf} de {self.disciplina}."
     
p=Pessoa("João", "12345678900")
a=Aluno()
pr=Professor()

print(p.apresentar())
print(a.apresentar())
print(pr.apresentar())
     
# class BolsaMixin:
#     def calcular_bolsa(self) -> float:
#         return 1200.0

# class AlunoBolsista(BolsaMixin, Aluno):
#     def apresentar(self) -> str:
#         base = super().apresentar()
#         return f"{base} e recebo uma bolsa de R$ {self.calcular_bolsa():.2F}"
    
# def apresentar_todos(pessoas: list[Pessoa]) -> list[str]:
#     return [p.apresentar() for p in pessoas]

# def main() -> None:
#     p = Pessoa("João", "12345678900")
#     a = Aluno("Ana","98765432100", "A123")
#     pr = Professor("Carlos","123456789", "Matemática")
#     ab = AlunoBolsista("Beatriz","55566677788","B456")

#     resultados = apresentar_todos([p,a,pr, ab])
#     for r in resultados:
#         print(r)

#     print("",
#           f"isinstance(ab, Pessoa): {isinstance(ab, Pessoa)}",
#           f"isinstance(ab, Aluno): {isinstance(ab, Aluno)}",
#           f"isinstance(ab, BolsaMixin): {isinstance(ab, BolsaMixin)}",
#           sep="\n")

#     print("MRO AlunoBolsista:")
#     for cls in AlunoBolsista.__mro__:
#         print(f" - {cls.__name__}")    

# if __name__ == "__main__":
#     main()