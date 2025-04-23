
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if nums is None or len(nums) <= 1:
            return

        n = len(nums)
        none_zero_index = 0
        for i in range(n):
            value = nums[i]
            if value == 0:
                none_zero_index = i + 1

                # find next none-zero element
                while none_zero_index < n and nums[none_zero_index] == 0:
                    none_zero_index += 1
                if none_zero_index < n:
                    # swap
                    nums[i] = nums[none_zero_index]
                    nums[none_zero_index] = 0
