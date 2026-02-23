import csv
import os

os.system('cls')

#path_file: str = f'D:/Git-Projetos/Python/JD-Curso_de_Python/Aula-04/Dados/exemplo.csv'
path_file: str = 'Dados/exemplo.csv'
arquivo_csv: list = []

with open(file=path_file, mode='r', encoding='utf-8') as arquivo:
    leitor_csv: csv.DictReader = csv.DictReader(arquivo)
    
    for linha in leitor_csv:
        arquivo_csv.append(linha)

print(f'Arquivo CSV: {arquivo_csv}')