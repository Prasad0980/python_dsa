class TreeNode:
    def __init__(self, data):
        self.data = data 
        self.left = None 
        self.right = None 
        

def preorder_traversal(node: TreeNode):
    if node:
        print(node.data, end=" ")
        preorder_traversal(node.left)
        preorder_traversal(node.right)

        
root = TreeNode("A")
root.left = TreeNode("B")
root.right = TreeNode("C")
root.left.left = TreeNode("D")
root.left.right = TreeNode("E")
root.left.left.left = TreeNode("G")
root.right.right = TreeNode("F")

preorder_traversal(root)