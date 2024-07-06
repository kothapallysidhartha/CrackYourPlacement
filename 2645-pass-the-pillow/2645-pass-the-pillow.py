class Solution(object):
    def passThePillow(self, n, time):
        """
        :type n: int
        :type time: int
        :rtype: int
        """
        s = time // (n - 1)
        return (time % (n - 1) + 1) if s % 2 == 0 else (n - time % (n - 1))
            
        