# -----------------------------------------------------------------------------
# Arquivo: common-functions.py
# Objetivo: Arquivo para armazenar funções comuns que podem ser usadas em 
# diferentes partes do projeto.
# Autor: Rogerio Tonini - rogerio.tonini@gmail.com
# -----------------------------------------------------------------------------
# Relação de funções:
#  1. clear_screen(): Limpa a tela do terminal.
# -----------------------------------------------------------------------------

import os

def clear_screen():
    """
    Objetivo: Limpar a tela do terminal.
    A função detecta o sistema operacional e executa o comando apropriado para
    limpar a tela.
    Args: Nenhum argumento é necessário.
    Return: Nenhum valor é retornado.
    """
    os.system('cls' if os.name == 'nt' else 'clear')
