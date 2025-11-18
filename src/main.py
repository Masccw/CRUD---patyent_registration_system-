# Biblioteca para marca o dia e hora
from datetime import datetime  as dt

# Importando funcoes criadas // Organizacao
from utils.EntradaDados import pedir_cpf,pedir_data_nascimento

# Classe Paciente importada
from utils.classePaciente import Paciente

# Importa CRUD origin
from utils.crud import Adicionar,Listar

#Programa rodando
while True: 
    print("\n1 - Adicionar Paciente\n2 - Listar Pacientes\n3 - Sair")       
    o = input(": ")
    if o == "1":
        Adicionar()
    elif o == "2":
        Listar()
    elif o == "3":break