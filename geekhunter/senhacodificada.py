'''
Encontre a chave para decodificar a mensagem
Recentemente, seu time decidiu se comunicar apenas utilizando mensagens codificadas.
Essas mensagens são encriptadas por uma chave diferente all day.
 o entanto, alguns dos seus colegas tem medo da segurança e o time decide que as
senhas são codificadas dentro de um texto simples e enviadas para 'all time' tamanho da senha.

A forma que isso funciona, é que a senha do dia com o tamanho N
pode ser encontrada procurando no texto pela substring mais frequente de tamanho N.


Sua missão é escrever um programa que, dado um tamanho N de senha e uma mensagem codificada,
determine a senha seguindo a estratégia acima.

Para ilustrar a tarefa, considere um exemplo em que a senha seja de tamanho 3 (N = 3)
e a mensagem codificada seja "onetwoone". A senha então seria "one", porque esta é a substring de tamanho 3,
que mais aparece em toda a mensagem (aparece duas vezes),
enquanto as outras cinco diferentes substrings aparecem apenas uma: "one", "net", "etw", "two", "woo", "oon", "one".



Entrada:
A primeira linha da entrada contem um inteiro T,
que representa a quantidade de entradas subsequentes.
As entradas seguintes contém um texto, onde a primeira posição representa um inteiro N(0 < N ≤ 10) que representa o tamanho da senha, seguido de uma mensagem codificada. Ex: (3 onetwoone)

Saída:
A saída deve conter a senha de tamanho N. Ex: (one)
'''

for i in range(0, 7):
    value = input()
    numero = int(value[0:2])
    if numero < 10 and numero != 0:
        palavra = value[2:len(value)]
        my_list = []
        if palavra != "":
            for j in range(0, len(palavra) - i):
                my_list.append(palavra[j:j + numero])

            palavraF = ''
            numeroF = 0

            for x in my_list:
                if numeroF < my_list.count(x):
                    numeroF = my_list.count(x)
                    palavraF = x
            print(palavraF)

    if numero == 10:
        palavra = value[3:len(value)]
        my_list = []
        if palavra != "":
            for j in range(0, len(palavra) - i):
                my_list.append(palavra[j:j + numero])

            palavraF = ''
            numeroF = 0

            for x in my_list:
                if numeroF < my_list.count(x):
                    numeroF = my_list.count(x)
                    palavraF = x
            print(palavraF)