# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
        
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True 
        return self.isMirror(root.left, root.right)

    
    def isMirror(self, left_root, right_root):
        if not left_root and not right_root:
            return True 
        if not left_root or not right_root:
            return False
        if left_root.val != right_root.val:
            return False 

        
        return ((self.isMirror(left_root.left, right_root.right)) 
                and (self.isMirror(left_root.right, right_root.left)))

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.left = TreeNode(4)
root.right.right = TreeNode(8)

s = Solution()
print(s.isSymmetric(root))