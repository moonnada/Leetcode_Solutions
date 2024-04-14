class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        
        while left <= right:
            mid = (left + right) // 2
            hrs = 0
            for pile in piles:
                hrs += math.ceil(pile/mid)
                
            if hrs > h:
                left = mid + 1
            else:
                right = mid- 1
        
        return left
                
                
        