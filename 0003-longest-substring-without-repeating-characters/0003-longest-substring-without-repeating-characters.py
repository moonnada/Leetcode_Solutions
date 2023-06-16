class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        U:
        q) can input str be empty?
        q) can it distinguish upper and lower cases?
        
        
        ex) "pwwkew"
             LR
               R
               
        ex) "abcabcbb"     
             LR
             
        M: sliding window, hashset
        
        P: 
            1. check edge cases(empty, one letter)
            2. init a set and leftptr
            3. traverse the input str
                3.1) while curVal is in set, then remove the val in the set and left++
                3.2) out of while loop(which means curVal is not in the set), put the curVal in the set
                3.3) get max length
                            
        '''
        
        if len(s) == 0 or len(s)==1: return len(s)
        
        charSet = set()
        
        left = maxCnt = 0
        
        for right in range(len(s)):
            while s[right] in charSet:
                charSet.remove(s[left])
                left += 1
                
            charSet.add(s[right])
            maxCnt = max(maxCnt, right - left + 1)
        
        return maxCnt