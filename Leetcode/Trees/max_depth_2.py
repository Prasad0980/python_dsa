from collections import deque

class TreeNode():
    def __init__(self, data, left=None, right=None):
        self.data = data 
        self.left = left 
        self.right = right
        

def max_depth(root):
    queue = deque([root])
    queue.append(None)
    count = 0 
    
    while queue:
        node = queue.popleft()
        if not node:
            count+=1
            if queue:
                queue.append(None)
            
        else:
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    
    return count

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.left = TreeNode(4)
root.right.right = TreeNode(8)

print(max_depth(root))