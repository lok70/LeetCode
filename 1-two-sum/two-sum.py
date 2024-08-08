class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}
        n = len(nums)

        for i in range(n):
            comp = target - nums[i]
            if comp in m:
                return [m[comp], i]
            m[nums[i]] = i

        return []
        