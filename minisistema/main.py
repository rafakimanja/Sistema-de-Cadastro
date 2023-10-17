'''
Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade
em um arquivo de texto simples. O sistema só vai ter 2 opções: cadastrar uma nova pessoa e
listar todas as pessoas cadastradas
'''

import cadastrar
import listar
from time import sleep


def cabecalho(nome):
    print(f'{"-"*40}')
    print(f'{nome:^40}')
    print(f'{"-" * 40}')


def menu():
    print('0 - Sair')
    print('1 - Cadastrar novo usuário')
    print('2 - Listar usuários cadastrados')
    print(f'{"-"*40}')
    esc = int(input('Seu escolha: '))
    print(f'{"-" * 40}')
    return esc


def main():

    while True:

        try:
            sleep(1)
            cabecalho('MENU PRINCIPAL')
            esc = menu()

            if esc < 0 or esc > 2:
                print('\033[31mDigite uma opção válida!\033[0m')

            match esc:

                case 0:
                    print('\033[33mVolte Sempre!\033[0m')
                    sleep(1)
                    break

                case 1:
                    cadastrar.novo_cad()

                case 2:
                    listar.lista_usu()

        except:

            print('\033[31mDigite uma opção válida!\033[0m')


if __name__ == '__main__':
    main()
