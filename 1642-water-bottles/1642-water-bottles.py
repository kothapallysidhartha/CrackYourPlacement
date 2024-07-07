class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        totalBottles = numBottles
        while numBottles >= numExchange:
            newBottles = numBottles // numExchange
            rBottles = numBottles % numExchange
            totalBottles += newBottles
            numBottles = newBottles + rBottles
        return totalBottles
