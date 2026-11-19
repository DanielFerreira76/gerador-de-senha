import random


def gerar(tamanho, letras, numeros, especiais):
    alfa = 'abcdefghijklmnopqrstuvwxyz'
    num = '1234567890'
    especial = '@#$%&*'
    caracteres = ''
    ok = False
    if letras == 1:
        caracteres += alfa
    if numeros == 1:
        caracteres += num
    if especiais == 1:
        caracteres += especial

    while not ok:
        senha = ''
        for a in range(tamanho):
                senha += random.choice(caracteres)
        if letras == 1:
            okl = any(b in senha for b in alfa)
        else:
            okl = True
        if numeros == 1:
            okn = any(b in senha for b in num)
        else:
            okn = True
        if especiais == 1:
            oke = any(b in senha for b in especial)
        else:
            oke = True
        ok = okl and okn and oke
        
    return senha


print('======================')
print('Gerador de Senhas'.center(22))
print('======================')
rep = 1
while True:
    while True:
        try:
            opcl = int(input('Incluir letras? [0 = não / 1 = sim] '))
            while not 0 <= opcl <= 1:
                print('Opção inválida, tente novamente!')
                opcl = int(input('Incluir letras? [0 = não / 1 = sim] '))
            break
        except ValueError:
            print('Opção inválida, tente novamente!')

    while True:
        try:
            opcn = int(input('Incluir números? [0 = não / 1 = sim] '))
            while not 0 <= opcn <= 1:
                print('Opção inválida, tente novamente!')
                opcn = int(input('Incluir números? [0 = não / 1 = sim] '))
            break
        except ValueError:
            print('Opção inválida, tente novamente!')

    while True:
        try:
            opce = int(input('Incluir caractéres especiais? [0 = não / 1 = sim] '))
            while not 0 <= opce <= 1:
                print('Opção inválida, tente novamente!')
                opce = int(input('Incluir caractéres especiais? [0 = não / 1 = sim] '))
            break
        except ValueError:
            print('Opção inválida, tente novamente!')

    while True:
        try:
            tam = int(input('Tamanho da senha: [entre 6 e 50] '))
            while not 6 <= tam <= 50:
                print('Tamanho inválido, tente novamente!')
                tam = int(input('Tamanho da senha: [entre 6 e 50] '))
            break
        except ValueError:
            print('Valor inválido, tente novamente!')

    if opcl == 0 and opcn == 0 and opce == 0:
        print('Não é possível gerar essa senha')
    else:
        print(f'A senha gerada foi: {gerar(tam, opcl, opcn, opce)}')

    while True:
        try:
            rep = int(input('Quer gerar outra senha? [0 = não / 1 = sim] '))
            while not 0 <= rep <= 1:
                print('Opção inválida, tente novamente!')
                rep = int(input('Quer gerar outra senha? [0 = não / 1 = sim] '))
            break
        except ValueError:
            print('Opção inválida, tente novamente!')
    if rep == 0:
        break
    else:
        while True:
            try:
                m = int(input('Quer mudar alguma preferência? [0 = não / 1 = sim] '))
                while not 0 <= m <= 1:
                    print('Opção inválida, tente novamente!')
                    m = int(input('Quer mudar alguma preferência? [0 = não / 1 = sim] '))
                break
            except ValueError:
                print('Opção inválida, tente novamente!')
        if m == 1:
            while True:
                while True:
                    try:
                        opcm = int(input('''Qual preferência quer mudar?
                        [ 1 ] Tamanho
                        [ 2 ] Incluir Letras
                        [ 3 ] Incluir Números
                        [ 4 ] Incluir Caractéres especiais
                        [ 5 ] Cancelar Mudança
                        Sua opção: '''))
                        while not 1 <= opcm <= 5:
                            opcm = int(input('Opção inválida, tente novamente: '))
                        break
                    except ValueError:
                        print('Opção inválida, tente novamente!')

                if opcm == 1:
                    while True:
                        try:
                            tam = int(input('Tamanho da senha: [entre 6 e 50] '))
                            while not 6 <= tam <= 50:
                                print('Tamanho inválido, tente novamente!')
                                tam = int(input('Tamanho da senha: [entre 6 e 50] '))
                            break
                        except ValueError:
                            print('Valor inválido, tente novamente!')

                elif opcm == 2:
                    while True:
                        try:
                            opcl = int(input('Incluir letras? [0 = não / 1 = sim] '))
                            while not 0 <= opcl <= 1:
                                print('Opção inválida, tente novamente!')
                                opcl = int(input('Incluir letras? [0 = não / 1 = sim] '))
                            break
                        except ValueError:
                            print('Opção inválida, tente novamente!')

                elif opcm == 3:
                    while True:
                        try:
                            opcn = int(input('Incluir números? [0 = não / 1 = sim] '))
                            while not 0 <= opcn <= 1:
                                print('Opção inválida, tente novamente!')
                                opcn = int(input('Incluir números? [0 = não / 1 = sim] '))
                            break
                        except ValueError:
                            print('Opção inválida, tente novamente!')

                elif opcm == 4:
                    while True:
                            try:
                                opce = int(input('Incluir caractéres especiais? [0 = não / 1 = sim] '))
                                while not 0 <= opce <= 1:
                                    print('Opção inválida, tente novamente!')
                                    opce = int(input('Incluir caractéres especiais? [0 = não / 1 = sim] '))
                                break
                            except ValueError:
                                print('Opção inválida, tente novamente!')

                elif opcm == 5:
                    break
                while True:
                    try:
                        c = int(input('Quer alterar mais alguma preferência? [0 = não / 1 = sim] '))
                        while not 0 <= c <= 1:
                            print('Opção inválida, tente novamente!')
                            c = int(input('Quer alterar mais alguma preferência? [0 = não / 1 = sim] '))
                        break
                    except ValueError:
                        print('Valor inválido, tente novamente!')
                if c == 0:
                    break
                
            if opcl == 0 and opcn == 0 and opce == 0:
                print('Não é possível gerar essa senha')
            else:
                print(f'A senha gerada foi: {gerar(tam, opcl, opcn, opce)}')
