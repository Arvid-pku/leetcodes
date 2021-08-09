from queue import Queue
class Solution:
    def orangesRotting(self, mat) -> int:
        q = Queue()
        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 2:
                    mat[i][j] = 0
                    q.put((i, j))
                elif mat[i][j] == 1:
                    mat[i][j] = len(mat)+len(mat[0])
                elif mat[i][j] == 0:
                    mat[i][j]= -1
        while not q.empty():
            id = q.get()
            for x, y in zip(dx, dy):
                if len(mat) > (id[0] + x) >= 0 and len(mat[0]) > (id[1] + y) >= 0 and mat[id[0]+x][id[1]+y] == len(mat)+len(mat[0]):
                    mat[id[0]+x][id[1]+y] = mat[id[0]][id[1]] + 1
                    # error:TypeError: 'int' object is not subscriptable
                    q.put((id[0]+x, id[1]+y))
        ans = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                ans = max(ans, mat[i][j])
        if ans == len(mat)+len(mat[0]):
            return -1
        else:
            return ans