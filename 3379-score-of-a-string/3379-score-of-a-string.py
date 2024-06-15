class Solution(object):
    def scoreOfString(self, s):
        """
        :type s: str
        :rtype: int
        """
        val=0
        for i in range(len(s)-1):
            val+=abs(ord(s[i])-ord(s[i+1]))
        return val
        