class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        newMap = {}
        for word in strs:
            temp = ''.join(sorted(word))
            if temp in newMap:
                newMap[temp].append(word)
            else:
                newMap[temp] = [word]
        
        return list(newMap.values())