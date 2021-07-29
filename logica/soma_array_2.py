# METODO 2

# Target 13

array = [4, 6, -5, 9, 12, 3, -1, 10]

# Time = O(nlogn) | Space: O(1)
def method2(array, target):
    array.sort()
    left = 0
    right = len(array) - 1

    while left < right:
        sum = array[left] + array[right]

        if sum == target:
            return array[left], array[right]
        elif sum < target:
            left += 1
        elif sum > target:
            right -= 1
    return ()


print(method2(array, 13))
