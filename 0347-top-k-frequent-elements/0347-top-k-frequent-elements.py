class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        U:
            q) input arr can be empty?
            q) what should i return if there is the same count but k is not sufficient
            
        num: [1,1,1,2,2,3] k=2 => [1,2]
        
        M : 
            hashmap (key: count, val: number), bucketsort
            
        P :
            1. init a map
            2. iterate a loop to put key and val inside the map
        '''
        
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        
        for n in nums:
            count[n] = count.get(n,0) + 1
            
        for n, cnt in count.items():
            freq[cnt].append(n)
            
        res = []
        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res