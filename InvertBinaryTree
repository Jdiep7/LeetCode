def invertTree(root):
        if not root: return None

        #root.left, root.right = root.right, root.left

        temp = root.left
        root.left = root.right
        root.right = temp
        print(temp)
        
        invertTree(root.left)
        invertTree(root.right)

        return root
        