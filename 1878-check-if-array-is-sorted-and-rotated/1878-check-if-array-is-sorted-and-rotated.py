class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        count = 0  # Count the number of "dips"
        n = len(nums)
        
        for i in range(n):
            if nums[i] > nums[(i + 1) % n]:  # Check next element (circular check)
                count += 1
                if count > 1:  # If more than one dip, it's not valid
                    return False
        return True
