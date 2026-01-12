class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # HashMap
        res = {}
        for num in nums:
            res[num] = res.get(num, 0) + 1
            #print(res)
            if res[num] > len(nums) // 2:
                return num
