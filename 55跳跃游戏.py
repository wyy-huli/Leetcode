# Leetcode
Leetcode-Python-Soultion
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        if nums[0] == 0 or len(nums) == 0:
            return False
        ans = 0
        i = 0
        while i <= ans:
            ans = max(i + nums[i],ans)
            i += 1
            if ans >= len(nums)-1:
                return True
        return False
