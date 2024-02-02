class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        set
        
        Input: nums = [100,4,200,1,3,2]
        Output: 4
        
        set = [100,4,200,1,3,2]
        longest = 0
        '''
       
        hashset = set(nums)
        longest = 0
        
        for num in hashset:
            if num-1 not in hashset:
                curVal = num
                curCnt = 1
                
                while curVal + 1 in hashset:
                    curVal += 1
                    curCnt += 1
                    
                longest = max(curCnt, longest)
                
        return longest