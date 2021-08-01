# mistake
class Solution:
    def nthPersonGetsNthSeat(self, n: int):
        if n == 1:
            return 1
        else:
            return 0.5


# class Solution {
# public:
#     double nthPersonGetsNthSeat(int n) {
#         if(n==1)//边界情况
#             return 1.0;

#         double p[100001];
#         p[1]=1.0;
#         p[2]=0.5;
#         for(int i=3;i<=n;i++)
#         {
#             p[i]=1.0/i;   
#             for(int k=2;k<i;k++)
#                 p[i]+=p[i-k+1]/i;
#         }
#         return p[n];
#     }
# };