#Declaração de Classe

class Gafanhoto:
    """
    Essa classe cria um Gafanhoto(pessoa), que tem nome e idade.
    Para criar uma pessoa, use
    nomedavariavel = Gafanhoto(nome, idade)
    """
    
    def __init__(self, nome='', idade=0): #Método Construtor
        #Atributos de Instancia:
        self.nome = nome
        self.idade = idade
        
    #Métodos de Instancia:
    def aniversario(self):
        self.idade += 1
        
    def __str__(self):#Método para retornar o nome e a idade do gafanhoto, ao passar os valores dos parametros.
        return f'{self.nome} é Gafanhoto, e tem {self.idade} anos.'
    def __getstate__(self):#Método para retornar o estado do objeto.
        return f'Estado: nome = {self.nome}, idade = {self.idade}'
        
pessoa1 = Gafanhoto('João', 22)
print(pessoa1)