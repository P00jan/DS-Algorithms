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