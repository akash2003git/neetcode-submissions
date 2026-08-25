class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        bucket = [[] for i in range(len(nums) + 1)]

        # Create the frequency map
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        # Create the bucket
        for num, count in count.items():
            bucket[count].append(num)

        res = []
        for i in range(len(bucket) - 1, -1, -1):
            for n in bucket[i]:
                if len(res) < k:
                    res.append(n)
            

        return res
            