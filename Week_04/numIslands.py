
# coding: utf-8

# In[3]:


def numIslands( grid) : 
    if not grid:
        return 0
    count=0
    for hang in range(len(grid)):
        for lie in range(len(grid[0])):
            if grid[hang][lie]=='1':
                count+=1
                self.dfs(grid,hang,lie)
    return count
    def dfs(self,grid,h,l):
        if h<0 or l<0 or h>=len(grid) or l>=len(grid[0]) or grid[h][l]!='1':
            return
        grid[h][l]='0'
        self.dfs(grid,h,l-1)
        self.dfs(grid,h,l+1)
        self.dfs(grid,h-1,l)
        self.dfs(grid,h+1,l)

