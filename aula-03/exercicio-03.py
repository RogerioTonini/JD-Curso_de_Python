### Exercício 3: Filtragem de Logs por Severidade
# Você está analisando logs de uma aplicação e precisa filtrar mensagens  com severidade 'ERROR'. Dado um registro de log 
# em formato de dicionário como `log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}`.
# Escreva um programa que imprima a mensagem se a severidade for 'ERROR'.
import os

os.system('cls' if os.name == 'nt' else 'clear')

# Exemplo de registro de log
# log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}
arquivo_log: list = []
log_file_path: str = f'D:/Git-Projetos/Python/JD-Curso_de_Python/dados/aula-03-arq-log.txt'

with open(log_file_path, 'r', encoding='utf-8') as file:
    print(f'--- Iniciando leitura de {log_file_path} ---')

    try:
        for line in file:
            # .strip() remove espaços em branco e a quebra de linha (\n) do final
            line = line.strip()
            if line:
                # Converte a linha em um dicionário
                campos = line.split(',')
                log = {
                    'timestamp': campos[0],
                    'level': campos[1],
                    'message': campos[2]
                }
                arquivo_log.append(log)
    except FileNotFoundError:
        print(f'Erro: O arquivo {log_file_path} não foi encontrado.')
    except Exception as e:
        print(f'Ocorreu um erro: {e}')

print('O arquivo de log possui: {len(arquivo_log)} registros. Seu conteúdo:\n')
print(f'{arquivo_log}: \n')
print('Os registros de erros ocorreram em:\n')
for log in arquivo_log:
    if log['level'] == 'ERROR':
        print(f"Timestamp: {log['timestamp']} - Message: {log['message']}")
print()
