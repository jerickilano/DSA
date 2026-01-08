class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Two Pointers
        left = 0
        for right in range(len(nums)):
            if nums[right] != val:
                nums[left] = nums[right]
                left += 1
        return left