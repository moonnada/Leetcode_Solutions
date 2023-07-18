class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        '''
        U:
            keypoints: return the minimun number 
            how many bananas should she eat per hour
            
            ex) [30, 11, 23, 4, 20] , h=6
                 
                 
        '''
        left, right = 1, max(piles)
        
        while left <= right:
            mid = (left + right) // 2
            hours = 0
            
            for pile in piles:
                hours += math.ceil(pile / mid)
                
            if hours > h: left = mid + 1
            else: right = mid -1
                
        return left