class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s= ''.join(c.lower() for c in s if c.isalnum())
        if s==s[::-1]:
            return True
        return False
        