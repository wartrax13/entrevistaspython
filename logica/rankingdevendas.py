'''Ranking de Vendas
Contextualização:
Neste cenário, você é desenvolvedor de uma empresa que presta um serviço de
consultoria jurídica num modelo digital de assinaturas.
Durante o mês, os vendedores competem em um ranking de vendas.
O ranking obedece a um único e simples critério, a quantidade de assinaturas vendidas por cada vendedor.
Não existe critério de desempate, de forma que os vendedores
com o mesmo número de vendas ocupam a mesma posição no ranking.
Por exemplo: se 5 vendedores efetuam respectivamente 30, 12, 30, 18 e 12 vendas,
teríamos um ranking com 2 vendedores ocupando a primeira posição (com 30 vendas),
1 vendedor na segunda posição (com 18 vendas) e outros 2 vendedores na terceira posição (com 12 vendas).

Seu desafio:

Com base no número de vendas de todos os vendedores, a exceção de Carlos,
verificar que posição Carlos ocupará no ranking, em algumas simulações de valores para o seu número de vendas.
Mantendo o exemplo anterior, para o vetor V=[30, 12, 30, 18, 12],
que representa o número de vendas dos outros vendedores e o vetor C=[20, 10, 35],
que representa as simulações de vendas de Carlos, o resultado das simulações é [2, 4, 1], visto que:

Se Carlos efetuar 20 vendas, ocupará a posição 2 no ranking;
Se Carlos efetuar 10 vendas, ocupará a posição 4;
Se Carlos efetuar 35 vendas, ocupará a posição 1.

Formato de Entrada (todas as linhas de entrada são dados do tipo string):

A primeira linha contém o número de elementos do vetor V
A segunda linha contém os elementos do vetor V separados por espaço
A terceira linha contém o número de elementos do vetor C
A quarta linha contém os elementos do vetor C separados por espaço.

Formato de saída:
Para cada valor em C, imprima o valor da posição Carlos na simulação,
cada valor deve ser impresso em uma nova linha.

Exemplo de entrada:
5
30 12 30 18 12
3
20 10 35

Exemplo de Saída:
2
4
1

test1
Saída:
7
55 100 100 40 100 50 35
20 60 40 10

test2
Saída:
10
30 0 15 20 30 10 10 15 20 0
2
1 40

'''
#entrada
# test 1
'''Saída:
7
55 100 100 40 100 50 35
20 60 40 10'''

# test 2
'''Saída:
10
30 0 15 20 30 10 10 15 20 0
2
1 40'''
V = [30, 0, 15, 20, 30, 10, 10, 15, 20, 0]
V_set = list(set(V))
C = [1,40]
#saida2
print(len(V))
print(*V)
print(len(C))
print(*C)
'''#exercício2
x = 0
for x in range(len(C)):
    def codigo(x):
        V_set.append(C[x])
        V_set.sort(reverse=True)
        return V_set.index(C[x]) + 1
print(codigo(0))
V_set.pop(V_set.index(C[0]))
print(codigo(1))
'''


'''while x < len(C):
    x -= 1
    def code(x):
        V_set.append(C[x])
        V_set.sort(reverse=True)
        return V_set.index(C[x]) + 1
    print(code(0))'''

'''
def code(x):
    V_set.append(C[x])
    V_set.sort(reverse=True)
    return V_set.index(C[x]) + 1

print(code(0))
V_set.pop(V_set.index(C[0]))
print(code(1))
print(code(2))

'''