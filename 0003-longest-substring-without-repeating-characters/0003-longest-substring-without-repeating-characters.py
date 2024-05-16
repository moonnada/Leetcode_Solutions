class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        set = {c,a}
                       r 
        Input: s = "baca"
                      l
                      
        curLongest              
        maxlongest = 3
        
        Output: 3
        '''
        hset = set()
        left = longest = 0
        for right in range(len(s)):          
            while s[right] in hset:
                hset.remove(s[left])
                left += 1
            
            hset.add(s[right])

                
            longest = max(longest, right-left+1)
        
        return longest
    
    
    