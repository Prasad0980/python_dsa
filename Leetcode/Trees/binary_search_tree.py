class TreeNode():
    def __init__(self, val):
        self.val = val 
        self.left = None 
        self.right = None 
        

def bst_implementation(root, value):
    if not root:
        return TreeNode(value)
    
    if value < root.val:
        root.left = bst_implementation(root.left, value)
    else:
        root.right = bst_implementation(root.right, value)
    print(root.val)  
    return root


def create_bst(values):
    if not values:
        return None
    
    root = TreeNode(values[0])
    
    for value in values[1:]:
        bst_implementation(root, value)
        
    return root

# Example usage
values = [50, 30, 70, 20, 40, 60, 80]
bst_root = create_bst(values)

# Let's print the tree using inorder traversal to verify it's correct
def inorder_traversal(node):
    if node:
        inorder_traversal(node.left)
        print(node.val, end=" ")
        inorder_traversal(node.right)

# print("Inorder traversal of the created BST:")
# inorder_traversal(bst_root)  # Should print: 20 30 40 50 60 70 80

def search_bst(value, root): #this takes Olog(N) time
    if not root or root.val == value:
        return [root] if not root else [root, root.val] 
    
    if value < root.val:
        return search_bst(value, root.left)
    else:
        return search_bst(value, root.right)


print(search_bst(81, bst_root))