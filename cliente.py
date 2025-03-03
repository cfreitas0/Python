from Principal import conta_bancaria


class Cliente:

    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf


    def sacar(self, valor):
        self.idade -=  valor
        self.nome -= valor

    def depositar(self, din):
        self.nome += din
        self.idade += din





