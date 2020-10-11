def levelOrder(self, root: 'Node') -> List[List[int]]:
    if not root:
        return []
    res=[]
    def bfs(current):
        queue=[current]
        while queue:
            nxt=[]
            temp=[]
            for node in queue:
                tmp.append(node.val)
                for child in node.children():
                    nxt.append(child)
            res.append(temp)
            queue=nxt
    bfs(root)
    return res
