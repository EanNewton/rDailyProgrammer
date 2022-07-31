def p393(raw: int) -> int:
    """
    Making Change [Easy]

    The country of Examplania has coins that are worth 1, 5, 10, 25, 100, and 500 currency units.
    At the Zeroth Bank of Examplania, you are trained to make various amounts of money by using as many ¤500 coins as
     possible, then as many ¤100 coins as possible, and so on down.

    For instance, if you want to give someone ¤468, you would give them four ¤100 coins, two ¤25 coins, one ¤10 coin,
    one ¤5 coin, and three ¤1 coins, for a total of 11 coins.

    Write a function to return the number of coins you use to make a given amount of change.

    change(0) => 0
    change(12) => 3
    change(468) => 11
    change(123456) => 254

    (This is a repost of Challenge #65 [easy], originally posted by u/oskar_s
    in June 2012.
    https://www.reddit.com/r/dailyprogrammer/comments/v3a89/6152012_challenge_65_easy/
    )
    :param raw:
    :return:
    """

    result = 0
    print(f"\nNew - {raw}\n")
    for op in [500, 100, 25, 10, 5, 1]:
        print(op)
        while raw - op >= 0:
            result += 1
            raw -= op
            print(raw, op, result)
    print(f"Returning: {result}")
    return result



def test() -> bool:
    assert p393(0) == 0
    assert p393(12) == 3
    assert p393(468) == 11
    assert p393(123456) == 254
    print("Passed!")
    return True

test()