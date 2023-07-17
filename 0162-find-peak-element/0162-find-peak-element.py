class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        '''
        U:
            - the input arr contains multiple peeks, return the index to any of the peaks.
            - the input list can have negative values
            - cant have the same numbers continuously
            - must write in o(lgn) time.
            
        M: binary search
        
        
            
        '''
        left , right = 0, len(nums) -1
        
        while left <= right:
            mid = (left + right) // 2
            #left neighbor greater
            if mid > 0 and nums[mid] < nums[mid-1]: 
                right = mid -1
            
            #right neighbor greater
            elif mid<len(nums)-1 and nums[mid] < nums[mid+1]:
                left = mid + 1
            
            else: return mid
