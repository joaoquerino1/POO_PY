from rich import print
from rich.panel import Panel

class Produto:
    
    def __init__(self, nome, preço):
        
        self.nome = nome
        self.preço = preço
        
    def __str__(self):
        return f'O produto {self.nome} custa R${self.preço:,.2f}'
    
    def etiqueta(self):
        conteudo = f'{self.nome.center(30, '=')}'
        conteudo += f"{'-' * 30}"
        preçoF = f"R${self.preço:,.2f}"
        conteudo += f'{preçoF.center(30, '.')}'
        etiqueta = Panel(conteudo, title="Produto", width=34)
        print(etiqueta)
        
p1 = Produto('Iphone', 5_000_85)
p1.etiqueta()