class Solution(object):
    def passThePillow(self, n, time):
        """
        :type n: int
        :type time: int
        :rtype: int
        """
        t=1
        m=0
        while time:
            if t!=n and m!=n:
                t+=1
            elif t==1:
                m=0
                t+=1
            else:
                m=n
                t-=1
            time-=1
        return t
        