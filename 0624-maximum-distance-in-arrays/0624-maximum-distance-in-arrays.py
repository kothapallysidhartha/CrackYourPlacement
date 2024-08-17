class Solution(object):
    def maxDistance(self, arrays):
        """
        :type arrays: List[List[int]]
        :rtype: int
        """
        mi=arrays[0][0]
        ma=arrays[0][-1]
        dif=0
        for i in range(1,len(arrays)):
            c_mi=arrays[i][0]
            c_ma=arrays[i][-1]

            dif=max(dif,abs(c_ma-mi))
            dif=max(dif,abs(ma-c_mi))
            mi=min(mi,c_mi)
            ma=max(ma,c_ma)

        return dif

        