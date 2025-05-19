from collections import deque

class TreeNode():
    def __init__(self, data, left=None, right=None):
        self.data = data 
        self.left = left 
        self.right = right
        
    
def level_order_traversal(root):
    if not root:
        return []
    
    queue = deque([root])
    result = list()
    
    while queue:
        
        val = queue.popleft()
        result.append(val.data)
        
        if val.left:
            queue.append(val.left)
        if val.right:
            queue.append(val.right)
            
    return result

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.left = TreeNode(4)
root.right.right = TreeNode(8)

print(level_order_traversal(root))