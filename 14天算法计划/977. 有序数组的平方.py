class Solution:
    def sortedSquares(self, nums):
        pixel =  self.getPixel(nums)
        forward = pixel + 1
        backward = pixel
        ans = []
        while backward >= 0 or forward < len(nums):
            # error do not forget =
            if (backward < 0 and forward < len(nums)) or (forward < len(nums) and abs(nums[backward]) >= abs(nums[forward])):
                ans.append(nums[forward]*nums[forward])
                forward = forward + 1
            elif (backward >= 0 and forward >= len(nums)) or (backward >= 0 and abs(nums[backward]) < abs(nums[forward])):
                ans.append(nums[backward]*nums[backward])
                backward = backward - 1
        return ans
        
         
    
    def getPixel(self, nums):
        left = 0
        right = len(nums) - 1
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] < 0:
                left = middle + 1
            elif nums[middle] > 0:
                right = middle - 1
            else:
                return middle
        # error do not forget range
        if right >= len(nums) or right < 0:
            return left
        elif left >= len(nums) or left < 0:
            return right
        if nums[right]*nums[right] < nums[left]*nums[left]:
            return right
        else:
            return left

nums = [-1]

print(Solution().sortedSquares(nums))