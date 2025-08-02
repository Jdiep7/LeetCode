# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def MaxDepth(root):
    def checkDepth(root, count):
        if not root:
            return count
        
        left_side = checkDepth(root.left, count+1)
        right_side = checkDepth(root.right, count+1)
        
        return max(left_side, right_side)

    return checkDepth(root, 0)