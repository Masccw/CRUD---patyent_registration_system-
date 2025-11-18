# Importando funcoes criadas // Organizacao
from utils.EntradaDados import pedir_cpf,pedir_data_nascimento

#Puxa Classe Paciente
from utils.classePaciente import Paciente

# Biblioteca para marca o dia que foi inserido
from datetime import datetime as dt

Lista = []

# adicionar paciente // CREATE

def Adicionar():
    nomeUsuario = input("Digite o nome: ").title()
    cpf = pedir_cpf()
    dataNasc = pedir_data_nascimento()
    endereco = input("Digite o Endereco: ")

    #Dia da atual da internacao
    dia = dt.now().date()

    #Objeto
    p1 = Paciente(nomeUsuario, cpf, dataNasc, endereco, dia)
    Lista.append(p1)



#Listagem de pacientes // READ
def Listar():
    if Lista:
        for i, paciente in enumerate(Lista):
            print(f"\n[{i}] | {paciente}\n")
    else:
        print("nao existe lista!")