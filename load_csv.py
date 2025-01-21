import time
from src.interface.classes.csv_class_load import CsvProcessor
from datetime import datetime

# Definindo o caminho do arquivo e os parâmetros de filtro
start = time.time()
arquivo_csv = "data/campeonato-brasileiro-gols.csv"
filtro_coluna = "clube"
filtro_info = "Vasco"


# Instanciando o objeto CsvProcessor e carregando o arquivo CSV
arquivo_CSV = CsvProcessor(arquivo_csv)
arquivo_CSV.carregar_csv()

# Filtrando os dados
df_filtrado = arquivo_CSV.filtrar_por_clube(filtro_coluna, filtro_info)


# Modificação para corrigir valores nulos sem usar metodos da classe.
if arquivo_CSV.df_filtrado is not None:
    arquivo_CSV.df_filtrado["tipo_de_gol"] = arquivo_CSV.df_filtrado[
        "tipo_de_gol"
    ].fillna("Normal")

# Verificando o conteúdo filtrado (opcional)

print(df_filtrado.head(10))

# Gerando horario
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

# Salvando os dados filtrados em um novo arquivo
arquivo_CSV.salvar_dados(f"data/Gols-Vasco-Brasileirão-{timestamp}.csv")

# Medindo o tempo de execução
stop = time.time()
print(f"Tempo de execução: {stop - start} segundos")
