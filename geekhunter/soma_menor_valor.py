'''
Soma do menor vetor único
Dado um vetor, você deve incrementar em 1 qualquer elemento duplicado até que todos os seu elementos sejam únicos. Adicionado a isto, a soma de todos os elementos deve ser a menor possível dentro das regras, por exemplo, caso o vetor seja [3, 2, 1, 2, 7] então este vetor com elementos únicos seria [3, 2, 1, 4, 7] e os seus elementos somados apresentam o menor valor possível de 17 onde 3 + 2 + 1 + 4 + 7 = 17.

Explicação:

Primeira iteração possível: v = [3, 2, 1, 2, 7] o elemento v[3] é um 2repetido, então incrementamos em 1.
Segunda iteração: v = [3, 2, 1, 3, 7] o elemento v[3] é um 3repetido, então incrementamos em 1.
Terceira iteração: v = [3, 2, 1, 4, 7] o elemento v[3] é único com o menor valor único possível.

Entrada:
A primeira linha informa quantas linhas subsequentes serão enviadas.
Cada subsequente linha informa um elemento do vetor. ex:

'''

n = int(input())
v = []

for x in range(n):
    v_ele = [int(x) for x in input().split(' ')]
    case = True
    while case:
        if v_ele[0] in v:
            v_ele[0] += 1
        else:
            case = False
    v.append(v_ele[0])

print(sum(v))
