# -----------------------------------------------------------------------------
# Arquivo: model.py
# Objetivo: Funções para tratamento de arquivos(abertura, leitura, escrita,
# validação, fechamento, etc).
# Autor: Rogerio Tonini - rogerio.tonini@gmail.com
# -----------------------------------------------------------------------------
# Relação de funções:
#  1. read_file(filepath: str, separator: str) 
#     -> Tuple[List[str], List[Dict[str, str]]]: 
#     Lê um arquivo de log ou texto e retorna o cabeçalho e os dados.
#  2. read_file_v2(filepath: str, separator: str) 
#     -> Tuple[List[str], List[Dict[str, str]]]: 
#     Lê um arquivo usando a biblioteca CSV e retorna o cabeçalho e os dados.
# -----------------------------------------------------------------------------

import csv

from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple

def read_file(
    filepath: Path | str,
    separator: str
) -> Tuple[List[str], List[Dict[str, str]]]:
    """
    Lê um arquivo, extensão LOG ou TXT retorna cabeçalho/dados
    Args:
        filepath: Caminho do arquivo de log
        separator: Separador de campos no arquivo
        
    Returns:
        Tupla (cabeçalho, dados)
    """
    filepath = Path(filepath)
    if not filepath.exists():
        raise FileNotFoundError(f'Arquivo não encontrado: {filepath}')

    print(f'Processando: {filepath}\n')
    cabecalho: List[str] = []
    dados: List[Dict[str, str]] = []

    with open(filepath, 'r', encoding='utf-8') as file:
        cabecalho = file.readline().strip().split(separator)    # Primeira linha = cabeçalho
        for line in file:                                       # Demais linhas = dados
            line = line.strip()
            if line:
                campos = line.split(separator)
                registro = dict(zip(cabecalho, campos))
                dados.append(registro)

    print(f'Total de registros processados: {len(dados)}')
    return cabecalho, dados


def read_file_v2(
    filepath: Path | str,
    separator: str
) -> Tuple[List[str], List[Dict[str, str]]]:
    """
    Lê um arquivo, exensão CSV, LOG ou TXT retorna cabeçalho/dados.
    Usa a biblioteca CSV.
    Args:
        filepath: Caminho do arquivo de log
        separator: Separador de campos no arquivo

    Returns:
        Tupla (cabeçalho, dados)
    """
    filepath = Path(filepath)
    if not filepath.exists():
        raise FileNotFoundError(f'Arquivo não encontrado: {filepath}')
    
    print(f'Processando: {filepath}\n')
    dados: List[Dict[str, str]] = []

    with open(filepath, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        cabecalho = list(reader.fieldnames or [])        # Obter cabeçalho
        for row in reader:                               # Ler dados
            dados.append(dict(row))

    print(f'Total de registros processados: {len(dados)}')
    return cabecalho, dados


def write_occurrences_file(
    ocorrencias: List[Dict[str, Any]],
    data_path: Path | str
) -> Path:
    """
    Grava ocorrências suspeitas em arquivo CSV
    Args:
        ocorrencias: Lista de dicionários com ocorrências
        diretorio: Diretório onde salvar o arquivo
    Returns:
        Path do arquivo criado
    Example:
        >>> ocorrencias = [
        ...     {
        ...         'data': '15-01-2024',
        ...         'dia_da_semana': 'sábado',
        ...         'hora': '22:30:00',
        ...         'valor': 6000.00,
        ...         'status': 'SUSPEITO'
        ...     }
        ... ]
        >>> arquivo = write_occurrences_file(ocorrencias, 'dados/')
    """
    # Gerar nome do arquivo com data/hora do processamento
    agora = datetime.now()
    file_name = f'ocorrencias_{agora.strftime('%Y%m%d_%H%M')}.csv'

    # Criar path completo
    directory: Path = Path(data_path)
    file_path: Path = Path(data_path) / file_name

    # Garantir que diretório existe
    directory.mkdir(parents=True, exist_ok=True)

    # Gravar arquivo
    if ocorrencias:
        with open(file_path, 'w', encoding='utf-8', newline='') as file:
            # Definir colunas
            fieldnames = [
                'data',
                'dia_da_semana',
                'hora',
                'valor',
                'status'
            ]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(ocorrencias)
        print(f'\n* * * * *  Arquivo criado: {file_path} * * * * *')
    else:
        print('\n* * *  Nenhuma ocorrência suspeita encontrada!  * * *')
    return file_path
