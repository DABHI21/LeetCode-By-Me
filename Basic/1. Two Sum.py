class Solution:
    def twoSum(self, nums, target) :
        for i in range(0,len(nums)-1):
            for x in range(i+1,len(nums)):
                if nums[i]+nums[x]==target:
                    return i,x 