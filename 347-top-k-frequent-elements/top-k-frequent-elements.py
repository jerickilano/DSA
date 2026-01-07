class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # HashMap + Sorting
        # k = 2
        # [1,1,1,2,2,3]
        # Value : Frequency
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        # Add frequencies in seperate array
        arr = []
        for num, cnt in count.items():
            arr.append([cnt, num])
        arr.sort() # sort

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res