class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        Input: nums = [100,4,200,1,3,2]
        Output: 4
        
        M: hashset
        
        P: 
            1.init a set with the input list
            2.traverse the hashset
                2.1) while hashset not has cur-1, curval = cur-1
                2.2) while hashset has cur+1, curLeng++, cur+1
                2.3) get the max longest
        '''
        
        curSet = set(nums)
        longest = 0
        
        for num in curSet:
            if num-1 not in curSet:
                curVal = num
                curCnt = 1
                
                while curVal+1 in curSet:
                    curVal+=1
                    curCnt+=1
                
                longest = max(curCnt, longest)
            
        return longest