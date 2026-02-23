# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
import os
os.system('cls' if os.name == 'nt' else 'clear')

def obter_numero_inteiro(prompt: str) -> int:
    while True:
        try:
            numero: int = int(input(prompt))
            return numero
        except KeyboardInterrupt:
            print('\nEntrada interrompida pelo usuário. Encerrando o programa.')
            exit()
        except ValueError:
            print('Entrada inválida. Por favor, digite um número inteiro.')

numero1: int = obter_numero_inteiro('Digite o primeiro número inteiro: ')
numero2: int = obter_numero_inteiro('Digite o segundo número inteiro: ')
resultado: int = numero1 * numero2
print(f'\nO resultado da multiplicação de {numero1} por {numero2} é: {resultado}\n')
