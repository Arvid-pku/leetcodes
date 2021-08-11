class Solution:
    def permute(self, nums):
        ans = []
        now = []
        self.getall(nums, len(nums), ans, now)
        return ans

    def getall(self, lis, k, ans, now):
        if k == 0:
            ans.append(now)
            return
        mynow = now[:]
        for i in range(len(lis)):
            mynow.append(lis[i])
            
            if len(lis) - i > 0:
                self.getall(lis[0:i]+lis[i+1:], k-1, ans, mynow)
            # 回溯
            mynow = now[:]


x = Solution().permute([1, 2,3 ,4])
print(x)