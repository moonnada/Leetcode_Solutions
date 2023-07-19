class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        '''
        U:
            key points:
                1. len(nums1) = len(num2)
                2. return the maximum possible
        '''
        pairs = [(n1, n2) for n1, n2 in zip(nums1, nums2)]
        pairs = sorted(pairs, key=lambda p:p[1], reverse=True)
        
        minHeap = []
        n1Sum = 0
        res = 0
        
        for n1, n2 in pairs:
            n1Sum += n1
            heapq.heappush(minHeap, n1)
            
            if len(minHeap) > k:
                n1pop = heapq.heappop(minHeap)
                n1Sum -= n1pop
            
            if len(minHeap) == k:
                res = max(res, n1Sum * n2)
                
        return res