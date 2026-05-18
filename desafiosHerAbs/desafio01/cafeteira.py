from abc import ABC, abstractmethod

class BebidaQuente(ABC):

    def preparar(self):

        print("--- Preparando a bebida quente ---")
        self.ferver_agua()
        self.misturar()
        self.servir()
        print("--- Bebida quente pronta! ---")

    def ferver_agua(self):
        print("1. Fervendo água a 100ºC.")

    @abstractmethod
    def misturar(self):
        print("2. Misturando os ingredientes da bebida quente.")

    @abstractmethod
    def servir(self):
        print("3. Servindo a bebida quente.")


class Cafe(BebidaQuente):
    
    def misturar(self):
        print("2. Misturando café em pó com água fervente.")

    def servir(self):
        print("3. Servindo o café quente.")

class Cha(BebidaQuente):
    
    def misturar(self):
        print("2. Misturando chá de saquinho com água fervente.")

    def servir(self):
        print("3. Servindo o chá quente com canela e limão na caneca.")

class LeiteQuente(BebidaQuente):
    
    def misturar(self):
        print("2. Passando vapor pressurizado pelo bico do leite.")

    def servir(self):
        print("3. Servindo o leite quente ja com café.")