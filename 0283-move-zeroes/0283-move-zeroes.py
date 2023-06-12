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
        
        M:
        arr
        
        P:
        1. traverse the input arr to count and find 0
            2. if 0 is found, then delete it and count is incremented
        3. while cnt <= 0, add 0 into the arr
        '''
        left = 0
        for right in range(len(nums)):
            if nums[right]:
                nums[left], nums[right] = nums[right], nums[left]
                left+= 1
        return nums