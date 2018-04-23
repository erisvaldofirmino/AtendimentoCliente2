" Criando a classe [Veiculo] "

class Veiculo:

    "Definindo o construtor"
    def __init__(self, placa, marca, modelo):
        self.placa = placa
        self.marca = marca
        self.modelo = modelo

    "Definindo os métodos Setters e Getters"
    def setPlaca(self, placa):
        self.placa = placa

    def setMarca(self, marca):
        self.marca = marca

    def setModelo(self, modelo):
        self.modelo = modelo

    def getPlaca(self):
        return self.placa

    def getMarca(self):
        return self.marca

    def getModelo(self):
        return self.modelo