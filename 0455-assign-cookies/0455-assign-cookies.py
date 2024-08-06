class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        """c=0
        d={}
        for i in s:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        for i in g:
            if i in d and d[i]!=0:
                c+=1
                d[i]-=1
            
        return c
        """
        g.sort()
        s.sort()
        m=0
        n=0
        #c=0
        while n<len(s) and m < len(g):
            if s[n]>=g[m]:
                #c+=1
                m+=1
            n+=1
        return m
        