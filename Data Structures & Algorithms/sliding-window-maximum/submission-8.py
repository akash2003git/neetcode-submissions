class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        l = 0
        res = []

        for r in range(len(nums)):
            while q and nums[r] > nums[q[-1]]:
                q.pop()
            q.append(r)

            if l > q[0]:
                q.popleft()

            if r - l + 1 == k:
                res.append(nums[q[0]])
                l += 1

        return res


       
#     l   r
# 0 1 2 3 4 5 6
# 1 2 1 0 4 2 6

# q => 4