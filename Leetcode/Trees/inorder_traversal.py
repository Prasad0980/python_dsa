class TreeNode:
    def __init__(self, data):
        self.data = data 
        self.left = None 
        self.right = None 
        

def inorder_traversal(node: TreeNode):
    if node:
        inorder_traversal(node.left)
        print(node.data, end=" ")
        op.append(node.data)
        inorder_traversal(node.right)
    return op
        
root = TreeNode("A")
root.left = TreeNode("B")
root.right = TreeNode("C")
root.left.left = TreeNode("D")
root.left.right = TreeNode("E")
root.left.left.left = TreeNode("G")
root.right.right = TreeNode("F")

inorder_traversal(root)