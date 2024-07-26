class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """if not nums:
            return 0
        j = 1 
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[j] = nums[i]
                j += 1
        nums = nums[:j]
    
        return (len(nums))"""

        neww=[]
        for i in nums:
            if i not in neww:
                neww.append(i)
        for i in range(len(neww)):
            nums[i]=neww[i]  
        
        #print(nums)
        #neww=len(nums)
        return len(neww)
        


