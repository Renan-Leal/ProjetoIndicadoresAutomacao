def separar_por_loja(lojas_df, vendas_df):
    dic_tabelas_lojas = {}
    for loja in lojas_df['Loja']:
        dic_tabelas_lojas[loja] = vendas_df.loc[vendas_df['Loja'] == loja, :]
    return dic_tabelas_lojas


def organizar_pastas(caminho_backup, dia_indicador, dic_tabelas_lojas):
    from pathlib import Path
    caminho_backup = Path(caminho_backup)
    arquivos = caminho_backup.iterdir()
    lista_lojas = [arquivo.name for arquivo in arquivos]
    for loja in dic_tabelas_lojas:
        if loja not in lista_lojas:
            Path(caminho_backup / f'{loja}').mkdir()
            arquivo_nome = f'{dia_indicador.month}_{dia_indicador.day}_{loja}.xlsx'
            dic_tabelas_lojas[loja].to_excel(Path(caminho_backup / loja / arquivo_nome))
