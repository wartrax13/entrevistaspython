from collections import Counter


def contar_letras(s: str):
    """
    >>> contar_letras('pedro')
    {'p': 1, 'e': 1, 'd': 1, 'r': 1, 'o': 1}
    >>> contar_letras('Ppedro')
    {'P': 1, 'p': 1, 'e': 1, 'd': 1, 'r': 1, 'o': 1}
    >>> contar_letras('banana')
    {'b': 1, 'a': 3, 'n': 2}



    :param s:
    :return:
    """
    dct={} # {'b': 1, 'a': 1, 'n': 1}
    for letra in s: # s = 'banana' letra = 'b'
        dct[letra]= dct.get(letra, 0) + 1

    return dct