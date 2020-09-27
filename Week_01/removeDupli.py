class Solution(object):
    def removeDuplicates(self,nums):
         nums[:]=list(sorted(set(nums)))
         return  nums

