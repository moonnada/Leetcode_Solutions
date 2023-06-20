class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        '''
        U:
        q) what if two input strs lengths are different?
        q) can two input strs be empty?
        
        ex) 'cabbba'  ,  'abbccc'
          1. caabbb       abbccc
          2. baaccc
          3. abbccc
          
        M: hashmap, sliding window
        
        P: 
            1. check edge cases(empty, different lengths)
            2. counts the occurrence of letters in two words
            3. if letters and occurrence are the same, return true else false
        '''
        
        if len(word1) != len(word2): return False
    
        c1 = Counter(word1)
        c2 = Counter(word2)
        
        if set(word1) == set(word2) and sorted(list(c1.values())) == sorted(list(c2.values())):
            return True
        else: return False
        