class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * (len(nums))
        postfix = [1] * (len(nums))
        result_list = []
        i = 0
        j = len(nums) - 1
        while i < len(nums):
            if i == 0:
                prefix[i] = 1 * nums[i]
                postfix[j] = 1 * nums[j]
                i += 1
                j -= 1
            else:
                prefix[i] = prefix[i-1] * nums[i]
                postfix[j] = postfix[j+1] * nums[j]
                i += 1
                j -= 1
        # print(prefix)
        # print(postfix)
        i = 0
        while i < len(nums):
            if i == 0:
                result_list.append(postfix[i])
                i += 1
            elif i == (len(nums) - 1):
                result_list.append(prefix[i])
                i += 1
            else:
                result_list.append(prefix[i-1]*postfix[i+1])
                i += 1
        return result_list
        
            

