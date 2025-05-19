class TreeNode():
    def __init__(self, data, left=None, right=None):
        self.data = data 
        self.left = left 
        self.right = right
        
def sum_nodes(root):
    if not root:
        return 0
    
    left_sum = sum_nodes(root.left)
    right_sum = sum_nodes(root.right)
    
    return left_sum+right_sum+root.data 

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.left = TreeNode(4)
root.right.right = TreeNode(100)

print(sum_nodes(root))