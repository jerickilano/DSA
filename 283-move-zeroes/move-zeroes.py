class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Two pointer (Same direction)
        # [0,1,0,3,12]
        #  L
        #    R
        # L : tracks the location of the next non-zero
        # R : iterates to find nonzeros to switch with left
        l, r = 0, 0
        while r < len(nums):

            # Swap in place
            if nums[r] != 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1

            r += 1