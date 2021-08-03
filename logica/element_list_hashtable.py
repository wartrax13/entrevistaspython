# Pular de dois em dois
# Sort
# 
# Complexidade:
# O(n)
# Memória: O(n),
def with_hash_table(numbers):
    num_dict = {}
    for i in numbers:
        if i in num_dict:
            num_dict[i] += 1
        else:
            num_dict[i] = 1

    for number, counter in num_dict.items():
        if counter == 1:
            return number

    return None


numbers = [10, 8, 3, 7, 3, 9, 9, 2, 7, 10, 2]
numbers_1 = [10, 3, 7, 3, 9, 9, 2, 7, 10, 2, 8]

print(with_hash_table(numbers_1))
