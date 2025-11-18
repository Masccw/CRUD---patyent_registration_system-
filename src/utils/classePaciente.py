class Paciente():
    def __init__(self, nome, cpf, datNasc, endereco, dia):
        self.nome = nome
        self.cpf = cpf
        self.datNasc = datNasc
        self.endereco = endereco
        self.dia = dia

    def __str__(self):
        return f"\nNome: {self.nome}\nCPF: {self.cpf}\nData de nascimento: {self.datNasc}\nEndereco: {self.endereco}\nInternado: {self.dia}\n"