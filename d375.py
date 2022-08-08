def p375(n: int) -> int:
    """
    Add one to each digit [Easy]
    A number is input in computer then a new no should get printed by adding one to each of its digit.
    If you encounter a 9, insert a 10 (don't carry over, just shift things around).

    For example, 998 becomes 10109.
    :param n:
    :return:
    """
    return int("".join([str(int(_)+1) for _ in str(n)]))

def test():
    assert p375(998) == 10109

test()