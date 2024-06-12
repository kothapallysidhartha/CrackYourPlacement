class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        emp = 0
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                empty_prev = (i == 0 or flowerbed[i - 1] == 0)
                empty_next = (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0)
                
                if empty_prev and empty_next:
                    flowerbed[i] = 1
                    emp += 1
                    
            if emp >= n:
                return True
                
        return False

