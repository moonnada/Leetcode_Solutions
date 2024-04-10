class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        1. check edge cases(empty or one char)
        2. init a map(key: sorted word, value: a list of the sorted word)
        3. traverse the input list to find group the anagram
            3.1) sort the cur word
            3.2) if the sorted word in the map, then add the original word into the map
            3.3) else put the sorted word inthe map as key
        4. return map.values
        '''
        
        # if len(strs) == 0 or len(str) == 1: return strs
        
        hmap = {}
        
        for word in strs:
            sortedWord = ''.join(sorted(word))
            if sortedWord in hmap:
                hmap[sortedWord].append(word)
            else:
                hmap[sortedWord] = [word]
                
        return list(hmap.values())
        