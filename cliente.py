" Criando a Classe [Cliente] "

class Cliente:

    "Definindo o construtor"
    def __init__(self, nome, contato, endereco):
        self.nome = nome
        self.contato = contato
        self.endereco = endereco

    "Definindo os métodos Setters e Getters"
    def setNome(self, nome):
        self.nome = nome

    def setContato(self, contato):
        self.contato = contato

    def setEndereco(self, endereco):
        self.endereco = endereco

    def getNome(self):
        return self.nome

    def getContato(self):
        return self.contato

    def getEndereco(self):
        return self.endereco