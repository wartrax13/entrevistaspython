def phoneword(phonenumber):
    """
    Return all possible phonewords respective to a phonenumber

    :param phonenumber: str
    :return: list of str with all phonewords

    A cada iteração eu multiplico os resultados anteriores.
    4
    3
    0(3**n) <= ? <=0(4**n) => 0(a**n) - EXPONECIAL

    MEMÓRIA - EXPONENCIAL

    """
    digit_to_chars = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    n = len(phonenumber)

    def phoneword_rec(previous_results, cursor):
        if cursor == n:
            return previous_results
        digit = phonenumber[cursor]
        results = []
        for char in digit_to_chars[digit]:
            results.extend(
                prev_result + char for prev_result in previous_results)
        return phoneword_rec(results, cursor + 1)

    return phoneword_rec([''], 0)


print(phoneword(''))  # ['']
print(phoneword('736'))  # ['REN 'SEN']
