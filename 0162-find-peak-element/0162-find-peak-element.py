class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        '''
        U:
            keypoints:
            - the input arr contains multiple peeks, return the index to any of the peaks.
            - the input list can have negative values
            - cant have the same numbers continuously
            - must write in o(lgn) time.
            
            ex) [9,2,1] => return 0
            
        M: binary search
        
        P: 
            1. init two ptrs as left and right
            2. while left <= right,
                2.1) check the left neighbor is greater. if it is, the right val is moved to the left side
                2.2) check the right neighbor is greater. if it is, the left val is moved to the right side
                2.3) else return the mid index ()
                
        '''
        left, right = 0, len(nums) -1
        
        while left <= right:
            # mid = (left + right) // 2
            mid = left + (right-left) // 2
            if nums[mid] < nums[mid-1] and mid > 0:
                right = mid-1
            
            elif mid < len(nums)-1 and nums[mid] < nums[mid+1]:
                left = mid+1
            
            else: return mid
