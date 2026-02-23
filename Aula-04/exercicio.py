# Crie um dicionário para armazenar as informações de um livro: título, autor, ano de publicação e número de páginas.
# Em seguida, imprima as informações do livro.

import os
from typing import Any, Dict

os.system('cls')

livro_01: Dict[str, Any] = {
    'titulo': 'O Senhor dos Anéis',
    'autor': 'J.R.R. Tolkien',
    'ano_publicacao': 1954,
}

livro_02: Dict[str, Any] = {
    'titulo': '1984',
    'autor': 'George Orwell',
    'ano_publicacao': 1948,
}

# for livro in lista_livros:
#     print(f"Informações do Livro:")
#     print(f"Título: {livro['titulo']}")
#     print(f"Autor: {livro['autor']}")
#     print(f"Ano de Publicação: {livro['ano_publicacao']}")
# print('')

lista_livros: list = [livro_01, livro_02]

lista_livros_dict: dict = {'livro_01': livro_01, 'livro_02': livro_02}

print(f'-> Lista de Livros: {lista_livros_dict}')
print('')
print(f'Informações do Livro 01:')
print(f"Título: {livro_01['titulo']}")
print(f"Autor: {livro_01['autor']}")
print(f"Ano de Publicação: {livro_01['ano_publicacao']}")
