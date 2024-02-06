class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
                    l r
        Input: s = "dvdf"
        Output: 3
        
       1. init a set
       2. put the 1st char into the set
       3. iterative the input str from 1 to the end
        3.1) if cur char is not in the set, curCnt++. get the max length too
        3.2) else left++
        '''
        
        if len(s) == 0 or len(s) == 1: return len(s)
        
        charSet = set()
        
        left = maxCnt = 0
        
        for right in range(len(s)):
            while s[right] in charSet:
                charSet.remove(s[left])
                left += 1
                
            charSet.add(s[right])
            maxCnt = max( maxCnt, right-left+1)
            
        return maxCnt
                
        
    