class Solution(object):
    def threeConsecutiveOdds(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        c=0
        i=0
        while i<len(arr):
            if arr[i]%2!=0:
                i+=1
                c+=1
                if c==3:
                    return True
            else:
                c=0
                i+=1
        return False
        