class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for i in range(len(nums)+1)]
        d = {}
        
        for i in nums:
            d[i] = d.get(i,0) + 1
            
        for num,cnt in d.items():
            freq[cnt].append(num)
            
        ans = []
        for i in range(len(freq)-1,0,-1):
            for num in freq[i]:
                ans.append(num)
                
                if len(ans)==k: return ans
        