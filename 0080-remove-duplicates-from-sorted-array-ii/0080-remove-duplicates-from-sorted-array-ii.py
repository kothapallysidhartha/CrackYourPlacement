class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d={}
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        for key,value in d.items():
            while value >=3:
                nums.remove(key)
                value-=1 
        return len(nums)
        