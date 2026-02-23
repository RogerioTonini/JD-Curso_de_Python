import os

os.system('cls')

produto_1: str = 'sapato'
produto_2: str = 'camisa'
produto_3: str = 'calça'

# Pode ser criado de 2 formas:
# 1.Inserindo os elementos uma a um
produtos: list[str] = []
produtos.append(produto_1)
produtos.append(produto_2)
produtos.append(produto_3)

# 2. Criando a lista já com os elementos
produtos_1: list[str] = [produto_1, produto_2, produto_3]

print(f'Lista Produtos: {produtos} / Lista Produtos_1: {produtos_1}')
print('')

# removendo o último elemento da lista, muito mais performatico do que remover um elemento específico, pois não é necessário realocar os elementos restantes
produtos.pop()
produtos_1.pop()

print(f'Lista Produtos: {produtos} / Lista Produtos_1: {produtos_1}')
