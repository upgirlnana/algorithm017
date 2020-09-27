class Solution(object):
    def twoSum(self, nums, target):
        indexls = []
        for  i in range(len(nums)):
            another=target-nums[i]
            temp=nums[i+1:]
            if another in temp:
                indexls.append(i)
                indexls.append(i+1+temp.index(another))
                break
            else:
                continue
        return indexls


