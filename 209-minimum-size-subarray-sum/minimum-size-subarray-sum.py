class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # target = 4
        # curr_sum = 4
        # min_size = 2
        # [1,4,4]
        #  L
        #    R 
        l = 0
        curr_sum = 0
        min_size = 10000000000
        for r in range(len(nums)):
            curr_sum += nums[r]

            while curr_sum >= target:
                min_size = min(min_size, r - l + 1)
                curr_sum -= nums[l]
                l += 1
        
        if min_size == 10000000000:
            return 0

        return min_size

