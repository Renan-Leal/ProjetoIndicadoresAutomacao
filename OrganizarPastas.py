from pathlib import Path
class OrganizarPastas():

    def __init__(self):
        pass

    def organizar_pastas(self, caminho_backup, dia_indicador, dic_tabelas_lojas):
        caminho_backup = Path(caminho_backup)
        arquivos = caminho_backup.iterdir()
        lista_lojas = [arquivo.name for arquivo in arquivos]
        for loja in dic_tabelas_lojas:
            if loja not in lista_lojas:
                Path(caminho_backup / f'{loja}').mkdir()
                arquivo_nome = f'{dia_indicador.month}_{dia_indicador.day}_{loja}.xlsx'
                dic_tabelas_lojas[loja].to_excel(Path(caminho_backup / loja / arquivo_nome))