class Solution(object):
    def maximumCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k=-1
        for i in range(len(nums)):
            if nums[i]<0:
                k=i
            elif nums[i]>=1:
                return len(nums[:k+1]) if len(nums[:i])>len(nums[i:]) else len(nums[i:])
        if k>=0:
            return len(nums[:k+1])
        else:
            return 0
        

        
        