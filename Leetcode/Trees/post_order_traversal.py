class TreeNode:
    def __init__(self, data):
        self.data = data 
        self.left = None 
        self.right = None 
        

def postorder_traversal(node: TreeNode):
    if node:
        postorder_traversal(node.left)
        postorder_traversal(node.right)
        print(node.data, end=" ")

        
root = TreeNode("A")
root.left = TreeNode("B")
root.right = TreeNode("C")
root.left.left = TreeNode("D")
root.left.right = TreeNode("E")
root.left.left.left = TreeNode("G")
root.right.right = TreeNode("F")

postorder_traversal(root)