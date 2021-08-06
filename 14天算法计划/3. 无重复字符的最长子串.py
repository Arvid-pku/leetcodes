class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # error: 注意x字符可能的形式
        # hhhhh  我直接死磕（懒人。。
        x = 'QWERTYUI"OPASDFGH!@[]#$%^+-=-_~`.&*()JKLZXCVBNMqwertyuiopasdfghjklzx\'|\\:;{}cvbnm 1234567890！!@#￥%……&*（）(),./<>?'
        chdict = {}
        for i in x:
            chdict[i] = 0
        left = 0
        right = 0
        maxlen = 1
        ans = 1
        # error 下面使用了s[0] 需要判断
        if len(s) == 0:
            return 0
        chdict[s[0]] = 1
        # error: 下面加一，注意范围
        while right < len(s) - 1:
            right = right + 1
            while chdict[s[right]] != 0:
                chdict[s[left]] = chdict[s[left]] - 1
                left = left + 1
                maxlen = maxlen - 1
            chdict[s[right]] = chdict[s[right]] + 1
            maxlen = maxlen + 1
            ans = max(maxlen, ans)
        return ans
        
s = "abcabcbb"
print(Solution().lengthOfLongestSubstring(s))