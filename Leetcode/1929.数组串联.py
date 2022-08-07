#
# @lc app=leetcode.cn id=1929 lang=python3
#
# [1929] 数组串联
#
from typing import List
# @lc code=start
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums.append(nums[i])
        return nums
        
# @lc code=end

