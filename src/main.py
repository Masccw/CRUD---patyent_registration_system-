# Importa CRUD origin
from utils.crud import Adicionar,Listar, Atualizar, Remover

#Programa rodando
while True: 
    print("---Menu de pacientes---\n1 - Adicionar Paciente\n2 - Listar Pacientes\n3 - Atualizar paciente\n4 - Remover\n5 - Sair")       
    o = input("\nDigite sua opção: ")
    if o == "1":
        Adicionar.adicionar_paciente()
    elif o == "2":
        Listar.listar_paciente()
    elif o == "3":
        Atualizar.atualizar_paciente()
    elif o =="4":
        Remover.remover_paciente()
    elif o == "5":
        print("Finalizando...")
        break
    else: 
        print("Opção inválida. Tente novamente.")