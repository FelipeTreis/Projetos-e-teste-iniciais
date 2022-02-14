n = float(input('insira um numero entre 0 e 10: '))

if n > 10:
    print(f'Valor invalido')

for _ in range(11):
    maximo = max(n, float(input('insira um numero entre 0 e 10: ')))

    if maximo > 10:
        print(f'Valor invalido')
    else:
        print(f'o numero informado foi: {n}')
        break
