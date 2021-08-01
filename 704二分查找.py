class Solution:
    def search(self, nums, target):
        left = 0
        right = len(nums)
        while left < right:
            middle = (left + right) // 2
            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                left = middle
            else:
                right = middle
        return -1

my = Solution()
nums = [-1,0,3,5,9,12]
target = 2
print(my.search(nums, target))

            
