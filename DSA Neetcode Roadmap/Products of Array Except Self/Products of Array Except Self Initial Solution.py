import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result_list = []
        for i in range(len(nums)):
            result_list.append(math.prod(nums[:i] + nums[i+1:]))
        return result_list