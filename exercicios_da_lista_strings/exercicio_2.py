nome = input(f'Coloque seu nome aqui: ').upper()
print(nome[::-1])
print(nome.split()[::-1])

lista = [1,2,3,4,5,6,7,8,9]
for i in reversed(lista):
    print(i)