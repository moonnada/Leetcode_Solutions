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
        
        hashset = set(nums)
        longest = 0
        
        for num in hashset:
            if num-1 not in hashset:
                curVal = num
                curCnt = 1
                
                while curVal+1 in hashset:
                    curVal+=1
                    curCnt+=1
                
                longest = max(longest, curCnt)
                
        return longest