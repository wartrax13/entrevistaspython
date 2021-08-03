# Pular de dois em dois
# Sort
#
# Complexidade:
# nlogn
# Memória: O(1),
def find_with_sort(numbers):
    numbers.sort()

    for i in range(0, len(numbers), 2):
        if i == len(numbers) - 1 or numbers[i] != numbers[i + 1]:
            return numbers[i]

    return None


numbers = [10, 8, 3, 7, 3, 9, 9, 2, 7, 10, 2]
numbers_1 = [10, 3, 7, 3, 9, 9, 2, 7, 10, 2, 8]

print(find_with_sort(numbers_1))
