class Solution:
    def maxArea(self, height: List[int]) -> int:
        '''
        U:
        q) what if input arr is empty?
         1 2 3 4 5 6 7 8 9
        [1,8,6,2,5,4,8,3,7]
         L               R        
        
        M: two ptrs
        
        P:
            1. init two ptrs(left and right)
            2. while left < right: 
                2.1) get width (right - left)
                2.2) get height by comparing arr[right] and arr[left] to find min
                2.3) get area( width * height)
                2.4) save cur area as max and keep looping to find max
                2.5) compare elements of left and right and if one of each is less than others then move to the move to next one
        '''
        
        left, right = 0, len(height)-1
        
        curArea = maxArea = 0
        
        while left < right:
            width = right - left
            curHeight = min(height[left], height[right])
            curArea = width * curHeight
            maxArea = max(curArea, maxArea)
            
            if height[left] <= height[right]:
                left += 1
            else: right -= 1
                
        return maxArea
            
            