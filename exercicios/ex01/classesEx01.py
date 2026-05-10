class Pessoa:
    def __init__(self, nome = "", idade = 0):
        self.nome = nome
        self.idade = idade

    def fazerAniversario(self):
        self.idade += 1


class Aluno(Pessoa):
    def __init__(self, nome = "", idade = 0, curso = "", turma = ""):
        super().__init__(nome, idade)
        self.curso = curso
        self.turma = turma

    def fazerMatricula(self):
        print (f"{self.nome} acabou de fazer sua matricula no curso {self.curso} na turma {self.turma}")


class Professor(Pessoa):
    def __init__(self, nome = "", idade = 0, especialidade = "", nivel = ""):
        super().__init__(nome, idade)
        self.especialidade = especialidade
        self.nivel = nivel

    def darAula(self):
        print (f"Professor {self.nome} começou a dar aula.")


class Funcionario(Pessoa):
    def __init__(self, nome = "", idade = 0, cargo = "", setor = ""):
        super().__init__(nome, idade)
        self.cargo = cargo
        self.setor = setor

    def baterPonto(self):
        print(f"{self.nome} acabou de bater o ponto.")