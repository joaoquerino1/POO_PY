from pessoa import Pessoa

class Aluno(Pessoa):
    def __init__(self, nome = "", idade = 0, curso = "", turma = ""):
        super().__init__(nome, idade)
        self.curso = curso
        self.turma = turma

    def fazerMatricula(self):
        print (f"{self.nome} acabou de fazer sua matricula no curso {self.curso} na turma {self.turma}")