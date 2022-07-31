import functools
import time


def timer(func):
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        tic = time.perf_counter()
        value = func(*args, **kwargs)
        toc = time.perf_counter()
        elapsed_time = toc - tic
        print(f"Elapsed time: {elapsed_time:0.4f} seconds")
        return value
    return wrapper_timer


@timer
def p390(n: int) -> int:
    """
    Given a number n, determine the number of times the digit "1" appears
    if you write out all numbers from 1 to n inclusive.

    f(1) = 1
    f(5) = 1
    f(10) = 2
    f(20) = 12
    f(1234) = 689
    f(5123) = 2557
    f(70000) = 38000
    f(123321) = 93395
    f(3^35) = 90051450678399649

    You should be able to handle large inputs like 335 efficiently,
    meaning much faster than iterating over all numbers from 1 to n.
    Find f(520) before posting your solution. The answer is 15 digits long and the sum of its digits is 74.
    :param n:
    :return:
    """

    # Naive / Bruteforce Method, slow
    return sum([str(x).count('1') for x in range(n+1)])
    # sum = 0
    # for _ in range(n+1):
    #     sum += str(_).count('1')
    #     # if _ % 100_000_000 == 0:
    #     #     print(f"{round(float(((_ / n+1) - 1) * 100), 2)}% {_ / 100_000_000}: {sum}")
    # return sum

@timer
def p3901(n: int) -> int:
    pass
    # Recursive, check 1, 10, 100, etc * leading digit and sum
    # Broken on 10, 100, etc.
    # if n < 1: return 0
    # elif n < 9: return 1
    # else:
    #     sum = 0
    #     strlen = len(str(n))
    #     lead = int(str(n)[0])
    #     scale = pow(10, strlen-1)
    #
    #     for _ in range(scale+1):
    #         #print(_)
    #         sum += str(_).count('1')
    #         if _ % 1_000 == 0:
    #             print(f"{round(float(((_ / n+1) - 1) * 100), 2)}% {_ / 1_000}: {sum}")
    #     return (sum * lead) + p3901(int(str(n)[1:]))


def test() -> bool:
    assert p390(1) == 1
    assert p390(5) == 1
    assert p390(10) == 2
    assert p390(20) == 12
    assert p390(1234) == 689
    assert p390(5123) == 2557
    assert p390(70000) == 38000
    assert p390(123321) == 93395
    assert p390(pow(3, 35)) == 90051450678399649
    print("Passed!")
    return True

def test2() -> bool:
    assert p3901(1) == 1
    assert p3901(5) == 1
    assert p3901(10) == 2
    assert p3901(20) == 12
    assert p3901(1234) == 689
    assert p3901(5123) == 2557
    assert p3901(70000) == 38000
    assert p3901(123321) == 93395
    assert p3901(pow(3, 35)) == 90051450678399649
    print("Passed!")
    return True


def p390b1(n: int) -> int:
    """
    f(35199981) = 35199981. Efficiently find the sum of all n such that f(n) = n.
    This should take a fraction of a second, depending on your programming language.

    The answer is 11 digits long and the sum of its digits is 53.

    (This is a repost of Challenge #45 [difficult], originally posted by u/oskar_s
    in April 2012. Check that post for hints and more detail.
    https://www.reddit.com/r/dailyprogrammer/comments/sv6xs/4272012_challenge_45_difficult/
    )
    :param n:
    :return:
    """
