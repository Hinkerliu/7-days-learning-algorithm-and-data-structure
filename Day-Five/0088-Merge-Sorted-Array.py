class Solution(object):
    def merge(self, nums1, m, nums2, n):
        p1 = m-1 #point on nums1
        p2 = n-1 #point on nums2
        pos = m+n-1 #point on nums1 that we are editting
        while p1>=0 and p2>=0:
            if nums1[p1]>nums2[p2]:
                nums1[pos] = nums1[p1]
                p1 = p1-1
                pos = pos-1
            else:
                nums1[pos] = nums2[p2]
                p2 = p2-1
                pos = pos-1        
        #One of the array is done, put the rest in place
        nums1[:p2+1] = nums2[:p2+1]