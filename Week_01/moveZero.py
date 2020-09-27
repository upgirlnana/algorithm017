class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        length=len(nums)
        # def check(i):
        #     return False if i==0 else True
        # nums=list(filter(check,nums))
        nums[:]=[i for i in nums if i!=0]
        for j in range(length-len(nums)):
            nums.append(0)