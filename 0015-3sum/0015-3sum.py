class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        Input: nums = [-1,0,1,2,-1,-4]
        Output: [[-1,-1,2],[-1,0,1]]
        
        sort = [-4,-1,-1,0,1,2]
        
        1. sort the input list
        2. init 2 ptr (left, right)
        '''
        ans = []
        nums.sort()
        
        for i,val in enumerate(nums):
            if i>0 and val == nums[i-1]: continue
                
            left, right = i+1, len(nums)-1
            
            while left < right:
                threeSum = val + nums[left] + nums[right]
                
                if threeSum > 0:
                    right -=1
                elif threeSum < 0:
                    left += 1
                else:
                    ans.append([val, nums[left], nums[right]])
                    left+=1
                    
                    while nums[left] == nums[left-1] and left < right:
                        left+=1
                        
        return ans