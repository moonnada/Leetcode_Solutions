class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        ex) Input: nums = [4,5,6,7,0,1,2], target = 6
            Output: 4
            
        '''
        
        left, right = 0, len(nums)-1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target: return mid
            
            elif nums[left] <= nums[mid]:
                if nums[mid] < target or nums[left] > target:
                    left = mid + 1
                else:
                    right = mid -1 
            else:
                if nums[mid] > target or nums[right] < target:
                    right = mid -1 
                else:
                    left = mid + 1
            
        return -1