class Solution:
    def floodFill(self, image, sr: int, sc: int, newColor: int):
        oldColor = image[sr][sc]
        # error: 笑死了
        if oldColor == newColor:
            return image
        self.change(image, oldColor, sr, sc, newColor)
        return image
    def change(self, image, oldColor, sr, sc, newColor):
        if sr < 0 or sr >= len(image) or sc < 0 or sc >= len(image[0]):
            return
        if image[sr][sc] != oldColor:
            return
        image[sr][sc] = newColor
        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]
        for x, y in zip(dx, dy):
            self.change(image, oldColor, sr + x, sc + y, newColor)

Solution().floodFill([[0,0,0],[0,1,1]],1,1,1)