class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # brute force: nested loop, every index against itself
        # optimal: single pass, keep track of seen, if complement in seen, return

        seen = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in seen:
                return [seen[diff], i]
            seen[n] = i

        
        