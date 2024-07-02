class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        k = {}
        new = []
        for i in nums1:
            if i not in k:
                k[i] = 1
            else:
                k[i] += 1
        for i in nums2:
            if i in k and k[i] > 0:
                new.append(i)
                k[i] -= 1
        return new
