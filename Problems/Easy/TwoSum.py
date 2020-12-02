class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        h = {}
        for index1,value1 in enumerate(nums):
            comp = target - value1
            if comp in h:
                return [h[comp], index1]
            h[value1] = index1
