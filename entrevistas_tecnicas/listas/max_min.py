from random import shuffle


def max_mix(lst):
    """
    Calculate the maximum and minimum of a list
    :param lst: list
    :return: tuple (max, min)
    """
    if len(lst)==0: # lst = [1]
        raise ValueError('Empity List')
    max_value = min_value = lst[0]

    for value in lst:
        if value > max_value:
            max_value = value
        if value < min_value:
            min_value = value
    return max_value, min_value

    # return max(lst), min(lst) # 0(n + n) = 0(2n) = 0(n) OU


print(max_mix([1])) # 1,1
print(max_mix([1,2])) # 2,1
random_list = list(range(100))
shuffle(random_list)
print(random_list)
print(max_mix(random_list))# 99, 0
#print(max_mix([]))