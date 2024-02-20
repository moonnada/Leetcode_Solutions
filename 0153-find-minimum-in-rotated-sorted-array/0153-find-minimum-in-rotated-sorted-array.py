class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
        Input: nums = [9,0,1,2,3,4,5,6]
        Output: 0
        
        if num[left] > nums[mid]:
            right = mid -1
        else if num[right] < nums[mid]
            left = mid +1
        '''
        
        left, right = 0, len(nums)-1
        
        while left < right:
            mid = (left + right) //2
            
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
                
        return nums[left]