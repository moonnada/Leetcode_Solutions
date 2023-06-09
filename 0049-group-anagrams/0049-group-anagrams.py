class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
            1. init a map and mapping charCount to list of anagrams
            2. iterate a loop to get count by using unicode
            3. inside a loop, create a new loop to count each letter
            4. append cur word into map
            5. return map's val
        '''
        
        hashmap = collections.defaultdict(list)
        for str in strs:
            count = [0] * 26
            for cnt in str:
                count[ord(cnt) - ord('a')] += 1
            
            hashmap[tuple(count)].append(str)
            
        return hashmap.values()
            