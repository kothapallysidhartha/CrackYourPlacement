class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        d={}
        for i in nums1:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        k=[]
        for i in nums2:
            if i in d:
                if i not in k:
                    k.append(i)
        return k

        
        