from itertools import zip_longest


def p397(a: str, b:str) -> bool:
    """
    Roman Numeral Comparison
    For the purpose of today's challenge, a Roman numeral is a non-empty string of the characters
    M, D, C, L, X, V, and I, each of which has the value 1000, 500, 100, 50, 10, 5, and 1.
    The characters are arranged in descending order, and the total value of the numeral is the sum of
    the values of its characters.
    For example, the numeral MDCCXXVIIII has the value 1000 + 500 + 2x100 + 2x10 + 5 + 4x1 = 1729.

    This challenge uses only additive notation for roman numerals.
    There's also subtractive notation, where 9 would be written as IX.
    You don't need to handle subtractive notation (but you can if you want to, as an optional bonus).

    Given two Roman numerals, return whether the first one is less than the second one:

    p397("I", "I") => false
    p397("I", "II") => true
    p397("II", "I") => false
    p397("V", "IIII") => false
    p397("MDCLXV", "MDCLXVI") => true
    p397("MM", "MDCCCCLXXXXVIIII") => false

    You only need to correctly handle the case where there are at most 1 each of
    D, L, and V, and at most 4 each of C, X, and I. You don't need to validate the input, but you can if you want.
    Any behavior for invalid inputs like p397("V", "IIIIIIIIII") is fine - true, false, or error.

    (This challenge is a repost of Challenge #66 [Easy], originally posted by u/rya11111
    in June 2012. Roman numerals have appeared in several previous challenges.
    https://www.reddit.com/r/dailyprogrammer/comments/v89c4/6182012_challenge_66_easy/
    )
    :param a:
    :param b:
    :return:
    """
    roman_to_arabic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    sum_a = 0
    sum_b = 0
    for a_, b_ in zip_longest([c for c in a], [c for c in b], fillvalue='-'):
        sum_a += roman_to_arabic[a_]
        sum_b += roman_to_arabic[b_]
    if sum_a < sum_b:
        return True
    else:
        return False


def p397b1(a: str, b: str) -> bool:
    """
    Try to complete the challenge without actually determining the numerical values of the inputs.
    :param a:
    :param b:
    :return:
    """


def p397b2(a: str, b:str) -> bool:
    """
    You don't need to handle subtractive notation (but you can if you want to, as an optional bonus).
    :param a:
    :param b:
    :return:
    """


def p397b3(a: str, b:str) -> bool:
    """
    You only need to correctly handle the case where there are at most 1 each of
    D, L, and V, and at most 4 each of C, X, and I.
    You don't need to validate the input, but you can if you want.
    :param a:
    :param b:
    :return:
    """
    roman_to_arabic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    sum_a = 0
    sum_b = 0
    for a_, b_ in zip_longest([c for c in a], [c for c in b], fillvalue='-'):
        sum_a += roman_to_arabic[a_] if a_ in roman_to_arabic else 0
        sum_b += roman_to_arabic[b_] if b_ in roman_to_arabic else 0
    if sum_a < sum_b:
        return True
    else:
        return False

def test():
    assert not p397("I", "I")
    assert p397("I", "II")
    assert not p397("II", "I")
    assert not p397("V", "IIII")
    assert p397("MDCLXV", "MDCLXVI")
    assert not p397("MM", "MDCCCCLXXXXVIIII")
    print("Passed!")

test()