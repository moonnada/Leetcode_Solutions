class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
                      r
                     r 
        Input: s = "pwwkew"
        Output: 3
        
        
        '''
        hashSet = set()
        left = longest  = 0
        
        for right in range(len(s)):
            while s[right] in hashSet:
                hashSet.remove(s[left])
                left += 1
            
            hashSet.add(s[right])
            longest = max(longest, right-left+1)
            
        return longest