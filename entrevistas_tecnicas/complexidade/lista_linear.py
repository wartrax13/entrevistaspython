#funções importadas
from random import shuffle

lst = list(range(12))
print('para imprimir a lista um item de cada vez')
for v in lst: print(v)

print('boleano para ver se há um elemento na lista')
print(2 in lst)
print(12 in lst)

print('para saber em qual posição está na lista')
print(lst.index(11))

print('para contar quanto de um item tem numa lista')
print(lst.count(11))

print('slice: fatiamento')
print(lst[1:7])
print(lst[:7])
print(lst[1:])
print(lst[:])

lst2=list(range(13,16))
print(lst2)

print('concatenação')
print(lst+lst2)

print('concatenação2')
lst2.extend(lst)
print(lst2)

print('multiplicação')
print(lst[5] * 10)

print('Reverter lista (criando reverse)')
print(list(reversed(lst)))
lst.reverse()
print(lst)

print('Inserir no início')
lst.insert(0, 13)
print(lst)

print('Remover')
print(lst.pop(0))
print(lst)

#importando funções
shuffle(lst)
print(lst)

#Transformar strings em lista .split()
print('Metodos fora da lista - strings para lista')
x = 'Curso entrevista tecnica'
print(x.split())
#Listas e strings
print('Metodos fora da lista - lista para strings')
','.join(b)




