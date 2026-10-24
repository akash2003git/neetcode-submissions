class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        if len(A) > len(B):
            A, B = B, A

        total = len(A) + len(B)
        half = total // 2
        l, r = 0, len(A) - 1

        while True:
            i = (l + r) // 2
            j = half - i - 2

            A_min = A[i] if i >= 0 else float("-inf")
            A_max = A[i + 1] if i + 1 < len(A) else float("inf")
            B_min = B[j] if j >= 0 else float("-inf")
            B_max = B[j + 1] if j + 1 < len(B) else float("inf")

            if A_min <= B_max and B_min <= A_max:
                if total % 2 == 0:
                    return (max(A_min, B_min) + min(A_max, B_max)) / 2
                return min(A_max, B_max)
            elif A_min > B_max:
                r = i - 1
            else:
                l = i + 1
        