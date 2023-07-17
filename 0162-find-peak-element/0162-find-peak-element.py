class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        '''
        U:
            - the input arr contains multiple peeks, return the index to any of the peaks.
            - the input list can have negative values
            - cant have the same numbers continuously
            - must write in o(lgn) time.
            
            q) 
            
        '''
        left , right = 0, len(nums) -1
        
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid+1]:
                right = mid
            else: left = mid + 1
                
        return left