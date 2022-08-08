#
# @lc app=leetcode.cn id=1480 lang=python3
#
# [1480] 一维数组的动态和
#
from typing import List
# @lc code=start
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        opt = []
        for i in range(len(nums)):
            opt.append(sum(nums[:i+1]))
        return opt
# @lc code=end

