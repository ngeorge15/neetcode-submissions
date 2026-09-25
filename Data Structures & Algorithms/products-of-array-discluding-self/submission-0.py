class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prods = []
        prod = 1
        for i in nums:
            prods.append(prod)
            prod *= i
        
        count = len(nums) - 1
        prod = 1
        for i in reversed(nums):
            prods[count] *= prod
            prod *= i
            count -= 1
        return prods
        