class Solution:
    def minSwaps(self, nums: List[int])->int:
        n = len(nums)
        num_ones = nums.count(1)
        
        extended_nums = nums + nums
        
        current_window_zeros = extended_nums[:num_ones].count(0)
        min_swaps = current_window_zeros
        
        for i in range(1, n):
            if extended_nums[i - 1] == 0:
                current_window_zeros -= 1
            if extended_nums[i + num_ones - 1] == 0:
                current_window_zeros += 1
            min_swaps = min(min_swaps, current_window_zeros)
        
        return min_swaps

        