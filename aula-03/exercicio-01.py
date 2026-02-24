### Exercício 1: Verificação de Qualidade de Dados
# Você está analisando um conjunto de dados de vendas e precisa garantir 
# que todos os registros tenham valores positivos para `quantidade` e `preço`. 
# Escreva um programa que verifique esses campos e imprima "Dados válidos" se ambos 
# forem positivos ou "Dados inválidos" caso contrário.
# Exemplo de registro de venda: {'produto': 'Notebook', 'quantidade': 5, 'preço': 2500.00},
import sys
from pathlib import Path

# Como a árvore de pastas não é a padrão, sou obrigado a adicionar pasta raiz ao path
# para poder impotar o módulo common_functions.py
sys.path.insert(0, str(Path(__file__).parent.parent))

import curso_python.libs.common_functions as cf

cf.clear_screen()  # Limpa a tela antes de iniciar o programa
print()
lista_vendas = [
    {'produto': 'Notebook', 'quantidade': 5, 'preço': 2500.00},
    {'produto': 'Mouse', 'quantidade': 10, 'preço': 50.00},
    {'produto': 'Teclado', 'quantidade': -3, 'preço': 150.00},  # Quantidade inválida
    {'produto': 'Monitor', 'quantidade': 2, 'preço': -800.00}   # Preço inválido
]
# Verificação de qualidade dos dados
for registro_venda in lista_vendas:
    print(f'Dados da venda: {registro_venda}')
    print()
    if registro_venda['quantidade'] > 0 and registro_venda['preço'] > 0:
        print('==> Dados válidos')
    else:
        print(' * * *  Dados inválidos  * * *')
    print()
