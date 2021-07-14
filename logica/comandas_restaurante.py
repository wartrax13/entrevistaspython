'''Comandas em um Restaurante

Você é responsável pelo sistema de atendimentos e geração de comandas de um restaurante. Todas as mesas geram uma lista de itens consumidos.

Uma das principais funcionalidades desse sistema é dividir o valor total de consumo pelo número de clientes da mesa, mas uma melhoria foi apontada: nem todos os itens consumidos devem ser incluídos na divisão comum da conta (entre todos os clientes na mesa).

Exemplo:

Em uma mesa com o número de clientes C=4, foram consumidos os seguintes itens com seus respectivos valores:

bebidas: 150
entrada: 100
principal: 400
sobremesa: 300
reserva: 40

Foi identificado que os itens "bebidas" e "reservas" não vão fazer parte da divisão comum da conta. Podemos concluir então que:

O valor total da conta é 990
O valor que cada cliente da mesa deve pagar na divisão comum é 200, visto que o total de itens, com exceção dos itens "bebidas" e "reserva", é 800 e devemos dividir esse valor pelos 4 clientes da mesa.
Por fim, o valor resultante dos itens "bebidas" e "reserva", desconsiderados na divisão comum é 190.

Seu desafio:

Com base nos itens consumidos em uma mesa, no número de clientes da mesa e nos itens que devem ser retirados da divisão comum, você deve ser capaz de determinar:

O valor total da conta;
O valor que cada cliente deve pagar resultante da divisão comum.
Por fim, o valor total resultante dos itens que não fizeram parte da divisão comum.

Obs.: Todos os valores de saída devem ser convertidos para o tipo "inteiro", evitando problemas de formatação da sua resposta.

Formato de Entrada (todas as linhas de entrada são do tipo string):

A primeira linha contém o número C de clientes da mesa
A segunda linha contém a quantidade N de itens consumidos
As N linhas seguintes trazem cada uma, um item e seu respectivo valor separados por espaço.
A linha seguinte contém os itens que devem ser desconsiderados na divisão comum, separados por espaço

Formato de Saída (todas as linhas de saída devem ser convertidas para o tipo "inteiro"):

A primeira linha deve conter o valor total da conta
A segunda linha deve conter o valor que cada cliente precisa pagar como resultado da divisão comum.
A terceira linha deve conter o valor total resultante dos itens que não fizeram parte da divisão comum

                    Exemplo de entrada:
                        6
                        4
                        entrada 150
                        bebidas 60
                        principal 240
                        sobremesa 30
                        entrada bebidas sobremesa

                    Exemplo de saída:

                    TEST CASE 1
                    Resultado:
                    ENTRADAS
                        3
                        7
                        item01 200
                        item02 40
                        item03 60
                        item04 80
                        item05 100
                        item06 80
                        item07 35
                        item03 item04 item07

                    Saída esperada:
                        595
                        140
                        175

TEST CASE 2 (OCULTO)
Resultado:

TEST CASE 3 (OCULTO)
Resultado:


                    TEST 4 
                    ENTRADAS:
                        6
                        4
                        entrada 150
                        bebidas 60
                        principal 240
                        sobremesa 30
                        entrada bebidas sobremesa

                        RESULTADO
                    Saída esperada
                        480
                        40
                        240
                        '''


#tentativa TEST 4

C = int(input())# input
D = int(input()) # input
entrada = input().split() # input
bebidas = input().split() # input
principal = input().split() # input
sobremesa = input().split() # input
reserva = input().split() # input
list(reserva)
x = [entrada[1], bebidas[1], principal[1], sobremesa[1]]

b = int(list.pop(bebidas))
e = int(list.pop(entrada))
s = int(list.pop(sobremesa))
p = int(list.pop(principal))
soma = b + e + s + p
print(soma)
print(int(p / C))
print(e + b + s)




