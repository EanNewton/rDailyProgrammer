def p388(n: int) -> int:
    """
    Next Palindrome [Intermediate]
    :param n:
    :return:
    """
    # increment by one and convert to a list of single digits
    n = [int(_) for _ in str(n + 1)]

    for i in range(len(n) // 2):
        if n[-1 - i] > n[i]:
            _ = 2
            while (n[-i - _] + 1) // 10:
                n[-i - _] = 0
                _ += 1
            n[-i - _] = n[-i - _] + 1

        n[-i - 1] = n[i]

    return int("".join(map(str, n)))

def test():
    print(p388(123))
    print(p388(312))
    print(p388(3 ** 39))
