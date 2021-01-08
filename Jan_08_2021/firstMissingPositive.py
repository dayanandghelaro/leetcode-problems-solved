class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if nums is None or len(nums)==0:
            return 1
        else:
            m = max(nums)
            if len(nums) > m:
                m = len(nums)
            for i in range(1, m+2):
                if i not in nums:
                    return i
            return 1
