from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        littleD = Counter(s1)
        br = len(s1)
        for i in range(br, len(s2)+1): 
            m = s2[i-br:i]
            tryD = Counter(m)
            if self.test(littleD, tryD):
                return True
        return False

    def test(self, littleD, tryD):
        for x in littleD.keys():
            if tryD[x] != littleD[x]:
                return False
        return True
        
s1 = 'adc'
s2 = 'dcda'

Solution().checkInclusion(s1, s2)