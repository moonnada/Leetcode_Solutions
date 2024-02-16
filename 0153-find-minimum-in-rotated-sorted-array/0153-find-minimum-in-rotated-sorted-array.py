class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
        Input: nums = [8,0,1,2,3,4,6,7]
        Output: 0
        '''
        start, end = 0, len(nums)-1
        
        while start < end:
            mid = (start + end) // 2
            if nums[mid] > nums[end]:
                start = mid+1
            else:
                end = mid
                
        return nums[start]
        
        