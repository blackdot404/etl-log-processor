def save_csv(df, output_path, num_day):
    print('\U0001f4be [3/4] LOAD: Exportando o arquivo CSV...')

    file_path = f'{output_path}/rel_final_{num_day}.csv'

    df.to_csv(
        file_path,
        index=False,
        sep=';',
        lineterminator='\r\n',
        encoding='utf-8',
    )

    print(f'\U0001f4c1 LOAD: Arquivo salvo em: {file_path}\n')
