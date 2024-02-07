class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
                       r
                    l
        Input: s = "AABABBABB", k = 1
        Output: 4
        
        
        while k >0, 
            r++
            curLen++
        
        
        '''
        count = {}
        ans = 0
        left = 0
        
        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1
            
            while right - left +1 - max(count.values()) > k:
                count[s[left]] -= 1
                left += 1
                
            ans = max(ans, right - left +1)
        return ans