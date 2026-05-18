from abc import ABC, abstractmethod

class Pessoa(ABC):
    def __init__(self, nome = "", idade = 0):
        self.nome = nome
        self.idade = idade

    def fazerAniversario(self):
        self.idade += 1

    @abstractmethod
    def estudar(self):
        pass


class Aluno(Pessoa):
    def __init__(self, nome = "", idade = 0, curso = "", turma = ""):
        super().__init__(nome, idade)
        self.curso = curso
        self.turma = turma

    def fazerMatricula(self):
        print (f"{self.nome} acabou de fazer sua matricula no curso {self.curso} na turma {self.turma}")

    def estudar(self):
        print(f"{self.nome} está estudando para a prova de {self.curso}.")

class Professor(Pessoa):
    def __init__(self, nome = "", idade = 0, especialidade = "", nivel = ""):
        super().__init__(nome, idade)
        self.especialidade = especialidade
        self.nivel = nivel

    def darAula(self):
        print (f"Professor {self.nome} começou a dar aula.")

    def estudar(self):
        print(f"Professor {self.nome} está estudando para preparar a aula de {self.especialidade}.")

class Funcionario(Pessoa):
    def __init__(self, nome = "", idade = 0, cargo = "", setor = ""):
        super().__init__(nome, idade)
        self.cargo = cargo
        self.setor = setor

    def baterPonto(self):
        print(f"{self.nome} acabou de bater o ponto.")

    def estudar(self):
        print(f"{self.nome} está estudando para melhorar suas habilidades no cargo de {self.cargo}.")