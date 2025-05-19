# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Base cases
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        
        # Check current node values
        if p.val != q.val:
            return False
        
        # Check left and right subtrees - IMPORTANT: return the results
        return (self.isSameTree(p.left, q.left) and 
                self.isSameTree(p.right, q.right))

root = TreeNode("A")
root.left = TreeNode("B")
root.right = TreeNode("C")
root.left.left = TreeNode("D")
root.left.right = TreeNode("E")
root.left.left.left = TreeNode("G")
root.right.right = TreeNode("F")

root2 = TreeNode("A")
root2.left = TreeNode("B")
root2.right = TreeNode("C")
root2.left.left = TreeNode("D")
root2.left.right = TreeNode("E")
root2.left.left.left = TreeNode("G")
root2.right.right = TreeNode("F")

s = Solution()
print(s.isSameTree(root, root2))