class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        for i in range(len(prices)):
            r = i+1
            
            while r < len(prices) and prices[i] < prices[r]:
                curProfit = prices[r] - prices[i]
                maxProfit = max(maxProfit, curProfit)
                r += 1
                
        return maxProfit
        