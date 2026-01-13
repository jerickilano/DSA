class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        one = m
        two = 0
        
        # appends values of nums2 to the end of nums1
        while two < n:
            nums1[m] = nums2[two]
            m += 1
            two += 1

        # 2 pointers to sort the resulting nums 1 array
        for l in range(len(nums1)):
            r = l
            while r < len(nums1):
                if nums1[r] < nums1[l]:
                    nums1[l], nums1[r] = nums1[r], nums1[l]
                r += 1