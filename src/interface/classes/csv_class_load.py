import pandas as pd
import time

start = time.time()


class CsvProcessor:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.df = None
        self.df_filtrado = None

    def carregar_csv(self):
        """Carrega o CSV no dataframe"""
        self.df = pd.read_csv(self.file_path)

    def filtrar_por_clube(self, coluna, atributo):
        """Filtra os dados pela coluna e atributo especificados"""
        self.df_filtrado = self.df[self.df[coluna] == atributo]
        return (
            self.df_filtrado
        )  # Agora retornamos o DataFrame filtrado para uso posterior

    def salvar_dados(self, file_path: str):
        """Salva o DataFrame filtrado ou o original no caminho fornecido"""
        try:
            if self.df_filtrado is not None:
                self.df_filtrado.to_csv(
                    file_path, index=False, encoding="utf-8-sig"
                )
                print(f"Arquivo filtrado salvo em{file_path}")
            else:
                print("Nenhum arquivo foi salvo pois não há modificação")
            return True
        except Exception as e:
            print(f"Erro ao salvar arquivo:{e}")
            return False
