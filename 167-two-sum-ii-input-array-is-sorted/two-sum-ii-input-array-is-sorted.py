class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Two Pointer Converging
        # [2,7,11,15], target = 9
        #  L
        #          R
        # twosum = 17
        l, r, = 0, len(numbers) - 1

        while l < r:
            twosum = numbers[l] + numbers[r]
            if twosum == target:
                return [l + 1, r + 1]
            elif twosum > target:
                r -= 1
            else:
                l += 1
        return [0, 0]