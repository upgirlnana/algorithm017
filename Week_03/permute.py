
# coding: utf-8

# In[ ]:


def permute(self, nums: List[int]) -> List[List[int]]:
        # for i in range(len(nums)):
        #     for j in (i+1:le)
        if len(nums) == 1:
            return [nums]
        resultList = []
        for n in nums:
            subNums = nums.copy()
            subNums.remove(n)
            subResultList = self.permute(subNums)
            for subResult in subResultList:
                subResult.insert(0, n)
                resultList.append(subResult)
        return resultList

