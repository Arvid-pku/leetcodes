class Solution:
    def reverseString(self, s) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(s) - 1
        while left < right:
            x = s[left]
            s[left] = s[right]
            s[right] = x
            left = left + 1
            right = right - 1
            
            
