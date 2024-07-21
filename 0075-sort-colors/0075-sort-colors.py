class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """


        """d = {}
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        
        index = 0
        for key in sorted(d.keys()):
            for _ in range(d[key]):
                nums[index] = key
                index += 1"""
        start=0
        mid=0
        end=len(nums)-1
        while mid<=end:
            if nums[mid]==0:
                nums[start],nums[mid]=nums[mid],nums[start]
                mid+=1
                start+=1
                #end-=1
            elif nums[mid]==1:
                mid+=1
            else:
                nums[mid],nums[end]=nums[end],nums[mid]
                end-=1
        
