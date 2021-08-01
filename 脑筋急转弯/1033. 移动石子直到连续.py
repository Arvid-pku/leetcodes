class Solution:
    def numMovesStones(self, a: int, b: int, c: int):
        ls = sorted([a, b, c])
        minstep = 0
        maxstep = 0
        # error  乱序！
        if ls[0] < ls[1] - 2 and ls[2] > ls[1] + 2: 
            minstep = 2
        elif ls[0] == ls[1] - 1 and ls[2] == ls[1] + 1:
            minstep = 0
        else:
            minstep = 1
        maxstep = ls[1] - ls[0] - 1 + ls[2] - ls[1] - 1
        return [minstep, maxstep]
