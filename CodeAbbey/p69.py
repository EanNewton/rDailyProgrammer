def fib():
    a=0
    b=1
    while(True):
        yield b
        a,b= b,a+b

def p69(raw):
    result = []
    raw = raw[1].strip().split()
    for each in raw:
        f = fib()
        i = 0
        while next(f) % int(each) != 0:
            i += 1
        result.append(str(i+1))
    return " ".join(result)


import sys

print(p69(sys.stdin.readlines()))