class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        ans = ""
        for i in s:
            if i == '(':
                if stack:
                    ans += '('
                stack.append('(')
            elif i == ')':
                stack.pop()
                if stack:
                    ans += ')'
        return ans
