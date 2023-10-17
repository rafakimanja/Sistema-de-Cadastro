import main
from time import sleep


def lista_usu():

    try:
        sleep(1)
        main.cabecalho('LISTAGEM DE USUARIOS')

        database = open('database.txt', 'r')

        for linha in database:
            dados = linha.split(';')
            dados[1] = dados[1].replace('\n', '')
            print(f'\033[036m{dados[0]:<30}{dados[1]:>3} anos\033[0m')

    except Exception as erro:
        print(f'\033[31mNão foi possivel listar os usuários devido a: {erro}\033[0m')

    finally:
        print(f'{"-"*40}')
        print(' ')
        sleep(1)
