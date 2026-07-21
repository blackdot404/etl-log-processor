from database import insert_df_to_sql
from extract import read_excel
from load import save_csv
from transform import transform_data


def run_pipeline():
    excel_path = './data/raw/data_example.xlsx'
    output_path = './data/processed'

    # 1. Etapa de extração
    df_raw = read_excel(excel_path)

    # 2. Etapa de tratamento(seguindo regra de negocio)
    df_cleaned, num_day = transform_data(df_raw)

    if not df_cleaned.empty:
        # 3. Etapa de geração do arquivo final
        save_csv(df_cleaned, output_path, num_day)

        # 4. Etapa de importação no banco de dados
        insert_df_to_sql(df_cleaned)
    else:
        print(
            '\U0001f6d1 ERROR: Processo interrompido com segurança (nenhum CSV vazio foi gerado).\n'  # noqa: E501
        )


if __name__ == '__main__':
    run_pipeline()
