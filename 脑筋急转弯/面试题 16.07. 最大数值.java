class Solution {
    public int maximum(int a, int b) {
        int ans = 0;
        boolean flag = (a < b) && ((ans += b) < 100);
        flag = (a > b) && ((ans += a) < 100);
        flag = (a == b) && ((ans += a) < 100);
        return ans;
        }
    }
}