class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ballin = 0
        ball = 0
        right = len(prices)-1

        while right != ball:
            now_ballin = prices[right] - prices[ball]
            if now_ballin > ballin:
                ballin = now_ballin 
            right-=1
            if right == ball:
                right = len(prices)-1
                ball +=1
        
        return ballin
        