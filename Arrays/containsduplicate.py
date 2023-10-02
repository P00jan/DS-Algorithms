"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
"""
class Solution:
    def containsDuplicate(nums: list[int]) -> bool:
        hashset = set()
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False

# Test with different values
nums1 = [1, 2, 3, 4, 5]
result1 = Solution.containsDuplicate(nums1)
print(f"Result for nums1: {result1}")  # Should print "Result for nums1: False"

nums2 = [1, 2, 3, 2, 4, 5]
result2 = Solution.containsDuplicate(nums2)
print(f"Result for nums2: {result2}")  # Should print "Result for nums2: True"

nums3 = [1, 1, 2, 2, 3, 3]
result3 = Solution.containsDuplicate(nums3)
print(f"Result for nums3: {result3}")  # Should print "Result for nums3: True"



'''
Output:
Result for nums1: False
Result for nums2: True
Result for nums3: True

Explanation:
We take nums in list form and except whatever the return we will get from funtion will be boolean which is true or false
After that we create a hashset and we will iterate each element from nums and check if it is there in hashset or not, if it is 
already there then we will return true and if it is not there then we will add that element to our hashset.
'''