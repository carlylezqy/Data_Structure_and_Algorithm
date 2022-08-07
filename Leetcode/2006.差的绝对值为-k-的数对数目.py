#
# @lc app=leetcode.cn id=2006 lang=python3
#
# [2006] 差的绝对值为 K 的数对数目
#
from typing import List
# @lc code=start
class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        count = 0
        for i, v in enumerate(nums):
            for j in range(i + 1, len(nums)):
                if abs(v - nums[j]) == k:
                    count += 1
        return count
# @lc code=end

