from collections import Counter

def longest_palindrome(s: str) -> int:
    """Given a string s, find the maximum length of 
    self constructed palindrome"""
    
    cnt = Counter()

    for char in s:
        cnt[char] += 1

    

