class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        '''
        U:
            q) can input arr be empty?
        
            ex) [1,1,1,0,0,0,1,1,1,1,0], k = 2
                 L
            
        M: sliding window
        
        P: 
            1. init a left as 0
            2. traverse the input arr
                2.1) k -= 1- curVal (if rightpt is 0, then k is decremented. if rightpt is 1, then k is remained)
                2.2) if k < 0, k += 1 - leftpt (if curVal is 0, then k is incremented. if leftpt is 1, then k is remained)
                2.3) left is incremented
            3. return right - left + 1
        '''
        left = 0
        
        for right in range(len(nums)):
            k -= 1- nums[right]
        
            if k < 0:
                k += 1- nums[left]
                left+=1
                
        return right-left+1
        