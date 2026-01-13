class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # Iterate and add n & n + 1
        n = len(nums)
        res = [0] * n * 2
        for i in range(len(nums)):
            res[i] += nums[i]
            res[i + n] += nums[i]
        return res