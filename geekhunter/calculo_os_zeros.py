'''
Calcule os zeros

Dado uma entrada composta por dois números,
conte quantos zeros existem entre estes dois números (incluindo eles mesmos).
Deve ser contado cada zero presente nos números.
Os números sempre são positivos e entre 0 e 999,
e o primeiro número sempre é menor do que o segundo.
A primeira linha da entrada sempre o números de tuplas que serão passadas pelo algoritmo
e as próximas linhas serão as tuplas (uma por linha).
Veja o exemplo abaixo:
Entrada:
4
7 28
98 111
63 69
199 201

Saida:
2
12
0
3
'''

n = int(input())
for i in range(n):
    x = [int(x) for x in input().split(' ')]
    a, b = x
    lista = []
    q = ''
    for z in range(a, b+1):
        q += str(z)

    print(q.count('0'))

