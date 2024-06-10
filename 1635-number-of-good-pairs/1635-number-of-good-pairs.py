class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        c = 0
        for num in nums:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1
        
        for count in d.values():
            c += (count * (count - 1)) // 2  
        
        return c
