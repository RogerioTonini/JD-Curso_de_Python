# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
import os

os.system('cls' if os.name == 'nt' else 'clear')

numero_valido: bool = False
while not numero_valido:
    try:
        numero: int = int(input('Digite um número inteiro: '))
        if numero <= 0:
            print('\nPor favor, digite um número inteiro positivo.\n')
        else:
            numero_valido = True
    except KeyboardInterrupt as e:
        print('\nEntrada interrompida pelo usuário. Encerrando o programa.')
        exit()
    except ValueError:
        print('Entrada inválida. Por favor, digite um número inteiro.')

resto: int = numero % 5
print(f'O resto da divisão de {numero} por 5 é: {resto}\n')