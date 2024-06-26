class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        d={}
        for i in s:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        s=""
        for key,value in d.items():
            max_key = max(d, key=d.get)
            max_value = d[max_key]
            s=s+(max_key)*max_value
            del d[max_key]
        return s
        