class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        if len(nums)>0:
            return [i for i in nums if nums.count(i)>1][0]
