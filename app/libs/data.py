# -----------------------------------------------------------------------------
# Arquivo: data.py
# Objetivo: Funções para tratamento de tipos de dados, validação e limpeza.
# Autor: Rogerio Tonini - rogerio.tonini@gmail.com
# -----------------------------------------------------------------------------
# Relação de funções:
#  1. day_of_week(data: datetime) 
#     -> str: 
#     Retorna o nome do dia da semana em português (Brasil) para uma data fornecida.
#  2. convert_to_datetime(data_str: str, hora_str: str) 
#     -> datetime:
#     Converte strings de data e hora para um objeto datetime.
#  3. _detect_and_normalize_hour(hora_str: str)
#     -> tuple[str, str]:
#     Função auxiliar para detectar o formato da hora e normalizar microssegundos.
#  4. is_weekend(data: datetime)
#     -> bool:
#     Verifica se a data é um sábado ou domingo.
#  5. is_outside_business_hours(hora: datetime)
#     -> bool:
#     Verifica se a hora está fora do horário comercial (9h-18h).
#  6. is_high_value(valor: float, limite: float)
#     -> bool:
#     Verifica se o valor excede um limite definido.
#  7. analyze_transactions(registro: Dict[str, str])
#     -> Dict[str, Any] | None:
#     Analisa um registro de transação e retorna um dicionário com detalhes se 
#       for suspeita, ou None caso contrário.
# -----------------------------------------------------------------------------

from datetime import datetime
import re
from typing import Any, Dict, List

def day_of_week(data: datetime) -> str:
    """
    Retorna nome do dia da semana em português (Brasil)
    
    Args:
        data: Objeto datetime
        
    Returns:
        Nome do dia da semana
    """
    dias = [
        'seg',
        'ter',
        'qua',
        'qui',
        'sex',
        'sáb',
        'dom'
    ]
    return dias[data.weekday()]


def convert_to_datetime(date_str: str, hour_str: str) -> datetime:
    """
    Converte strings de data e hora para datetime
    
    Suporta múltiplos formatos com detecção automática de microssegundos
    
    Args:
        date_str: Data como string
        hour_str: Hora como string (suporta 1-6 casas decimais)
        
    Returns:
        Objeto datetime
        
    Raises:
        ValueError: Se formato não reconhecido
    """
    # Formatos de data/hora suportados
    date_formats: list[str] = ['%d/%m/%Y', '%d-%m-%Y', '%Y-%m-%d']
    hour_format, hour_normalized = _detect_and_normalize_hour(hour_str)
    datetime_str = f'{date_str} {hour_normalized}'    # Combinar data e hora
    
    # Tentar todas as combinações de formato de data
    for date_fmt in date_formats:
        format_str = f'{date_fmt} {hour_format}'
        try:
            return datetime.strptime(datetime_str, format_str)
        except ValueError:
            continue
    
    # Se nenhum formato funcionou
    raise ValueError(
        f'Formato de data/hora não reconhecido: {date_str} {hour_str}'
    )


def _detect_and_normalize_hour(hour_str: str) -> tuple[str, str]:
    """
    Detecta o formato da hora e normaliza microssegundos
    
    Args:
        hour_str: Hora como string
        
    Returns:
        Tupla (formato_strptime, hora_normalizada)
        
    Examples:
        >>> _detect_and_normalize_hour('10:30')
        ('%H:%M', '10:30')
        
        >>> _detect_and_normalize_hour('10:30:45')
        ('%H:%M:%S', '10:30:45')
        
        >>> _detect_and_normalize_hour('10:30:45.1')
        ('%H:%M:%S.%f', '10:30:45.100000')
        
        >>> _detect_and_normalize_hour('10:30:45.123456')
        ('%H:%M:%S.%f', '10:30:45.123456')
    """
    # Padrão: HH:MM:SS.ffffff (com 1-6 casas decimais opcionais)
    pattern: str = r'^(\d{2}):(\d{2})(?::(\d{2})(?:\.(\d{1,6}))?)?$'
    match: re.Match | None = re.match(pattern, hour_str.strip())
    
    if not match:
        raise ValueError(f'Formato de hora inválido: {hour_str}')

    hour, minute, second, microsecond = match.groups()

    if second is None:          # Caso 1: HH:MM (sem segundos)
        return '%H:%M', f'{hour}:{minute}'
    elif microsecond is None:   # Caso 2: HH:MM:SS (sem microssegundos)
        return '%H:%M:%S', f'{hour}:{minute}:{second}'
    else:
        # Caso 3: HH:MM:SS.f (com 1-6 casas decimais) - Normalizar para 6 dígitos
        microsecond_normalized = microsecond.ljust(6, '0')
    return '%H:%M:%S.%f', f'{hour}:{minute}:{second}.{microsecond_normalized}'


def is_weekend(data: datetime) -> bool:
    """
    Verifica se é sábado ou domingo
    weekday(): 0=segunda, ..., 5=sábado, 6=domingo
    
    Args:
        data: Objeto datetime
        
    Returns:
        True se for final de semana
    """

    return data.weekday() in [5, 6]


def is_outside_business_hours(hora: datetime) -> bool:
    """
    Verifica se está fora do horário comercial (9h-18h)
    
    Args:
        hora: Objeto datetime
        
    Returns:
        True se fora do horário comercial
    """
    hora_int = hora.hour
    return hora_int < 9 or hora_int >= 18


def is_high_value(
    valor: float, 
    limite: float
) -> bool:
    """
    Verifica se valor excede o limite
    
    Args:
        valor: Valor a verificar
        limite: Limite máximo permitido
        
    Returns:
        True se valor acima do limite
    """
    return valor > limite


def analyze_transactions(
    registro: Dict[str, str],
    limite: float,
    index_data: int,
    index_hora: int
    ) -> Dict[str, Any] | None:
    """
    Analisa se transação é suspeita
    
    Args:
        registro: Dicionário com data, hora, valor
        
    Returns:
        Dicionário com ocorrência ou None se não suspeita
    """
    try:
        field_item: List[str] = [valor.strip() for valor in registro.values()]
        valor_str: str = field_item[index_data + 2] if index_data + 2 < len(field_item) else registro['valor'].strip()

        dt = convert_to_datetime(field_item[index_data], field_item[index_hora])

        # Converter valor (remover R$, pontos e substituir vírgula)
        valor_limpo = float(
            valor_str
            .replace('R$', '')
            # .replace('.', '')
            .replace(',', '.')
            .strip()
        )
        # Critérios de suspeita
        fim_semana = is_weekend(dt)
        fora_horario = is_outside_business_hours(dt)
        valor_alto = is_high_value(valor_limpo, limite)

        # Se UM dos critérios for  TRUE, então = SUSPEITO
        if fim_semana or fora_horario or valor_alto:
            return {
                'data': dt.strftime('%d-%m-%Y'),
                'dia_da_semana': day_of_week(dt),
                'hora': dt.strftime('%H:%M:%S'),
                'valor': f'{valor_limpo:.2f}',
                'status': 'SUSPEITO'
            }
        return None
    except (ValueError, KeyError) as e:
        print(f'⚠️  Erro ao processar registro {registro}: {e}')
        return None
