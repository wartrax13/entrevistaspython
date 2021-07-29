# METHOD3


array = [4, 6, -5, 9, 12, 3, -1, 10]
#TIME = O(n) | Space: O(n)


def method3(array, target):
    hashtable = {}
    for num in array:
        if target - num in hashtable:
            return target - num, num
        else:
            hashtable[num] = True

    return ()


print(method3(array, 13))
