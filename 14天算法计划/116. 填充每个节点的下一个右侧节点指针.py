# Definition for a Node.
from queue import Queue


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        q = Queue()
        q.put(root)
        total = -1
        powers = 0
        # 因为不知道如何使用队列的首元素，所以只能get的时候，所以保存了一下上一个来链接
        # 感觉用list切片更好做。。
        # 用deque也可以，弹出再appendleft
        ago = Node()
        if not root:
            return root
        while not q.empty():
            front = q.get()
            if front.left:
                q.put(front.left)
                q.put(front.right)
            # error 有点点绕，主要就是判断二的幂
            if 2**powers - 1 == total:
                ago.next = None
                powers = powers + 1
                total = 0
            else:
                ago.next = front
                total = total + 1
            ago = front
        return root