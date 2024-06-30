class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            if target-nums[i] in nums:
                j=i+1
                while j<len(nums):
                    if nums[j]+nums[i]==target:
                         return [j,i]
                    j+=1
        return [-1,-1]
                

        