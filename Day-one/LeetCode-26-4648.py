class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        numslen = len(nums)
        if numslen == 0:
            return 0
        left = 0
        for i in range(1, numslen):
            if nums[left] != nums[i]:
                left += 1
                nums[left] = nums[i]
        return left + 1
