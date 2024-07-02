class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        p = []
        n = []
        for i in nums:
            if i >= 0:
                p.append(i)
            else:
                n.append(i)
        
        result = []
        for i in range(len(p)):
            result.append(p[i])
            if i < len(n):
                result.append(n[i])
                
        return result
