class Solution:
    def getLastMoment(self, n: int, left, right):
        if len(left) == 0:
            left = [0]
        if len(right) == 0:
            right = [n]
         
        return max(max(left), max([n - x for x in right]))