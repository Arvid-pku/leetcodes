List = list
class Solution:
    def singleNumber(self, nums: List) -> int:
        ans = 0
        for num in nums:
            ans = ans ^ num
        return ans