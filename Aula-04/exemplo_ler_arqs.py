import csv
import os

os.system('cls')

path_file: str = f'D:/Git-Projetos/Python/JD-Curso_de_Python/dados/aula-04-dados.csv'
# path_file: str = 'Dados/exemplo.csv'
arquivo_csv: list = []

with open(file=path_file, mode='r', encoding='utf-8') as arquivo:
    try:
        leitor_csv: csv.DictReader = csv.DictReader(arquivo)
        leitor_csv: csv.DictReader = csv.DictReader(arquivo)
    
        for linha in leitor_csv:
            arquivo_csv.append(linha)
    except FileNotFoundError as e:
        print(f'Erro: Arquivo não encontrado. Detalhes: {e}')
    except Exception as e:
        print(f'Erro ao ler o arquivo. Detalhes: {e}')
print(f'Arquivo CSV: {arquivo_csv}')