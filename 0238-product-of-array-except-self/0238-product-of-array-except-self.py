class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        U:  q) input arr can be empty?
            q) input arr is sorted?
            
                 
        M: make an index for pre and post
        
        P:
            1. init ans arr 
            2. init a preIndex as 1 and get product by iterating a loop
            3. init a postIndex as 1 and get ans by iterating a loop
            
        '''
        
        ans = [1] * len(nums)
        preIndex = 1
        for i in range(len(nums)):
            ans[i] = preIndex
            preIndex *= nums[i]
        
        postIndex = 1
        for i in reversed(range(len(nums))):
            ans[i] *= postIndex
            postIndex *= nums[i]
            
        return ans
        