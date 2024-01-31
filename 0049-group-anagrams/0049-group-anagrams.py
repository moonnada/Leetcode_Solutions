class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
    
#         q) can have the same letters consecutively?
#         asd
        
#         0. init a hashmap (key: a word, value: array of the anagram words)
#         1. traverse the input arr to make group anagrams
#             1.1) sort the cur word
#             1.2) if map has the cur sorted word, then put its array
#             1.2) if not, then put the word as a new key and value in the map
#         2. return the map's value

        # time = o(m * nlgn)
        # space = o(n)
        
        anagrams = {}
        for word in strs:
            temp = ''.join(sorted(word))
            
            if temp in anagrams:
                anagrams[temp].append(word)
            else:
                anagrams[temp] = [word]
                
        return list(anagrams.values())