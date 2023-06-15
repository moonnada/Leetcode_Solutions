class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        U:
            q) is input arr sorted?
            q) can arr be empty?
            q) can I return without sort?
            
            ex) [-1,0,1,2,-1,-4]
            =>[ [-1,0,1], [-1,-1,2] ]
            
                [-4,-1,-1,0,1,2]
                  L           R
                  
                  
        M: two ptrs
        
        P: 
            1. sort input arr
            2. traverse the input arr
                2.1) check there is a duplicate num for the iterator. if it is, just pass the num
                2.2) init two ptrs(left and right)
                2.3) while left < right:
                2.4) if sum of the cur three ptrs  > 0: right--
                2.5) else if sum < 0: left++
                2.6) else put three ptrs in to ans arr
                2.7) left ptr is incremented to avoid adding duplicate
                2.8) make another loop to avoid duplicate 
        '''
        
        ans = []
        nums.sort()
        
        for i,val in enumerate(nums):
            if i>0 and val == nums[i-1]: continue
            
            left, right = i+1, len(nums)-1
            
            while left < right:
                threeSum = val + nums[left] + nums[right]
                if threeSum > 0:
                    right -= 1
                elif threeSum < 0:
                    left += 1
                else:
                    ans.append([val, nums[left], nums[right]])
                    left += 1
                    
                    while nums[left] == nums[left-1] and left < right:
                        left+=1
                        
        return ans