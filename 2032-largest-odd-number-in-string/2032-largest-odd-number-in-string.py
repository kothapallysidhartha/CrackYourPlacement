class Solution(object):
    def largestOddNumber(self, num):
        """
        :type num: str
        :rtype: str
        """
        """def checkodd(num):
            if num % 2 != 0:
                return num
            elif num < 10:
                return ""
            return checkodd(num // 10) 

        num = int(num)  
        odd_num = checkodd(num)
        return str(odd_num) if odd_num != "" else ""
        """

        for i in range(len(num) - 1, -1, -1):
            if int(num[i]) % 2 != 0:  
                return num[:i + 1]   
        return ""  

