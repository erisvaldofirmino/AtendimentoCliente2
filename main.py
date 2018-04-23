"""Criando o método principal [main.py] para interagir com as demais classes"""

"""Importando as classes necessárias"""

from servico import Servico
from categoria import Categoria

"Variável de controle para implementar a rotina de serviço"

checklist = True

while (checklist):
    Op_Cli = int(input("Nível do cliente [10 VIP] - [00 Comum]: "))
    Op_Veic = input("Categoria do Veículo [A = Carro | B = Moto | Caminhão = C | Bike = D]: ")
    print("\n")

    if (Op_Cli == 10):
        if (Op_Veic == "A" or Op_Veic == "a"):

            Nome        = input("Nome do Cliente: ")
            Contato     = input("Contato do cliente: ")
            Ender       = input("Endereço do cliente: ")
            Placa       = input("Placa do vículo: ")
            Marca       = input("Marca do veículo: ")
            Modelo      = input("Modelo do Veículol: ")
            Tipo        = input("Tipo de lavagem: ")
            Hr_Ent      = input("Hora de entrada: ")
            Hr_Saida    = input("Hora de saída: ")
            Valor       = input("Valor do serviço: ")

            servReal = Servico(Tipo, Hr_Ent, Hr_Saida, Valor, Nome, Contato, Ender, Placa, Marca, Modelo)
            categ = Categoria(Op_Cli, Op_Veic)

            print("\n")
            print("Cliente........: {} | Categoria...: {} | Veículo...: {}".format(servReal.getNome(), categ.nivelCliente(),
                  categ.categoriaVeiculo()))
            print("Contato........: ", servReal.getContato())
            print("Endereço.......: ", servReal.getEndereco())
            print("Placa..........: ", servReal.getPlaca())
            print("Fabricante.....: ", servReal.getMarca())
            print("Modelo.........: ", servReal.getModelo())
            print("Serviço........: ", servReal.getTipo())
            print("Hr de entrada..: ", servReal.getHr_Entrada())
            print("Hr de entrada..: ", servReal.getHr_Saida())
            print("Valor do pago..: ", servReal.getValor())

        else:
            pass
    else:
        checklist = False