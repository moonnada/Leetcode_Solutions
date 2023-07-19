class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        '''
        U:
            key points:
                1. len(nums1) = len(num2)
                2. return the maximum possible
        '''
        res = 0
        totalSum = 0
        heap = []
        
        merged = [(nums2[i] , nums1[i]) for i in range(len(nums1))]
        merged.sort(reverse=True)
        
        for maxOf2, num1val in merged:
            if len(heap) == k:
                totalSum -= heapq.heappop(heap)
                
            totalSum += num1val
            heapq.heappush(heap, num1val)
            
            if len(heap) == k:
                res = max(res, totalSum * maxOf2)
        
        return res