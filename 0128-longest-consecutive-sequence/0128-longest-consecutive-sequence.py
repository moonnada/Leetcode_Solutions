class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hset = set(nums)
        longest = 0
        
        for num in hset:
            
            if not num-1 in hset:
                curNum = num
                cnt = 1
                
                while curNum + 1 in hset:
                    curNum +=1
                    cnt += 1
                    
                longest = max(cnt, longest)
                
        return longest