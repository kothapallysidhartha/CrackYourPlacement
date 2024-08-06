class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        c5=0
        c10=0
        c20=0
        #bills.sort()
        for i in bills:
            if i==5:
                c5+=1
            elif i==10:
                c10+=1
                if c5:
                    c5-=1
                else:
                    return False
            else:
                c20+=1
                if c10>=1 and c5>=1:
                    c10-=1
                    c5-=1
                elif c5>=3:
                    c5-=3
                else:
                    return False
        return True
                
                
        