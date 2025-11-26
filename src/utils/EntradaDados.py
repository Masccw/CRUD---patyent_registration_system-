from datetime import datetime as dt
from validate_docbr import CPF

def pedir_cpf():
    while True:
        cpf = CPF()
        numero_cpf = input("Digite o CPF: ")
        if cpf.validate(numero_cpf):
            print(f"O CPF {numero_cpf} é válido.")        
        else:
            print(f"O CPF {numero_cpf} é inválido.")
        return numero_cpf


def pedir_data_nascimento():
    while True:
        data = input("Data de nascimento (dd/mm/aaaa): ")
        try:
            return dt.strptime(data, "%d/%m/%Y").date()

        except ValueError:
            print("Formato inválido! Use exatamente dd/mm/aaaa.\n")

