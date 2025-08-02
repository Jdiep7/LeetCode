# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def diameterOfBinaryTree(root):
    res = 0
    def checkDiamter(root):
        nonlocal res
        
        if not root:
            return 0

        left_side = checkDiamter(root.left)
        right_side = checkDiamter(root.right)
        
        res = max(res, left_side + right_side)
        
        return max(right_side, left_side) + 1
    
    return res