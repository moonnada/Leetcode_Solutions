class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        maxContainer = 0
        
        while left < right:
            curHeight = min(height[left], height[right])
            curWeight = (right+1) - (left+1)
            
            curContainer = curHeight * curWeight
            maxContainer = max(maxContainer, curContainer)
            
            if height[left] < height[right]: left +=1 
            else: right -=1
            
        return maxContainer
        