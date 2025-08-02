# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isBalanced(root):
    def checkBalance(root):
        if not root:
            return 0
        
        left_side = checkBalance(root.left)
        right_side = checkBalance(root.right)
        
        if left_side == -1 or right_side == -1:
            return -1
        
        if abs(left_side - right_side) > 1:
            return -1
        
        return max(left_side, right_side) + 1 
    return checkBalance() != -1