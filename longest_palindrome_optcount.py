from collections import Counter

"""leetcode: 409. Longest Palindrome"""
def longest_palindrome(s: str) -> int:
    """find the length of longest palindrome of string s.
    
    Parameters
    ----------
    s: string/characters used to construct the longest palindromes
    """
    even = 0
    carrier = 0
 
    for v in Counter(s).values():
        if v % 2 == 0:
            even += v
        elif v % 2 == 1 and v > 1:
            even += v - 1
            carrier = 1
        elif v == 1:
            carrier = 1
    return even + carrier

assert longest_palindrome("abccccdd") == 7
assert longest_palindrome("a") == 1
assert longest_palindrome("bb") == 2
