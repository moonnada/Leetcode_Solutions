class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        '''
        U:
        q) can arr be empty?
        
        ex) [0,1,1,1,0,1,1,0,1]
             
             
    
     
             
        M: sliding window
        
        P:
        1. init a left,zerocnt, cnt as 0
        2. traverse the input arr 
            2.1) if zero is found, zerocnt++
            2.2) while zerocnt > 1, if nums[start] ==0, zerocnt--. start++
            2.3) get max
        '''
        
        left = maxCnt = zeroCnt = 0
        
        for right in range(len(nums)):
            if nums[right] == 0:
                zeroCnt += 1
                
            while zeroCnt > 1:
                if nums[left] == 0:
                    zeroCnt -= 1
                left += 1
                
            maxCnt = max(maxCnt, right-left)
            
        return maxCnt