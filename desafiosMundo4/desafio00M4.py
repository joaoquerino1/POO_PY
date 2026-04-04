from rich import print
from rich import inspect

class Funcionario:
    #Atributo de classe
    empresa = 'Botinha Enterprises'
    
    def __init__(self, nome, setor, cargo): #Método Construtor
        
        self.nome = nome
        self.setor = setor
        self.cargo = cargo
        
    def apresentaçao(self): #Método de Apresentação, que retorna o texto com os atributos passados nos parâmetros, quando é chamada a classe.
        return f'Olá! Meu nome é [blue]{self.nome}[/blue], sou do setor [red]{self.setor}[/red] e meu cargo é o de {self.cargo} na empresa [yellow]{Funcionario.empresa}[/yellow]'
        
c1 = Funcionario('RoseMary', 'Administrativo', 'Recursos Humanos', )
print(c1.apresentaçao())