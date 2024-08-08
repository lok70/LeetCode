class Solution(object):
    def runningSum(self, nums):
        res = []
        for i in range(len(nums)):
            runsum = 0
            for j in range(i+1):
                runsum += nums[j]
            res.append(runsum)
        return res
        