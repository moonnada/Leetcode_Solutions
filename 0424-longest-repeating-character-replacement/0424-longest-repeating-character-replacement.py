class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        1. init a hashmap
        2. count each val in the input str
        3. iterative the input str to get the longest 
            3.1) if right - left +1 - max hashmap val > k, then remove the cur val in the map, left++
            3.2) else get the length
        '''
        
        count = {}
        left = longest = 0
        
        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1
            
            while right - left + 1 - max(count.values()) > k:
                count[s[left]] -= 1
                left += 1
                
            longest = max(longest, right-left+1)
            
        return longest