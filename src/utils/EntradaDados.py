from datetime import datetime as dt

def pedir_cpf():
    while True:
        try:
            cpf = int(input("Digite o CPF: "))
            return cpf
        except ValueError:
            print("Digite apenas números inteiros.\n")


def pedir_data_nascimento():
    while True:
        data = input("Data de nascimento (dd/mm/aaaa): ")
        try:
            return dt.strptime(data, "%d/%m/%Y").date()

        except ValueError:
            print("Formato inválido! Use exatamente dd/mm/aaaa.\n")
