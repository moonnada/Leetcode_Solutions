class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        '''
        
                        1 2 2 3
        Input: piles = [3,6,7,11], h = 8
        Output: 4
        
        
        '''
        left, right = 1, max(piles)
        
        while left <= right:
            mid = (left + right) // 2
            hrs = 0
            for pile in piles:
                hrs += math.ceil(pile/mid)
                
            if hrs > h:
                left = mid + 1
            else:
                right = mid - 1
                
        return left