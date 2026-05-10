from rich import print, inspect
from classesEx01 import Pessoa, Aluno, Professor, Funcionario

def main():
    a1 = Aluno("João", 23, "Analise e Desenvolvimento de Sistemas", "EAD Unicesumar")
    a1.fazerAniversario()
    a1.fazerMatricula()
    #inspect(a1, methods=True)

    p1 = Professor("Gustavo", 35, "Programação", "Mestrado")
    p1.fazerAniversario()
    p1.darAula()

    #inspect(p1, methods=True)

    f1 = Funcionario("Maria", 28, "Secretária", "Administrativo")
    f1.fazerAniversario()
    f1.baterPonto()
    #inspect(f1, methods=True)

if __name__ == "__main__":
    main()
    