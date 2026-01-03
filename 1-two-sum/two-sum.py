class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Time: O(n) Space: O(N)
        seen = {}
        for i, num in enumerate(nums): # Enumerate to have access to the indices of the array
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        return [0,0]