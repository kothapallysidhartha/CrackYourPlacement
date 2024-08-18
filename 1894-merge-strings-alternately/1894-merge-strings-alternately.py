class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        k=len(word1) if len(word1)>=len(word2) else len(word2)
        v=""
        for i in range(k):
            if i in range(len(word1)):
                v=v+word1[i]
            if i in range(len(word2)):
                v=v+word2[i]
        return v