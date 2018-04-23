""" Criando a classe [Categoria] => para selecionar o nivel do cliente e a classificação do veículo"""

class Categoria(object):

    def __init__(self, cliente, veiculo):
        self.cliente = cliente
        self.veiculo = veiculo


    def nivelCliente(self):
        if (self.cliente == 10):

            self.cliente = "VIP"
            return self.cliente

        else:

            self.cliente = "Comum"
            return self.cliente

    def categoriaVeiculo(self):
        if (self.veiculo == "A" or self.veiculo == "a"):

            self.veiculo = "Carro"
            return self.veiculo

        elif (self.veiculo == "B" or self.veiculo == "b"):

            self.veiculo = "Moto"
            return self.veiculo

        elif (self.veiculo == "C" or self.veiculo == "c"):

            self.veiculo = "Autocarga"
            return self.veiculo

        else:
            self.veiculo = "Bike"
            return self.veiculo