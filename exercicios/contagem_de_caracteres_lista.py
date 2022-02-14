def contar_caracters(s):
    '''Funcao que conta os carcteres de uma string
    ex:
    >>> contar_caracters('felipe')
    e: 2
    f: 1
    i: 1
    p: 1
    l: 1
    :param s: string a ser contada
    '''
    caracteres_ordenados = sorted(s)

    caracter_anterior = caracteres_ordenados
    contagem = 1

    for caracter in caracteres_ordenados[1:]:
        if caracter == caracter_anterior:
            contagem += 1
        else:
            print(f'{caracter_anterior}:{contagem}')
            caracter_anterior = caracter
            contagem = 1

if __name__ == '__main__':
    contar_caracters('felipe')
    print()
