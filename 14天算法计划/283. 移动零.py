class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # error, sorted
        # myend = len(nums) - 1
        # mybegin = 0
        # while mybegin < myend:
        #     if mybegin == 0:
        #         x = nums[mybegin]
        #         nums[mybegin] = nums[myend]
        #         nums[myend] = x
        #         myend = myend - 1
        #     mybegin = mybegin + 1
        mylist = 0
        youlist = 0
        while youlist < len(nums):
            # error: not youlist, is nums[youlist]
            if nums[youlist] != 0:
                nums[mylist] = nums[youlist]
                mylist = mylist + 1
            youlist = youlist + 1
        for i in range(mylist, len(nums)):
            nums[i] = 0

nums = [0,1,0,3,12]
Solution().moveZeroes(nums)