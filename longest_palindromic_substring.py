"""leetcode: 5 Longest Palindromic Substring
"""

def longest_palindromic_substring(s: str) -> str:
    """Given string s, return the longest palindromic substring in s
    
    Parameters
    ----------
    s: string s that are used to construct the substring s
    """
    def ispalindrome(s: str) -> bool:
        ptr1 = 0
        ptr2 = len(s) - 1
        while s[ptr1] == s[ptr2] and ptr1 < ptr2:
            ptr1 += 1
            ptr2 -= 1
        return (ptr1 >= ptr2)
    
    def memoization(s, memo={}):
        if not s: return ""
        if s in memo.keys(): return memo[s]
        
        if ispalindrome(s):
            memo[s] = s
        else:
            xs = helper(s[:-1])
            ys = helper(s[1:])
            if len(xs) >= len(ys): memo[s] = xs
            else: memo[s] = ys
        return memo[s]
    
    def naive(s):
        if ispalindrome(s): return s
        xs = naive(s[1:])
        ys = naive(s[:-1])
        if len(xs) > len(ys): return xs
        else: return ys
    
    return memoization(s)

assert longest_palindromic_substring("babad") == "bab"
assert longest_palindromic_substring("cbbd") == "bb"
assert longest_palindromic_substring("a") == "a"
assert longest_palindromic_substring("ac") == "a"
