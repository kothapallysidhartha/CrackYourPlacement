class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price = float('inf')  # Initialize with infinity for finding the minimum price.
        max_profit = 0  # Initialize maximum profit as 0.

        for price in prices:
            # Update minimum price if current price is lower.
            if price < min_price:
                min_price = price
            
            # Calculate profit if current price is sold after buying at min_price.
            profit = price - min_price
            
            # Update maximum profit if current profit is higher.
            if profit > max_profit:
                max_profit = profit
        
        return max_profit
