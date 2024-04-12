class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = maxFreq = longest = 0
        d = {}
        
        for right in range(len(s)):
            d[s[right]] = d.get(s[right], 0 )+1
            maxFreq = max(maxFreq, d[s[right]])
            
            while right - left + 1 - maxFreq > k:
                d[s[left]] -= 1
                left += 1
                
            longest = max(longest, right-left+1)
            
        return longest