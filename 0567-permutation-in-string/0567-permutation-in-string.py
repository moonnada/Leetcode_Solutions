class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        '''
                                ab
        Input: s1 = "ab", s2 = "eidbaooo"
        Output: true
        
     
            
        
        '''
        if len(s1) > len(s2): return False
        
        freqS1, freqS2 = [0] * 26, [0]*26
        
        for i in range(len(s1)):
            freqS1[ord(s1[i]) - ord('a') ] += 1
            freqS2[ord(s2[i]) - ord('a')] += 1
            
        if freqS1 == freqS2: return True
        
        for i in range(len(s1), len(s2)):
            freqS2[ord(s2[i]) - ord('a')] += 1
            freqS2[ord(s2[i- len(s1)]) - ord('a')] -= 1
            
            if freqS1 == freqS2: return True
            
        return False