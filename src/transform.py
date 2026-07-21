from datetime import datetime, timedelta

import pandas as pd


def transform_data(df):
    print('\u2699\ufe0f [2/4] TRANSFORM: Aplicando regras de negocios...')

    # Configurações do processamento

    # Retira espaço e pontos nas colunas
    df.columns = df.columns.str.replace(' ', '_', regex=False).str.replace(
        '.', '_', regex=False
    )

    column_day = 'DIA'
    column_new = 'DATA_IMPORT'
    column_ref = 'OUTROS'
    column_remove = ['LOGIN']
    column_ignore = ['EXAMPLE']

    # Inserindo nova coluna usando a coluna de referencia
    if column_ref in df.columns:
        target_position = list(df.columns).index(column_ref) + 1
        if column_new not in df.columns:
            df.insert(loc=target_position, column=column_new, value=datetime.now())

    # Removendo colunas
    df = df.drop(columns=column_remove, errors='ignore')

    # Definindo a data para filtra (D-1)
    yday = datetime.now() - timedelta(days=1)
    num_day = yday.day

    df[column_day] = pd.to_numeric(df[column_day], errors='coerce')
    df = df[df[column_day] == num_day]

    if df.empty:
        print(f'\u26a0 AVISO: Nenhuma informação encontrada para o dia {num_day}.')
        return df, num_day

    # Em caso de campos com hífen trocar por 0
    df = df.replace('---', 0)

    # Convertendo colunas hora (HH:MM:SS) para segundos
    converted_columns = 0
    for col in df.columns:
        if col == column_day or col in column_ignore:
            continue

        if df[col].astype(str).str.contains(':', na=False).any():
            col_temp = (
                df[col].astype(str).replace({'0': '00:00:00', '0.0': '00:00:00'})
            )
            try:
                df[col] = (
                    pd
                    .to_timedelta(col_temp)
                    .dt.total_seconds()
                    .fillna(0)
                    .astype(int)
                )
                converted_columns += 1
            except ValueError:
                continue

    print(
        f'\u2714\ufe0f TRANSFORM: Concluido! {converted_columns} colunas processadas com sucesso.'  # noqa: E501
    )

    # Garante que o dia seja um numero inteiro
    df[column_day] = df[column_day].astype(int)

    return df, num_day
