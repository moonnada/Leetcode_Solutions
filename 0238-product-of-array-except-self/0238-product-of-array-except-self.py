class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        U:  q) input arr can be empty?
            q) input arr is sorted?
            
            [1,2,3,4]
             1 1 2 6
             
            24  12  4  1
            
        =>  24 12 8 6
        
        
             [1,2,3,4]
             1 1 2 6
                 8 6
                 
        M: two arr(start from left and from right)
        
        P:
            1. init an arr for left to right
            2. iterate a loop to get product 
            3. init an arr for right to left
            4. iterate a loop to get product
            5. get each product to combine left and right arrs
                
        '''
        
        length = len(nums)
        
        left, right, ans = [0]*length, [0]*length,[0]*length
        
        left[0] = 1
        for i in range(1, length):
            left[i] = nums[i-1] * left[i-1]
            
        right[length-1] = 1
        for i in reversed(range(length-1)):
            right[i] = nums[i+1] * right[i+1]
            
        for i in range(length):
            ans[i] = left[i] * right[i];
            
        return ans