class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        '''
        U: 
        q) what if the input arr is empty?
        q) what if the input arr doesnt have a 0 
        q) is the input arr sorted? and output would be sorted?
        
        [0,1,0,3,12]
         L
           R
        [1,0,0,3,12]
           L
               R
        [1,3,0,0,12]
           L
               R
        M:
        two ptrs
        
        P:
        1. init a first ptr as 0 
        2. traverse the input arr to swap if cur val is not 0. and the first val is incremented
        '''
        left = 0
        for right in range(len(nums)):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left+=1
        
        return nums