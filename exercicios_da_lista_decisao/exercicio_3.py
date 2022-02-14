sexo = input('Digite seu sexo,(M para masculino, F para feminino, I para indefinido): ').upper()

if sexo == 'M':
    print('masculino')
elif sexo == 'F':
    print('feminino')
elif sexo == 'I':
    print('indefinido')
else :
    print('sexo invalido')
