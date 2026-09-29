class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        
        longest = 0
        for n in nums:
            curr = 0
            if n-1 not in num_set:
                while n in num_set:
                    curr += 1
                    n += 1
                longest = max(curr, longest) 

        return longest   
