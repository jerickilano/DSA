class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        # Two Pointer
        # Triangle if: sum of any 2 sides is greater than the third side
        # [2,2,3,4]
        #  l
        #        r
        #      m
        nums.sort()
        count = 0
        # r is index of the largest side (c)
        for r in range(len(nums) - 1, 1, -1):
            l, m = 0, r - 1
            while l < m:
                if nums[l] + nums[m] > nums[r]:
                    count += m - l # because numbers in between can interchange
                    m -= 1
                else:
                    l += 1
        return count

        