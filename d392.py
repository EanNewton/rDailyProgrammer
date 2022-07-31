from copy import deepcopy


def p392(raw: list, n: int) -> list:
    """
    Pancake Sort [Intermediate]

    Implement the flipfront function. Given an array of integers and a number n between 2 and the length of
    the array (inclusive), return the array with the order of the first n elements reversed.

    flipfront([0, 1, 2, 3, 4], 2) => [1, 0, 2, 3, 4]
    flipfront([0, 1, 2, 3, 4], 3) => [2, 1, 0, 3, 4]
    flipfront([0, 1, 2, 3, 4], 5) => [4, 3, 2, 1, 0]
    flipfront([1, 2, 2, 2], 3) => [2, 2, 1, 2]

    Optionally, as an optimization, modify the array in-place (in which case you don't need to return it).
    It's also fine to have the array be a global variable or member variable,
    in which case you only need to pass in the argument n.
    :param raw: 
    :param n:
    :return:
    """
    # raw[:n] = raw[:n][::-1]
    # return raw
    return [a for b in [raw[:n][::-1], raw[n:]] for a in b]


def p392b1(raw: list) -> list:
    """
    Given an array of integers, sort the array (smallest to largest) using the flipfront function on the entire array.
    For example, the array:

    [3, 1, 2, 1]

    may be sorted with three calls to flipfront:

    flipfront([3, 1, 2, 1], 4) => [1, 2, 1, 3]
    flipfront([1, 2, 1, 3], 2) => [2, 1, 1, 3]
    flipfront([2, 1, 1, 3], 3) => [1, 1, 2, 3]

    Make sure you correctly handle elements that appear more than once in the array!

    You may not modify the array by any other means, but you may examine it however you want.
    You can even make a copy of the array and manipulate the copy, including sorting it using some other algorithm.
    :param raw:
    :return:
    """
    sorted_ = deepcopy(raw)
    sorted_.sort()
    print(f"New Bonus: {raw}")
    while raw != sorted_:
        pass
    return raw


def p392b2(raw: list) -> int:
    """
    Try to minimize the number of times you call flipfront while sorting.
    Note that this is different from minimizing the runtime of your program.

    How many flipfront calls do you require to sort this list of 10,000 integers?
    My record is 11,930. Can you do better?
    https://gist.githubusercontent.com/cosmologicon/9e6e430d29023f24d1b885fd9c175603/raw/ea5f00e1b84eb963dd1a2f5159a49b5a6d0320f7/gistfile1.txt

    (This is a repost of Challenge #63 [intermediate], originally posted by u/oskar_s
    in June 2012.
    https://www.reddit.com/r/dailyprogrammer/comments/uw16v/6112012_challenge_63_intermediate/
    )
    :param raw:
    :return:
    """

    
def test() -> bool:
    assert p392([0, 1, 2, 3, 4], 2) == [1, 0, 2, 3, 4]
    assert p392([0, 1, 2, 3, 4], 3) == [2, 1, 0, 3, 4]
    assert p392([0, 1, 2, 3, 4], 5) == [4, 3, 2, 1, 0]
    assert p392([1, 2, 2, 2], 3) == [2, 2, 1, 2]
    print("Passed!")
    assert p392b1([3, 1, 2, 1]) == [1, 1, 2, 3]
    assert p392b1([4, 8, 1, 3]) == [1, 3, 4, 8]
    assert p392b1([2, 1, 0, 5, 1, 3]) == [0, 1, 1, 2, 3, 5]
    print("Passed!")
    return True


test()