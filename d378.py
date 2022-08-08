def w1(raw: list) -> list:
    """
    Given a sequence of answers, return the same set of answers with all the 0's removed.
    :param raw:
    :return:
    """
    return [x for x in raw if x != 0]


def w2(raw: list) -> list:
    """
    Given a sequence of answers, return the sequence sorted in descending order,
    so that the first number is the largest and the last number is the smallest.
    :param raw:
    :return:
    """
    raw.sort()
    return raw[::-1]


def w3(n: int, raw: list) -> bool:
    """
    Given a number N and a sequence of answers, return True if N is greater than the number of answers
    (i.e. the length of the sequence), and False if N is less than or equal to the number of answers.
    For instance, given 7 and [6, 5, 5, 3, 2, 2, 2], you would return False, because 7 is less than or equal to 7.
    :param n:
    :param raw:
    :return:
    """
    return True if n > len(raw) else False


def w4(n: int, raw: list) -> list:
    """
    Given a number N and a sequence in descending order, subtract 1 from each of the first N answers in the sequence,
    and return the result. For instance, given N = 4 and the sequence [5, 4, 3, 2, 1], you would subtract 1 from
    each of the first 4 answers (5, 4, 3, and 2) to get 4, 3, 2, and 1.
    The rest of the sequence (1) would not be affected:
    :param n:
    :param raw:
    :return:
    """
    return [raw[x] - 1 if n > x else raw[x] for x in range(len(raw))]


def p378(raw: list) -> bool:
    """
    Havel-Hakimi Algorithm [Easy]
    Perform the Havel-Hakimi algorithm on a given sequence of answers.
    This algorithm will return true if the answers are consistent (i.e. it's possible that
    everyone is telling the truth) and false if the answers are inconsistent (i.e. someone must be lying):

        Remove all 0's from the sequence (i.e. warmup1).
        If the sequence is now empty (no elements left), stop and return true.
        Sort the sequence in descending order (i.e. warmup2).
        Remove the first answer (which is also the largest answer, or tied for the largest) from the sequence and
            call it N. The sequence is now 1 shorter than it was after the previous step.
        If N is greater than the length of this new sequence (i.e. warmup3), stop and return false.
        Subtract 1 from each of the first N elements of the new sequence (i.e. warmup4).
        Continue from step 1 using the sequence from the previous step.

    Eventually you'll either return true in step 2, or false in step 5.

    You don't have to follow these steps exactly: as long as you return the right answer, that's fine.
    Also, if you answered the warmup questions, you may use your warmup solutions to build your challenge solution,
    but you don't have to.
    :param raw:
    :return:
    """
    raw = w1(raw)
    if len(raw) == 0:
        return True
    raw = w2(raw)
    n = raw.pop(0)
    if n > len(raw):
        return False
    raw = w4(n, raw)
    return p378(raw)


def c1(r):
    r=[_ for _ in r if _!=0]
    if len(r)==0:return 1
    r.sort()
    r=r[::-1]
    n=r.pop(0)
    if n>len(r):return 0
    r=[r[_]-1if n>_ else r[_]for _ in range(len(r))]
    return c1(r)


def test_w4():
    assert w4(4, [5, 4, 3, 2, 1]) == [4, 3, 2, 1, 1]
    assert w4(11, [14, 13, 13, 13, 12, 10, 8, 8, 7, 7, 6, 6, 4, 4, 2]) == [13, 12, 12, 12, 11, 9, 7, 7, 6, 6, 5, 6, 4, 4, 2]
    assert w4(1, [10, 10, 10]) == [9, 10, 10]
    assert w4(3, [10, 10, 10]) == [9, 9, 9]
    assert w4(1, [1]) == [0]
    print("Passed!")
    
def test():
    assert p378([5, 3, 0, 2, 6, 2, 0, 7, 2, 5]) == False
    assert p378([4, 2, 0, 1, 5, 0]) == False
    assert p378([3, 1, 2, 3, 1, 0]) == True
    assert p378([16, 9, 9, 15, 9, 7, 9, 11, 17, 11, 4, 9, 12, 14, 14, 12, 17, 0, 3, 16]) == True
    assert p378([14, 10, 17, 13, 4, 8, 6, 7, 13, 13, 17, 18, 8, 17, 2, 14, 6, 4, 7, 12]) == True
    assert p378([15, 18, 6, 13, 12, 4, 4, 14, 1, 6, 18, 2, 6, 16, 0, 9, 10, 7, 12, 3]) == False
    assert p378([6, 0, 10, 10, 10, 5, 8, 3, 0, 14, 16, 2, 13, 1, 2, 13, 6, 15, 5, 1]) == False
    assert p378([2, 2, 0]) == False
    assert p378([3, 2, 1]) == False
    assert p378([1, 1]) == True
    assert p378([1]) == False
    assert p378([]) == True
    print("Passed!")

# test_w4()
test()