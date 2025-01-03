class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # Define 32-bit signed integer range
        INT_MIN, INT_MAX = -2**31, 2**31 - 1

        # Check range condition for input
        if x < INT_MIN or x > INT_MAX:
            return 0

        # Reverse integer handling negative cases
        if x >= 0:
            rev = int(str(x)[::-1])
        else:
            rev = -int(str(-x)[::-1])

        # Check if the reversed integer is within the 32-bit signed range
        if rev < INT_MIN or rev > INT_MAX:
            return 0

        return rev
