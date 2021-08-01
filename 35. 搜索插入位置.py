class Solution:
    def searchInsert(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                 left = middle + 1
            else:
                right = middle - 1
        return 1+(left + right) // 2

my = Solution()
nums = [1,3,5,6]
target = 0
print(my.searchInsert(nums, target))
      