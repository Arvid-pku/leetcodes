# mistake

class Solution:
    def sumNums(self, n: int) -> int:
        ans = n
        flag =  (n > 0) and (ans = ans + self.sumNums(n-1)) > 0
        return ans
print(Solution().sumNums(10))


# java
# (x == 10) > 1

# class Solution {

#     public int sumNums(int n) {
#         int sum = n;
#         boolean flag = n > 0 && (sum += sumNums(n - 1)) > 0;
#         return sum;
#     }
# }