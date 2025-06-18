class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums_set = set(nums)
        counter = [1]
        counter_index = 0
        for i in nums:
            left_item = i - 1
            if left_item in nums_set:
                continue
            right_item = i + 1
            while right_item in nums_set:
                counter[counter_index] += 1
                right_item += 1
            counter_index += 1
            counter.append(1)
        return max(counter)
