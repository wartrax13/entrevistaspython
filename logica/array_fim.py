
vendedores = input()
array = [int(i) for i in input().split()]
number = int(input())
vend = input()
vend = int(vend)
x = 0
while x < number:
    n = array.pop(0)
    array.append(n)
    x +=1

print(array[0])
print(array.index(vend))
