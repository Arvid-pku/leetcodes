# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        if root1 or root2:
            root = TreeNode()
            self.mymerge(root, root1, root2)
        else:
            root = None
        return root
    def mymerge(self, root, root1, root2):
        if root1 and root2:
            root.val = root1.val + root2.val
            if root1.left or root2.left:
                root.left = TreeNode()
                self.mymerge(root.left, root1.left, root2.left)
            if root1.right or root2.right:
                root.right = TreeNode()
                self.mymerge(root.right, root1.right, root2.right)
        elif root1:
            root.val = root1.val
            if root1.left:
                root.left = TreeNode()
                self.mymerge(root.left, root1.left, None)
            if root1.right:
                root.right = TreeNode()
                self.mymerge(root.right, root1.right, None)
        elif root2:
            root.val = root2.val
            if root2.left:
                root.left = TreeNode()
                self.mymerge(root.left, None, root2.left)
            if root2.right:
                root.right = TreeNode()
                self.mymerge(root.right, None, root2.right)
        else:
            return
        