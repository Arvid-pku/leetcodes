def isBadVersion(version):
    pass

class Solution:
    def firstBadVersion(self, n):
        left = 1
        right = n
        ans = n  # error, behind is true
        while left <= right:
            middle = (left + right) // 2
            if isBadVersion(middle):
                ans = middle
                right = middle - 1
            else:
                left = middle + 1
        return ans
            