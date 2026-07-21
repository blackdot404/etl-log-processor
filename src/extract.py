import sys

import pandas as pd


def read_excel(excel_path):
    print('\n \U0001f680 Iniciando o processamento do pipeline de ETL...\n')
    print('\U0001f4c2 [1/4] EXTRACT: Lendo o arquivo Excel...')
    try:
        df = pd.read_excel(excel_path)
        return df
    except FileNotFoundError:
        print(
            f"\u274c ERROR: O arquivo '{excel_path}' não foi encontrado. Verifique o nome ou o caminho.\n"  # noqa: E501
        )
        sys.exit(1)
