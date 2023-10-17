import main
from time import sleep


def novo_cad():

    try:
        sleep(1)
        main.cabecalho('CADASTRO DE USUARIOS')

        nome = str(input('Digite o nome do usuario: '))
        idade = int(input('Digite a sua idade: '))

        database = open('database.txt', 'a')

        database.write(f'{nome};{idade}\n')

        print('\033[32mUsuario cadastrado!\033[0m')

    except Exception as erro:
        print(f'\033[31mnão foi possivel cadastros novo usuario devido a: {erro}\033[0m')

    finally:
        print(f'{"-" * 40}')
        print(' ')
        sleep(1)