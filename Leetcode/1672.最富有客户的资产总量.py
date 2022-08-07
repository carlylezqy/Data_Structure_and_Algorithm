#
# @lc app=leetcode.cn id=1672 lang=python3
#
# [1672] 最富有客户的资产总量
#
from typing import List
# @lc code=start
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_value = 0
        for i in accounts:
            if sum(i) > max_value:
                max_value = sum(i)
        return max_value
    
# @lc code=end

