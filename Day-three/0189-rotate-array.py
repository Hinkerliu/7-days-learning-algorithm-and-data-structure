class Solution:
    def rotate(self, nums, k):
	# Faster 使用切片
        n = len(nums)
        k = k % n
		# nums[n-k:]是后面一部分的元素，nums[:n-k]是前面一部分的元素
        nums[:] = nums[n-k:] + nums[:n-k]