
# coding: utf-8

# In[ ]:


def findContentChildren(self, g: List[int], s: List[int]) -> int:
       g.sort()
       s.sort()
       temp=0
       # count=0
       for i in range(len(s)):
           if temp<len(g):
               if s[i]<g[temp]:
                   continue
               else:
                   temp+=1
       return temp

