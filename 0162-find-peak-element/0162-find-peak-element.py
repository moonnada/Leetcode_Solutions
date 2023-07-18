class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        '''
        U:
            keypoints: nums[-1] = nums[n] = -inf
            
            ex) [1,2,1,3,5,6,4] 
                L    M       R
        P:
            1. init two ptrs as left and right
            2. while left <= right,
                2.1) get the mid point
                2.2) check the right greater. if mid < len(list) -1 and list[mid] < list[mid+1], left = mid + 1
                2.3) check the left greater. if 0< mid and list[mid] > list[mid-1], right = mid -1
            3. return mid
        '''
        
        left, right = 0, len(nums)-1
        
        while left <= right:
            mid = left + (right-left) // 2
            
            if mid < len(nums)-1 and nums[mid] < nums[mid+1]: left = mid +1
            
            elif mid > 0 and nums[mid] < nums[mid-1]: right = mid-1
            
            else: return mid