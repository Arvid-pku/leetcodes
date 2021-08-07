class Solution:
    def maxAreaOfIsland(self, grid) -> int:
        maxA = 0
        for x in range(len(grid)):
            for y in range(len(grid[x])):
                maxA = max(maxA,self.floodFill(grid, x, y))
        return maxA
        
    def floodFill(self, image, sr: int, sc: int):

        if image[sr][sc] == 0:
            return 0
        m = self.change(image, 1, sr, sc, 0, 0)
        return m
    def change(self, image, oldColor, sr, sc, newColor, nowA):
        if sr < 0 or sr >= len(image) or sc < 0 or sc >= len(image[0]):
            return nowA
        if image[sr][sc] != oldColor:
            return nowA
        image[sr][sc] = newColor
        nowA = nowA + 1
        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]
        for x, y in zip(dx, dy):
            nowA = max(nowA,self.change(image, oldColor, sr + x, sc + y, newColor, nowA))
        return nowA
xx = Solution().maxAreaOfIsland([[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]])
xx