class Solution:
    def climbStairs(self, n: int) -> int:
        ans = [-1]*n
        if n >= 1:
            ans[0] = 1
        if n >= 2:
            ans[1] = 2
        if n >= 3:
            ans[2] = 3
        self.myf(ans, n)
        return ans[n-1]
    def myf(self, ans, n):
        if ans[n-1] != -1:
            return ans[n-1]
        ans[n-1] = self.myf(ans, n-1) + self.myf(ans, n-2)
        return ans[n-1]
Solution().climbStairs(4)