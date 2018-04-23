""" Criando a classe [Servico] esta classe herdará das
    classe [Cliente e Veiculo] suas características"""

"Importando as classes [Cliente e Veiculo]"

from cliente import Cliente
from veiculo import Veiculo

class Servico(Cliente, Veiculo):
    def __init__(self, tipo, hr_entrada, hr_saida, valor, nome, contato, endereco, placa, marca, modelo):
        super().__init__(placa, marca, modelo)
        super().__init__(nome, contato, endereco)


        "Declaracao das variáveis da classe [Servico]"
        self.tipo = tipo
        self.hr_entrada = hr_entrada
        self.hr_saida = hr_saida
        self.valor = valor

    "Na classe filha os métodos Getters e Setter sao usados apenas com os parãmetros da classe local"
    def getTipo(self):
        return self.tipo

    def getHr_Entrada(self):
        return self.hr_entrada

    def getHr_Saida(self):
        return self.hr_saida

    def getValor(self):
        return self.valor

    def setTipo(self, tipo):
        self.tipo = tipo

    def setHr_Entrada(self, hr_entrada):
        self.hr_entrada = hr_entrada

    def setHr_Saida(self, hr_saida):
        self.hr_saida = hr_saida

    def setValor(self, valor):
        self.valor = valor