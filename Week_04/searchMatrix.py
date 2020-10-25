
# coding: utf-8

# In[3]:


def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        hang=len(matrix)
        if not hang:
            return False
        lie=len(matrix[0])
        if not lie:
            return False
        for i in range(len(matrix)):
            if target>matrix[i][lie-1]:
                continue
            else:
                low=0
                high=lie-1
                
                while low<=high:
                    mid=(low+high)//2
                    if matrix[i][mid]==target:
                        return True
                    elif matrix[i][mid]>target:
                       high=mid-1
                    else:
                        low=mid+1
        return False

