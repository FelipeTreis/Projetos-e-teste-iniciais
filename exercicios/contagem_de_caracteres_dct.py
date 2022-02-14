def contar_caracters(s):
    '''Funcao que conta os carcteres de uma string
    ex:
    >>> contar_caracters('felipe')
    {e: 2, f: 1, i: 1, p: 1, l: 1}
    :param s: string a ser contada
    '''


    resultado = {}

    for caracter in s:
        contagem = resultado.get(caracter, 0) + 1
        contagem += 1
        resultado [caracter] = contagem

    return resultado

if __name__ == '__main__':
    print(contar_caracters('felipe'))


