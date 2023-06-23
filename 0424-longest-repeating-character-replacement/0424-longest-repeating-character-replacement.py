class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        U: 
        q) can input str or k be empty || 0?
        Q) input str have only upper letter?
        
        ex) "AABABBB", k = 1
             L
                R
             
             for r in s
                 if s[l] == s[r], cnt++
                 else
                    while k >0,
                        k--. cnt++

                maxCnt = max(cnt, maxCnt)
             
             
        
        '''
        left = 0
        freqMap = {}
        maxFreq = 0
        strLen = 0
        
        for right in range(len(s)):
            freqMap[s[right]] = freqMap.get(s[right],0) + 1
            
            maxFreq = max(maxFreq, freqMap[s[right]])
            
            isValid = (right - left + 1 - maxFreq <= k)
            
            if not isValid:
                freqMap[s[left]] -= 1
                left += 1
                
            strLen = right - left + 1
            
        return strLen