class Solution:
    def maxArea(self, height: List[int]) -> int:
        '''
                         0 1 2 3 4 5 6 7 8
        Input: height = [1,8,6,2,5,4,8,3,7]
        Output: 49
        
        key points: get valid width and height
        
        two pointers
        
        1. init two ptrs(left and right)
        2. while left < right
            2.1) get a height to compare left and right val(choose the longest one)
            2.2) get a weight right - left + 1
            2.3) if arr[left] < arr[right], left++
            2.4) else right--
            2.5) get the max container 
        '''
        
        left, right = 0, len(height)-1
        maxContain = 0
        while left < right:
            curHeight = min(height[left], height[right])
            curWeight = right - left
            
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

                
            maxContain = max(curHeight*curWeight, maxContain)
            
        return maxContain