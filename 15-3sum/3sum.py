class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Time: O(n^2) Space: O(m) m the number of triplets
        # Two Pointers w/ .sort()
        # [a,b,c,d,e,f,g]
        #  i,L, , , , ,R

        res = []
        nums.sort()

        for i, a in enumerate(nums): # iterate through the index and the value
            if a > 0:
                break

            if i > 0 and a == nums[i - 1]: # avoid duplicate values
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        return res