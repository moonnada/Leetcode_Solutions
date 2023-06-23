class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        U: 
        q) can input str or k be empty || 0?
        Q) input str have only upper letter?
        
        M: hashmap, sliding window
        
        P:
            1. init global values( first ptr, map, countFreq, strLen)
            2. iterate over the input str
                2.1) count each char and put key and val into map
                2.2) get max freqNum
                2.3) init a valid point as boolean. 
                2.4) if cur point is not valid, remove the left ptr in map, and left ptr is incremented
                2.5) get the longest len of str
        '''
       
        left = 0
        freqMap = {}
        strLen = 0
        maxFreq = 0
        
        for right in range(len(s)):
            freqMap[s[right]] = freqMap.get(s[right], 0) + 1
            maxFreq = max(maxFreq, freqMap[s[right]])
            
            isValid = right - left + 1 - maxFreq <= k
            
            if not isValid:
                freqMap[s[left]] -= 1
                left += 1
                
            strLen = right - left + 1
            
        return strLen