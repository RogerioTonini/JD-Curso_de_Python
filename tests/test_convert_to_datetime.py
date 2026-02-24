"""
Testes para convert_to_datetime com microssegundos variáveis
"""
import sys

from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

import app.libs.data as data

def test_convert_to_datetime():
    """Testa todos os formatos suportados"""
    
    # ========================================
    # TESTES SEM MICROSSEGUNDOS
    # ========================================
    
    # HH:MM
    dt = data.convert_to_datetime('15/01/2024', '10:30')
    assert dt == datetime(2024, 1, 15, 10, 30)
    print('✅ HH:MM')
    
    # HH:MM:SS
    dt = data.convert_to_datetime('15/01/2024', '10:30:45')
    assert dt == datetime(2024, 1, 15, 10, 30, 45)
    print('✅ HH:MM:SS')
    
    # ========================================
    # TESTES COM MICROSSEGUNDOS (1-6 casas)
    # ========================================
    
    # 1 casa decimal (décimos de segundo)
    dt = data.convert_to_datetime('15/01/2024', '10:30:45.1')
    assert dt == datetime(2024, 1, 15, 10, 30, 45, 100000)
    print('✅ HH:MM:SS.f (1 casa)')
    
    # 2 casas decimais (centésimos de segundo)
    dt = data.convert_to_datetime('15/01/2024', '10:30:45.12')
    assert dt == datetime(2024, 1, 15, 10, 30, 45, 120000)
    print('✅ HH:MM:SS.ff (2 casas)')
    
    # 3 casas decimais (milissegundos)
    dt = data.convert_to_datetime('15/01/2024', '10:30:45.123')
    assert dt == datetime(2024, 1, 15, 10, 30, 45, 123000)
    print('✅ HH:MM:SS.fff (3 casas)')
    
    # 4 casas decimais
    dt = data.convert_to_datetime('15/01/2024', '10:30:45.1234')
    assert dt == datetime(2024, 1, 15, 10, 30, 45, 123400)
    print('✅ HH:MM:SS.ffff (4 casas)')
    
    # 5 casas decimais
    dt = data.convert_to_datetime('15/01/2024', '10:30:45.12345')
    assert dt == datetime(2024, 1, 15, 10, 30, 45, 123450)
    print('✅ HH:MM:SS.fffff (5 casas)')
    
    # 6 casas decimais (microssegundos completos)
    dt = data.convert_to_datetime('15/01/2024', '10:30:45.123456')
    assert dt == datetime(2024, 1, 15, 10, 30, 45, 123456)
    print('✅ HH:MM:SS.ffffff (6 casas)')
    
    # ========================================
    # TESTES COM DIFERENTES FORMATOS DE DATA
    # ========================================
    
    # DD-MM-YYYY
    dt = data.convert_to_datetime('15-01-2024', '10:30:45.123')
    assert dt == datetime(2024, 1, 15, 10, 30, 45, 123000)
    print('✅ DD-MM-YYYY')
    
    # YYYY-MM-DD
    dt = data.convert_to_datetime('2024-01-15', '10:30:45.123')
    assert dt == datetime(2024, 1, 15, 10, 30, 45, 123000)
    print('✅ YYYY-MM-DD')
    
    # ========================================
    # TESTES DE ERRO
    # ========================================
    
    try:
        data.convert_to_datetime('invalid', '10:30')
        assert False, 'Deveria levantar ValueError'
    except ValueError:
        print('✅ Erro para data inválida')
    
    try:
        data.convert_to_datetime('15/01/2024', 'invalid')
        assert False, 'Deveria levantar ValueError'
    except ValueError:
        print('✅ Erro para hora inválida')
    
    print('\n🎉 Todos os testes passaram!')


# Executar testes
if __name__ == '__main__':
    test_convert_to_datetime()