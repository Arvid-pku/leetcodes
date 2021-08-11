class Solution:
    def letterCasePermutation(self, s: str):
        ans = []
        now = []
        self.getall(list(s), 0, ans, now)
        return [''.join(x) for x in ans]

    def getall(self, lis, i, ans, now):
        if i == len(lis):
            ans.append(now)
            return
        mynow = now[:]
        mynow.append(lis[i])
        self.getall(lis, i+1, ans, mynow)
        mynow = now[:]
        if 97 <= ord(lis[i]) <= 122:
            mynow.append(lis[i].upper())
            self.getall(lis, i+1, ans, mynow)
        elif 65 <= ord(lis[i]) <= 90:
            mynow.append(lis[i].lower())
            self.getall(lis, i+1, ans, mynow)



        # 回溯
        mynow = now[:]

x = Solution().letterCasePermutation('C')
print(x)