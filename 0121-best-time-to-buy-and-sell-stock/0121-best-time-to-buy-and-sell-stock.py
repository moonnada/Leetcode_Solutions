class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        Input: prices = [7,1,5,3,6,4]
        Output: 5
        
        1. init a set and left ptr 
        2. traverse the input list to find max profit
            2.1) if cur element > cur left, remove cur element in the set. left ++
            2.2) else add cur element into the set. calculate the max profit
        '''
        
        left = maxProfit = 0
        
        for right in range(1, len(prices)):
            if prices[left] >= prices[right]: left = right
            else:
                maxProfit = max(maxProfit, prices[right]- prices[left])
        
        return maxProfit