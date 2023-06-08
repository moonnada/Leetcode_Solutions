class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        U: 
            q) input arr can be empty?
            q) input arr is sorted?

        M:
            hashmap (key: indice , val: element)
        P:
            1. init a map
            2. traverse the input arr to put key and val inside a map
                2.1) if target - curVal is in the map, then return the cur Indice and map's indice
                2.2) else put cur val and key inside a map
        '''
        
        hashmap = {}
        for i in range(len(nums)):
            lookFor = target - nums[i]
            if lookFor in hashmap:
                return [i, hashmap[lookFor]]
            hashmap[nums[i]] = i