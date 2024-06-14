import re
from collections import defaultdict

class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        # Convert paragraph to lowercase and remove punctuations except spaces
        paragraph = re.sub(r'[^\w\s]', ' ', paragraph.lower())
        
        words = paragraph.split()
        
        banned_set = set(banned)
        
        word_count = defaultdict(int)
        
        for word in words:
            if word not in banned_set:
                word_count[word] += 1
        
        max_count = 0
        result = ""
        for word, count in word_count.items():
            if count > max_count:
                max_count = count
                result = word
        
        return result