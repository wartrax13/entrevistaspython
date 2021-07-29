#METODO 1
#Time = O(n^2) - quadratica/ Time: O(1)
#FORÇA BRUTA
#target = 11

def method1(array, target):
    for i in range(len(array)-1):
        for j in range(i+1, len(array)):
            if array[i] + array[j] == target:
                return (array[i], array[j])

    return False


array = [4,6,-5,9,12,3,-1,10]
print(method1(array, 11))