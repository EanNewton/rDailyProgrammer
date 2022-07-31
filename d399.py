from typing import Tuple


def p399(raw: str) -> int:
    """
    Assign every lowercase letter a value, from 1 for a to 26 for z.
    Given a string of lowercase letters, find the sum of the values of the letters in the string.
    :param raw:
    :return:
    """

    offset = ord('a') - 1
    sum = 0
    print(raw)
    for line in raw:
        for _ in line.strip():
            if _:
                print(f"Sum: {sum}")
                print(f"{_}: {ord(_)}")
                sum += ord(_) - offset
    return sum


# Bonus Challenges
# use the enable1 word list:
# https://raw.githubusercontent.com/dolph/dictionary/master/enable1.txt
def d399b1() -> str:
    """
    microspectrophotometries is the only word with a letter sum of 317. Find the only word with a letter sum of 319.
    :return:
    """


def d399b2() -> int:
    """
    How many words have an odd letter sum?
    :return:
    """


def d399b3() -> Tuple[int, str]:
    """
    There are 1921 words with a letter sum of 100, making it the second most common letter sum.
    What letter sum is most common, and how many words have it?
    :return:
    """


def d399b4() -> Tuple[str, str]:
    """
    zyzzyva and biodegradabilities have the same letter sum as each other (151),
    and their lengths differ by 11 letters.
    Find the other pair of words with the same letter sum whose lengths differ by 11 letters.
    :return:
    """


def d399b5() -> Tuple[str, str]:
    """
    cytotoxicity and unreservedness have the same letter sum as each other (188), and they have no letters in common.
    Find a pair of words that have no letters in common,
    and that have the same letter sum, which is larger than 188.
    (There are two such pairs, and one word appears in both pairs.)
    :return:
    """


def d399b6() -> Tuple[list, int]:
    """
    The list of word { geographically, eavesdropper, woodworker, oxymorons } contains 4 words.
    Each word in the list has both a different number of letters, and a different letter sum.
    The list is sorted both in descending order of word length, and ascending order of letter sum.
    hat's the longest such list you can find?
    :return:
    """
