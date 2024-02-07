class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
                    0123
                       r
                    l
        Input: s = "AABABBABB", k = 1
        Output: 4
        A:4
        B:5
        
        1. init a map to count each alphabet in the str
        2. iterative over the input str to count each alphabet in the map
            2.1)count each letter
            2.2)if cur position - max countVal > k, left++, remove the curleft in map
            2.3)else get the max length
        
        '''
        
        count = {}
        left = maxLen = 0
        
        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1
            
            while right - left +1 - max(count.values()) > k:
                count[s[left]] -= 1
                left += 1
                
            
            maxLen = max(maxLen, right - left +1)
        
        return maxLen
            
       