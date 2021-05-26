from collections import Counter

"""leetcode: 409. Longest Palindrome"""
def longest_palindrome(s: str) -> int:
    """find the length of longest palindrome of string s.
    
    Parameters
    ----------
    s: string/characters used to construct the longest palindromes
    """
    ret = 0
    carrier = 0
    if len(s) == 0: return ret
    for v in Counter(s).itervalues():
        if v % 2 == 0:
            ret += v
        elif v % 2 == 1 and v > 1:
            ret += v - 1
            carrier = 1
        elif v == 1:
            carrier = 1
    return ret + carrier

assert longest_palindrome("abccccdd") == 7
assert longest_palindrome("a") == 1
assert longest_palindrome("bb") == 2
