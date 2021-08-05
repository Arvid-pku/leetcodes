class Solution:
    def twoSum(self, numbers, target: int):
        left = 0
        right = len(numbers)
        while left < right:
            if numbers[left] + numbers[right] < target:
                left = left + 1
            elif numbers[left] + numbers[right] > target:
                right = right - 1
            else:
                return [left+1, right+1]

# a+b+c=0 同理