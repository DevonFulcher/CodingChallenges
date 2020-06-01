class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

'''
    1
   / \
  2   2
 / \ / \
3  4 4  3
'''

def isSymmetricHelper(rightNode, leftNode):
    if (leftNode == None and rightNode == None):
        return True
    if (leftNode == None or rightNode == None):
        return False
    return rightNode.val == leftNode.val and \
        isSymmetricHelper(leftNode.left, rightNode.right) and \
        isSymmetricHelper(leftNode.right, rightNode.left)

def isSymmetric(root):
    if root == None:
        return True
    return isSymmetricHelper(root.right, root.left)