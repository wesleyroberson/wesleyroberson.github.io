nums1 = [1, 4, 5, 0, 0, 0]
m = 3
nums2 = [2, 3, 4]
n = 3


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        while m >= 0 or n >= 0:
            if n < 1:
                break
            elif m < 1:
                nums1[n - 1] = nums2[n - 1]
                n -= 1
            elif nums2[n - 1] >= nums1[m - 1]:
                nums1[m + n - 1] = nums2[n - 1]
                n -= 1
            else:
                nums1[m + n - 1] = nums1[m - 1]
                m -= 1


solution = Solution()
solution.merge(nums1, m, nums2, n)
print(nums1)

# 26 ms (beats 25.41%)
# 13.12 MB (beats 90.79%)


# or
'''for i in range(n):
       nums1[m + i] = nums2[i]
       nums1.sort()'''


# first success:
#         nums3 = []
#         while len(nums1) > 0:
#             nums3.append(nums1.pop(0))
#         i_count = 0
#         j_count = 0
#         while i_count < m or j_count < n:
#             if i_count == m:
#                 nums1.append(nums2[j_count])
#                 j_count += 1
#             elif j_count == n:
#                 nums1.append(nums3[i_count])
#                 i_count += 1
#             elif nums2[j_count] < nums3[i_count]:
#                 nums1.append(nums2[j_count])
#                 j_count += 1
#             else:
#                 nums1.append(nums3[i_count])
#                 i_count += 1

# 23 ms (beats 45.41%)
# 13.3 MB (beats 26.75%)
