class Solution:
    def rob(self, nums) -> int:
        # ans 是取最后一个的答案
        ans = [0]*(len(nums)+5)
        ans[0] = nums[0]
        if len(nums) <= 1:
            return ans[len(nums)-1]
        ans[1] = nums[1]
        if len(nums) <= 2:
            return max(ans[len(nums)-1], ans[0])
        ans[2] = nums[0] + nums[2]
        for i in range(3, len(nums)):
            ans[i] = max(nums[i] + ans[i-2], nums[i] + ans[i-3])
        return max(ans[len(nums)-1], ans[len(nums)-2])

Solution().rob([1, 3, 4,6])