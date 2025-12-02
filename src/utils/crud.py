# Importando funcoes criadas // Organizacao
from utils.EntradaDados import pedir_cpf,pedir_data_nascimento, Lista

#Puxa Classe Paciente
from utils.classePaciente import Paciente

# Biblioteca para marca o dia que foi inserido
from datetime import datetime as dt

# adicionar paciente // CREATE
class Adicionar:
    #É um método que pertence a uma classe e não a uma instância(objeto) específica dela
    @staticmethod
    def adicionar_paciente():
    
        nomeUsuario = str(input("Digite o nome: ")).title() 
        while nomeUsuario == "":
            nomeUsuario = str(input("Digite o nome: ")).strip().title()

        cpf = pedir_cpf()
        dataNasc = pedir_data_nascimento()
        endereco = str(input("Digite o Endereco: "))
        #Dia da atual da internacao
        dia = dt.now().date()

        #Objeto
        Lista.append(Paciente(nomeUsuario, cpf, dataNasc,  endereco, dia))

        print(f"\nPaciente {nomeUsuario} adicionado com sucesso!\n")

#Listagem de pacientes // READ
class Listar:
    @staticmethod
    def listar_paciente():
        if Lista:
            for i, paciente in enumerate(Lista):
                print(f"\n[{i}] | {paciente}\n") 
        else:
            print("nao existe lista!")

#Atualizar pacientes // UPDATE
class Atualizar:
    @staticmethod
    def atualizar_paciente():
            cpf_alterar = input("Digite o CPF do paciente que deseja alterar(Com ponto e hífen): ")

            print("Somente números inteiros")
    
            for paciente in Lista:
                if cpf_alterar == paciente.cpf: 
                    print(f"Paciente encontrado: {paciente.nome} ")
                    print("\nDeixe em branco para não alterar o campo\n")
                
                    #.strip() remove espaços em branco no início e no fim de uma string.
                    novo_nome = str(input("Digite o novo nome: ")).strip().title()
                    if novo_nome:
                        paciente.nome = novo_nome

                    nova_data = pedir_data_nascimento()
                    if nova_data:
                        paciente.dataNasc = nova_data
                     
                    novo_endereco = str(input("Digite o Endereco: ")).strip()
                    if novo_endereco:
                        paciente.endereco = novo_endereco

                    print("\nPaciente atualizado com sucesso")
                    return
        
            print("Nenhum paciente com esse CPF encontrado")

#Remover pacientes // DELETE
class Remover:
    @staticmethod
    def remover_paciente():
        cpf_remove = input("Digite o número de CPF do paciente que desseja remover(Com ponto e hífen): ")

        for paciente in Lista:
            if paciente.cpf == cpf_remove:
                Lista.remove(paciente)
                print(f"Paciente {paciente.nome} removido com sucesso")
                return
    
        print("Paciente não encontrado")
