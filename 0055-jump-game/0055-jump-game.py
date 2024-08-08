class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        maxx=0
        if nums[0]==0 and len(nums)>1:
            return False
        
        for i in range(len(nums)-1):
            #break
            if i>maxx:
                return False
            if i+nums[i]>maxx:
                maxx=max(maxx,i+nums[i])
        
            
            
        return True if maxx>=len(nums)-1 else False

        
        