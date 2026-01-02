class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 3 pointer
        # 0 = red, 1 = white, 2 = blue
        # L : next available red spot
        # R : next available blue spot
        # [2,0,2,1,1,0]
        #  L
        #  M
        #            R
        l, m, r = 0, 0, len(nums) - 1
        while m <= r:
            #print(nums[l],nums[m],nums[r])
            # blue check
            if nums[m] == 2:
                nums[r], nums[m] = nums[m], nums[r]
                r -= 1
            # red check
            elif nums[m] == 0:
                nums[l], nums[m] = nums[m], nums[l]
                l += 1
                m += 1
            # iterate m
            else:
                m += 1