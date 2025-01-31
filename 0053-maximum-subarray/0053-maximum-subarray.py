class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ms=nums[0]
        curr=0
        for i in range(len(nums)):
            curr+=nums[i]
            ms=max(ms,curr)
            if curr<0:
                curr=0
        return ms