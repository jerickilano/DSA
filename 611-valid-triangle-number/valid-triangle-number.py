class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        # 3 pointer + sort
        # triangle if sums of any two sides is greater than 3rd side
        # [2,2,3,4]
        #  L   R i
        nums.sort()
        count = 0
        for i in range(len(nums) - 1, 1, -1):
            l, r = 0, i - 1
            while r > l:
                sums = nums[l] + nums[r]
                # print(l, r, i)
                if sums > nums[i]:
                    count += r - l
                    r -= 1
                else:
                    l += 1
    
        return count
            