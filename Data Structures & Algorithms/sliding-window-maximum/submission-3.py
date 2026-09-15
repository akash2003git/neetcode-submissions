class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []

        # Store indices of useful elements in monotonically decreasing
        # order of their corresponding values.
        q = collections.deque()

        # l and r represent the left and right boundaries of the window.
        l = r = 0

        while r < len(nums):
            # Remove indices whose values are smaller than nums[r].
            # Such values can never become the maximum of the current
            # or any future window containing nums[r].
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            # Add the current element's index.
            q.append(r)

            # Remove the index at the front if it lies outside
            # the current window [l, r].
            #
            # We store indices, rather than values, so that we can
            # determine when an element has left the window.
            if q[0] < l:
                q.popleft()

            # Start recording maximums once the window reaches size k.
            if r - l + 1 >= k:
                # Because the deque stores values in decreasing order,
                # its front always contains the index of the maximum
                # element in the current window.
                output.append(nums[q[0]])

                # Slide the window one position to the right.
                l += 1

            # Expand the right side of the window.
            r += 1

        return output