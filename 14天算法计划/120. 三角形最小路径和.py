class Solution:
    def minimumTotal(self, triangle) -> int:
        ans = [-100000]*len(triangle[-1])
        ans[0] = triangle[0][0]
        for i in range(1, len(triangle)):
            for j in range(len(triangle[i])):
                x = len(triangle[i]) - 1 - j
                if x == len(triangle[i]) - 1:
                    ans[x] = ans[x - 1] + triangle[i][x]
                elif x == 0:
                    ans[x] = ans[0] + triangle[i][x]
                else:
                    ans[x] = min(ans[x], ans[x - 1]) + triangle[i][x]
        return min(ans[:len(triangle[-1])])

triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
print(Solution().minimumTotal(triangle))
