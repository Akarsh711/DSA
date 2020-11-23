# Root : where tree starts
# Child : Node Having and childs
# Leaf : Which Don't have any childs

# Binary Tree : The Tree whose only have two childs each [right ,left]

# Binay Search Tree(BST) : It follows a order which says left sub tree should be less
# then the root and right sub should be large

  #         (10)   <- Root Node
  #       /      \         __ 
  #     (5)      (20)       / Child Node
  #     /  \      /  \
  #    (3)(9)    (15)(25)
  #   / \        /  \    \
  #  /   \      /    \    \
  # (1)  (4)   (13)  (17)  (30) <- Leaf Node 

# Also with Binary Tree our search get pretty easy
 
# Insertion in BST -  O(logn)
# Let's say we have 19 to insert on above tree then first we check
# is 19 is bigger or smaller then root?
#   - It is bigger so it go to right
# Now is 19 bigger or smaller then 20 ?
#   - It is smaller so it go ot left
# So, we do this again and again until we got to and empty spot where no node exists
# so it come after 17
# This is called an balanced tree if it not it become O(n) for insertion as well as in searching

# Travesing -
# There is Three Types for doing it:
# - Inorder   : left -> root -> right            [ABC] It allows to print in order in BST
# - Preorder  : visit root node -> left -> right [BAC]
# - Postorder : left -> right -> root            [ACB]


class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, value):
        if value<= self.data:
            if self.left == None:
                 self.left = Node(value) 
            else:
                self.left.insert(value)
        else:
            if self.right == None:
                self.right = Node(value)
            else:
                self.right.insert(value)

    def find(self, value):
        if(value == self.data):
            return True
        elif value<self.data:
            if self.left == None:
                return False
            else:
                return self.left.find(value)

        elif self.right == None:
            return False
        else:
            return self.right.find(value)
 
    def InOrderTraversal(self):
        if self.left != None:
            self.left.InOrderTraversal()
        print( self.data),
        if self.right !=None:
            self.right.InOrderTraversal()
    
    def PreOrderTraversal(self):
        print(self.data)
        if self.left!= None:
            self.left.PreOrderTraversal()
        if self.right != None:
            self.right.PreOrderTraversal()
    
    def PostOrderTraversal(self):
        if self.left != None:
            self.left.PostOrderTraversal()
        if self.right != None:
            self.right.PostOrderTraversal()
        print(self.data)
        
    # Another way of doing inorder
    def inorderTraversal(self, root):
        res = []
        if root:
            res = self.inorderTraversal(root.left)
            res.append(root.data)
            res = res + self.inorderTraversal(root.right)
        return res
        
if __name__ == "__main__":
    root = Node(20)
    root.insert(19)
    root.insert(21)
    
    root.insert(18)
    root.insert(22)
    print(root.find(18))
    root.InOrderTraversal()
    print('-----------')
    root.PreOrderTraversal()
    print('-----------')
    root.PostOrderTraversal()
    print(root.inorderTraversal(root))
    
    input("waiting for input")
