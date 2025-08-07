def isSubtree(self, root, subRoot):
        def isSameTree(p, q):
            def checkTree(p, q):
                if not p and not q:
                    return 0
                elif (not p and q) or (not q and p):
                    return -1
                else:
                    if p.val != q.val:
                        return -1
                    else:
                        left_side = checkTree(p.left, q.left)
                        right_side = checkTree(p.right, q.right)
                
                        if left_side == 0 and right_side == 0:
                            return 0
                        else:
                            return -1

            
            return checkTree(p,q) != -1

        
        def checkSubTree(root, subRoot):
            if not root:
                return False
            
            if isSameTree(root, subRoot):
                return True

            
            return checkSubTree(root.left, subRoot) or checkSubTree(root.right, subRoot)
        
        if not subRoot:
            return True
        
        return checkSubTree(root, subRoot)
