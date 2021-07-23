def hanoi(n, orig='A', aux='B', dest='C'):
    """Recursive Solution to Hanoi Tower
    t(n) = 1 + 2(t(n-1))
    t(n) = 1 + 2 + 4(t(n-2))
    t(n) = 1 + 2 + 4 + 8(t(n-3))
    t(n) = 1 + 2 + 4 + 8 + 16(t(n-4))
    t(n) = 1 + 2 + 4 + 8 + 16 ... 2**n
    2(t(n)) = 2 + 4 + 8 + 16 + 32 ... 2**(n+1)

    m(n) = 1 + m(n-1)
    """
    if n >= 1:
        hanoi(n - 1, orig, dest, aux)
        print('{} -> {} : {}'.format(orig, dest, n))
        hanoi(n - 1, aux, orig, dest)


for i in range(1, 4):
    print('######## Hanoi %s' % i)
    hanoi(i)
