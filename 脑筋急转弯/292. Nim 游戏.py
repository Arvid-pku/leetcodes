class Solution:
    def canWinNim(self, n: int) -> bool:
        return n % 4 != 0

for n in range(10):
    print(n)
    print(Solution().canWinNim(n))