class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        maxProfit = 0
        
        for right in range(1, len(prices)):
            if prices[left] >= prices[right]: left = right
            else:
                maxProfit = max(maxProfit, prices[right]-prices[left])
                
        return maxProfit
            
        
#         maxProfit = 0
#         for i in range(len(prices)):
#             r = i+1
            
#             while r < len(prices) and prices[i] < prices[r]:
#                 curProfit = prices[r] - prices[i]
#                 maxProfit = max(maxProfit, curProfit)
#                 r += 1
                
#         return maxProfit       