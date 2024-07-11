class Solution(object):
    def maximumStrongPairXor(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        k=0
        for i in nums:
            for j in nums:
                if abs(i-j)<=min(i,j):
                    if k<(i^j):
                        k=i^j
        return k
        