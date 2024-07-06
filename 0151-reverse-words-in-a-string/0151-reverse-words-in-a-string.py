class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Helper function to reverse characters in a string list from start to end indices
        def reverse(string_list, start, end):
            while start < end:
                string_list[start], string_list[end] = string_list[end], string_list[start]
                start += 1
                end -= 1
        
        # Trim leading and trailing spaces and reduce multiple spaces to single space
        s = s.strip()
        s = ' '.join(s.split())
        
        # Convert string to list to perform in-place modifications
        string_list = list(s)
        
        # Reverse the entire string
        reverse(string_list, 0, len(string_list) - 1)
        
        start = 0
        for end in range(len(string_list) + 1):
            if end == len(string_list) or string_list[end] == ' ':
                # Reverse each word in the reversed string
                reverse(string_list, start, end - 1)
                start = end + 1
        
        # Convert list back to string and return
        return ''.join(string_list)