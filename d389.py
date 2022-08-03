from random import shuffle, choice


def p389(contestant: list) -> float:
    """
    The Monty Hall Problem [Easy]
    For the purpose of today's challenge, the Monty Hall scenario goes like this:

    1) There are three closed doors, labeled #1, #2, and #3. Monty Hall randomly selects one of the three doors and
    puts a prize behind it. The other two doors hide nothing.

    2) A contestant, who does not know where the prize is, selects one of the three doors.
    This door is not opened yet.

    3) Monty chooses one of the three doors and opens it.
    The door that Monty opens (a) does not hide the prize,
    and (b) is not the door that the contestant selected. T
    here may be one or two such doors. If there are two, Monty randomly selects one or the other.

    4) There are now two closed doors, the one the contestant selected in step 2, and one they didn't select.
    The contestant decides whether to keep their original choice, or to switch to the other closed door.

    5) The contestant wins if the door they selected in step 4 is
    the same as the one Monty put a prize behind in step 1.

    Challenge
    A contestant's strategy is given by their choices in steps 2 and 4. Write a program to determine the success rate
    of a contestant's strategy by simulating the game 1000 times and calculating the fraction of the times
    the contestant wins. Determine the success rate for these two contestants:

    Alice chooses door #1 in step 2, and always sticks with door #1 in step 4.
    Bob chooses door #1 in step 2, and always switches to the other closed door in step 4.

    :param n:
    :return:
    """
    doors = [True, False, False]
    shuffle(doors)
    monty = 0
    while monty == contestant[0] or doors[monty]:
        monty = choice((0, 1, 2))
    doors.pop(monty)
    if contestant[1](monty):
        # print("switching doors!")
        (doors.pop(-1) if contestant[0] == 2 else doors.pop(contestant[0]))
        return doors[0]
    # print("staying with my door!")
    return doors[-1] if contestant[0] == 2 else doors[contestant[0]]


def p389b1():
    """
    Optional bonus
    Find success rates for these other contestants:

    Carol chooses randomly from the available options in both step 2 and step 4.

    Dave chooses randomly in step 2, and always sticks with his door in step 4.

    Erin chooses randomly in step 2, and always switches in step 4.

    Frank chooses door #1 in step 2, and switches to door #2 if available in step 4.
    If door #2 is not available because it was opened, then he stays with door #1.

    Gina always uses either Alice's or Bob's strategy.
    She remembers whether her previous strategy worked and changes it accordingly.
    On her first game, she uses Alice's strategy. Thereafter, if she won the previous game, then she sticks with
    the same strategy as the previous game. If she lost the previous game, then she switches
    (Alice to Bob or Bob to Alice).

    It's possible to calculate all of these probabilities without doing any simulation, of course,
    but today's challenge is to find the fractions through simulation.
    (This is a repost of Challenge #49 [easy], originally posted by u/oskar_s
    in May 2012.
    https://www.reddit.com/r/dailyprogrammer/comments/tb2h0/572012_challenge_49_easy/
    )
    :return:
    """
    pass


def test():
    alice = [0, lambda _: False]
    bob = [0, lambda _: True]
    carol = [choice((0, 1, 2)), lambda _: choice((True, False))]
    dave = [choice((0, 1, 2)), lambda _: False]
    erin = [choice((0, 1, 2)), lambda _: True]
    frank = [0, lambda x: True if x != 1 else False]
    gina = None

    def monty(contestant=None) -> str:
        if contestant is None:
            contestant = [0, lambda _: True]
        wins = 0
        gina_last = [alice, bob]
        for _ in range(1000):
            gina = gina_last[0]
            if p389(contestant):
                wins += 1
            gina_last = gina_last[::-1]
        return f"{float(wins / 1000):.2%}"

    print(f"Alice: {monty(alice)}")
    print(f"Bob: {monty(bob)}")
    print(f"Carol: {monty(carol)}")
    print(f"Dave: {monty(dave)}")
    print(f"Erin: {monty(erin)}")
    print(f"Frank: {monty(frank)}")
    print(f"Gina: {monty(gina)}")

test()