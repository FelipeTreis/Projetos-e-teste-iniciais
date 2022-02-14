n = input('Insira seu nome aqui: ')
i = int(input('Agora insira sua idade: '))

print(f'Bem vindo: {n.upper()}')

if i < 18:
    print('Menor de idade, voce nao pode acessar')
else:
    print('Voce tem acesso')