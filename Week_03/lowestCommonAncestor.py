
# coding: utf-8

# In[ ]:


def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
       if (not root) or (p==root) or (q==root):
           return root
           # self.method()
       left=self.lowestCommonAncestor(root.left,p,q)
       right=self.lowestCommonAncestor(root.right,p,q)
       if not left:
           return right
       if not right:
           return left
       if left and right:
           return root

