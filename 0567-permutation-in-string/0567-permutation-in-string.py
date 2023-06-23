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
            2. permutate s1
            3. traverse the input s2 to find s1's permutation
        '''
        if len(s1) > len(s2):
            return False
        
        s1freq =  [0]*26
        s2freq =  [0]*26
        
        for i in range(len(s1)):
            s1freq[ord(s1[i])-97] += 1
            s2freq[ord(s2[i])-97] += 1 
            
        if s1freq == s2freq:
            return True
        
        for i in range(len(s1),len(s2)):
            
            s2freq[ord(s2[i])-97] += 1
            s2freq[ord(s2[i-len(s1)])-97] -= 1
            
            if s1freq == s2freq:
                return True
        
        return False
        