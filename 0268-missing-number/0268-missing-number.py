class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n= sum(nums)
        t= (len(nums) *(len(nums)+1))//2
        return t-n
        
            
