class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ball = prices[0]
        ballin = 0

        for price in prices:
            if price < ball:
                ball = price
            elif price - ball > ballin:
                ballin = price - ball
        
        return ballin
        