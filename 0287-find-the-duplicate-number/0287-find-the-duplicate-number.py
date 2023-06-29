class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        '''
        U:
            key points: always have one repeated num, uses only o(1) space complexity
            
        M: sorting?
        
        P: 
            1. sort input arr
            2. traverse to find a duplicate num
                2.1) if find, return the num
        '''
        nums.sort()
        
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return nums[i]
        
        return -1