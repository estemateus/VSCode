# -- APLICAÇÃO DE BANCO DE DADOS COM PYTHON --

# SGBD -> Sistemas de Gerenciamento de Banco de Dados
# Modelo CRUD -> Create, Read, Update, Delete
# Create -> Inserção de novos registros
# Read -> Recuperação de informações
# Update -> Modificação de registros existentes
# Delete -> Exclusão de dados

# Python é uma linguagem muito utilizada para interagir com SGBD
# Ela faz isso por meio de bibliotecas como sqlite3
# Essa biblioteca segue o modelo CRUD
# Python simplifica a implementação dessas operações CRUD

# Linguagem SQL -> Structured Query Language | Linguagem de Consulta Estruturada
# As instruções em SQL podem ser agrupadas em 3 categorias principais: DDL | DML | DCL

# DDL -> Data Definition Language | Liguagem de Definição de Dados
# Essas instruções se concentram na estrutura do banco de dados, permitindo a criação, modificação e exclusão de bancos de dados e tabelas
# Exemplos de comandos: CREATE (Cria tabelas); ALTER (Modifica a estrutura); DROP (Exclui tabelas ou bancos de dados

# DML -> Data Manipulation Language | Linguagem de Manipulação de Dados
# Essas instruções são usadas para recuperar, atualizar, inserir e excluir dados no banco de dados
# Exemplos de comandos: SELECT (Recupera dados); INSERT (Adiciona novos registros); UPDATE (Modifica registros existentes); DELETE (Exclui registros)

# DCL -> Data Control Language | Linguagem de Controle de Dados
# Essas instruções lidam com a com a segurança e a autorização de acesso aos dados no banco de dados
# Exemplos de comandos: GRANT (Concede privilégios); REVOKE (Revoga privilégios)

# Além disso, o SQL também oferece funcionalidades avançadas, como agregações, junções, subconsultas e transações
# Elas viabilizam consultas complexas e a manipulação eficaz de dados
# A flexibilidade do SQL o torna uma linguagem poderosa para trabalhar com bancos de dados relacionais, independente do SGBD
# A base comum permite que os desenvolvedores escrevam consultas portáteis que funcionam em múltiplas plataformas

# -- CONEXÃO COM BANCO DE DADOS --

# RDBMS -> Sistema Gerenciador de Banco de Dados Relacional
# ODBC -> Open Database Connectivity | Conectividade Aberta de Banco de Dados
# JDBC -> Java Database Connectivity | Conectividade em Java de Banco de Dados
# API -> Interface de Programação de Aplicativos
# PEP 249 -> Python Database API Specification v2.0
# Driver -> Software responsável por traduzir as chamadas ODBC e JBDC para a linguagem compreendida pelo RDBMS

# Ao desenvolver uma aplicação em uma linguagem que precisa interagir com um RDBMS, é preciso estabelecer uma conexão entre esses dois processos.
# Estabelecida a conxão, podemos enviar comandos SQL para realizar operações no banco de dados
# Para viabilizar essa comunicação entre a linguagem e o RDBMS, usamos ODBC e JDBC
# Ambos oferecem uma maneira padronizada de os programadores acessarem recursos do banco de dados a partir de uma API
# Uma das grandes vantagens dessas tecnologias é a possibilidade de que uma aplicação acesse diferentes SGDBs sem ter que recompilar código
# Isso se torna viável pois a comunicação direta com o RDBMS é realizada pelo Driver

# Em Python usamos bibliotecas específicas que incorporam drivers de fornecedores para se comunicar com um RDBMS
# Isso permite a conexão e a execução de comandos SQL no banco de dados

# O PEP 249 estabelece regras que os fornecedores devem seguir ao criar módulos para acessar o banco de dados
# Uma delas é que todos precisam implementar um método chamado "connect(parameters...)" para conceber a conexão com o banco
# Isso facilita a alteração do banco de dados, pois apenas os parâmetros de conexão precisam ser ajustados, sem a necessidade de modificar o código

# SQLite -> Biblioteca de banco de dados escrita em C que oferece um mecanismo SQL completo, compacto e de alta confiabilidade
# O SQLite opera sem a necessidade de um servidor separado, diferentemente da maioria dos BDs SQL
# Ele lê e escreve diretamente em  arquivos de disco
# É um banco de dados completo, contendo tabelas, índicies, triggers e visualizações e é armazenado em um único arquivo no sistema de arquivos.
# Para Python possui um módulo integrado chamado sqlite3, que permite a interação com o mecanismo do banco de dados SQLite

# -----------------------------------------------

# -- CRIANDO UM BANCO DE DADOS

import sqlite3 # Importando o módulo sqlite3

#1. Conectar ao banco de dados (ou criar um novo)
conn = sqlite3.connect("exemplo.db")

#2. Criar um objeto cursor
cursor = conn.cursor()

#3. Definir o comando SQL para criar a tabela
create_table = '''
CREATE TABLE IF NOT EXISTS Produtos (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    preco REAL NOT NULL,
    estoque INTEGER
);
'''

#4. Executar o comando SQL para criar a tabela
cursor.execute(create_table)

#5. Confirmar as alterações
conn.commit()

#6. Fechar a conexão
conn.close()

