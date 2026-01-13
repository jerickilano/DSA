class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Two Pointers but start at the end of each array
        one = m - 1            # last valid index in nums1
        two = n - 1            # last index in nums2
        write = m + n - 1      # position to write into nums1

        while two >= 0:
            if one >= 0 and nums1[one] > nums2[two]:
                nums1[write] = nums1[one]
                one -= 1
            else:
                nums1[write] = nums2[two]
                two -= 1
            write -= 1


        # one = m
        # two = 0
        
        # # appends values of nums2 to the end of nums1
        # while two < n:
        #     nums1[m] = nums2[two]
        #     m += 1
        #     two += 1

        # # 2 pointers to sort the resulting nums 1 array
        # for l in range(len(nums1)):
        #     r = l
        #     while r < len(nums1):
        #         if nums1[r] < nums1[l]:
        #             nums1[l], nums1[r] = nums1[r], nums1[l]
        #         r += 1