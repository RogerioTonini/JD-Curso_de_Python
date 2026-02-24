### Exercício 5: Detecção de Anomalias em Dados de Transações
# Você está trabalhando em um sistema de detecção de fraude e precisa identificar 
# transações suspeitas. 
# Uma transação é considerada suspeita se o valor for superior ao VALOR DIGITADO,
# ou se ocorrer fora do horário comercial (antes das 9h ou depois das 18h) ou
# for no final de semna. 

import sys

from pathlib import Path
from typing import Any, List, Dict

sys.path.insert(0, str(Path(__file__).parent.parent))

import app.libs.common_functions as cf
import app.libs.data as data
import app.libs.model as model

def validate_input(prompt: str) -> float:
    while True:
        try:
            value: float = float(input(prompt))
            if value <= 0:
                print('Por favor, digite um número positivo.')
                continue
            return value
        except KeyboardInterrupt:
            print('\nEntrada interrompida pelo usuário. Encerrando o programa.')
            exit()
        except ValueError:
            print('Entrada inválida. Por favor, digite um número válido!.')

def main():
    cf.clear_screen()

    valor_limite: float = validate_input(
        'Digite o valor limite para transações suspeitas: '
    )

    caracter_separador: str = ','  # Defina o separador correto do seu arquivo
    data_path: Path = Path('D:/Git-Projetos/Python/JD-Curso_de_Python/dados/')
    file_data_path: Path = Path(data_path / 'aula-03-exerc-05.txt')
    try:
        print(f'--- Iniciando leitura de {file_data_path} ---')
        cabecalho, linhas = model.read_file_v2(
            filepath = file_data_path, 
            separator = caracter_separador
        )
        print(f'Total de registros processados: {len(linhas)}\n')
        print('\n🔍 Analisando transações...')
        ocorrencias: List[Dict[str, Any]] = []
        
        for registro in linhas:
            ocorrencia = data.analyze_transactions(registro, valor_limite, 0, 1)
            if ocorrencia:
                ocorrencias.append(ocorrencia)
        
        # Exibir resultados
        print('\n' + '=' * 70)
        print('RESULTADOS DA ANÁLISE')
        print('=' * 70)
        print(f'\nTotal de transações analisadas: {len(linhas)}')
        print(f'Transações suspeitas encontradas: {len(ocorrencias)}')
        
        if ocorrencias:
            print(f'\n   OCORRÊNCIAS SUSPEITAS:')
            print('-' * 70)
            for i, oc in enumerate(ocorrencias, 1):
                print(
                    f'{i:2d}. {oc["data"]} ({oc["dia_da_semana"]}) '
                    f'às {oc["hora"]} - R$ {oc["valor"]} - '
                    f'{oc["status"]}'
                )
            arquivo_gerado = model.write_occurrences_file(
                ocorrencias,
                data_path
            )
            print(f'\n* * * * *  Processamento concluído!  * * * *')
        else:
            print('\n* *  Nenhuma transação suspeita encontrada! * *')
        print('=' * 70)
    except FileNotFoundError:
        print(f'\n* * * Arquivo não encontrado: {file_data_path} * * *')
    except Exception as e:
        print(f'\n* * * Erro ao processar: {e} * * *')
        import traceback
        traceback.print_exc()


if __name__ == '__main__':
    main()