#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#    相对数组排序
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count=0
        arr=[]
        other=[]
        for i in range(len(arr2)):
            for j in range(len(arr1)):
                if arr2[i]==arr1[j]:
                    arr.append(arr1[j])     
                elif i==0 and arr1[j] not in arr2:
                    other.append(arr1[j])             
        
        other.sort()
        arr.extend(other)    
        arr1=arr
        return arr1
#     二进制位数反转
    def reverseBits(self, n: int) -> int:
        # n=str(n)
        # return n[::-1]
        temp=0
        count=31
        while n:
            temp+=(n&1)<<count
            n>>=1
            count-=1
        return temp
#     判断是否是2的幂
     def isPowerOfTwo(self, n: int) -> bool:
        if n==0:
            return False
        else:
            while(n):
                if  n!=1 and n%2==1:
                    return False
                n//=2
            return True
#         字母的有效异位
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        else:
            return (True if sorted(s)==sorted(t) else False)
def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        merged = []
        for interval in intervals:
            # 如果列表为空，或者当前的区域与已经存在的没有交叉区域，就是结束位置没落在当前的区间内，直接添加
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # 否则的话，已经存在的区间的结束位置落在当前区间内，比较已经添加的区间的结束位置与当前区间的结束位置，选择较大的值作为这个合并区间的结束值，开始位置是已经排序的了，不用再比较
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged

