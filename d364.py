import random


def p364(raw: str) -> int:
    """
    Dice Roller [Easy]

    Input description

    Your input will contain one or more lines, where each line will be in the form of "NdM"; for example:

    3d6
    4d12
    1d10
    5d4

    If you've ever played D&D you probably recognize those, but for the rest of you, this is what those mean:

    The first number is the number of dice to roll, the d just means "dice", it's just used to split up
    the two numbers, and the second number is how many sides the dice have. So the above example of "3d6" means
    "roll 3 6-sided dice". Also, just in case you didn't know, in D&D, not all the dice we roll are the normal cubes.
    A d6 is a cube, because it's a 6-sided die, but a d20 has twenty sides,
    so it looks a lot closer to a ball than a cube.

    The first number, the number of dice to roll, can be any integer between 1 and 100, inclusive.

    The second number, the number of sides of the dice, can be any integer between 2 and 100, inclusive.
    Output description

    You should output the sum of all the rolls of that specified die, each on their own line.
    so if your input is "3d6", the output should look something like

    14

    Just a single number, you rolled 3 6-sided dice, and they added up to 14.
    :param raw:
    :return:
    """
    vars = list(map(int, raw.split('d')))
    if vars[0] > 0 and vars[1] > 0:
        result = sum([random.randint(1, vars[1]) for _ in range(vars[0])])
        print(f"{raw} => {result}")
        return result


def b1(raw: str) -> str:
    """
    In addition to the sum of all dice rolls for your output, print out the result of each roll on the same line,
    using a format that looks something like

    14: 6 3 5
    22: 10 7 1 4
    9: 9
    11: 3 2 2 1 3

    You could also try setting it up so that you can manually input more rolls.
    that way you can just leave the program open and every time you want to roll more dice,
    you just type it in and hit enter.
    :param raw:
    :return:
    """
    vars = list(map(int, raw.split('d')))
    if vars[0] > 0 and vars[1] > 0:
        result = [random.randint(1, vars[1]) for _ in range(vars[0])]
        result = (f"{raw} => {sum(result)}: {result}")
        print(result)
        return result


def test() -> bool:
    p364('1d1')
    p364('5d1')
    p364('5d0')
    p364('5d12')
    p364('6d4')
    p364('1d2')
    p364('1d8')
    p364('3d6')
    p364('4d20')
    p364('100d100')
    print("Passed!")
    return True

def testb1() -> bool:
    b1('1d1')
    b1('5d1')
    b1('5d0')
    b1('5d12')
    b1('6d4')
    b1('1d2')
    b1('1d8')
    b1('3d6')
    b1('4d20')
    b1('100d100')
    print("Passed!")
    return True


test()
testb1()