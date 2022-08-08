# def p383(raw1: str, raw2: str) -> bool:
#     """
#     Necklace Matching [Easy]
#
#     In this example, you could take the N off NICOLE and slide it around to the other end to make ICOLEN.
#     Do it again to get COLENI, and so on. For the purpose of today's challenge, we'll say that the
#     strings "nicole", "icolen", and "coleni" describe the same necklace.
#
#     Generally, two strings describe the same necklace if you can remove some number of letters from the
#      beginning of one, attach them to the end in their original ordering, and get the other string.
#      Reordering the letters in some other way does not, in general, produce a string that describes the same necklace.
#
#     Write a function that returns whether two strings describe the same necklace
#     :param raw1:
#     :param raw2:
#     :return:
#     """
#     return True if raw2 in [raw1[e:] + raw1[:e] for e in range(len(raw1) + 1)] else False

# def b1(raw: str) -> int:
#     """
#     If you have a string of N letters and you move each letter one at a time from the start to the end,
#     you'll eventually get back to the string you started with, after N steps. Sometimes,
#     you'll see the same string you started with before N steps. For instance, if you start with "abcabcabc",
#     you'll see the same string ("abcabcabc") 3 times over the course of moving a letter 9 times.
#
#     Write a function that returns the number of times you encounter the same starting string if
#     you move each letter in the string from the start to the end, one at a time.
#     :param raw:
#     :return:
#     """
#     if raw == "": return 1
#     return [raw[e:] + raw[:e] for e in range(len(raw))].count(raw)
from typing import Set
from time import perf_counter


def p383(r,R):
    return 1if R in[r[e:]+r[:e]for e in range(len(r)+1)]else 0

def b1(r):
    return[r[e:]+r[:e]for e in range(len(r))].count(r)if r else 1

def b2() -> set[str]:
    """
    There is exactly one set of four words in the enable1 word list that all describe the same necklace.
    Find the four words.
    https://raw.githubusercontent.com/dolph/dictionary/master/enable1.txt
    :param raw:
    :return:
    """
    vars = set()
    duplicates = dict()
    with open("d383b2", "r") as f:
        # Generate all possibilities
        for word in f:
            word = word.strip()
            # Searching for a match of 4, eliminate anything shorter as not possible
            if len(word) >= 4:
                var = [word[e:]+word[:e]for e in range(len(word)+1)]
                if len(var) > 3:
                    var.sort()
                    for perm in var:
                        if perm in vars:
                            duplicates[word] = var
                        else:
                            vars.add(perm)
    # Look for matches in dataset
    scores = dict()
    comps = [set(x) for x in duplicates.values()]
    tic = perf_counter()
    for i, key in enumerate(duplicates.keys()):
        count = 0
        for each in comps:
            if key in each:
                count += 1
        if count == 4:
            return comps[0]
        # Try to make it slightly faster (lol) over time by reducing # of entries needing scanned
        comps.pop(0)
        # Give user feedback so we know it hasn't crashed
        if i % 1000 == 0:
            toc = perf_counter()
            elapsed_time = toc - tic
            print(len(comps))
            print(f"Elapsed time: {elapsed_time:0.4f} seconds")
            print(f"[{i / len(duplicates):.2%}] -- {len(scores)}/{len(duplicates)}: {key}")
            tic = perf_counter()


def b2():
    V,d=set(),dict()
    with open("d383b2","r")as f:
        for w in f:
            if len(w)>3:
                v=[w[e:]+w[:e]for e in range(len(w)+1)]
                if len(v)>3:
                    for p in v:
                        if p in V:d[w]=v
                        else:V.add(p)
    C=[set(x)for x in d.values()]
    for i,k in enumerate(d.keys()):
        c=0
        for e in C:
            if k in e:c+=1
        if c==4:return C[0]



def test() -> bool:
    assert p383("nicole", "icolen") == True
    assert p383("nicole", "lenico") == True
    assert p383("nicole", "coneli") == False
    assert p383("aabaaaaabaab", "aabaabaabaaa") == True
    assert p383("abc", "cba") == False
    assert p383("xxyyy", "xxxyy") == False
    assert p383("xyxxz", "xxyxz") == False
    assert p383("x", "x") == True
    assert p383("x", "xx") == False
    assert p383("x", "") == False
    assert p383("", "") == True
    print("Passed!")
    return True

def testb1() -> bool:
    assert b1("abc") == 1
    assert b1("abcabcabc") == 3
    assert b1("abcabcabcx") == 1
    assert b1("aaaaaa") == 6
    assert b1("a") == 1
    assert b1("") == 1
    print("Passed!")
    return True


def testb2() -> bool:
    print(b2())

test()
testb1()
testb2()
