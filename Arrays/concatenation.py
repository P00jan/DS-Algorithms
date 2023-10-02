"""
Given an integer array nums of length n, you want to create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).

Specifically, ans is the concatenation of two nums arrays.

Return the array ans.
"""
class Solution:
    def getConcatenation(nums: list[int]) -> list[int]:
        ans = []    
        for i in range(2):
            for n in nums:
                ans.append(n)
        return ans
nums = [1,2,3]
result = Solution.getConcatenation(nums)
print(f"The concatenation of the array is: {result}")

"""
Output:
The concatenation of the array is: [1, 2, 3, 1, 2, 3]

Explanation:
We are taking the empty array/list and running 2 loops, the first loop is for how many times you want to concatenate and 
the second loop is to concatenate each number in nums array/list to the ans array/list
"""