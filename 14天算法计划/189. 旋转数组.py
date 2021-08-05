# mistake ! wonderful!
class Solution:
    def rotate(self, nums, k: int) -> None:
        print(-(k % len(nums)), len(nums) - k % len(nums))
        print(-(k), len(nums) - k)
        # error do not forget mod
        nums[: ] = (nums[i] for i in range(-(k % len(nums)), len(nums) - k % len(nums)))


nums = [-1]

Solution().rotate(nums, 2)


# wonderful:
# class Solution {
# public:
#     void rotate(vector<int>& nums, int k) {
#         // 三次翻转搞定
#         k = k % nums.size();
#         reverse(nums.begin(), nums.begin() + nums.size() - k);
#         reverse(nums.begin() + nums.size() - k, nums.end());
#         reverse(nums.begin(), nums.end());
#     }
# };