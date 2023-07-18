class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        '''
        U:
            keypoints: 
                - return the minimum number 
                - how many bananas could she eat per hour
            
            ex) [30, 11, 23, 4, 20] , h=6
            
                1  2 3....   29 30 
                
                M: binary search
        
        P:
            1. init two ptrs as left and right 
            2. while left <= right,
                2.1) get the mid point
                2.2) init a hours val
                2.3) traverse the input list to get valid hours
                    2.4) if hours > target, update the left point
                    2.5) else, update the right point              
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