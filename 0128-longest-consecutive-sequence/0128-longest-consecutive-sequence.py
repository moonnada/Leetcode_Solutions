class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        U:
            q) can input arr be empty?
            
        M:
            set
            
        P:
            1. init a set and count val
            2. iterate a loop to find a val in the set
                2.1) if a val -1 is not in set, then curVal would be a new current value
                2.2) set count val as 1
                2.3) while val + 1 in set, keep incrementing curval and count
                2.4) out of while loop, get a max count
            
        '''
        
        hashset = set(nums)
        longest = 0
        
        for num in hashset:
            if num - 1 not in hashset:
                curVal = num
                curCnt = 1
                
                while curVal + 1 in hashset:
                    curVal +=1
                    curCnt +=1
                    
                longest = max(longest, curCnt)
                
        return longest