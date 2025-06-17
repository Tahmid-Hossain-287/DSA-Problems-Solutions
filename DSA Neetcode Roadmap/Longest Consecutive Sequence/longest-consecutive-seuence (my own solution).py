class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        heapq.heapify(nums)
        counter = [1]
        last_item = heapq.heappop(nums)
        counter_index = 0
        for i in range(len(nums)):
            current_item = heapq.heappop(nums)
            difference = current_item - last_item
            last_item = current_item
            if difference == 1:
                counter[counter_index] += 1
            elif difference > 1:
                counter.append(1)
                counter_index += 1
            elif difference < 1:
                continue
        print(counter)
        return max(counter)