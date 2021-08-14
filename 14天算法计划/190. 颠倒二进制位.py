class Solution:
    def reverseBits(self, n: int) -> int:
        x = bin(n)[2:]
        print(x)
        x = list(x)
        x = ['0']*(32 - len(x)) + x
        print(x)
        # x = list(str(bin(n)[2:]))
        x.reverse()
        return int(''.join(x), 2)