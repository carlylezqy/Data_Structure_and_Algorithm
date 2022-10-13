#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i , v1 in enumerate(nums):
            for j, v2 in enumerate(nums):
                if v1 + v2 == target and i != j:
                    return [i, j]
# @lc code=end

