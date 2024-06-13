class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        li = [-1, -1]
        for i in range(len(nums)):
            if nums[i] == target:
                if li[0] == -1:
                    li[0] = i
                li[1] = i
        return li      