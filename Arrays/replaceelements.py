class Solution:
    def replaceElements(arr: list[int]) -> list[int]:
        maxNum = -1
        for i in range(len(arr) - 1, -1, -1):
            temp = maxNum
            if arr[i] > maxNum:
                maxNum = arr[i]
            arr[i] = temp
        return arr
arr1 = [17,18,4,5,6,1]
result1 = Solution.replaceElements(arr1)
print(f"The replaced elements are: {result1}")

arr2 = [1,2,14,19,5,4,8,4,2]
result2 = Solution.replaceElements(arr2)
print(f"The replaced elements are: {result2}")

"""
Output:
The replaced elements are: [18, 6, 6, 6, 1, -1]
The replaced elements are: [19, 19, 19, 8, 8, 8, 4, 2, -1]


Explanation:
We are assigning the max num with -1 and we start from reverse end as we always have to check 1 element if we 
start from beginning we have to check all the elements in the array, the logic is simple if the given element in array is bigger than the element 
we stored in temp variable it will replace it in temp and in array.
"""