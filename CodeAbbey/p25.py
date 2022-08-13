import sys


def calc(a, c, m, x0, n):
    for _ in range(n):
        x0 = (a * x0 + c) % m
    return x0


def p25(raw):
    raw = [_.strip().split() for _ in raw]
    result = []
    for _ in raw[1:]:
        result.append(str(calc(*tuple(map(int, _)))))
    return " ".join(result)


def g(r,C=lambda a,c,m,x,n:[x:=(a*x+c)%m for _ in range(n)][-1]):
    return " ".join([str(C(*tuple(map(int, _))))for _ in[_.strip().split()for _ in r][1:]])


test = sys.stdin.readlines()
print(p25(test))
print(g(test))