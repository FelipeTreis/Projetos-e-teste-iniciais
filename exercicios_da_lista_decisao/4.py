nome = input('insira seu nome:').upper()
print(f'Seja bem vindo: {nome}')

idade = input('insira sua idade: ')

if idade >= '18' :
    print('maior de idade')
elif idade < '18' :
    print('menor de idade')
