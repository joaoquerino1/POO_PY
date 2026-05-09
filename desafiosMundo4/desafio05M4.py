from rich import print

class Caneta:
    
    def __init__(self, cor = 'azul'):
        escolha = ''
        match cor.lower().strip():
            case "azul":
                escolha = "[blue]"
            case "vermelho" | "vermelha":
                escolha = "[red]"
            case "verde":
                escolha = "[green]"
            case "amarelo" | "amarela":
                escolha = "[yellow]"
            case _:
                escolha = "[white]"
        self.cor = escolha
        self.tampada = True
        
    def escrever(self, msg):
        if self.tampada:
            print(f":prohibited: A {self.cor}caneta[/] está tampada!")
        else:
            print(f"{self.cor}{msg}[/]")
        
    def quebrar_linha(self, qtd):
        print("\n" * qtd, end='')
    
    def tampar(self):
        self.tampada = True
    
    def destampar(self):
        self.tampada = False
    
    
c1 = Caneta("azul")
c2 = Caneta("vermelho")
c3 = Caneta("verde")
c4 = Caneta("amarelo")

c2.destampar()
c2.escrever("Hello people!")