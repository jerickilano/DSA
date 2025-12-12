class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Time: O(n) Space: O(n)
        # HashMap (one pass)/for each num in enum(nums)/check 
        # if diff is in map/return index of diff AND current i
        
        map = {}
        for i, num in enumerate(nums):
            diff = target - nums[i]
            if diff in map:
                return [map[diff], i]
            map[num] = i
        return [0,0]
