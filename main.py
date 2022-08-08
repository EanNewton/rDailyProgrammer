import sys

def p399(raw: str) -> int:
    """
    Letter Value Sum [Easy]

    Assign every lowercase letter a value, from 1 for a to 26 for z.
    Given a string of lowercase letters, find the sum of the values of the letters in the string.
    :param raw:
    :return:
    """

    import d399
    return d399.p399(raw)


# TODO Incomplete
def p398(raw: str) -> int:
    """
    Matrix Sum [Difficult]

    Consider this 5x5 matrix of numbers:

    123456789   752880530   826085747  576968456   721429729
    173957326   1031077599  407299684  67656429    96549194
    1048156299  663035648   604085049  1017819398  325233271
    942914780   664359365   770319362  52838563    720059384
    472459921   662187582   163882767  987977812   394465693

    If you select 5 elements from this matrix such that no two elements come from the same row or column,
    what is the smallest possible sum?
    The answer in this case is 1099762961 (123456789 + 96549194 + 663035648 + 52838563 + 163882767).
    :param raw:
    :return:
    """


def p397(a: str, b:str) -> bool:
    """
    Roman Numeral Comparison [Easy]

    For the purpose of today's challenge, a Roman numeral is a non-empty string of the characters
    M, D, C, L, X, V, and I, each of which has the value 1000, 500, 100, 50, 10, 5, and 1.
    The characters are arranged in descending order, and the total value of the numeral is the sum of
    the values of its characters.
    For example, the numeral MDCCXXVIIII has the value 1000 + 500 + 2x100 + 2x10 + 5 + 4x1 = 1729.

    This challenge uses only additive notation for roman numerals.
    There's also subtractive notation, where 9 would be written as IX.
    You don't need to handle subtractive notation (but you can if you want to, as an optional bonus).

    Given two Roman numerals, return whether the first one is less than the second one:

    numcompare("I", "I") => false
    numcompare("I", "II") => true
    numcompare("II", "I") => false
    numcompare("V", "IIII") => false
    numcompare("MDCLXV", "MDCLXVI") => true
    numcompare("MM", "MDCCCCLXXXXVIIII") => false

    You only need to correctly handle the case where there are at most 1 each of
    D, L, and V, and at most 4 each of C, X, and I. You don't need to validate the input, but you can if you want.
    Any behavior for invalid inputs like numcompare("V", "IIIIIIIIII") is fine - true, false, or error.
    Try to complete the challenge without actually determining the numerical values of the inputs.

    (This challenge is a repost of Challenge #66 [Easy], originally posted by u/rya11111
    in June 2012. Roman numerals have appeared in several previous challenges.
    https://www.reddit.com/r/dailyprogrammer/comments/v89c4/6182012_challenge_66_easy/
    )
    :param a:
    :param b:
    :return:
    """
    import d397
    return d397.p397(a, b)


# TODO Incomplete
def p396(n: int, h: int) -> int:
    """
    Phone Drop [Intermediate]

    Given N, the number of phone prototypes you have, and H, the maximum height that needs to be tested,
    determine the maximum number of trials required by an optimal strategy to determine K.
    You should be able to at least handle values of H up to 999.
    :param n:
    :param h:
    :return:
    """


def p395(raw: list) -> list:
    """
    Nonogram Row [Easy]

    Given a binary array of any length, return an array of positive integers that represent the lengths of the sets of
    consecutive 1's in the input array, in order from left to right.
    :param raw:
    :return:
    """
    import d395
    return d395.p395(raw)


# TODO Incomplete
def p394(p: int, q: int, e=65537) -> str:
    """
    RSA Encryption [Difficult]

    If you're not familiar with some of the background topics for today's challenge,
    you'll need to do some reading on your own. Feel free to ask if you're lost,
    but try to figure it out yourself first. This is a difficult challenge.

    Implement the RSA key generation process following the specification on Wikipedia,
    or some other similar specification.
    Randomly generate 256-bit or larger values for p and q, using the Fermat primality test

    or something similar. Use e = 65537. Provide functions to encrypt and decrypt a whole number representing a message,
    using your selected n. Verify that when you encrypt and then decrypt the input 12345, you get 12345 back.

    It's recommended that you use a large-number library for
    this challenge if your language doesn't support big integers.

    (This is a repost of Challenge #60 [difficult], originally posted by u/rya11111
    in June 2012.
    https://www.reddit.com/r/dailyprogrammer/comments/ukj67/642012_challenge_60_difficult/
    )
    :param p:
    :param q:
    :param e:
    :return:
    """


def p393(raw: int) -> int:
    """
    Making Change [Easy]

    The country of Examplania has coins that are worth 1, 5, 10, 25, 100, and 500 currency units.
    At the Zeroth Bank of Examplania, you are trained to make various amounts of money by using as many ¤500 coins as
    possible, then as many ¤100 coins as possible, and so on down.

    For instance, if you want to give someone ¤468, you would give them four ¤100 coins, two ¤25 coins, one ¤10 coin,
    one ¤5 coin, and three ¤1 coins, for a total of 11 coins.

    Write a function to return the number of coins you use to make a given amount of change.
    :param raw:
    :return:
    """
    import d393
    return d393.p393(raw)


def p392(raw: list, n: int) -> list:
    """
    Pancake Sort [Intermediate]

    Implement the flipfront function. Given an array of integers and a number n between 2 and the length of
    the array (inclusive), return the array with the order of the first n elements reversed.
    :param raw:
    :param n:
    :return:
    """
    import d392
    return d392.p392(raw, n)


def p391(raw: int) -> str:
    """
    The ABACABA Sequence [Easy]

    Write a program to print the 26th iteration of the ABACABA sequence.
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
    :param raw:
    :return:
    """
    import d391
    return d391.p391(raw)


# TODO Need efficient solution
# Challenge
def p390(raw: int) -> int:
    """

    :param raw:
    :return:
    """
    import d390
    return d390.p390()


def p389(raw: int) -> float:
    """
    The Monty Hall Problem [Easy]
    :param raw:
    :return:
    """
    import d389
    d389.test()


def p388(raw: int) -> int:
    """
    Next Palindrome [Intermediate]
    :param raw:
    :return:
    """
    import d388
    return d388.p388(raw)


def p387(raw: str, n: int) -> str:
    """
    Caeser Cipher [Easy]
    :param raw:
    :param n:
    :return:
    """
    import d387
    return d387.p387b2(raw, n)


def p383():
    """
    Necklace Matching [Easy]
    :return:
    """
    import d383


def p378():
    """
    Havel-Hakimi Algorithm [Easy]
    :return:
    """
    import d378


def p375():
    """
    Add one to each digit [Easy]
    :return:
    """
    import d375


if __name__ == '__main__':
 #print(globals()['d' + input('>')](multi_in()))  # ENTER to EOF
 print(globals()['p'+input('>')](sys.stdin.readlines())) # Ctrl-D to EOF
 #print(globals()['p' + input('>')](open(0).read()))  # Ctrl-D to EOF
