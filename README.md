# 🚀 Automação de ETL: Processamento de Logs para SQL Server

[![Python Version](https://img.shields.io/badge/python-3.14%2B-blue.svg)](https://www.python.org/)
[![Poetry](https://img.shields.io/badge/poetry-package%20manager-cyan)](https://python-poetry.org/)
[![Pandas](https://img.shields.io/badge/pandas-data%20manipulation-150458.svg)](https://pandas.pydata.org/)
[![SQL Server](https://img.shields.io/badge/SQL%20Server-Database-CC292B.svg)](https://www.microsoft.com/sql-server)

## 📌 Sobre o Projeto
Este projeto consiste em um pipeline de Engenharia de Dados (ETL) desenvolvido em Python para automatizar o tratamento de planilhas de log e viabilizar a ingestão eficiente em um banco de dados **SQL Server**. 

O script extrai dados de arquivos Excel, realiza limpeza e transformações complexas (como conversão de formatos de tempo). Além disso, padroniza o *schema* das colunas de forma dinâmica, exporta um arquivo CSV local para auditoria (camada *Staging*) e realiza a inserção direta no banco de dados via rede utilizando abstração ORM.

## 🎯 O Desafio Técnico e a Solução
Durante a integração entre o ambiente de processamento (Linux) e o banco de dados (SQL Server / Windows), surgiram desafios específicos de formatação e performance que foram solucionados neste projeto:

* **Vetorização com Pandas:** A planilha original possuía mais de 40 colunas de tempo no formato `HH:MM:SS`. Para garantir alta performance, a transformação de horas para segundos foi feita utilizando operações vetorizadas do Pandas, evitando loops lentos.
* **Tratamento de Dados Ausentes:** Valores inválidos (como `---`) foram tratados e convertidos para `0`, garantindo a integridade dos tipos numéricos no banco de dados.
* **Padronização de Schema:** Os cabeçalhos originais em Excel possuíam espaços e pontos que quebravam a inserção no SQL Server. Foi implementada uma limpeza via Expressões Regulares (*Regex*) para substituir esses caracteres por *underline* (`_`), garantindo compatibilidade total.
* **Inserção Segura via Rede (Linux -> SQL Server):** Configuração robusta dos drivers Microsoft ODBC 17 no Linux, integrados com SQLAlchemy e `pyodbc`. A conexão utiliza *URL Encoding* para senhas complexas e validação de certificados SSL flexibilizada (`TrustServerCertificate=yes`), eliminando a necessidade de transferir arquivos físicos para o servidor do banco.

## 📁 Estrutura do Repositório

O projeto adota uma arquitetura modular para facilitar a manutenção e escalabilidade:

```text
├── data/
│   ├── data_example/           # Amostra de dados fictícios para teste do script
│   ├── raw/                    # Arquivos brutos antes de serem tratados
│   └── processed/              # Arquivos processados(tratados)
├── src/
│   ├── main.py                 # Orquestrador do pipeline (Entrypoint)
│   ├── extract.py              # Módulo responsável pela leitura do Excel
│   ├── transform.py            # Módulo de limpeza de dados e regras de negócio
│   ├── load.py                 # Módulo de salvamento em disco (Staging CSV)
│   └── database.py             # Módulo de conexão segura e inserção no banco de dados
├── .env.example                # Template de configuração de variáveis de ambiente
├── .gitignore                  # Arquivos ignorados (dados reais, logs, cache, .env)
├── pyproject.toml              # Configurações e dependências (Poetry)
├── poetry.lock                 # Trava de versões das dependências
└── README.md                   # Documentação do projeto
```

> **Nota:** Os dados originais são confidenciais e foram inseridos no `.gitignore`. Para rodar o projeto, utilize o arquivo de testes na pasta `data_example/`.

## 🛠️ Tecnologias Utilizadas
* **Linguagem:** Python
* **Manipulação de Dados:** Pandas, OpenPyXL
* **Gerenciamento de Ambiente:** Poetry, python-dotenv
* **Banco de Dados & ORM:** Microsoft SQL Server, SQLAlchemy, pyodbc
* **Ambiente de Execução:** Linux

## 🚀 Como Executar o Projeto

### 1. Pré-requisitos
* Certifique-se de ter o Python (3.14+) e o [Poetry](https://python-poetry.org/docs/#installation) instalados em sua máquina.
* É obrigatório possuir o pacote `msodbcsql17` (Microsoft ODBC Driver 17 for SQL Server) e `unixodbc-dev` instalados no sistema operacional Linux.

### 2. Configuração do Ambiente Seguro
Duplique o arquivo `.env.example`, renomeie-o para `.env` e insira as credenciais reais do seu banco de dados:
```env
DB_SERVER=seu_servidor_ou_ip
DB_NAME=seu_banco_de_dados
DB_USER=seu_usuario
DB_PASS=sua_senha_super_secreta
```

### 3. Instalação das dependências
Clone este repositório e instale as dependências executando o comando abaixo na raiz do projeto:
```bash
poetry install
```

### 4. Execução do Pipeline
Para iniciar o pipeline, que fará a extração, transformação e a carga direta (via ORM) no banco de dados, execute o módulo principal:
```bash
poetry run python src/main.py
```
O histórico de execução (terminal) exibirá *feedbacks* visuais de progresso e o arquivo processado será gerado automaticamente na pasta `data/processed/`.

---
*Desenvolvido por [Edgar Andrade](https://www.linkedin.com/in/edlimash/)*