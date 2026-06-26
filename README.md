# climate-data-flow


## Pipeline ETL de Dados Meteorológicos

Este projeto é uma implementação prática de um pipeline de **Engenharia de Dados** de ponta a ponta, projetado para extrair, transformar e carregar dados meteorológicos de uma API externa.

### 🚀 Tecnologias Utilizadas
* **Linguagem:** Python 3.12+
* **Orquestração:** Apache Airflow
* **Infraestrutura:** Docker & Docker Compose
* **Banco de Dados:** PostgreSQL
* **Processamento:** Pandas
* **Gerenciamento de Pacotes:** uv

### 🏗️ Arquitetura do Projeto
O pipeline segue o fluxo **ETL (Extract, Transform, Load)**:
1. **Extract:** Coleta de dados via API do *OpenWeather*.
2. **Transform:** Limpeza e normalização dos dados utilizando *Pandas*.
3. **Load:** Ingestão dos dados processados em um banco de dados *PostgreSQL*.

### 🛠️ Como Executar

#### Pré-requisitos
- Docker Desktop instalado.
- Python 3.12+.
- `uv` instalado (gerenciador de pacotes).

#### Configuração
1. Clone o repositório.
2. Crie um arquivo `.env` na pasta `config` com suas variáveis de ambiente (API Key).
3. Inicie os serviços do projeto utilizando o Docker Compose:
   bash
   docker-compose up -d
   
4. Acesse o **Airflow** em `http://localhost:8080` para orquestrar a execução da DAG `weather_pipeline`.

### 📂 Estrutura do Repositório
- `src/`: Scripts Python de extração, transformação e carga.
- `dags/`: Arquivos de configuração do Airflow.
- `config/`: Configurações e variáveis de ambiente.
- `notebooks/`: Análises exploratórias dos dados.

---

*Dica: Lembre-se de não subir o arquivo `.env` ou a pasta `data` para o GitHub, utilizando o `.gitignore` conforme mencionado no vídeo (1:07:50).* 
