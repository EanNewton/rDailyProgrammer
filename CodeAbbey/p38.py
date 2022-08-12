import math
import sys

def quadratic(a: int, b: int, c: int):
    """

    :param a:
    :param b:
    :param c:
    :return:
    """
    var = b * b - 4 * a * c
    sqrt = math.sqrt(abs(var))

    if var > 0:
        x1 = (-b + sqrt) / (2 * a)
        x2 = (-b - sqrt) / (2 * a)
    elif var == 0:
        x1 = x2 = -b / (2 * a)
    else:
        x1 = x2 = complex(-b / (2 * 1), sqrt)
    return x1, x2


# TODO Not returning expected results
def p38(raw: list) -> str:
    """

    :param raw:
    :return:
    """
    results = []
    
    for _ in range(1, len(raw)):
        a, b, c = raw[_].split()
        x1, x2 = quadratic(int(a), int(b), int(c))
        if x1.imag:
            results.append(f"{x1.real:.0f}+{x1.imag:.0f}i {x2.real:.0f}-{x2.imag:.0f}i; ")
        else:
            results.append(f"{x1.real:.0f} {x2.real:.0f}; ")
    return "".join(results)

print(p38(sys.stdin.readlines()))
