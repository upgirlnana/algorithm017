class Solution(object):
    def merge(self, nums1, m, nums2, n):
        if m == 0 and n!=0:
            nums1[:] = nums2[0:n]
        elif n == 0 and m!=0:
            nums1[:] = nums1[0:m]
        elif m==0 and n==0:
            nums1[:] = [0]
        else:
            nums1[:] = nums1[0:3]
            nums1.extend(nums2[0:n])
            # (nums1[0:m]).extend(nums2[0:n])
            nums1[:] = sorted(nums1)


