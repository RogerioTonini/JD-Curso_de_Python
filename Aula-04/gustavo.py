# Não ocorre erro, pois o Type Hinting é apenas uma anotação para indicar o tipo esperado de uma variável, mas não impede que outros tipos sejam atribuídos a ela. 
# No entanto, isso pode levar a comportamentos inesperados ou erros em tempo de execução se o código tentar usar a variável de uma maneira que não seja compatível com o tipo real atribuído a ela.
# Para que seja possível realizar operações matemáticas com a variável 'idade', é necessário convertê-la para um tipo numérico, como int ou float e também criar uma validação para garantir que a entrada do usuário seja um número válido.
# Ou ainda a utilização da biblioteca 'mypy' para realizar a verificação de tipos em tempo de desenvolvimento, o que pode ajudar a identificar inconsistências entre os tipos anotados e os tipos reais usados no código.

idade: int = input('Digite sua idade: ')
print(f'Sua idade é: {idade}', type(idade))

#  ---------------------------------------------------------

# Versões para corrigir o problema:

# Opção 1: Converter explicitamente
# idade: int = int(input('Digite sua idade: '))
# print(f'Sua idade é: {idade}', type(idade))
# Saída: Sua idade é: 25 <class 'int'>

# Opção 2: Type hint correto
# idade_str: str = input('Digite sua idade: ')
# idade: int = int(idade_str)

# Opção 3: Com tratamento de erro
# try:
#     idade: int = int(input('Digite sua idade: '))
# except ValueError:
#     print("Erro: digite um número válido")