import time
from src.interface.classes.csv_class_load import CsvProcessor
from datetime import datetime

# Definindo o caminho do arquivo e os parâmetros de filtro
start = time.time()
arquivo_csv = "data/campeonato-brasileiro-gols.csv"
filtro = "clube"
limite = "Vasco"

# Instanciando o objeto CsvProcessor e carregando o arquivo CSV
arquivo_CSV = CsvProcessor(arquivo_csv)
arquivo_CSV.carregar_csv()

# Filtrando os dados
df_filtrado = arquivo_CSV.filtrar_por_(filtro, limite)

if arquivo_CSV.df_filtrado is not None:
    arquivo_CSV.df_filtrado["tipo_de_gol"] = arquivo_CSV.df_filtrado[
        "tipo_de_gol"
    ].fillna("Normal")

# Verificando o conteúdo filtrado (opcional)
print(df_filtrado)

# Gerando horario
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
