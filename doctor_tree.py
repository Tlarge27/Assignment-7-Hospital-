class DoctorNode:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None


class DoctorTree:
    def __init__(self):
        self.root = None

    def insert(self, parent_name, employee_name, side):
        new_node = DoctorNode(employee_name)
        if self.root is None:
            if parent_name == employee_name:
                self.root = new_node
                return True
            else:
                return False

        parent_node = self._find(self.root, parent_name)
        if parent_node is None:
            return False

        if side.lower() == "left":
            if parent_node.left is None:
                parent_node.left = new_node
                return True
            else:
                return False
        elif side.lower() == "right":
            if parent_node.right is None:
                parent_node.right = new_node
                return True
            else:
                return False
        else:
            return False

    def _find(self, node, name):
        if node is None:
            return None
        if node.name == name:
            return node
        left_search = self._find(node.left, name)
        if left_search:
            return left_search
        return self._find(node.right, name)

    def preorder(self, node):
        if node is None:
            return []
        return [node.name] + self.preorder(node.left) + self.preorder(node.right)

    def inorder(self, node):
        if node is None:
            return []
        return self.inorder(node.left) + [node.name] + self.inorder(node.right)

    def postorder(self, node):
        if node is None:
            return []
        return self.postorder(node.left) + self.postorder(node.right) + [node.name]


if __name__ == "__main__":
    tree = DoctorTree()
    tree.root = DoctorNode("Dr. Croft")
    tree.insert("Dr. Croft", "Dr. Goldsmith", "right")
    tree.insert("Dr. Croft", "Dr. Phan", "left")
    tree.insert("Dr. Phan", "Dr. Carson", "right")
    tree.insert("Dr. Phan", "Dr. Morgan", "left")

    print("Preorder:", tree.preorder(tree.root))
    print("Inorder:", tree.inorder(tree.root))
    print("Postorder:", tree.postorder(tree.root))

# The tree created here is a binary tree that shows which doctors report to who and who is ultimately in charge.
# Each Doctor is a Node named after the doctor and can have up to two people reporting to them. One on their left and one on their right.
# The Tree class manages the structure and adds new doctors under whatever patient is specified using inserts. The tree is useful because 
# it clearly shows who is in charge and who reports to who. Higher ranking doctors are on top with newer lower ranking doctors on the bottom.
# Using a tree makes it easy to find current doctors, and it's easy to add new doctors. 
#
# There is three ways to work through this tree. There is Preorder, inorder, and postorder. 
# The preorder goes to the main doctor first, then its left reports, then its right report. 
# The inorder goes to the doctors that are on the left of the tree underneath the main doctor, starting from lowest to highest. 
# It then goes to the main doctor, then to the doctor on the right that reports to the main doctor. 

# A software engineer would use preorder when they need to see the top item first and then go through everything underneath it. 
# they'd use inorder when they want to see the tree in order, like from smallest to biggest or shortest to tallest.
# they would most likely use postorder when making edits to a tree. Like if a boss were to fire an employee their name would be removed  
# from the bottom of the tree
# 
#
#
#
#