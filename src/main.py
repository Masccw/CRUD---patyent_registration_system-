# Criacao de lista com 1 elemento senao ela nao existe
lista = []


# Funcao Adicionar
def Adicionar(nome):
        lista.append(nome)

# Funcao Listar
def  Listar():
    if lista:
        for i, nome in enumerate(lista):
            print(f"[{i}] - {nome}]") 
    else:
        print("Lista nao existe!")


#Rodar o programa
while True:
    nome = input("Digite o nome: ")
    if nome == "":break
    Adicionar(nome)
    
Listar()