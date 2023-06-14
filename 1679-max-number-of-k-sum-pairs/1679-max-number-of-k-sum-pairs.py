class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        '''
        U:
        q) can input arr be empty?
        q) is input sorted? 
        ex) [1,2,3,4] k=5
             L     R
         
         
        ex) [3,1,3,4,3], k=6
        
            [1,3,3,3,4]
            
         M: two ptrs
         
         P: 
         1. init two ptrs as left and right
         2. while left < right, 
         2.1) if combine of elements of left and right are equal to k, then left++, right--, and cnt++
         2.2) else if arr[left] + arr[left] < k, left++
         2.3) else right--
         
         time: o(nlgn), space: o(1)
        '''
        counter = defaultdict(int)
        cnt = 0
        
        for x in nums:
            comp = k - x
            if counter[comp] > 0:
                counter[comp]-=1
                cnt+=1
            else:
                counter[x]+=1
                
        return cnt
        
#         left, right = 0, len(nums)-1
#         cnt = 0
#         nums.sort()
        
#         while left < right:
#             val = nums[left] + nums[right]
#             if val < k:
#                 left+=1
#             elif val > k:
#                 right-=1
#             else:
#                 right-=1
#                 left+=1
#                 cnt+=1
                
#         return cnt



        