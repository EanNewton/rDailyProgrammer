def p395(raw: list) -> list:
    """
    Nonogram Row [Easy]

    Given a binary array of any length, return an array of positive integers that represent the lengths of the sets of
    consecutive 1's in the input array, in order from left to right.

    (This challenge is based on Challenge #59 [intermediate], originally posted by u/oskar_s in June 2012.
    Nonograms have been featured multiple times on r/dailyprogrammer since then (search).
    https://www.reddit.com/r/dailyprogrammer/comments/uh03h/622012_challenge_59_intermediate/
    )
    :param raw:
    :return:
    """
    if len(raw) > 0:
        lengths = []
        sum = 0
        for i, _ in enumerate(raw):
            if i + 1 == len(raw):
                if raw[i] == 1:
                    sum += 1
                lengths.append(sum)
            elif _ == 0:
                lengths.append(sum)
                sum = 0
            else:
                sum += 1
        return [_ for _ in lengths if _ > 0]
    else:
        return []


def test() -> bool:
    assert p395([]) == []
    assert p395([0, 0, 0, 0, 0]) == []
    assert p395([1, 1, 1, 1, 1]) == [5]
    assert p395([0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1]) == [5, 4]
    assert p395([1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0]) == [2, 1, 3]
    assert p395([0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1]) == [2, 1, 3]
    assert p395([1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == [1, 1, 1, 1, 1, 1, 1, 1]
    print("Passed!")
    return True
