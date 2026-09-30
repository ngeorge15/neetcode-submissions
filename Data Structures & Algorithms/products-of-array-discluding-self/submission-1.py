class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        output = []
        prefix = 1

        for n in nums:
            output.append(prefix)
            prefix *= n

        suffix = 1
        for i in range(len(nums) - 1, -1, -1):
            output[i] *= suffix
            suffix *= nums[i]
        
        return output
# [1, 1, 2, 8]
# [8] suff = 6
# [12, 8] suff = 24
# 9