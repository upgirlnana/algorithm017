def inandpreorder(self, root: TreeNode) -> List[int]:
    def dfs(current):
        if not current:
            return
 #       preorder
        res.append(current.val)
        dfs(current.left)
        dfs(current.right)
#       inorder
        dfs(current.left)
        res.append(current.val)
        dfs(current.right)
#       postorder
        dfs(current.left)
        dfs(current.right)
        res.append(current.val)
    res=[]
    dfs(root)
    return res

