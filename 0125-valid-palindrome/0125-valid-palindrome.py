class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = ''.join(c.lower() for c in s if c.isalnum())
        for i in range(int(len(s) / 2)):
            if s[i] != s[-i - 1]:
                return False
        return True
