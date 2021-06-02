"""leetcode: 5 Longest Palindromic Substring
"""

from typing import Tuple


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
            xs = memoization(s[:-1])
            ys = memoization(s[1:])
            if len(xs) >= len(ys): memo[s] = xs
            else: memo[s] = ys
        return memo[s]
    
    def ispalindrome_with_index(s: str, start: int, end: int) -> bool:
        end = end - 1
        while s[start] == s[end] and start < end:
            start += 1
            end -= 1
        return start >= end
    
    def memoization_optimization_1(
        s: str, start: int, end: int, memo={}) -> Tuple[int, int]:
        if end - start == 1: return (start, end)
        if (start, end) in memo: return memo[(start, end)]
        if ispalindrome_with_index(s, start, end):
            memo[(start, end)] = (start, end)
        else:
            i, j = memoization_optimization_1(s, start+1, end, memo)
            x, y = memoization_optimization_1(s, start, end-1, memo)
            if j - i > y - x:
                memo[(start, end)] = (i, j)
            else:
                memo[(start, end)] = (x, y)
        return memo[(start, end)]
                
    def naive(s):
        if ispalindrome(s): return s
        xs = naive(s[1:])
        ys = naive(s[:-1])
        if len(xs) > len(ys): return xs
        else: return ys
    
    istart, iend = memoization_optimization_1(s, 0, len(s))
    return s[istart:iend]

assert longest_palindromic_substring("babad") == "bab"
assert longest_palindromic_substring("cbbd") == "bb"
assert longest_palindromic_substring("a") == "a"
assert longest_palindromic_substring("ac") == "a"
assert longest_palindromic_substring("bjaa") == "aa"
assert longest_palindromic_substring("eabcb") == "bcb"

import time
s = time.time()
print(longest_palindromic_substring("esbtzjaaijqkgmtaajpsdfiqtvxsgfvijpxrvxgfumsuprzlyvhclgkhccmcnquukivlpnjlfteljvykbddtrpmxzcrdqinsnlsteonhcegtkoszzonkwjevlasgjlcquzuhdmmkhfniozhuphcfkeobturbuoefhmtgcvhlsezvkpgfebbdbhiuwdcftenihseorykdguoqotqyscwymtjejpdzqepjkadtftzwebxwyuqwyeegwxhroaaymusddwnjkvsvrwwsmolmidoybsotaqufhepinkkxicvzrgbgsarmizugbvtzfxghkhthzpuetufqvigmyhmlsgfaaqmmlblxbqxpluhaawqkdluwfirfngbhdkjjyfsxglsnakskcbsyafqpwmwmoxjwlhjduayqyzmpkmrjhbqyhongfdxmuwaqgjkcpatgbrqdllbzodnrifvhcfvgbixbwywanivsdjnbrgskyifgvksadvgzzzuogzcukskjxbohofdimkmyqypyuexypwnjlrfpbtkqyngvxjcwvngmilgwbpcsseoywetatfjijsbcekaixvqreelnlmdonknmxerjjhvmqiztsgjkijjtcyetuygqgsikxctvpxrqtuhxreidhwcklkkjayvqdzqqapgdqaapefzjfngdvjsiiivnkfimqkkucltgavwlakcfyhnpgmqxgfyjziliyqhugphhjtlllgtlcsibfdktzhcfuallqlonbsgyyvvyarvaxmchtyrtkgekkmhejwvsuumhcfcyncgeqtltfmhtlsfswaqpmwpjwgvksvazhwyrzwhyjjdbphhjcmurdcgtbvpkhbkpirhysrpcrntetacyfvgjivhaxgpqhbjahruuejdmaghoaquhiafjqaionbrjbjksxaezosxqmncejjptcksnoq"))
e = time.time() - s
print(f"total run time: {e}")