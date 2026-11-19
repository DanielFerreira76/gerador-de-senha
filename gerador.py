import random


def gerar(tamanho, letrasmi, letrasma, numeros, especiais):
    alfami = 'abcdefghijklmnopqrstuvwxyz'
    alfama = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    num = '1234567890'
    especial = '@#$%&*'
    caracteres = ''
    ok = False
    if letrasmi == 1:
        caracteres += alfami
    if letrasma == 1:
        caracteres += alfama
    if numeros == 1:
        caracteres += num
    if especiais == 1:
        caracteres += especial

    while not ok:
        senha = ''
        for _ in range(tamanho):
                senha += random.choice(caracteres)
        if letrasmi == 1:
            okli = any(b in senha for b in alfami)
        else:
            okli = True
        if letrasma == 1:
            okla = any(b in senha for b in alfama)
        else:
            okla = True
        if numeros == 1:
            okn = any(b in senha for b in num)
        else:
            okn = True
        if especiais == 1:
            oke = any(b in senha for b in especial)
        else:
            oke = True
        ok = okli and okla and okn and oke
        
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
opcli = selectnum('Incluir letras minúsculas? [0 = não / 1 = sim] ')
opcla = selectnum('Incluir letras maiúsculas? [0 = não / 1 = sim] ')
opcn = selectnum('Incluir números? [0 = não / 1 = sim] ')
opce = selectnum('Incluir caracteres especiais? [0 = não / 1 = sim] ')

while True:
    if opcli == 0 and opcla == 0 and opcn == 0 and opce == 0:
        print('Não é possível gerar essa senha')
    else:
        print(f'A senha gerada foi: {gerar(tam, opcli, opcla, opcn, opce)}')

    rep = selectnum('Quer gerar outra senha? [0 = não / 1 = sim] ')
    if rep == 0:
        break

    m = selectnum('Quer mudar alguma preferência? [0 = não / 1 = sim] ')
    if m == 1:
        while True:
            opcm = selectnum('''Qual preferência quer mudar?
[ 1 ] Tamanho
[ 2 ] Incluir Letras Minúsculas
[ 3 ] Incluir Letras Maiúsculas
[ 4 ] Incluir Números
[ 5 ] Incluir Caracteres especiais
[ 6 ] Cancelar Mudança
Sua opção: ''', 1, 6)
            if opcm == 1:
                tam = selectnum('Tamanho da senha: [entre 6 e 50] ', 6, 50)
            elif opcm == 2:
                opcli = selectnum('Incluir letras minúsculas? [0 = não / 1 = sim] ')
            elif opcm == 3:
                opcla = selectnum('Incluir letras maiúsculas? [0 = não / 1 = sim] ')
            elif opcm == 4:
                opcn = selectnum('Incluir números? [0 = não / 1 = sim] ')
            elif opcm == 5:
                opce = selectnum('Incluir caracteres especiais? [0 = não / 1 = sim] ')
            elif opcm == 6:
                break

            c = selectnum('Quer alterar mais alguma preferência? [0 = não / 1 = sim] ')
            if c == 0:
                break

print('Programa encerrado!')
