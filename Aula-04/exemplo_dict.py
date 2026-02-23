import json
import os

os.system('cls')

produto_list: list = ['sapato', 39, 10.38, True]

produto_dict_01: dict = {
    'nome': 'sapato',
    'quantidade': 39,
    'preco': 10.38,
    'disponivel': True
}

produto_dict_02: dict = {
    'nome': 'televisao',
    'quantidade': 10,
    'preco': 70.38,
    'disponivel': False
}

print(f'Produto List: {produto_list}')
print('')
print(f' Produto Dict 01: {produto_dict_01}')
print('')
print(f'Produto Dict 02: {produto_dict_02}')

carrinho: list = []
carrinho.append(produto_dict_01)
carrinho.append(produto_dict_02)

print('')
print(f'Carrinho: {carrinho}')
print('')

# Convertendo o dicionário para JSON
carrinho_json: str = json.dumps(carrinho)
print(f'Carrinho JSON: {carrinho_json}')
print('')