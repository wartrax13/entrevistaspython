# COM BITS
# XOR
# 
# Complexidade:
# O(n)
# Memória: O(1),
def with_XOR(numbers):
    number = 0

    for i in numbers:
        number ^= i
    return number



numbers = [10, 8, 3, 7, 3, 9, 9, 2, 7, 10, 2]
numbers_1 = [10, 3, 7, 3, 9, 9, 2, 7, 10, 2, 8]

print(with_XOR(numbers_1))
