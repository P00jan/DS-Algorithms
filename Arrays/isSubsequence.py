"""
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).
"""
class Solution:
    def isSubsequence(s: str, t: str) -> bool:
        for c in s:
            i = t.find(c)
            if i == -1:
                return False
            else:
                t = t[i+1:]
        return True
s1 = "abc"
t1 = "axvbdc"
result1 = Solution.isSubsequence(s1, t1) 
print(f"S is the subsequence of T: {result1}")

s2 = "abc"
t2 = "bjckza"
result2 = Solution.isSubsequence(s2,t2)
print(f"S is the subsequence of T: {result2}")

