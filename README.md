

# 🌦️ Climate Data Flow: Pipeline ETL Meteorológico
O objetivo deste projeto é construir um pipeline **ETL (Extract, Transform, Load)** completo que coleta dados climáticos em tempo real, processa-os e os armazena de forma estruturada para análise.

O projeto foca não apenas no código de processamento, mas também na **infraestrutura como código** e na **orquestração** profissional de tarefas.

## 🏗️ Arquitetura e Fluxo de Dados

O pipeline segue um fluxo robusto dividido em três etapas principais:

1.  **Extração (Extract):** Consumo de dados climáticos da cidade de São Paulo via **API OpenWeather** em formato JSON.
2.  **Transformação (Transform):** Utilização do **Pandas** para:
    *   Normalizar colunas aninhadas (JSON para tabular).
    *   Limpeza de dados e remoção de colunas desnecessárias (ex: *weather*, *icon*, *sys_type*).
    *   Renomeação de colunas para padrões de banco de dados (removendo pontos e espaços).
    *   **Conversão de fuso horário** para `America/Sao_Paulo` nos campos de data e hora.
3.  **Carga (Load):** Ingestão dos dados processados em um banco **PostgreSQL** utilizando **SQLAlchemy**, garantindo a persistência histórica através do modo *append*.

## 🚀 Tecnologias e Ferramentas

*   **Linguagem:** Python 3.12+.
*   **Gerenciamento de Pacotes:** `uv` (alternativa extremamente rápida ao pip/poetry).
*   **Orquestração:** **Apache Airflow 2.10+** utilizando a moderna **TaskFlow API** (@dag e @task).
*   **Infraestrutura:** **Docker & Docker Compose** para conteinerização de todos os serviços (Airflow, Postgres, Redis).
*   **Banco de Dados:** PostgreSQL 14.
*   **Bibliotecas Python Principais:** `pandas`, `sqlalchemy`, `requests`, `python-dotenv`, `psycopg2-binary`.

## 📂 Estrutura do Repositório

```text
├── config/          # Arquivos .env e configurações de ambiente
├── dags/            # Definição do pipeline (DAG) do Airflow
├── notebooks/       # Análise exploratória inicial dos dados (Jupyter)
├── src/             # Scripts Python modulares (Extract, Transform, Load)
├── logs/            # Logs de execução do Airflow (gerado automaticamente)
├── docker-compose.yaml # Orquestração dos containers
└── pyproject.toml   # Gerenciamento de dependências via uv
```

## 🛠️ Como Executar

### Pré-requisitos
*   **Docker Desktop** instalado.
*   **Python 3.12+** e o gerenciador **uv**.
*   Chave de API do [OpenWeather](https://openweathermap.org/api).
*   *Usuários Windows:* Recomendado uso do **WSL2** para melhor compatibilidade com o Docker e Airflow.

### Passo a Passo

1.  **Clonagem e Ambiente:**
    ```bash
    git clone https://github.com/seu-usuario/climate-data-flow.git
    cd climate-data-flow
    uv venv && source .venv/bin/activate  # Inicia ambiente virtual com uv
    ```

2.  **Configuração de Variáveis:**
    Crie um arquivo `.env` na pasta `config/` seguindo o modelo:
    ```env
    API_KEY=sua_chave_aqui
    DB_USER=seu_usuario
    DB_PASSWORD=sua_senha
    DB_NAME=weather_data
    ```

3.  **Subindo a Infraestrutura:**
    ```bash
    docker-compose up -d
    ```
    *Isso iniciará o Airflow (Webserver, Scheduler, Worker) e o banco PostgreSQL.*

4.  **Acesso:**
    *   **Airflow UI:** `http://localhost:8080` (Login padrão: `airflow` / `airflow`).
    *   Ative a DAG `YouTube_weather_pipeline` para iniciar a execução agendada (padrão: a cada hora).

## 📈 Monitoramento e Resultados
É possível validar a ingestão dos dados acessando o banco via terminal ou ferramentas como **PGAdmin**. O pipeline garante que, mesmo em múltiplas execuções, os dados sejam anexados corretamente sem duplicar a estrutura da tabela.

