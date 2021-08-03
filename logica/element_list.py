#Complexidade:
# n²
# Memória: O(1),
def find_force_brute(numbers):
    for i in range(len(numbers)):
        found = False
        for j in range(len(numbers)):
            if i != j and numbers[i] == numbers[j]:
                found = True
                break

        if found == False:
            return numbers[i]
    return None


numbers = [10, 8, 3, 7, 3, 9, 9, 2, 7, 10, 2]
numbers_1 = [10, 3, 7, 3, 9, 9, 2, 7, 10, 2, 8]

print(find_force_brute(numbers_1))
