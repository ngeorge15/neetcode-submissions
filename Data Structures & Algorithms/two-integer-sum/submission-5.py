class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev = {}

        for i, n in enumerate(nums):
            comp = target - n

            if comp in prev:
                return [prev[comp], i]
            
            prev[n] = i
        