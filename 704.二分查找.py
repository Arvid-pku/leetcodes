class Solution:
    def search(self, nums, target):
        left = 0
        right = len(nums) - 1 # error
        while left <= right:  # error
            middle = (left + right) // 2
            print(left, right, middle, len(nums))
            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                left = middle + 1 # error
            else:
                right = middle - 1
                  
        return -1

my = Solution()
nums = [-1,0,3,5,9,12]
target = 13
print(my.search(nums, target))

            
