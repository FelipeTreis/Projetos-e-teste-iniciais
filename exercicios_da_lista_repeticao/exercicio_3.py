nome = input('Insira seu nome: ')

sobrenome = input('Insira seu sobrenome: ')

idade = int(input('Insira sua idade: '))

salario = float(input('Insira seu salario: '))

sexo = input('Insira seu sexo("M" para masculino,"F" para feminino, "I" para indefinido): ').upper()

estado_civil = input('insira seu estado civil("S" para solteiro(a), "C" para casado(a),'
                '"V" para viuvo(a),"D" para divorciado(a): ').upper()

n = nome + sobrenome

print(n)

if idade > 0:
    print(f'{idade} anos')
elif idade < 150:
    print(f'{idade} anos')
else:
    print(f'idade invalida')

if sexo == 'M':
    print('Sexo masculino')
elif sexo == 'F':
    print('Sexo feminino')
elif sexo == 'I':
    print('Sexo indefinido')
else:
    print('Sexo invalido')

if estado_civil == 'S':
    print('Estado civil: Solteiro(a)')
elif estado_civil == 'C':
    print('Estado civil: Casado(a)')
elif estado_civil == 'V':
    print('Estado civil: Viuvo(a)')
elif estado_civil == 'D':
    print('Estado civil: Divorciado(a)')
else:
    print('Estado civil invalido')

if salario >= 0:
    print(f'Salario atual: R${salario} reais')
else:
    print('salario invalido')




