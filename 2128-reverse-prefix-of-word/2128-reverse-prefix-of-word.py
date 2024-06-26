class Solution(object):
    def reversePrefix(self, word, ch):
        """
        :type word: str
        :type ch: str
        :rtype: str
        """
        try:
            i = word.index(ch) 
        except ValueError:
            return word  
        
        prefix = word[:i+1]  
        reversed_prefix = prefix[::-1]  
        
        return reversed_prefix + word[i+1:]  
