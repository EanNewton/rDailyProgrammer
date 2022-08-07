import string


def p387(c: str, n: int) -> str:
    """
    Caesar Cipher [Easy]

    Warmup

    Given a lowercase letter and a number between 0 and 26, return that letter Caesar shifted by that number.
    To Caesar shift a letter by a number, advance it in the alphabet by that many steps,
    wrapping around from z back to a:

    warmup('a', 0) => 'a'
    warmup('a', 1) => 'b'
    warmup('a', 5) => 'f'
    warmup('a', 26) => 'a'
    warmup('d', 15) => 's'
    warmup('z', 1) => 'a'
    warmup('q', 22) => 'm'

    Hint: taking a number modulo 26 will wrap around from 25 back to 0.
    This is commonly represented using the modulus operator %. For example, 29 % 26 = 3.
    Finding a way to map from the letters a-z to the numbers 0-25 and back will help.
    :param c:
    :param n:
    :return:
    """

    alphabet = string.ascii_lowercase
    mod = (n + alphabet.index(c)) % 26
    # print(f"{c:<1} {n:^2} => {alphabet[mod]:>1}")
    return alphabet[mod]


def p387b1(raw: str, n: int) -> str:
    """
    Given a string of lowercase letters and a number,
    return a string with each letter Caesar shifted by the given amount.

    caesar("a", 1) => "b"
    caesar("abcz", 1) => "bcda"
    caesar("irk", 13) => "vex"
    caesar("fusion", 6) => "layout"
    caesar("dailyprogrammer", 6) => "jgorevxumxgsskx"
    caesar("jgorevxumxgsskx", 20) => "dailyprogrammer"

    Hint: you can use the warmup function as a helper function.
    :param raw:
    :param n:
    :return:
    """
    result = []
    for char in raw:
        result.append(p387(char, n))
    result = "".join(result)
    # print(f"{raw:<{len(raw)}} {n:^2} => {result:>{len(result)}}")
    return result


def p387b2(raw: str, n: int) -> str:
    """
    Correctly handle capital letters and non-letter characters.
    Capital letters should also be shifted like lowercase letters, but remain capitalized. Leave non-letter characters,
    such as spaces and punctuation, unshifted.

    caesar("Daily Programmer!", 6) => "Jgore Vxumxgsskx!"

    If you speak a language that doesn't use the 26-letter A-Z alphabet that English does,
    handle strings in that language in whatever way makes the most sense to you! In English,
    if a string is encoded using the number N, you can decode it using the number 26 - N.
    Make sure that for your language, there's some similar way to decode strings.
    :param raw:
    :param n:
    :return:
    """
    alphabet = [string.ascii_lowercase, string.ascii_uppercase]
    result = []
    for char in raw:
        if char in alphabet[0]:
            mod = (n + alphabet[0].index(char)) % 26
            result.append(alphabet[0][mod])
        elif char in alphabet[1]:
            mod = (n + alphabet[1].index(char)) % 26
            result.append(alphabet[1][mod])
        else:
            result.append(char)
    result = "".join(result)
    # print(f"{raw:<{len(raw)}} {n:^2} => {result:>{len(result)}}")
    return result


def p387b3(raw: str) -> str:
    """
    Given a string of English text that has been Caesar shifted by some number between 0 and 26,
    write a function to make a best guess of what the original string was.
    You can typically do this by hand easily enough, but the challenge is to write a program to do it automatically.
    Decode the following strings:

    Zol abyulk tl puav h ulda.

    Tfdv ef wlikyvi, wfi uvrky rnrzkj pfl rcc nzky erjkp, szx, gfzekp kvvky.

    Qv wzlmz bw uiqvbiqv iqz-axmml dmtwkqbg, i aeittwe vmmla bw jmib qba eqvoa nwzbg-bpzmm bquma mdmzg amkwvl, zqopb?

    One simple way is by using a letter frequency table. Assign each letter in the string a score,
    with 3 for a, -1 for b, 1 for c, etc., as follows:

    3,-1,1,1,4,0,0,2,2,-5,-2,1,0,2,3,0,-6,2,2,3,1,-1,0,-5,0,-7

    The average score of the letters in a string will tell you how its letter distribution compares to typical English.
    Higher is better. Typical English will have an average score around 2, and strings of random letters will have an
    average score around 0. Just test out each possible shift for the string, and take the one with the highest score.
    There are other good ways to do it, though.

    (This challenge is based on Challenge #47 [easy], originally posted by u/oskar_s
    in May 2012.)
    :param raw:
    :return:
    """
    alphabet = string.ascii_lowercase
    scoreboard = [3,-1,1,1,4,0,0,2,2,-5,-2,1,0,2,3,0,-6,2,2,3,1,-1,0,-5,0,-7]
    score = None
    index_max = 0
    for _ in range(26):
        test_score = 0
        for c in p387b2(raw, _):
            if c.lower() in alphabet:
                test_score += scoreboard[alphabet.index(c.lower())]
        # print(f"score: {score} test_score: {test_score}")
        if not score or test_score > score:
            score = test_score
            index_max = _
    result = p387b2(raw, index_max)
    print(f"{raw} {index_max}\n=> {result}")
    return result

# A="abcdefghijklmnopqrstuvwxyz"
# from string import ascii_lowercase as A
A=list(map(chr,range(65,91)))
def p012(s,n):
    i=lambda _:((n+A.index(_.upper()))%26)
    return"".join([(A[i(c)].lower(),A[i(c)])[c in A]if c.upper()in A else c for c in s])
def p3(r):
    M=[sum([3,-1,1,1,4,0,0,2,2,-5,-2,1,0,2,3,0,-6,2,2,3,1,-1,0,-5,0,-7][A.index(c.upper())]if c.upper()in A else 0for c in p012(r,_))for _ in range(26)]
    return p012(r,M.index(max(M)))


def test() -> bool:
    assert p387('a', 0) == 'a'
    assert p387('a', 1) == 'b'
    assert p387('a', 5) == 'f'
    assert p387('a', 26) == 'a'
    assert p387('d', 15) == 's'
    assert p387('z', 1) == 'a'
    assert p387('q', 22) == 'm'
    print("Passed!")
    return True


def testb1() -> bool:
    assert p387b1('a', 1) == 'b'
    assert p387b1('abcz', 1) == 'bcda'
    assert p387b1('irk', 13) == 'vex'
    assert p387b1('fusion', 6) == 'layout'
    assert p387b1('dailyprogrammer', 6) == 'jgorevxumxgsskx'
    assert p387b1('jgorevxumxgsskx', 20) == 'dailyprogrammer'
    print("Passed!")
    return True


def testb2() -> bool:
    assert p387b2("Daily Programmer!", 6) == "Jgore Vxumxgsskx!"
    print("Passed!")
    return True


def testb2g() -> bool:
    assert p012("Daily Programmer!", 6) == "Jgore Vxumxgsskx!"
    print("Passed!")
    return True


def testb3() -> bool:
    print(p387b3("Zol abyulk tl puav h ulda."))
    print(p387b3("Tfdv ef wlikyvi, wfi uvrky rnrzkj pfl rcc nzky erjkp, szx, gfzekp kvvky."))
    print(p387b3("Qv wzlmz bw uiqvbiqv iqz-axmml dmtwkqbg, "
                 "i aeittwe vmmla bw jmib qba eqvoa nwzbg-bpzmm bquma mdmzg amkwvl, zqopb?"))


def testb3g() -> bool:
    print(p3("Zol abyulk tl puav h ulda."))
    print(p3("Tfdv ef wlikyvi, wfi uvrky rnrzkj pfl rcc nzky erjkp, szx, gfzekp kvvky."))
    print(p3("Qv wzlmz bw uiqvbiqv iqz-axmml dmtwkqbg, "
                 "i aeittwe vmmla bw jmib qba eqvoa nwzbg-bpzmm bquma mdmzg amkwvl, zqopb?"))


# test()
# testb1()
# testb2()
# testb2g()
# testb3()
testb3g()
