class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        '''
        U:
            q) can input arr be empty?
        
            ex) [1,1,1,0,0,0,1,1,1,1,0], k = 2
                 L
            
        M: sliding window
        
        P: 
            1. traverse the input arr
            2. if curVal is 1, cnt++
            3. if curVal is not 0 and k > 0, cnt++ and k--
            4. while k == 0, left++, k--
            
            
        '''
        
        i = 0
        for j in range(len(nums)):
            k -= 1 - nums[j]
            if k < 0:
                k += 1 - nums[i]
                i += 1
        return j - i + 1