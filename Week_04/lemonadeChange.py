
# coding: utf-8

# In[ ]:


def lemonadeChange(self, bills: List[int]) -> bool:
        if len(bills)==0:
            return False
        five_count=0
        ten_count=0
        twenty_count=0
        for i in range(len(bills)):
            if i==0 and bills[i]<5:
                return False
            elif bills[i]==5:
                five_count+=1
            elif bills[i]==10:
                if five_count<1:
                    return False
                else:
                    five_count-=1
                    ten_count+=1
            elif bills[i]==20:
                if ten_count!=0 and five_count!=0:
                    ten_count-=1
                    five_count-=1
                    twenty_count+=1
                elif ten_count==0 and five_count>=3:
                    five_count-=3
                    twenty_count+=1
                else:
                    return False
        return five_count or ten_count or twenty_count

