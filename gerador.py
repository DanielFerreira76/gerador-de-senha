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
        for _ in range(tamanho):
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


def selectnum(txt, minimo=0, maximo=1):
    while True:
        try:
            resp = int(input(txt))
            while not minimo <= resp <= maximo:
                print('Opção inválida, tente novamente!')
                resp = int(input(txt))
            break
        except ValueError:
                print('Opção inválida, tente novamente!')
    return resp


print('======================')
print('Gerador de Senhas'.center(22))
print('======================')
tam = selectnum('Tamanho da senha: [entre 6 e 50] ', 6, 50)
opcl = selectnum('Incluir letras? [0 = não / 1 = sim] ')
opcn = selectnum('Incluir números? [0 = não / 1 = sim] ')
opce = selectnum('Incluir caractéres especiais? [0 = não / 1 = sim] ')

while True:
    if opcl == 0 and opcn == 0 and opce == 0:
        print('Não é possível gerar essa senha')
    else:
        print(f'A senha gerada foi: {gerar(tam, opcl, opcn, opce)}')

    rep = selectnum('Quer gerar outra senha? [0 = não / 1 = sim] ')
    if rep == 0:
        break

    m = selectnum('Quer mudar alguma preferência? [0 = não / 1 = sim] ')
    if m == 1:
        while True:
            opcm = selectnum('''Qual preferência quer mudar?
[ 1 ] Tamanho
[ 2 ] Incluir Letras
[ 3 ] Incluir Números
[ 4 ] Incluir Caractéres especiais
[ 5 ] Cancelar Mudança
Sua opção: ''', 1, 5)
            if opcm == 1:
                tam = selectnum('Tamanho da senha: [entre 6 e 50] ', 6, 50)
            elif opcm == 2:
                opcl = selectnum('Incluir letras? [0 = não / 1 = sim] ')
            elif opcm == 3:
                opcn = selectnum('Incluir números? [0 = não / 1 = sim] ')
            elif opcm == 4:
                opce = selectnum('Incluir caractéres especiais? [0 = não / 1 = sim] ')
            elif opcm == 5:
                break

            c = selectnum('Quer alterar mais alguma preferência? [0 = não / 1 = sim] ')
            if c == 0:
                break

print('Programa encerrado!')
