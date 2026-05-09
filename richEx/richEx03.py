from rich import print
from rich import inspect


class ContaBancaria:
    """
    Cria uma conta bancaria que deixa fazer saques e depositos.
    """
    
    def __init__(self, id, nome, saldo=0):
        self.id = id
        self.titular = nome
        self.saldo = saldo
        
    def __str__(self):
        return f'A conta {self.id} de {self.titular} tem R${self.saldo:,.2f} reais.'
    
    def depositar(self, valor):
        self.saldo += valor
        
    def sacar(self, valor):
        if valor > self.saldo:
            return f'Saque NEGADO de R${valor:,.2f} na conta {self.id}: SALDO INSUFICIENTE.'
        else:    
            self.saldo -= valor
            return f'Saque de R${valor:,.2f} autorizado na conta {self.id}.'
    
c = ContaBancaria(111, 'Joaozin', 800)
inspect(c)