class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = 0  
        c = 0  

        for i in nums:
            if i == 1:
                c += 1
            else:
                if c > m:
                    m = c  
                c = 0  

        if c > m:  
            m = c
        
        return m
