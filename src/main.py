# Biblioteca datetime para marca o horario da internacao
from datetime import datetime as dt

# Criacao de lista com 1 elemento senao ela nao existe
lista = [{}]

# Funcao Adicionar
def Adicionar(nome):
        lista.append(nome)

# Funcao Listar
def  Listar():
    if lista:
        for i, pessoa in enumerate(lista):
            print(f"[{i}] - {pessoa}]") 
    else:
        print("Lista nao existe!")


#Rodar o programa
while True:
    print("\na - Adicionar novo paciente\nl - Listar pacientes\ns - sair")
    opcao = input(str("\nDigite a opcao: ")).lower()

    if opcao == "a":
        nomePaciente = input(str(("Digite o nome do paciente: ")))
        Adicionar(nomePaciente)
    
    elif opcao == "l":
         Listar()

    elif opcao == "s":break

    else:
         print("Opcao invalida!")