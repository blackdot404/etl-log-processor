import os

from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()


def insert_df_to_sql(df):
    print('\U0001f5c4 [4/4] DATABASE: Importando dados via SQLAlchemy(ORM)...')

    server = os.getenv('DB_SERVER') or '127.0.0.1'
    database = os.getenv('DB_NAME') or 'base_dados'
    username = os.getenv('DB_USER') or 'usuario_leitura'
    password = os.getenv('DB_PASS') or 'senha_padrao'
    table_name = os.getenv('DB_TABLE') or 'tb_dados_exemplo'
    schema_name = os.getenv('DB_SCHEMA') or 'dbo'

    # URL de conexão
    conn_url = f'mssql+pyodbc://{username}:{password}@{server}/{database}?driver=ODBC+Driver+17+for+SQL+Server'

    try:
        engine = create_engine(conn_url, fast_executemany=True)

        df.to_sql(
            name=table_name,
            schema=schema_name,
            con=engine,
            if_exists='append',
            index=False,
        )
        print(f"\u2714\ufe0f SUCESSO: Dados importados na tabela: '{table_name}'.")

    except Exception as e:
        print(f'\u274c ERROR: durante a importação para o banco de dados: \n{e}')
