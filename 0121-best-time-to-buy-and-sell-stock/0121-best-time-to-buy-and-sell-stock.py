class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        Input: prices = [7,1,5,3,6,4]
        Output: 5
        
        
        '''
        left= maxProfit = 0
        
        for right in range(1, len(prices)):
            if prices[left] >= prices[right]: left = right
            else:
                curProfit = prices[right] - prices[left]
                maxProfit = max(curProfit, maxProfit)
            
        return maxProfit
        