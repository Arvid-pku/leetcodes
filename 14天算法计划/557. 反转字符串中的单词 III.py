class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(' ')
        words = [''.join(self.reverseString(list(x))) for x in words]
        return ' '.join(words)
    def reverseString(self, s):
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
        return s