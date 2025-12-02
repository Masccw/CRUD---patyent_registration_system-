from datetime import datetime as dt
from validate_docbr import CPF

# Validar CPF ----
def pedir_cpf():
    cpf = CPF()
    while True:
        numero_cpf = input("Digite o CPF(Com ponto e hífen): ")
        
        if cpf.validate(numero_cpf):
            print(f"O CPF {numero_cpf} é válido.")  
            return numero_cpf      
        else:
            print(f"O CPF {numero_cpf} é inválido. Tente novamente")

# Validar data ----
def pedir_data_nascimento():
    while True:
        data = input("Data de nascimento (dd/mm/aaaa): ")
        if data == "":
            return None
        else:
            try:
                return dt.strptime(data, "%d/%m/%Y").date()

            except ValueError:
                print("Formato inválido! Use exatamente dd/mm/aaaa.\n")

# Lista que guarda pacientes temporariamente ----
Lista = []

