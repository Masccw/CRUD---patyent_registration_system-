<h1> CRUD---Sistema de Cadastro de Pacientes </h1>

<h2> Projeto CRUD </h2>

<h3> 1. Descrição do Problema </h3>
O Complexo Hospitalar da Universidade de Pernambuco (UPE) realiza milhares de atendimentos e internações todos os anos. Para melhorar o controle das informações e garantir padronização, é necessário um sistema de cadastro de pacientes que permita registrar, visualizar, atualizar e excluir dados de forma organizada e segura.

<h3>2. Objetivo do Sistema</h3>
Desenvolver um CRUD (Create, Read, Update, Delete) para gerenciar dados de pacientes atendidos nas unidades do Complexo Hospitalar. O sistema permitirá cadastrar novos pacientes, listar registros, editar informações e excluir cadastros.

<h2>Funcionalidades</h2>

<h3>3. Funcionalidades CRUD</h3>
Operação	Ação no Sistema	Exemplo

Create (Criar)	Registrar novo paciente no banco de dados	Cadastrar nome, CPF, data de nascimento, endereço etc.

Read (Ler)	Listar e pesquisar pacientes cadastrados	Exibir lista geral ou buscar por CPF/nome

Update (Atualizar)	Editar dados de um paciente existente	Corrigir telefone, endereço ou data de nascimento

Delete (Excluir)	Remover paciente do sistema	Excluir registros duplicados ou desatualizados


<h2> Banco De Dados </h2>

<h3>4. Estrutura de Dados (Tabela Pacientes) </h3>
<Strong>
    Tabela: pacientes
    Campo	Tipo	Descrição
    id_paciente	INT (PK, AUTO_INCREMENT)	Identificador único do paciente
    nome	VARCHAR(100)	Nome completo
    cpf	VARCHAR(14)	CPF do paciente
    data_nascimento	DATE	Data de nascimento
    sexo	ENUM('M', 'F', 'Outro')	Sexo biológico ou informado
    endereco	VARCHAR(150)	Endereço completo
    telefone	VARCHAR(20)	Telefone de contato
</Strong>



<h3>5. Requisitos Técnicos</h3>

• Banco de dados: MySQL
• Linguagem: PYTHON (com MySQL)
• Front-end: HTML, CSS e JavaScript

• Funcionalidades adicionais (opcionais):
  - Validação de CPF antes do cadastro
  - Busca dinâmica por nome
  - Confirmação antes de excluir paciente
  - Mensagens de sucesso/erro nas operações

<h3>6. Benefícios do CRUD de Pacientes</h3>
• Facilita o controle de informações dos atendimentos.
• Evita duplicidade de cadastros e erros de digitação.
• Permite atualizações rápidas e seguras dos dados.
• Cria base sólida para integrar futuramente com módulos de consultas, internações e indicadores.

<h3>7. Conclusão</h3>
O CRUD de Pacientes é a fundação do sistema hospitalar. Com ele, é possível estruturar uma base de dados limpa e consistente, garantindo qualidade e confiabilidade das informações. Esse módulo isolado pode funcionar de forma independente e futuramente ser expandido para incluir outras tabelas (como consultas e procedimentos).



