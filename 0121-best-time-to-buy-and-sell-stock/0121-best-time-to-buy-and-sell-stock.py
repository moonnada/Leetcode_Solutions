class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        U:
        q) can arr be empty?
        q) is input arr based on integer only?
        
        ex) [7,1,5,3,6,4]
             l r
               l r
            [7,6,4,3,1]
             l r
               l r
               
        M: sliding window
        
        P:
            1. init a ptr
            2. if left >= right, left++
            3. get the cur profit
            3. get max profit
        
        '''
        left = maxProfit = 0
        
        for right in range(1, len(prices)):
            if prices[left] >= prices[right]: left = right
            else:
                curProfit = prices[right] - prices[left]
                maxProfit = max(curProfit, maxProfit)
                
        return maxProfit