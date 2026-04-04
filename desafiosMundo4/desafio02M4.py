from rich.panel import Panel

class Churrasco:
    # Atributos de Classe
    consumo_padrao = 0.400  # Cada pessoa consome em média 400g de carne
    preco_kg = 82.40  # Cada kg de carne custa R$82.40

    def __init__(self, titulo, quantidade):
        self.titulo = titulo
        self.participantes = quantidade

    def __str__(self):
        return f"Esse é {self.titulo} com {self.participantes} pessoas participando."

    def calculo_qtd_carne(self) -> float:
        return self.participantes * self.__class__.consumo_padrao

    def calculo_custo_total(self) -> float:
        return self.calculo_qtd_carne() * self.__class__.preco_kg

    def calculo_custo_indv(self) -> float:
        return self.calculo_custo_total() / self.participantes

    def analisar(self):
        conteudo = f"\nAnalisando [green]{self.titulo}[/green] com {self.participantes} convidados."
        conteudo += f"\nCada participante comerá {self.__class__.consumo_padrao:.3f} kg e cada kg custa R${self.__class__.preco_kg:,.2f}"
        conteudo += f"\nRecomendo comprar {self.calculo_qtd_carne():.1f} kg de carne"  # Arredondado para 1 casa
        conteudo += f"\nO custo total será de R${self.calculo_custo_total():,.2f}"
        conteudo += f"\nCada pessoa pagará R${self.calculo_custo_indv():,.2f} para ajudar"
        painel = Panel(conteudo, title = self.titulo)
        print(painel)

# Testes
c1 = Churrasco('Churrasco da Yas', 10)
c2 = Churrasco('Aniversario da Yas <3', 15)
c1.analisar()
c2.analisar()
