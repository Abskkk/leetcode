class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        l, r = -1, len(nums1) - 1
        total = len(nums1) + len(nums2)
        half = total // 2
        while l <= r:
            index_1 = l + (r - l) // 2
            left_1 = nums1[index_1] if index_1 >= 0 else -float("inf")
            right_1 = nums1[index_1 + 1] if index_1 < len(nums1) - 1 else float("inf")
            index_2 = half - index_1 - 2
            left_2 = nums2[index_2] if index_2 >= 0 else -float("inf")
            right_2 = nums2[index_2 + 1] if index_2 < len(nums2) - 1 else float("inf")
            if left_1 <= right_2 and left_2 <= right_1:
                if total % 2 == 1:
                    return min(right_1, right_2)
                return (max(left_1, left_2) + min(right_1, right_2)) / 2
            elif left_1 > right_2:
                r = index_1 - 1
            else:
                l = index_1 + 1