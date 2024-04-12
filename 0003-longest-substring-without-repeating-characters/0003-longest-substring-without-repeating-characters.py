class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hset = set()
        longest = 0
        left = 0
        
        for right in range(len(s)):
            while s[right] in hset:
                hset.remove(s[left])
                left += 1
                
            hset.add(s[right])
            longest = max(longest, right-left+1)
        
        return longest