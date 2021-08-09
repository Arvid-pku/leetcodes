# mistake
# 所有0作为第1层，很妙
# 之前只想到遍历0，这样会很慢
# 也想到记录路径，但不是最优子结构
from queue import Queue
class Solution:
    def updateMatrix(self, mat):
        q = Queue()
        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    q.put((i, j))
                else:
                    mat[i][j] = len(mat)+len(mat[0])
        while not q.empty():
            id = q.get()
            for x, y in zip(dx, dy):
                if len(mat) > (id[0] + x) >= 0 and len(mat[0]) > (id[1] + y) >= 0 and mat[id[0]+x][id[1]+y] == len(mat)+len(mat[0]):
                    mat[id[0]+x][id[1]+y] = mat[id[0]][id[1]] + 1
                    # error:TypeError: 'int' object is not subscriptable
                    q.put((id[0]+x, id[1]+y))
        return mat


mat = [[0,0,0],[0,1,0],[0,0,0]]
Solution().updateMatrix(mat)