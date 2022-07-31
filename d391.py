import string
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
def p391(n: int) -> str:
    """
    The ABACABA Sequence [Easy]

    The ABACABA sequence is defined as follows: the first iteration is the first letter of the alphabet (a).
    To form the second iteration, you take the second letter (b) and put the first iteration (just a in this case)
    before and after it, to get aba. For each subsequent iteration, place a copy of the previous iteration on
    either side of the next letter of the alphabet.

    Here are the first 5 iterations of the sequence:

    a
    aba
    abacaba
    abacabadabacaba
    abacabadabacabaeabacabadabacaba

    The 26th and final iteration (i.e. the one that adds the z) is 67,108,863 characters long.
    If you use one byte for each character, this takes up just under 64 megabytes of space.

    Challenge

    Write a program to print the 26th iteration of the ABACABA sequence.
    If it's easier for you, it's also fine to print one character per line,
    instead of all the characters on a single line.
    Just printing the output can take a few minutes, depending on your setup.
    Feel free to test it out on something smaller instead, like the 20th iteration, which is only about 1 megabyte.
    :param n:
    :return:
    """
    alphabet = list(string.ascii_lowercase)
    last = ''
    for _ in range(n):
        last = f"{last}{alphabet[_]}{last}"
        # print(f"{n}:\n{last}")
    return last


def p391b1(n: int) -> str:
    """
    Complete the challenge using O(n) memory, where n is the iteration number.

    If you don't know what that means, here's another way to say it that's roughly equivalent in this case.
    You can have as many variables as you want, but they must each hold either a single number or character, or
    a structure (list, vector, dict, string, map, tree, etc.) whose size never gets much larger than 26.
    If a function calls itself recursively, the call stack must also be limited to a depth of about 26.
    (This is definitely an oversimplification, but that's the basic idea.
    Feel free to ask if you want to know about whether any particular approach uses O(n) memory.)
    :param n:
    :return:
    """

def test() -> bool:
    assert p391(1) == 'a'
    assert p391(2) == 'aba'
    assert p391(3) == 'abacaba'
    assert p391(4) == 'abacabadabacaba'
    assert p391(5) == 'abacabadabacabaeabacabadabacaba'
    print("Passed!")
    return True

# test()
# 391(26)