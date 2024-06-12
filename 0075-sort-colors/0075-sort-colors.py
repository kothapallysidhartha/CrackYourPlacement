class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        d = {}
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        
        index = 0
        for key in sorted(d.keys()):
            for _ in range(d[key]):
                nums[index] = key
                index += 1
