import sys
import itertools as it


def erat3( ):
    D = { 9: 3, 25: 5 }
    yield 2
    yield 3
    yield 5
    MASK= 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0,
    MODULOS= frozenset( (1, 7, 11, 13, 17, 19, 23, 29) )

    for q in it.compress(
            it.islice(it.count(7), 0, None, 2),
            it.cycle(MASK)):
        p = D.pop(q, None)
        if p is None:
            D[q*q] = q
            yield q
        else:
            x = q + 2*p
            while x in D or (x%30) not in MODULOS:
                x += 2*p
            D[x] = p


def p61(raw):
    raw = list(map(int, raw[1].strip().split()))
    results = []
    s = erat3()
    primes = [1]
    while len(primes) < max(raw) + 1:
        primes.append(next(s))
    for n in raw:
        results.append(str(primes[n]))
    return " ".join(results)



print(p61(sys.stdin.readlines()))