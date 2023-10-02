"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
"""
class Solution:
    def isAnagram(s: str, t: str) -> bool:
        if len(s)!=len(t):
            return ("Length is not same")

        s_dict , t_dict = {},{}
        for char in s:
            s_dict[char]=s_dict.get(char,0) + 1
        for char in t:
            t_dict[char]=t_dict.get(char,0) + 1
        
        if s_dict == t_dict:
            return True
        else:
            return False
s1 = ("cat")
t1 = ("tbc")
result1 = Solution.isAnagram(s1, t1)
print(f"The given strings are anagram? -> {result1}")

s2 = ("rat")
t2 = ("tar")
result2 = Solution.isAnagram(s2, t2)
print(f"The given strings are anagram? -> {result2}")

s3 = ("marshal")
t3 = ("lashar")
result3 = Solution.isAnagram(s3, t3)
print(f"The given strings are anagram? -> {result3}")


"""
Output: 
The given strings are anagram? -> False
The given strings are anagram? -> True
The given strings are anagram? -> Length is not same

Explanation:
For the strings we will check the length first if it is not same there won't be no anagram either so we return length is not same.
If length is same we will take 2 empty dictionaries after that we will check the occurances of each character in the string with
.get method and will increment the value of the occurances with 1 , we will do same for another string.
Later we will match the dictionaries with the same length and defined occurances with eachother and if occurances of each character are same in both
strings then the output will be true.
"""