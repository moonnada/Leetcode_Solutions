class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        [basic solution] 
        
        Input: nums = [1,2,3,4]
        Output: [24,12,8,6]
        
        left = [1,1,2,6]
        right = [24,12,4,1]
        
        left[0] = 1
        left[1] = left[0] * num[1]
        left[2] = left[1] * nums[2]
        left[3] = left[2] * nums[3]
        
        
        length = len(nums)
        
        left, right, ans = [0]*length,[0]*length, [0]*length
        
        left[0] = 1
        for i in range(1,length):
            left[i] = left[i-1]*nums[i-1]
            
        
        right[length-1] =1
        for i in reversed(range(length-1)):
            right[i] = right[i+1] * nums[i+1]
            
        for i in range(len(nums)):
            ans[i] = left[i] * right[i]
            
        return ans
        
        
        [optimal solution]
        
        Input: nums = [1,2,3,4]
        Output: [24,12,8,6]
        
        ans = [1, 1, 2,6]
            = [,8,6]
        
        '''
        ans = [1] * len(nums)
        preIdx = 1
        for i in range(len(nums)):
            ans[i] = preIdx
            preIdx *= nums[i]
            
        postIdx = 1
        for i in reversed(range(len(nums))):
            ans[i] *= postIdx
            postIdx *= nums[i]
            
        return ans
            
        