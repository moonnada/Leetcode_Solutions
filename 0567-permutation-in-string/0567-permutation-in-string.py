class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        '''
        U:
            permutation only?
            q) s1 len is alway smaller than s2?
            q) s1 and s2 consist only lowercases?
            
            ex) s1= 'ab', s2 = 'eidbaooo'
                newS1 = ba
            
        M: substring
        
        P:
            1. check edge cases(empty, s1 and s2 length)
            2. init a global values of count freq of both strs
            3. traverse the input str1 to get freq
            4. if both freq are equal, then reture true\
            5. traverse the input str2 to slide a window
                5.1) sliding window is incremented
                5.2) remove the left side of window
                5.3) if freq of both strs are equal, then return
            6. return false
        '''
        if len(s1) > len(s2): return False
        
        freqS1 = [0] * 26
        freqS2 = [0] * 26
        
        for i in range(len(s1)):
            freqS1[ord(s1[i]) - 97] += 1
            freqS2[ord(s2[i])- 97] += 1
            
        if freqS1 == freqS2:
            return True
        
        for i in range(len(s1), len(s2)):
            freqS2[ord(s2[i]) - 97] += 1
            freqS2[ord(s2[i - len(s1)]) - 97] -= 1
            
            if freqS1 == freqS2: return True
            
        return False