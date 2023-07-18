class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        '''
        P:
            1. get two ptrs as left and right 
            2. while left <= right:
                2.1) init the mid ptr
                2.2) traverse the piles list to get valid hours
                    2.2-1) get hours
                2.3) if hours > h, right = mid -1
                2.3) elif hours < h, left = mid +1
                
        '''
        
        left , right = 1, max(piles)
        
        while left <= right:
            mid = left + (right-left) // 2
            hours = 0

            for pile in piles:
                hours += math.ceil(pile/mid)
                
            if hours > h:
                    left = mid +1 
            else: right = mid -1

        return left