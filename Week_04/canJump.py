
# coding: utf-8

# In[ ]:


def canJump(self, nums: List[int]) -> bool:
        max_length = 0    
        n=len(nums)   
        for current_position, steps in enumerate(nums):   #i为当前位置，jump是当前位置的跳数
            if current_position<=max_length: 
                max_length=max(max_length,current_position+nums[current_position])
                 
        return max_length>=current_position

