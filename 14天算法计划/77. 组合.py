# 还是不太熟悉啊，尝试了一小会
class Solution:

    def combine(self, n: int, k: int):
        ans = []
        now = []
        if n == 0:
            return []
        self.getall([x for x in range(1, n+1)], k, ans, now)
        return ans

    def getall(self, lis, k, ans, now):
        if k == 0:
            ans.append(now)
            return
        mynow = now[:]
        for i in range(len(lis)):
            mynow.append(lis[i])
            if len(lis) - i >= k:
                self.getall(lis[i+1:], k-1, ans, mynow)
            # 回溯
            mynow = now[:]


x = Solution().combine(4, 2)
x