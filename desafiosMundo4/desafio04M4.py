from rich.panel import Panel
from rich.console import Console
from rich import print

class Gamer:
    
    def __init__(self, nome, nick):
        self.nome = nome
        self.nick = f'Jogador <{nick}>'
        self.jogos = []
      
        
    def add_favoritos(self, jogo):
        self.jogos.append(jogo)
        self.jogos.sort()
        
    def ficha(self):
        conteudo = f'\nNome real: [black on blue] {self.nome} [/]'
        conteudo += f'\nJogos favoritos:\n'
        for num, jogo in enumerate(self.jogos):
            conteudo += f"\n:video_game: [blue]{jogo}[/]"
        painel = Panel(conteudo.center(30), title=self.nick, width = 30)
        console = Console()
        console.print(painel)
        
jogador1 = Gamer('João Victor', 'Balmunng')
jogador1.add_favoritos('CS2')
jogador1.add_favoritos('Tibia')
jogador1.add_favoritos('Barony')
jogador1.ficha()
        
        