class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        freq = [[] for i in range(len(nums)+1)]
        
        for i in nums:
            d[i] = d.get(i,0) + 1
            
        for num, cnt in d.items():
            freq[cnt].append(num)
            
        res = []
        for i in range(len(freq)-1, 0 ,-1):
            for num in freq[i]:
                res.append(num)
            
                if len(res) == k: return res